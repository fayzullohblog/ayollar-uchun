from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class IpAddress(models.Model):
    ip = models.CharField(max_length=255)

    def get_client_ip(self):
        x_forwarded_for = self.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = self.META.get('REMOTE_ADDR')
        return ip

    def __str__(self):
        return self.ip

class BlogCategory(models.Model):
    title = models.CharField(max_length=128)

    slug = models.SlugField(unique=True, editable=False, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    body = RichTextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(unique=True, editable=False)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    views = models.ManyToManyField(IpAddress,blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug
            num = 1
            while Article.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{base_slug}-{num}"
                num += 1

        super().save(*args, **kwargs)


class BlogImages(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to="blog_images")

    def __str__(self) -> str:
        return str(self.id)


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )

    comment = models.CharField(max_length=150)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
