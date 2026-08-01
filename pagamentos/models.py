from django.db import models
from pedidos.models import Pedido

FORMA_PAGAMENTO_CHOICES = [
    ('PIX', 'Pix (Aprovação Instantânea)'),
    ('CARTAO_CREDITO', 'Cartão de Crédito'),
    ('CARTAO_DEBITO', 'Cartão de Débito'),
    ('DINHEIRO', 'Dinheiro / Pagamento no Balcão'),
]

STATUS_PAGAMENTO_CHOICES = [
    ('PENDENTE', 'Pendente'),
    ('CONCLUIDO', 'Concluído (Simulado)'),
    ('CANCELADO', 'Cancelado'),
]

class Pagamento(models.Model):
    pedido = models.OneToOneField(
        Pedido, 
        on_delete=models.CASCADE, 
        related_name='pagamento', 
        verbose_name="Pedido"
    )
    forma_pagamento = models.CharField(
        max_length=30, 
        choices=FORMA_PAGAMENTO_CHOICES, 
        default='PIX',
        verbose_name="Forma de Pagamento"
    )
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Valor Pago"
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_PAGAMENTO_CHOICES, 
        default='CONCLUIDO', 
        verbose_name="Status do Pagamento"
    )
    codigo_transacao = models.CharField(
        max_length=60, 
        blank=True, 
        null=True, 
        verbose_name="Código da Transação"
    )
    data_pagamento = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Data do Pagamento"
    )
    observacao = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Observações / Detalhes"
    )

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

    def __str__(self):
        return f"Pagamento #{self.id} - Pedido #{self.pedido.id} ({self.get_forma_pagamento_display()})"
