class artigo:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def get_artigo(self):
        return "titulo: " + self.titulo + "autor: " + self.autor

class edicao:
    def __init__ (self, numero, volume, data):
        self.numero = numero
        self.volume = volume
        self.data = data
        self.artigos = []
    
    def add_novo_artigo(self, artigos):
        self.artigos.append(artigos)
    
    def get_edicao(self):
        return "número da edição: " + str(self.numero) + "|" + " volume: " + srt(self.volume)
    
    def show_artigos(self):
        data = " "
        for artigo in self.artigo:
            print(artigo.get_artigos())
    
    def get_numero_de_arquivos(self):
        return len(self.artigos)

class revista:
    def __init__(self, titulo, issn, periodicidade):
        self.titulo = titulo
        self.issn = issn
        self.periodicidade = periodicidade
        self.edicoes = []
    
    def add_nova_edicao(self, edicao):
        num_artigos = edicao.get_numero_de_arquivos()
        if(num_arquivos >= 1 and num_arquivos <=5):
            self.edicoes.apprend(edicao)
            return "edição lançada com sucesso!"
        else:
            return " é necessário ter no máximo 5 artigos"
