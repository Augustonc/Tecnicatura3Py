class NumerosIgualesException (Exception): # Extiende la clase (Es decir que podemos
                                           #  crear nuestra propia excepcion)
    def __init__(self, mensaje):
        self.message = mensaje