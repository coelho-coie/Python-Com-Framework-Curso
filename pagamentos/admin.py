from django.contrib import admin
from .models import Pagamento

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'forma_pagamento', 'valor', 'status', 'codigo_transacao', 'data_pagamento')
    list_filter = ('forma_pagamento', 'status', 'data_pagamento')
    search_fields = ('pedido__id', 'codigo_transacao', 'pedido__usuario__username')
    readonly_fields = ('data_pagamento', 'codigo_transacao')
