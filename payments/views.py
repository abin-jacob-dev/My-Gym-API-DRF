from django.shortcuts import render
from rest_framework import generics
from .serializers import PaymentSerializer, PaymentStatusSerializer
from .models import Payment
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.permissions import IsGymOwner
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class CustomPagination(PageNumberPagination):
    page_size = 2
    page_query_param = "p"


class PaymentCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status="completed")


class PaymentListView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class PaymentDetailView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_owner():
            return Payment.objects.all()
        return Payment.objects.filter(user=self.request.user)


class PaymentHistoryView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        if self.request.user.is_owner():
            return Payment.objects.all().order_by("-payment_date")

        return Payment.objects.filter(user = self.request.user).order_by("-payment_date")


class PaymentStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsGymOwner]

    def patch(self, request, pk):
        try:
            payment = Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response(
                {"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PaymentStatusSerializer(payment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
