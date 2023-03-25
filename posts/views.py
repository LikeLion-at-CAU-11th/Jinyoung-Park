from django.shortcuts import render
from django.http import JsonResponse

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


def introduction(request):
    if request.method == "GET":
        return JsonResponse(
            {
                "status": 200,
                "success": True,
                "message": "메세지 전달 성공!",
                "data": [
                    {"name": "박진영", "age": 24, "major": "Economic"},
                    {"name": "민병록", "age": 24, "major": "Software"},
                ],
            }
        )
