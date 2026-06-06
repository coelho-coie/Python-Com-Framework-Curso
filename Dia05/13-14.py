with open("parte1.txt", "r", encoding="utf-8") as f_parte1:
    conteudo_parte1 = f_parte1.read()
        
with open("parte2.txt", "r", encoding="utf-8") as f_parte2:
    conteudo_parte2 = f_parte2.read()

with open("historia_completa.txt", "w", encoding="utf-8") as f_final:
    f_final.write(conteudo_parte1)
    f_final.write("\n") # Adiciona uma linha em branco entre as partes
    f_final.write(conteudo_parte2)
        
print("Arquivo 'historia_completa.txt' criado com sucesso!")