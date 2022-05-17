from django.urls import path
from .views import OrdersPageView, chargeView

urlpatterns = [
    path('', OrdersPageView.as_view(), name = "orders"),
    path('charge/', chargeView, name = "charge")
]