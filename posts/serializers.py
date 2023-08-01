from rest_framework import serializers
from .models import Post, Comment

from config import settings
import boto3
from botocore.exceptions import ClientError


# 이미지 검사
def is_image(image):
    file_extentions = ["jpg", "jpeg", "png", "gif"]
    file_extention = image.name.split(".")[-1].lower()

    if file_extention not in file_extentions:
        return False
    return True


# Post table
class PostSerializer(serializers.ModelSerializer):
    class Meta:  # 내부 데이터 접근할 때 사용
        model = Post

        fields = "__all__"  # 다 가져옴~

    # 유효한 이미지 파일인지 확인용
    def validate(self, data):
        image = data.get("thumbnail")
        if not is_image(image):
            raise serializers.ValidationError("이미지 파일이 아닙니다.")
        else:
            s3_url = self.save_image(image)
            if not s3_url:
                raise serializers.ValidationError("무효한 이미지 파일입니다.")
            data["thumbnail"] = s3_url
        return data

    def save_image(self, image):
        try:
            s3 = boto3.client(
                "s3",
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                region_name=settings.AWS_REGION,
            )
            bucket_name = settings.AWS_STORAGE_BUCKET_NAME
            file_path = image.name
            # 업로드
            s3.upload_fileobj(image, bucket_name, file_path)

            s3_url = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{file_path}"
            return s3_url
        except:
            print("s3 upload error")
            return None


# Comment table
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

        fields = "__all__"


# 추가


# 가져올 필드를 지정해줄 수도 있다.
# fields = ['writer', 'content']

# 제외할 필드를 지정해줄 수도 있다.
# exclude = ['id']

# create, update, delete는 안되고 read만 되는 필드를 선언할 수도 있다.(이름같이 변경되지 않아야하는 필드의 경우)
# read_only_fields = ['writer']
