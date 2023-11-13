from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import *
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import *
from rest_framework import permissions
import django_filters

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article
    count_hit = True


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "summary",
        "body",
        "photo",
    )
    template_name = "article_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    fields = (
        "title",
        "summary",
        "body",
        "photo",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser


#### API Views
class BlogCategoryAPIView(ListAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ["category", "author"]
    search_fields = [
        "title",
        "body",
    ]
    ordering_fields = ["created_at"]


class ArticleDetailAPIView(RetrieveAPIView):
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    count_hit = True

    def get_queryset(self):
        article_slug = self.kwargs.get("slug")

        return Article.objects.filter(slug=article_slug)

    def get(self, request, *args, **kwargs):
        # Get the client's IP address
        ip = get_client_ip(request)

        # Retrieve the article
        article = self.get_object()

        # Check if the IP address has already viewed the article
        if IpAddress.objects.filter(ip=ip).exists():
            article.views.add(IpAddress.objects.get(ip=ip))
        else:
            IpAddress.objects.create(ip=ip)
            article.views.add(IpAddress.objects.get(ip=ip))

        return super().get(request, *args, **kwargs)

class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer


class ArticleUpdateAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    # permission_classes = [permissions.IsAuthenticated]


class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    # permission_classes = [permissions.IsAuthenticated]
