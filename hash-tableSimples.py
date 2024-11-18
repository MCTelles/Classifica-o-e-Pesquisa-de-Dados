class HashTable:
    def __init__(self, size):
        # Inicializa a hash table com listas vazias
        self.size = size
        self.table = {i: [] for i in range(size)}
    
    def hash_function(self, key):
        # Função hash simples que retorna o índice da chave
        return hash(key) % self.size
    
    def insert(self, key, value):
        # Insere uma chave e valor na tabela de hash
        index = self.hash_function(key)
        self.table[index].append((key, value))
    
    def search(self, key):
        # Busca um valor pela chave
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None  # Retorna None se não encontrar a chave
    
    def delete(self, key):
        # Deleta uma chave e seu valor
        index = self.hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return True
        return False  # Retorna False se não encontrar a chave

# Exemplo de uso
htable = HashTable(10)
htable.insert('apple', 1)
htable.insert('banana', 2)

print(htable.search('apple'))  # Saída: 1
print(htable.search('banana'))  # Saída: 2
htable.delete('apple')
print(htable.search('apple'))  # Saída: None
