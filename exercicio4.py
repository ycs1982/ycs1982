class contador(object):
    """cria um contador"""

    #variavel de classe
    instancia = 0

    #construtor
    def inicio(self):
        """configurar o contador"""
        contador.instancia+=1
        self.reset()

    def reset(self):
        """configura o contador como 0"""
        self.valor = 0

    def incremento(self, montante = 1):
        """adiciona quantidade ao contador"""
        self.valor += montante

    def decremento(self, montante = 1):
        """subtrai o valor do contador"""
        self.valor -= montante

    #acessorios do contador
    def visualisar_valor(self):
        """retorna o valor do contador"""
        return self.valor

    def string(self):
        """retorna a representação de string do contador"""
        return str(self.valor)

    def __eq__(self, other):
        """Retorna True se self for igual a other ou False, caso contrário."""
        if self == other: return True
        if type(self) != type(other): return False
        return self.valor == other.valor




