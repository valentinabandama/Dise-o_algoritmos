class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class BST:
    def __init__(self):
        self.raiz = None

    # 🔹 Insertar valores en el árbol
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.insertar_raiz(self.raiz, valor)

    def insertar_raiz(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self.insertar_raiz(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self.insertar_raiz(nodo.derecha, valor)

    # 🔹 a) Mínimo
    def minimo(self):
        actual = self.raiz
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual.valor

    # 🔹 b) Máximo
    def maximo(self):
        actual = self.raiz
        while actual.derecha is not None:
            actual = actual.derecha
        return actual.valor

    # 🔹 c) Top N jugadores (mayores puntuaciones)
    def top_n(self, n):
        resultado = []

        def recorrido(nodo):
            if nodo is None or len(resultado) >= n:
                return
            #iniciamos el recorrido de orden inverso ---derecha--raiz--izquierda
            # 1. Ir a la derecha (valores más grandes)
            recorrido(nodo.derecha)

            # 2. Guardar el valor
            if len(resultado) < n:
                resultado.append(nodo.valor)

            # 3. Ir a la izquierda
            recorrido(nodo.izquierda)

        recorrido(self.raiz)
        return resultado


# 🔹 PRUEBA
torneo = BST()
puntos = [3200, 4100, 1800, 5000, 2700, 3900, 4600]

for i in puntos:
    torneo.insertar(i)

print("Mínimo:", torneo.minimo())    
print("Máximo:", torneo.maximo())    
print("Top 3:", torneo.top_n(3))    