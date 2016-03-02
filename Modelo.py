import abc

class Modelo(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def imprime(self):
        return

    @abc.abstractmethod
    def serializa(self):
        return

    @abc.abstractmethod
    def deserializa(self, serializado):
        return

    @abc.abstractmethod
    def siguientes(self):
        return

class Caballo(Modelo):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprime(self):
        print "El caballo esta en"
        print "x: ", self.x
        print "y: ", self.y

    def serializa(self):
        return str(self.x) + "," + str(self.y)

    def deserializa(self, serializado):
        variables = serializado.split(",",2)
        return Caballo(variables[0], variables[1])

nada = Caballo(3,4)
nada.imprime()
print nada.serializa()
otro = nada.deserializa(nada.serializa())
otro.imprime()
