"""Este modulo, tiene la estructura para crear modelos."""
import abc


class Modelo(object):
    """Esta clase es el modelo base para crear busquedas."""

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor para crear modelos."""
        pass

    @abc.abstractmethod
    def imprime(self):
        """Funcion para imprimir de manera humana los modelos."""
        return

    @abc.abstractmethod
    def serializa(self):
        """Esta funcion regresa un string serializado del modelo."""
        return

    @abc.abstractmethod
    def deserializa(self, serializado):
        """Esta funcion regresa un objeto modelo de un string serializado."""
        return

    @abc.abstractmethod
    def siguientes(self):
        """Regresa una lista de las posibles soluciones."""
        return


class Caballo(Modelo):
    """La clase que representa al caballo en un tablero de ajedrez."""

    width = 8
    eight = 8

    def __init__(self, x, y):
        """El constructor recibe la posicion del caballo."""
        self.x = x
        self.y = y

    def imprime(self):
        """Imprime la posicion del caballo."""
        print "El caballo esta en"
        print "x: ", self.x
        print "y: ", self.y

    def serializa(self):
        """Implementacion de serializa."""
        return str(self.x) + "," + str(self.y)

    def deserializa(self, serializado):
        """Implementacion de deserializa."""
        variables = serializado.split(",", 2)
        return Caballo(variables[0], variables[1])

    def valida(self, x, y):
        """Valida si una cordenada esta dentro del tablero."""
        return x < Caballo.width and x >= 0 and y < Caballo.eight and y >= 0

    def siguientes(self):
        """Crea todos los movientos posibles del caballo."""
        lista = []
        newx = self.x + 1
        newy = self.y + 2
        if (self.valida(newx, newy)):
            lista.append(Caballo(newx, newy))
        newx = self.x + 1
        newy = self.y - 2
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy))
        newx = self.x - 1
        newy = self.y + 2
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy))
        newx = self.x - 1
        newy = self.y - 2
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy))
        newx = self.x + 2
        newy = self.y + 1
        if (self.valida(newx, newy)):
            lista.append(Caballo(newx, newy))
        newx = self.x + 2
        newy = self.y - 1
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy))
        newx = self.x - 2
        newy = self.y + 1
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy))
        newx = self.x - 2
        newy = self.y - 1
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy))
        return lista

nada = Caballo(7, 7)
for estado in nada.siguientes():
    estado.imprime()
