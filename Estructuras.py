"""Este paquete contiene estructuras de datos.

Contiene definiciones e immplementacines de las
estructuras de datos distintas que se necesiten.
"""
import abc


class ColaAbstracta(object):
    """La definicion de una cola."""

    __metaclass__ = abc.ABCMeta

    def __init__():
        """Constructor de la clase cola."""
        pass

    @abc.abstractmethod
    def push(self, objeto):
        """Metodo para meter objeto en la cola."""
        return

    @abc.abstractmethod
    def pop(self, objeto):
        """Metodo para sacar objeto de la cola."""
        return


class ColaPython(ColaAbstracta):
    """Implementacion nativa de una cola.

    Esta implementacion usa la memoria
    asignada por la maquina virtual.
    """

    def __init__(self):
        """Constructor de la clase."""
        self.cola = []
        self.inicio = 0

    def push(self, objeto):
        """Implementacion de push."""
        self.cola.append(objeto)

    def pop(self):
        """Implementacion de pop."""
        variable = self.cola[self.inicio]
        self.inicio += 1
        return variable

cola = ColaPython()
cola.push("hola")
cola.push("adios")
print cola.pop()
print cola.pop()
