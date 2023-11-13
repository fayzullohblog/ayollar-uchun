from django.urls import path
from .views import *

urlpatterns = [
    path('', CourseList.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetail.as_view(), name='course-detail'),

    path('videos/', VideoList.as_view(), name='video-list'),
    path('videos/<int:pk>/', VideoDetail.as_view(), name='video-detail'),

    path('certificates/', CertificateList.as_view(), name='certificate-list'),
    path('certificates/<int:pk>/', CertificateDetail.as_view(), name='certificate-detail'),

    path('ratings/', CourseRatingList.as_view(), name='rating-list'),
    path('ratings/<int:pk>/', CourseRatingDetail.as_view(), name='rating-detail'),
    path("completed/",CourseCompletionView.as_view(),name='course-completion'),
    path("completed/<int:pk>/",CourseCompletionDetailView.as_view(),name='course-completion-detail'),
    # path("<int:course_id>/create_certificate/",CreateCertificateView.as_view(),name="create-certificate")
]