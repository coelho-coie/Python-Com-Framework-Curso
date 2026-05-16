
def Separador():
    print("\n" * 2)

# A função print() é o seu primeiro comando para exibir mensagens na tela.
print("Olá, Mestre! Python ao seu dispor.")

Separador()

# Cada print cria uma nova linha, perfeito para menus e listas.
print("=========================")
print("MÁQUINA DE REFRIGERANTES\n\tDO SENAI")
print("=========================")
print() # Um print vazio cria uma linha em branco.
print("1 - Coca-Cola   - R$ 5,00")
print("2 - Pepsi       - R$ 4,50")
print("3 - Guaraná     - R$ 4,00")
print("4 - Fanta Uva   - R$ 3,00")
print("5 - Sprite      - R$ 3,00")
print("6 - Coca-Zero   - R$ 5,00")
print()
print("=========================")

Separador()

# O sinal de '+' junta as strings. Lembre-se de adicionar o espaço " " manualmente.
print("Nome do Agente: " + "James" + " " + "Bond")

Separador()

# O operador '*' repete a string "*" 25 vezes, criando uma divisória impactante.
print("ALERTA DE SEGURANÇA")
print("*" * 30)
print("   Perigo: Rota de Colisão")
print("*" * 30)

Separador()

# A sequência '\n' (nova linha) permite estruturar um texto em várias linhas dentro de uma única string.
print("Destinatário:\nRua dos Códigos, 101\nBairro da Lógica - SP")

Separador()

print("Dom \tSeg \tTer \tQua \tQui \tSex \tSáb")
print("=======================================")
print(1, 2, 3, 4, 5, 6, 7, sep="\t")
print(8, 9, 10, 11, 12, 13, 14, sep="\t")
print(15, 16, 17, 18, 19, 20, 21, sep="\t")
print(22, 23, 24, 25, 26, 27, 28, sep="\t")
print(29, 30, sep="\t")
print("=======================================")

Separador()

# O argumento end=" >> " impede a quebra de linha e adiciona o separador.
print("Você está em: Início", end=" >> ")
print("Cursos", end=" >> ")
print("Python") # O último print finaliza a linha.

Separador()

# Para incluir aspas duplas dentro de uma string que já usa aspas duplas, usamos \".
print("Ele disse: \"Conhece-te a ti mesmo.\"")

Separador()

# Para exibir uma barra invertida literal, precisamos "escapá-la" com outra, formando o par \\.
print("O arquivo de log está em: C:\\Logs\\Sistema")

Separador()

# A combinação de '\n' (nova linha) e '\t' (tabulação) é ideal para criar tabelas simples.
print("Artefato\tValor (Gemas)\n========\t=============\nPoção\t\t50\nEspada\t\t250")

Separador()

# Os valores são passados diretamente para o método .format() e preenchem as chaves {}.
print("Na partida de hoje, o jogador {} marcou {} gols!".format("Pelé", 3))

Separador()

# %04d (inteiro com 4 dígitos) e %.2f (float com 2 casas) dão controle total.
# Os valores são passados diretamente para o operador % em uma tupla.
print("ID: %04d | Valor: R$ %.2f" % (7, 2500.7))

Separador()

# O modo 'a' (append) adiciona ao final do arquivo, sem apagar o que já existe.
with open('blackbox.log', 'a', encoding='utf-8') as f:
    print("23:55:10 - ALERTA: Tentativa de acesso não autorizado.", file=f)
    print("23:55:10 - INFO: Conexão com o servidor principal perdida.", file=f)

Separador()

# O modo 'w' (write) cria um novo arquivo.
with open('relatorio_senai.csv', 'w') as csv_file:
    # sep="," garante o formato CSV. file=csv_file direciona a saída para o arquivo.
    print("ID_ALUNO", "NOME_CURSO", "NOTA_FINAL", "CIDADE", sep=",", file=csv_file)

Separador()

import time

print("ALERTA: Sistema em inicialização...", flush=True)
time.sleep(2)
print("ALERTA: Verificando componentes...", flush=True)
time.sleep(2)
print("ALERTA: Sistema pronto para uso!", flush=True)