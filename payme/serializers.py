from datetime import datetime
from django.contrib.auth.models import User, Group

from rest_framework import serializers

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

    def create(self, validated_data):
        transaction = Transaction.objects.create(**validated_data)
        transaction.created_at = datetime.now()
        transaction.save()
        return transaction