from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging

from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import TransactionSerializer
from .models import Transaction
from .utils import capture_payment


logger = logging.getLogger(__name__)
# rzp_test_lWQJxvuqzC3bU2
# ZOWAzgA7NBO6K4qD6bVmOqyL

@permission_classes([AllowAny])
class TransactionAPIView(APIView):
    def post(self, request):
        payment_id = request.data["payment_id"]
        amount = request.data["amount"]
        resp = capture_payment({
            "payment_id": payment_id,
            "amount": amount
        })

        print("RESP:", resp)

        if resp is not None:
            request.data['response'] = resp
            if resp['status']:
                request.data['transaction_status'] = resp['status']
            serializer = TransactionSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                saved = serializer.save()
                print("SAVED:", saved)
                resp = {
                    "message": "Transaction created successfully.",
                }
                return Response(resp, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "message": "Payment does not exist."
        }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, payment_id):
        transaction = get_object_or_404(Transaction, payment_id=payment_id)
        print("TRANSACTIONS:", transaction)

        transaction_list = [{"id": tr.payment_id, "amount": tr.amount} for tr in transaction]
        print("LIST:", transaction_list)

        if transaction is not None:
            resp = {
                "message": "OK",
                "data": transaction_list
            }
            return Response(resp, status=status.HTTP_200_OK)
        return Response({
            "message": "NOT FOUND"
        }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            resp = {
                "message": "Transaction updated successfully.",
            }
            return Response(resp, status=status.HTTP_200_OK)
        

transaction_view = TransactionAPIView.as_view()