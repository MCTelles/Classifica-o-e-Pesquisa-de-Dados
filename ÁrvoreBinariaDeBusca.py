class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None


class ABB:
    def __init__(self):
        self.raiz = None

    # Função para inserir um valor na árvore
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerdo is None:
                no.esquerdo = No(valor)
            else:
                self._inserir_recursivo(no.esquerdo, valor)
        elif valor > no.valor:
            if no.direito is None:
                no.direito = No(valor)
            else:
                self._inserir_recursivo(no.direito, valor)

    # Função para buscar um valor na árvore
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, no, valor):
        if no is None or no.valor == valor:
            return no
        if valor < no.valor:
            return self._buscar_recursivo(no.esquerdo, valor)
        else:
            return self._buscar_recursivo(no.direito, valor)

    # Função para remover um nó
    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no, valor):
        if no is None:
            return no
        if valor < no.valor:
            no.esquerdo = self._remover_recursivo(no.esquerdo, valor)
        elif valor > no.valor:
            no.direito = self._remover_recursivo(no.direito, valor)
        else:
            # Caso 1: Nó sem filhos
            if no.esquerdo is None and no.direito is None:
                return None
            # Caso 2: Nó com um filho
            elif no.esquerdo is None:
                return no.direito
            elif no.direito is None:
                return no.esquerdo
            # Caso 3: Nó com dois filhos
            else:
                min_no = self._minimo(no.direito)
                no.valor = min_no.valor
                no.direito = self._remover_recursivo(no.direito, min_no.valor)
        return no

    def _minimo(self, no):
        while no.esquerdo is not None:
            no = no.esquerdo
        return no

    # Função para impressão em pré-ordem (raiz, esquerda, direita)
    def imprimir_pre_ordem(self):
        self._imprimir_pre_ordem_recursivo(self.raiz)
        print()

    def _imprimir_pre_ordem_recursivo(self, no):
        if no is not None:
            print(no.valor, end=" ")
            self._imprimir_pre_ordem_recursivo(no.esquerdo)
            self._imprimir_pre_ordem_recursivo(no.direito)

    # Função para impressão em ordem simétrica (esquerda, raiz, direita)
    def imprimir_ordem(self):
        self._imprimir_ordem_recursivo(self.raiz)
        print()

    def _imprimir_ordem_recursivo(self, no):
        if no is not None:
            self._imprimir_ordem_recursivo(no.esquerdo)
            print(no.valor, end=" ")
            self._imprimir_ordem_recursivo(no.direito)

    # Função para impressão em pós-ordem (esquerda, direita, raiz)
    def imprimir_pos_ordem(self):
        self._imprimir_pos_ordem_recursivo(self.raiz)
        print()

    def _imprimir_pos_ordem_recursivo(self, no):
        if no is not None:
            self._imprimir_pos_ordem_recursivo(no.esquerdo)
            self._imprimir_pos_ordem_recursivo(no.direito)
            print(no.valor, end=" ")


# Testando a implementação
if __name__ == "__main__":
    abb = ABB()

    # Inserção de elementos
    abb.inserir(50)
    abb.inserir(30)
    abb.inserir(20)
    abb.inserir(40)
    abb.inserir(70)
    abb.inserir(60)
    abb.inserir(80)

    # Impressões
    print("Árvore em pré-ordem:")
    abb.imprimir_pre_ordem()

    print("Árvore em ordem simétrica:")
    abb.imprimir_ordem()

    print("Árvore em pós-ordem:")
    abb.imprimir_pos_ordem()

    # Removendo um nó
    abb.remover(50)
    print("\nÁrvore após remoção do nó 50 em ordem simétrica:")
    abb.imprimir_ordem()

    # Busca
    resultado = abb.buscar(60)
    if resultado:
        print(f"Valor encontrado: {resultado.valor}")
    else:
        print("Valor não encontrado.")

# Árvore Rubro-Negra (Red-Black Tree)
# O que é? A Árvore Rubro-Negra é uma variação da Árvore Binária de Busca (ABB) com algumas propriedades adicionais que garantem um equilíbrio balanceado,
# o que torna as operações de inserção, remoção e busca eficientes, todas com complexidade O(log n) no pior caso.

# Para que serve? Ela é utilizada em implementações de estruturas de dados como mapas (exemplo: map em C++ e std::map),
# onde a eficiência das operações de busca, inserção e remoção é crítica.

# Como funciona? Cada nó na árvore tem uma cor (vermelho ou preto) e as seguintes regras devem ser seguidas:

# Cada nó é vermelho ou preto.
# A raiz é preta.
# Todas as folhas (nulos) são pretas.
# Se um nó é vermelho, seus filhos são pretos.
# Todo caminho de um nó até suas folhas contém o mesmo número de nós pretos.
# Essas regras garantem que a árvore esteja sempre balanceada, com a altura limitada a O(log n).

# Árvore B (B-tree)
# O que é? A Árvore B é uma árvore balanceada de busca multi-camadas que mantém os dados ordenados e permite buscas,
# inserções, e remoções eficientes. Cada nó pode ter múltiplos filhos, o que reduz a altura da árvore e melhora a performance de acesso a dados.

# Para que serve? É utilizada em sistemas de gerenciamento de banco de dados (SGBD) e sistemas de arquivos, onde grandes volumes de dados precisam ser armazenados e acessados rapidamente.

# Como funciona? A árvore B é balanceada, o que significa que todos os caminhos da raiz até as folhas têm a mesma altura.
# Cada nó pode ter múltiplos valores e filhos, e os valores dentro de cada nó são armazenados de forma ordenada.

# Árvore B+ (B+ tree)
# O que é? A Árvore B+ é uma variação da Árvore B em que os valores armazenados estão apenas nas folhas, enquanto os nós internos armazenam apenas chaves de navegação.
# Ela é mais eficiente para leitura sequencial de dados.

# Para que serve? A Árvore B+ é usada em bancos de dados e sistemas de arquivos, onde é necessário realizar buscas rápidas e também varreduras eficientes em intervalos de dados.

# Como funciona? A estrutura é muito parecida com a Árvore B, mas as folhas estão encadeadas de forma a permitir uma varredura sequencial rápida.
# O uso de encadeamento de folhas faz com que seja mais eficiente para consultas que requerem a leitura sequencial de dados.
