import treeNode


class BST:
    def __init__(self):
        self.root = None

    def insert(self, price, game):
        self.root = self._insert(self.root, price, game)

    def _insert(self, node, price, game):
        if not node:
            node = treeNode.TreeNode(price)
        if price == node.price:
            node.games.append(game)
        elif price < node.price:
            node.left = self._insert(node.left, price, game)
        else:
            node.right = self._insert(node.right, price, game)
        return node

    def search_price(self, price):
        return self._search_price(self.root, price)

    def _search_price(self, node, price):
        if not node:
            return []
        if price == node.price:
            return node.games
        elif price < node.price:
            return self._search_price(node.left, price)
        else:
            return self._search_price(node.right, price)

    def search_range(self, min_price, max_price):
        result = []
        self._search_range(self.root, min_price, max_price, result)
        return result

    def _search_range(self, node, min_price, max_price, result):
        if not node:
            return
        if min_price <= node.price <= max_price:
            result.extend(node.games)
        if min_price < node.price:
            self._search_range(node.left, min_price, max_price, result)
        if max_price > node.price:
            self._search_range(node.right, min_price, max_price, result)
