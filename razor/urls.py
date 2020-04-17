"""razor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from payme.views import transaction_view


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('orders/create/', create_order, name="create_order"),
    # path('orders/payment/', get_payment_for_order, name="get_payment_for_order"),
    path('payments/capture/', transaction_view, name="capture_payment"),
    path('payments/', transaction_view, name="get_transactions"),
    # path('payments/all/', fetch_all_payments, name="fetch_all_payments"),
    # path('payments/', get_payment, name="get_payment"),
]
