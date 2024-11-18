class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
    
    def hash_function(self, key):
        # Função hash simples que retorna o índice da chave
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        
        # Inserção no início da lista encadeada
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node
    
    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Se não encontrar a chave
    
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False  # Se não encontrar a chave

# Exemplo de uso
htable = HashTable(10)
htable.insert('apple', 1)
htable.insert('banana', 2)

print(htable.search('apple'))  # Saída: 1
print(htable.search('banana'))  # Saída: 2
htable.delete('apple')
print(htable.search('apple'))  # Saída: None
