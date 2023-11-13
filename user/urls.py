from django.urls import path
from .auth.views import RegisterGenericApiView
from rest_framework_simplejwt import views as jwt_views

from .views import UserProfileView, JobListView

urlpatterns = [
    path('register/', RegisterGenericApiView.as_view()),
    path('login/access/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    path('user/profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('job/', JobListView.as_view(), name='job-list')
]
