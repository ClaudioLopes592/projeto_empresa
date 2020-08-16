import sqlite3

class Banco():

    def criaConexao(self):
        self.conn = sqlite3.connect('empresa.db')
        self.cursor = self.conn.cursor()
        #print('Conectando ao banco de dados...')

    def desconectarBanco(self):
        self.conn.close()
        #print('Desconectando o banco de dados...')

    def montaTabelaUsuario(self):
        self.criaConexao()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_usuarios(
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_usuario VARCHAR(100),
            email_usuario VARCHAR(40),
            fone_usuario VARCHAR(14),
            login_usuario VARCHAR(40),
            senha_usuario VARCHAR(20),
            perfil_usuario VARCHAR(20))""")
        self.conn.commit()
        print('Tabela usuarios criada com sucesso!')
        self.desconectarBanco()

    def montaTabelaEntrada(self):
        self.criaConexao()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_entradas(
            id_entrada INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo_produto INTEGER,
            data_entrada VARCHAR(10),
            qtd_entrada INTEGER,
            valor_compra DECIMAL,
            total_compra DECIMAL,
            fornecedor VARCHAR(80),
            desc_produto VARCHAR(80),
            tipo_produto VARCHAR(20))""")
        self.conn.commit()
        print('Tabela entradas criada com sucesso!')
        self.desconectarBanco()