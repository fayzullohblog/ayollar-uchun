from django.urls import path

from .views import *

urlpatterns = [
    # path("<slug:slug>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    # path("<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    # path("<slug:slug>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    # path("new/", ArticleCreateView.as_view(), name="article_new"),
    # path("", ArticleListView.as_view(), name="article_list"),
    # API urls
    path("", ArticleListAPIView.as_view(), name="article-list"),
    path("categorys/", BlogCategoryAPIView.as_view(), name="blog-categorys"),
    path("<slug:slug>/",ArticleDetailAPIView.as_view(),name="article-detail"),
    path("create/", ArticleCreateAPIView.as_view(), name="article-create"),
    path("edit/<slug:slug>/", ArticleUpdateAPIView.as_view(), name="article-update"),
    path("delete/<slug:slug>/", ArticleDeleteAPIView.as_view(), name="article-update"),
]
