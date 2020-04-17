import razorpay
import logging

logger = logging.getLogger(__name__)

client = razorpay.Client(auth=("rzp_test_lWQJxvuqzC3bU2", "ZOWAzgA7NBO6K4qD6bVmOqyL"))

def create_order(data):
    """Returns new Razorpay Order object.\n
    Arguments:\n
    data = {
        "amount": 5100,
        "currency": "INR",
        "receipt": order_receipt,
        "notes": {},
        "payment_capture": '1'
    }
    """
    new_order = client.order.create(data)
    return new_order

def get_order_by_id(order_id):
    """Returns Order object of provided id.\n
    """
    order = client.order.fetch(order_id)
    return order

def fetch_all_payments():
    """Returns all Payment objects.
    """
    payments = client.payment.fetch_all()
    return payments

def get_payment_for_order(order_id):
    """Returns Payment object for order_id
    """
    payment = client.order.payments(order_id)
    return payment

def capture_payment(data):
    """Capture a payment.\n
    Arguments:\n
    data = {
        "payment_id": "pay_EeGLBWtSQC2bxi"
        "amount": 5100
    }
    """
    try:
        captured = client.payment.capture(data['payment_id'], data['amount'])
        return captured
    except Exception as e:
        logger.error(e)
        return None

def get_payment(payment_id):
    """Returns a Payment object of provided id.\n
    Arguments:
    payment_id = "pay_EeGLBWtSQC2bxi"
    """
    payment = client.payment.fetch(payment_id=payment_id)
    return payment
