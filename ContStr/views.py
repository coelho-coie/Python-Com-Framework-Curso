from django.shortcuts import render

def index(request):
    texto = ""
    total_caracteres = 0
    total_caracteres_sem_espaco = 0
    total_palavras = 0

    if request.method == "POST":
        texto = request.POST.get("texto", "")
        total_caracteres = len(texto)
        total_caracteres_sem_espaco = len(texto.replace(" ", ""))
        total_palavras = len(texto.split()) if texto.strip() else 0

    contexto = {
        "texto": texto,
        "total_caracteres": total_caracteres,
        "total_caracteres_sem_espaco": total_caracteres_sem_espaco,
        "total_palavras": total_palavras,
    }
    
    return render(request, "ContStr/index.html", contexto)