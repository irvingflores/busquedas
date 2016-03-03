"""Este modulo implementa la busqueda en anchura."""
import Estructuras


class Busqueda(object):
    """Esta clase implementa la busqueda de anchura."""

    def __init__(self, estadoInicial, estadoFinal):
        """El constructor de una busqueda.

        El constructor de la busqueda necesita como primer
        parametro el estado final al que se quiere llegar.
        """
        self.inicial = estadoInicial
        self.final = estadoFinal
        self.cola = Estructuras.ColaPython()
        self.diccionario = {}

    def aplicaBusqueda(self):
        """Este metodo crea el algoritmo para buscar."""
        while self.cola.size != 0:
            estado = self.cola.pop()
            resultado = self.introduceCola(estado)

    def introduceCola(self, generador):
        """Este metodo introduce a la cola los estados generados.

        Si al generar los estados se encuentra el resultado se
        regresa al final, si no se regresa None
        """
        resultado = None
        for estado in generador.siguientes():
            if (estado == self.inicial):
                resultado = estado
                break
            hashCode = estado.serializa()
            if hashCode not in self.diccionario:
                self.cola.push(hashCode)
        return resultado
