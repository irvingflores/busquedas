"""Este modulo, tiene la estructura para crear modelos."""
import abc
import pickle


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

    def serializa(self):
        """Esta funcion serializa un objeto en un string."""
        stringVariable = pickle.dumps(self)
        return stringVariable

    @staticmethod
    def deserializa(serializado):
        """Deseriaiza un string en el modelo."""
        return pickle.loads(serializado)

    @abc.abstractmethod
    def siguientes(self):
        """Regresa una lista de las posibles soluciones."""
        return


class Caballo(Modelo):
    """La clase que representa al caballo en un tablero de ajedrez."""

    def __init__(self, x, y, width, eight):
        """El constructor recibe la posicion del caballo."""
        self.x = x
        self.y = y
        self.width = width
        self.eight = eight

    def imprime(self):
        """Imprime la posicion del caballo."""
        print "El caballo esta en"
        print "x: ", self.x
        print "y: ", self.y

    def valida(self, x, y):
        """Valida si una cordenada esta dentro del tablero."""
        return x < self.width and x >= 0 and y < self.eight and y >= 0

    def siguientes(self):
        """Crea todos los movientos posibles del caballo."""
        lista = []
        newx = self.x + 1
        newy = self.y + 2
        if (self.valida(newx, newy)):
            lista.append(Caballo(newx, newy, self.width, self.eight))
        newx = self.x + 1
        newy = self.y - 2
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy, self.width, self.eight))
        newx = self.x - 1
        newy = self.y + 2
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy, self.width, self.eight))
        newx = self.x - 1
        newy = self.y - 2
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy, self.width, self.eight))
        newx = self.x + 2
        newy = self.y + 1
        if (self.valida(newx, newy)):
            lista.append(Caballo(newx, newy, self.width, self.eight))
        newx = self.x + 2
        newy = self.y - 1
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy, self.width, self.eight))
        newx = self.x - 2
        newy = self.y + 1
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy, self.width, self.eight))
        newx = self.x - 2
        newy = self.y - 1
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy, self.width, self.eight))
        return lista

nada = Caballo(7, 7, 8, 8)
otro = Caballo(7, 7, 8, 8)
print nada == otro
for estado in nada.siguientes():
    estado.imprime()
blabla = nada.serializa()
nana = Caballo.deserializa(blabla)
print nana == nada
