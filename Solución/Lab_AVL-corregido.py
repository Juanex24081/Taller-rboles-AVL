class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x  # Retorna la raiz luego de rotar

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y  # Retorna la raiz luego de rotar


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node

        # Actualizar la altura y balance del nodo
        updateHeight(node)

        balance = getBalance(node)

        # Si el nodo está desbalanceado, realizamos las rotaciones necesarias

        # Caso de rotación simple a la derecha (LL)
        if balance > 1 and value < node.left.value:
            return rotate_right(node)

        # Caso de rotación doble a la derecha (LR)
        if balance > 1 and value > node.left.value:
            node.left = rotate_left(node.left)
            return rotate_right(node)

        # Caso de rotación simple a la izquierda (RR)
        if balance < -1 and value > node.right.value:
            return rotate_left(node)

        # Caso de rotación doble a la izquierda (RL)
        if balance < -1 and value < node.right.value:
            node.right = rotate_right(node.right)
            return rotate_left(node)

        return node  # Retorna el nodo después de insertar


    # Recorrer el árbol de manera "In-Orden"

    def inorden_traversal(self):
        result = []
        self._inorden_recursive(self.root, result)
        return result

    def _inorden_recursive(self, node, result):
        if node:
            self._inorden_recursive(node.left, result)
            result.append(node.value)
            self._inorden_recursive(node.right, result)

    # Imprimir árbol
    def visualize(self):
        lista = []
        self._visualize_recursive(self.root, "", True, lista)
        return lista
   
    lista = []
    def _visualize_recursive(self, node, indent, last, lista):
        if node is not None:

            print(indent, "`- " if last else "|- ", node.value, sep="")
            
            indent += "   " if last else "|  "

            self._visualize_recursive(node.left, indent, False, lista)
            self._visualize_recursive(node.right, indent, True, lista)

            lista.append(f"(Nodo = {node.value}: Altura = {node.height}, Balance = {getBalance(node)})")


# ----- Ejecución -----

avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Después de inserciones ---")
avl.visualize()


# Imprimir la lista con las propiedades de los nodos
nodos_detalles = avl.visualize()

print("\n--- Detalles de los nodos ---")
for detalle in nodos_detalles:
    print(detalle)


print("\n--- Recorrido In-orden ---")
print(avl.inorden_traversal())
