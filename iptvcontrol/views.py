from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)  # Busca o cliente pelo ID
    if request.method == 'POST':
        # Atualiza os campos do cliente com os dados do formulário
        cliente.cliente = request.POST.get('cliente')
        cliente.mac = request.POST.get('mac')
        cliente.key = request.POST.get('key')
        cliente.m3u = request.POST.get('m3u')
        cliente.save()  # Salva as alterações no banco de dados
        return redirect('iptv_control')  # Redireciona para a página de controle

    # Renderiza o formulário de edição com os dados do cliente
    return render(request, 'editar_cliente.html', {'cliente': cliente})

def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)  # Busca o cliente pelo ID
    cliente.delete()  # Deleta o cliente
    return redirect('iptv_control')  # Redireciona para a página de controle

def iptv_control(request):
    if request.method == 'POST':
        # Captura os dados do formulário
        cliente_nome = request.POST.get('cliente')
        mac = request.POST.get('mac')
        key = request.POST.get('key')
        m3u = request.POST.get('m3u')

        # Salva um novo cliente no banco de dados
        novo_cliente = Cliente(cliente=cliente_nome, mac=mac, key=key, m3u=m3u)
        novo_cliente.save()

        return redirect('iptv_control')  # Redireciona após salvar

    # Recupera todos os clientes para exibição
    clientes = Cliente.objects.all()
    return render(request, 'iptvcontrol.html', {'clientes': clientes})
