"""Este modulo implementa la busqueda en anchura."""
import estructuras
import modelo


class Busqueda(object):
    """Esta clase implementa la busqueda de anchura."""

    def __init__(self, tipo, estadoInicial, estadoFinal):
        """El constructor de una busqueda.

        El constructor de la busqueda necesita como primer
        parametro el estado final al que se quiere llegar.
        """
        self.inicial = estadoInicial
        self.final = estadoFinal
        self.cola = estructuras.ColaPython()
        self.diccionario = {}
        self.padres = {}
        self.tipo = tipo

    def aplicaBusqueda(self):
        """Este metodo crea el algoritmo para buscar."""
        self.cola.push(self.inicial.serializa())
        self.padres[self.inicial.serializa()] = 1
        while self.cola.size > 0:
            estado = self.tipo.deserializa(self.cola.pop())
            resultadoPreliminar = self.introduceCola(estado)
            if resultadoPreliminar is not None:
                break
        print "Ya acabe"
        resultadoPreliminar.imprime()
        self.imprimeCamino(resultadoPreliminar)

    def imprimeCamino(self, final):
        """Este metodo imprime el camino para encontrar el objetivo."""
        papa = self.padres[final.serializa()]
        while papa != 1:
            self.tipo.deserializa(papa).imprime()
            papa = self.padres[papa]

    def introduceCola(self, generador):
        """Este metodo introduce a la cola los estados generados.

        Si al generar los estados se encuentra el resultado se
        regresa al final, si no se regresa None
        """
        resultado = None
        for estado in generador.siguientesEstados():
            if (estado == self.final):
                self.padres[estado.serializa()] = generador.serializa()
                resultado = estado
                break
            hashCode = estado.serializa()
            if hashCode not in self.diccionario:
                self.cola.push(hashCode)
                self.padres[hashCode] = generador.serializa()
                self.diccionario[hashCode] = 1
        return resultado

if __name__ == "__main__":

    caballoInicial = modelo.Caballo(2, 2, 8, 8)
    caballoFinal = modelo.Caballo(7, 3, 8, 8)
    programaNuevo = Busqueda(modelo.Caballo, caballoInicial, caballoFinal)
    programaNuevo.aplicaBusqueda()
