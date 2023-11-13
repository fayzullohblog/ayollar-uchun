from django.contrib import admin
from .models import *


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


class BlogImagesInline(admin.TabularInline):
    model = BlogImages


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine, BlogImagesInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(BlogCategory)
admin.site.register(BlogImages)
admin.site.register(IpAddress)
