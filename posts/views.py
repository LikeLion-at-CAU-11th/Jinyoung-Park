from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Post, Comment
import json

# Create your views here.


def hello_world(request):
    if request.method == "GET":
        return JsonResponse(
            {
                "status": 200,
                "success": True,
                "message": "메세지 전달 성공!",
                "data": "Hello world\n",
            }
        )


@require_http_methods(["GET", "PATCH", "DELETE"])
def post_detail(request, id):
    if request.method == "GET":
        post = get_object_or_404(Post, pk=id)
        category_json = {
            "id": post.post_id,
            "writer": post.writer,
            "content": post.content,
            "category": post.category,
        }

        return JsonResponse(
            {"status": 200, "message": "게시글 조회 성공", "data": category_json}
        )

    elif request.method == "PATCH":
        body = json.loads(request.body.decode("utf-8"))
        update_post = get_object_or_404(Post, pk=id)

        update_post.content = body["content"]
        update_post.category = body["category"]
        update_post.save()

        update_post_json = {
            "id": update_post.post_id,
            "writer": update_post.writer,
            "content": update_post.content,
            "category": update_post.category,
        }

        return JsonResponse(
            (
                {
                    "status": 200,
                    "message": "게시글 수정 성공~",
                    "data": update_post_json,
                }
            )
        )

    elif request.method == "DELETE":
        delete_post = get_object_or_404(Post, pk=id)
        delete_post.delete()

        return JsonResponse(
            {
                "status": 200,
                "message": "게시글 삭제 성공~",
                "data": None,
            }
        )


@require_http_methods(["GET"])
def get_post_all(request):
    post = Post.objects.all()
    post_list = []

    for item in post:
        post_list.append(
            {
                "id": item.post_id,
                "writer": item.writer,
                "content": item.content,
                "category": item.category,
            }
        )

    return JsonResponse({"status": 200, "message": "모든 게시글 조회 성공", "data": post_list})


@require_http_methods(["GET"])
def get_post_in_time(request):
    post_in_time = Post.objects.filter(
        created_at__gte="2023-04-05 22:00",
        created_at__lte="2023-04-12 19:00",  # 부등호 느낌으로다가 __gte(>=), __lte(<=) 사용해서 구간 사이에 있는 값 가져옴
    )
    post_in_time_list = []

    for item in post_in_time:
        post_in_time_list.append(
            {
                "id": item.post_id,
                "writer": item.writer,
                "content": item.content,
                "category": item.category,
            }
        )

    return JsonResponse(
        {"status": 200, "message": "시간 사이 게시글 조회 성공", "data": post_in_time_list}
    )


@require_http_methods(["POST"])
def create_post(request):
    body = json.loads(request.body.decode("utf-8"))  # 이해할 수 있는 형식으로 데이터 받아옴

    new_post = Post.objects.create(
        writer=body["writer"],
        content=body["content"],
        category=body["category"],
    )

    new_post_json = {
        "id": new_post.post_id,
        "writer": new_post.writer,
        "content": new_post.content,
        "category": new_post.category,
    }

    return JsonResponse(
        {"status": 200, "message": "게시글 목록 생성 성공", "data": new_post_json}
    )


@require_http_methods(["GET", "POST"])
def comment(request, post_id):
    if request.method == "GET":
        comment_all = Comment.objects.filter(post=post_id)
        comment_json_list = []

        for comment in comment_all:
            comment_json = {
                "writer": comment.writer,
                "content": comment.content,
            }
            comment_json_list.append(comment_json)

        return JsonResponse(
            {
                "status": 200,
                "message": "comment 읽어오기 성공",
                "data": comment_json_list,
            }
        )

    elif request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        body = json.loads(request.body.decode("utf-8"))

        new_comment = Comment.objects.create(
            writer=body["writer"],
            content=body["content"],
            post=post,  # Post의 값이 들어와야 함 so, 그냥 숫자를 넣으면 안되고 쿼리셋을 이용해서 원하는 pk(post_id)의 post를 불러와 사용하자,,(pk인 아이디만 가져오는 것이 아니라 pk에 해당하는 테이블 전체를 불러와야 하는듯...? 맞나..?)
        )

        new_comment_json = {
            "writer": new_comment.writer,
            "content": new_comment.content,
        }

        return JsonResponse(
            {
                "status": 200,
                "message": "comment 생성 성공",
                "data": new_comment_json,
            }
        )
