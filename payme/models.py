from django.contrib.postgres.fields import JSONField
from django.db import models


class Transaction(models.Model):
    # transaction_status = models.ForeignKey(TransactionStatus, on_delete=models.CASCADE, null=True)
    transaction_status = models.CharField(max_length=20, null=True)
    order_id = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    payment_id = models.CharField(max_length=50, null=True)
    payment_type = models.CharField(max_length=20, null=True)
    invoice_id = models.CharField(max_length=50, null=True)
    customer_id = models.CharField(max_length=50, null=True)
    card_id = models.CharField(max_length=50, null=True)
    settlement_id = models.CharField(max_length=50, null=True)
    response = JSONField(null=True)

    def __str__(self):
        return str(self.id)
