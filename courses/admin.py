from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Certificate)
admin.site.register(CourseRating)
admin.site.register(CourseCompletion)