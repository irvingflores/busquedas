"""Este modulo, tiene la estructura para crear modelos."""
import abc
import pickle


class Modelo(object):
    """Esta clase es el modelo base para crear busquedas."""

    __metaclass__ = abc.ABCMeta

    def __init__(self, pasos):
        """Constructor para crear modelos."""
        self.pasos = pasos

    @abc.abstractmethod
    def imprime(self):
        """Funcion para imprimir de manera humana los modelos."""
        return

    def serializa(self):
        """Esta funcion serializa un objeto en un string."""
        stringVariable = pickle.dumps(self)
        return stringVariable

    def __eq__(self, other):
        """Implementacion generica de igualdad de modelos."""
        if isinstance(other, self.__class__):
            dicSelf = self.__dict__.copy()
            dicOther = other.__dict__.copy()
            dicSelf["pasos"] = 0
            dicOther["pasos"] = 0
            return dicOther == dicSelf
        else:
            return False
        return (isinstance(other, self.__class__) and
                self.__dict__ == other.__dict__)

    def __ne__(self, other):
        """Implementacion generica de inequidad."""
        return not self.__eq__(other)

    @staticmethod
    def deserializa(serializado):
        """Deseriaiza un string en el modelo."""
        return pickle.loads(serializado)

    def siguientesEstados(self):
        """Calcula los siguientes estados agregando un paso."""
        return self.siguientes(self.pasos + 1)

    @abc.abstractmethod
    def siguientes(self, pasosSiguientes):
        """Regresa una lista de las posibles soluciones."""
        return


class Caballo(Modelo):
    """La clase que representa al caballo en un tablero de ajedrez."""

    def __init__(self, x, y, width, eight, pasos=0):
        """El constructor recibe la posicion del caballo."""
        super(Caballo, self).__init__(pasos)
        self.x = x
        self.y = y
        self.width = width
        self.eight = eight

    def imprime(self):
        """Imprime la posicion del caballo."""
        print "------------------"
        print "El caballo esta en"
        print "x: ", self.x
        print "y: ", self.y
        print "pasos: ", self.pasos
        print "------------------"

    def valida(self, x, y):
        """Valida si una cordenada esta dentro del tablero."""
        return x < self.width and x >= 0 and y < self.eight and y >= 0

    def siguientes(self, pasosSiguientes):
        """Crea todos los movientos posibles del caballo."""
        lista = []
        newx = self.x + 1
        newy = self.y + 2
        if (self.valida(newx, newy)):
            lista.append(Caballo(newx, newy, self.width,
                                 self.eight, pasosSiguientes))
        newx = self.x + 1
        newy = self.y - 2
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy, self.width,
                                 self.eight, pasosSiguientes))
        newx = self.x - 1
        newy = self.y + 2
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy, self.width,
                                 self.eight, pasosSiguientes))
        newx = self.x - 1
        newy = self.y - 2
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy, self.width,
                                 self.eight, pasosSiguientes))
        newx = self.x + 2
        newy = self.y + 1
        if (self.valida(newx, newy)):
            lista.append(Caballo(newx, newy, self.width,
                                 self.eight, pasosSiguientes))
        newx = self.x + 2
        newy = self.y - 1
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy, self.width,
                         self.eight, pasosSiguientes))
        newx = self.x - 2
        newy = self.y + 1
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy, self.width,
                                 self.eight, pasosSiguientes))
        newx = self.x - 2
        newy = self.y - 1
        if self.valida(newx, newy):
            lista.append(Caballo(newx, newy, self.width,
                                 self.eight, pasosSiguientes))
        return lista

if __name__ == "__main__":
    nada = Caballo(7, 7, 8, 8, 1)
    otro = Caballo(7, 7, 8, 8, 2)
    print nada == otro
    for estado in nada.siguientesEstados():
        estado.imprime()
        blabla = nada.serializa()
        nana = Caballo.deserializa(blabla)
        print nana == nada
    print otro.pasos
