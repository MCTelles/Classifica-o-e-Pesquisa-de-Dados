class TreeNode:
    def __init__(self, price):
        self.price = price
        self.games = []  # Lista de jogos com este preço
        self.left = None
        self.right = None
