# Lambda com 'if' interno: [resultado_se_verdade] if [teste] else [resultado_se_falso]
verificar_idade = lambda idade: "Maior" if idade >= 18 else "Menor"

print(f"Status 20 anos: {verificar_idade(20)}")
print(f"Status 15 anos: {verificar_idade(15)}")