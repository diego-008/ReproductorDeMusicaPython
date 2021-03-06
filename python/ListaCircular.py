from typing import Text
from Nodo import Nodo
class ListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.nombre = None
        self.size = 0

    def vacia(self):
        return self.primero == None

    def agregarInicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unirNodos()
        self.size+=1


    def agregarFinal(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)

        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.__unirNodos()
        self.size+=1


    def __unirNodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero
        pass

    def recorrerInicio(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recorrerFin(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
            if aux == self.ultimo:
                break

    def Ordenar(self):
        aux = self.primero
        while aux:
            aux2 = self.primero.siguiente
            aux3 = self.primero
            while aux2:
                if aux2.dato.reproducciones > aux3.dato.reproducciones:
                    tmp = aux3.dato
                    aux3.dato = aux2.dato
                    aux2.dato = tmp
                aux2 = aux2.siguiente
                aux3 = aux3.siguiente
                if aux2 == self.primero:
                    break
                

            aux = aux.siguiente
            if aux == self.primero:
                break
        