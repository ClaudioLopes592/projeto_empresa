from BancoDados.Banco import *
from Telas.entrada_produtos import Aplicacao

b = Banco()
b.criaConexao()
b.montaTabelaUsuario()
b.montaTabelaEntrada()
b.desconectarBanco()

e = Aplicacao()
e.salvarRegistro()