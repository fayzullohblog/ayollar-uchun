from django.urls import path
from .views import PaymentAPI, OrderListView, OrderDetailView

urlpatterns = [
    path("orders/",OrderListView.as_view(),name='order-list'),
    path("order/<str:uuid>/",OrderDetailView.as_view(),name='order-detail'),
    path('pay/<int:course_id>/', PaymentAPI.as_view(), name='make_payment'),

]