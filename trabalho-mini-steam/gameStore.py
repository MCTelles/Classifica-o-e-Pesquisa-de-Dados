import hashTable
import bst


class GameStore:
    def __init__(self):
        self.bst = bst.BST()  # BST para preços
        self.hash_table = hashTable.HashTable()  # Hash Table para gêneros
        self.games = {}  # ID como chave para detalhes do jogo

    def add_game(self, game_id, title, price, genres):
        game = {"id": game_id, "title": title, "price": price, "genres": genres}
        self.games[game_id] = game
        self.bst.insert(price, game)
        for genre in genres:
            self.hash_table.insert(genre, game_id)

    def search_by_price(self, price):
        return self.bst.search_price(price)

    def search_by_price_range(self, min_price, max_price):
        return self.bst.search_range(min_price, max_price)

    def search_by_genre(self, genre):
        ids = self.hash_table.search(genre)
        return [self.games[game_id] for game_id in ids]
