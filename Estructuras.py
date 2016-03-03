"""Este modulo contiene estructuras de datos.

En general se definen aqui las estructuras para las diferentes
tareas e implementaciones.
"""
import abc


class ColaAbstracta(object):
    """Clase abstracta de la cola."""

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor de la cola."""
        pass

    @abc.abstractmethod
    def push(self, objeto):
        """Metodo para insertar objetos en la cola."""
        return

    @abc.abstractmethod
    def pop(self, objeto):
        """Metodo para sacar un objeto de la cola."""
        return


class ColaPython(ColaAbstracta):
    """Implementacion nativa de la cola."""

    def __init__(self):
        """Constructor de la cola."""
        self.lista = []
        self.inicio = 0
        self.size = 0

    def push(self, objeto):
        """Implementacion de push."""
        print "Insertando objeto a la cola"
        #print objeto.imprime()
        self.lista.append(objeto)
        self.size += 1

    def pop(self):
        """Implementacion de pop."""
        if self.size == 0:
            raise ValueError("La lista esta vacia.")
        objetoPop = self.lista[self.inicio]
        #print "Sacando objeto de la cola"
        print objetoPop.imprime()
        self.lista[self.inicio] = None
        self.inicio += 1
        self.size -= 1
        return objetoPop

if __name__ == "__main__":
    cola = ColaPython()
    cola.push("hola")
    cola.push("adios")
    cola.push("nananana")
    print cola.pop()
    print cola.pop()
    print cola.pop()
    print cola.pop()
