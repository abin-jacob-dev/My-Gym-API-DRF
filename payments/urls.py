from django.urls import path
from .serializers import PaymentSerializer
from .models import Payment
from .views import (
    PaymentCreateView,
    PaymentDetailView,
    PaymentListView,
    PaymentHistoryView,
    PaymentStatusUpdateView,
)

urlpatterns = [
    path("", PaymentListView.as_view(), name="payment_list"),
    path("create/", PaymentCreateView.as_view(), name="payment_create"),
    path("detail/<int:pk>/", PaymentDetailView.as_view(), name="payment_detail"),
    path("history/", PaymentHistoryView.as_view(), name="payment_history"),
    path("status/<int:pk>/", PaymentStatusUpdateView.as_view(), name="payment_status"),
]
