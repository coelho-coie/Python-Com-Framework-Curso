class Playlist:
    def __init__(self):
        self.musicas = []

    def adicionar(self, nome):
        self.musicas.append(nome)

    def remover(self, nome):
        if nome in self.musicas:
            self.musicas.remove(nome)

rock = Playlist()
rock.adicionar("Highway to Hell")
rock.remover("Highway to Hell")
print(f"Sua playlist: {rock.musicas}")