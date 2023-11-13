from rest_framework import serializers
from .models import *
from user.serailizer import UserSerializer

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ("title", "slug")


class BlogCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Comment
        fields = "__all__"


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImages
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    comments = BlogCommentSerializer(many=True)
    category = BlogCategorySerializer()
    image = BlogImageSerializer(many=True)
    author = UserSerializer()
    views = serializers.SerializerMethodField()

    def get_views(self,obj):
            count = obj.views.count()
            return count
    class Meta:
        model = Article
        fields = [
            "created_at",
            "updated_at",
            "title",
            "body",
            "image",
            "author",
            "slug",
            "comments",
            "category",
            "views",
        ]
