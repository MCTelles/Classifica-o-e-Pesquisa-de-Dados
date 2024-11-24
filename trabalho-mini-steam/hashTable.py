# Tabela Hash para Gerenciamento de Jogos por Gênero
class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, genre, game_id):
        if genre not in self.table:
            self.table[genre] = []
        self.table[genre].append(game_id)

    def search(self, genre):
        return self.table.get(genre, [])
