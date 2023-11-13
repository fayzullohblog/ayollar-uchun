from django.db import models
from user.models import User
from utils.models import BaseModel
from uuid import uuid4

class Course(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='course_images/')
    average_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Video(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    is_watched = models.BooleanField(default=False)
    in_process_watching = models.BooleanField(default=False)
    watched_by = models.ManyToManyField(User, related_name='watched_videos', blank=True)

    def __str__(self):
        return self.title

class Certificate(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_identifier = models.CharField(max_length=88, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.certificate_identifier:
            self.certificate_identifier = str(uuid4())
        super(Certificate, self).save(*args, **kwargs)

    def __str__(self):
        return f"Certificate for {self.user.first_name} - {self.course.title}"

class CourseRating(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0, choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating by {self.user.first_name} on {self.course.title}"

class CourseCompletion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completion_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Course user: {self.user.first_name}"

    def has_completed_course(self, user, course):
        return CourseCompletion.objects.filter(user=user, course=course).exists()