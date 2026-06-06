# Crie um arquivo 'vendas.csv' para testar. Exemplo:
# Caneta,10,2
# Caderno,5,15

with open("vendas.csv", "r", encoding="utf-8") as f_vendas:
    with open("relatorio.txt", "w", encoding="utf-8") as f_relatorio:
        f_relatorio.write("--- Relatório de Faturamento ---\n")
        
        for linha in f_vendas:
            # .split(',') divide a linha 'Caneta,10,2' em ['Caneta', '10', '2']
            produto, quantidade_str, preco_str = linha.strip().split(',')
            
            # Convertemos os textos para números para poder calcular
            faturamento = int(quantidade_str) * int(preco_str)
            
            f_relatorio.write(f"Produto: {produto} - Faturamento: R$ {faturamento}\n")
            
print("Relatório gerado com sucesso!")