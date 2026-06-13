class Turma:
    def __init__(self):
        self.alunos = {}

    def lancar_nota(self, nome, nota):
        self.alunos[nome] = nota

    def ver_media(self):
        total = sum(self.alunos.values())
        return total / len(self.alunos)

python_class = Turma()
python_class.lancar_nota("Ana", 10)
python_class.lancar_nota("Beto", 8)
print(f"Média da turma: {python_class.ver_media()}")