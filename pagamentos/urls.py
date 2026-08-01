from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:pedido_id>/', views.checkout_pagamento, name='checkout_pagamento'),
    path('comprovante/<int:pedido_id>/', views.comprovante_pagamento, name='comprovante_pagamento'),
]
