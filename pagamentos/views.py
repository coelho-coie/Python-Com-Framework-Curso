import uuid
import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from pedidos.models import Pedido
from .models import Pagamento

def is_staff_or_admin(user):
    return user.is_staff or user.is_superuser or user.groups.filter(name__in=['Administradores', 'Funcionários']).exists()

@login_required
def checkout_pagamento(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    # Verifica se o usuário tem permissão para acessar este pedido
    if pedido.usuario != request.user and not is_staff_or_admin(request.user):
        messages.error(request, "Você não tem permissão para acessar este pedido.")
        return redirect('lista_pedidos')

    # Se o pedido já estiver pago, redireciona diretamente para o comprovante
    if pedido.pago and hasattr(pedido, 'pagamento'):
        messages.info(request, "Este pedido já foi pago!")
        return redirect('comprovante_pagamento', pedido_id=pedido.id)

    # Cálculo do valor total do pedido
    total_pedido = pedido.produtos.aggregate(Sum('preco'))['preco__sum'] or 0

    if request.method == 'POST':
        forma_pagamento = request.POST.get('forma_pagamento', 'PIX')
        observacoes = request.POST.get('observacoes', '')

        # Gera um código de transação simulado e realista
        prefixo = {
            'PIX': 'PIX',
            'CARTAO_CREDITO': 'CC',
            'CARTAO_DEBITO': 'CD',
            'DINHEIRO': 'DIN'
        }.get(forma_pagamento, 'SIM')
        
        código_random = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        codigo_transacao = f"SIM-{prefixo}-{código_random}"

        # Registra ou atualiza o Pagamento
        pagamento, created = Pagamento.objects.update_or_create(
            pedido=pedido,
            defaults={
                'forma_pagamento': forma_pagamento,
                'valor': total_pedido,
                'status': 'CONCLUIDO',
                'codigo_transacao': codigo_transacao,
                'observacao': observacoes
            }
        )

        # Atualiza o pedido para Pago
        pedido.pago = True
        pedido.save()

        messages.success(request, "🎉 Pagamento realizado com sucesso! (Simulação concluída)")
        return redirect('comprovante_pagamento', pedido_id=pedido.id)

    # Produtos detalhados para exibir no resumo
    produtos = pedido.produtos.all()

    context = {
        'pedido': pedido,
        'total_pedido': total_pedido,
        'produtos': produtos,
    }
    return render(request, 'pagamentos/checkout.html', context)

@login_required
def comprovante_pagamento(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    # Verifica permissão
    if pedido.usuario != request.user and not is_staff_or_admin(request.user):
        messages.error(request, "Você não tem permissão para visualizar este comprovante.")
        return redirect('lista_pedidos')

    pagamento = getattr(pedido, 'pagamento', None)
    total_pedido = pedido.produtos.aggregate(Sum('preco'))['preco__sum'] or 0

    context = {
        'pedido': pedido,
        'pagamento': pagamento,
        'total_pedido': total_pedido,
    }
    return render(request, 'pagamentos/comprovante.html', context)
