from django.db import models
from user.models import User
from courses.models import Course
from uuid import uuid4
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=88, unique=True, editable=False)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = str(uuid4())
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.first_name} - {self.course.title}"