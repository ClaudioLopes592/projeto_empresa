from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from BancoDados.Banco import *

app = tk.Tk()

class Aplicacao():

    def variaveis(self):
        self.codigo = self.txt_codigo.get()
        self.data = self.txt_data.get()
        self.quant = self.txt_quant.get()
        self.valor = self.txt_preco.get()
        self.total = self.calcularTotal()
        self.fornec = self.txt_fornec.get()
        self.nome = self.txt_desc.get()
        self.tipo = self.txt_tipo.get()

    def calcularTotal(self):
        self.a = self.txt_preco.get()
        self.a = float(self.a)
        self.x = self.txt_quant.get()
        self.x = int(self.x)
        self.r = self.a * self.x
        self.r = float(self.r)
        return self.r

    def salvarRegistro(self):
        self.variaveis()
        self.b.criaConexao()
        self.b.cursor.execute("""
        INSERT INTO tb_entradas(
            codigo_produto,data_entrada,qtd_entrada,valor_compra,total_compra,fornecedor,
            desc_produto,tipo_produto) VALUES (?,?,?,?,?,?,?,?)""",(self.codigo,self.data,
            self.quant,self.valor,self.total,self.fornec,self.nome,self.tipo))
        self.b.conn.commit()
        messagebox.showinfo('Informe', 'Registro salvo no banco com sucesso!')
        self.b.desconectarBanco()
        self.listarRegistro()
        self.limpaCampos()

    def listarRegistro(self):
        self.lista.delete(*self.lista.get_children())
        self.b.criaConexao()
        self.lis = self.b.cursor.execute("""
        SELECT codigo_produto,data_entrada,qtd_entrada,valor_compra,total_compra,fornecedor,
            desc_produto,tipo_produto FROM tb_entradas ORDER BY codigo_produto ASC;""")
        for i in self.lis:
            self.lista.insert('', tk.END, values = i)
        self.b.desconectarBanco()

    def selecionarRegistro(self, event):
        self.limpaCampos()
        self.lista.selection()
        for n in self.lista.selection():
            col1,col2,col3,col4,col5,col6,col7,col8 = self.lista.item(n, 'values')
            self.txt_codigo.insert(tk.END, col1)
            self.txt_data.insert(tk.END, col2)
            self.txt_quant.insert(tk.END, col3)
            self.txt_preco.insert(tk.END, col4)
            self.txt_total.insert(tk.END, col5)
            self.txt_fornec.insert(tk.END, col6)
            self.txt_desc.insert(tk.END, col7)
            self.txt_tipo.insert(tk.END, col8)

    def editarRegistro(self):
        self.variaveis()
        self.b.criaConexao()
        self.b.cursor.execute("""
        UPDATE tb_entradas SET data_entrada = ?, qtd_entrada = ?, valor_compra = ?,total_compra = ?, fornecedor = ?, desc_produto = ?, tipo_produto = ? WHERE codigo_produto = ?""", (self.data, self.quant, self.valor,self.total, self.fornec, self.nome, self.tipo, 
        self.codigo))
        self.b.conn.commit()
        messagebox.showinfo('Informe', 'Registro editado no Banco com sucesso!')
        self.b.desconectarBanco()
        self.listarRegistro()
        self.limpaCampos()

    def excluirRegistro(self):
        self.variaveis()
        self.b.criaConexao()
        self.questao = messagebox.askyesno('Excluir registro', 'Tem certeza que deseja excluir esse registro?')
        if self.questao == True:
            self.b.cursor.execute("""
            DELETE FROM tb_entradas WHERE codigo_produto=?""", (self.codigo, ))
            self.b.conn.commit()
            messagebox.showinfo('Informe', 'Registro excluído no Banco com sucesso!')
            self.b.desconectarBanco()
            self.listarRegistro()
            self.limpaCampos()
        else:
            self.app.quit()
            self.b.desconectarBanco()

    def limpaCampos(self):
        self.txt_codigo.delete(0, tk.END)
        self.txt_data.delete(0, tk.END)
        self.txt_quant.delete(0, tk.END)
        self.txt_preco.delete(0, tk.END)
        self.txt_total.delete(0, tk.END)
        self.txt_fornec.delete(0, tk.END)
        self.txt_desc.delete(0, tk.END)
        self.txt_tipo.delete(0, tk.END)
        self.txt_codigo.focus()

    def __init__(self):
        self.app = app
        self.b = Banco()
        self.telaEntrada()
        self.criarCampos()
        self.criarBotoes()
        self.criarTabela()
        self.listarRegistro()
        self.selecionarRegistro(None)
        app.mainloop()

    def telaEntrada(self):
        self.app.title('Tela entrada de produtos')
        self.app.geometry('822x500')
        self.app.resizable(FALSE, FALSE)
        self.app.config(bg='#1e3743')

    def criarCampos(self):
        self.lbl_codigo = tk.Label(self.app, text='Código Produto', bg='#1e3743',
        foreground='#ffffff', anchor='w').place(x=10, y=20, width=100, height=20)
        self.txt_codigo = tk.Entry(self.app)
        self.txt_codigo.place(x=130, y=20, width=60, height=20)

        self.lbl_data = tk.Label(self.app, text='Data Entrada', bg='#1e3743', foreground='#ffffff', anchor='w').place(
            x=280, y=20, width=90, height=20)
        self.txt_data = tk.Entry(self.app)
        self.txt_data.place(x=380, y=20, width=80, height=20)

        self.lbl_quant = tk.Label(self.app, text='Quantidade', bg='#1e3743', foreground='#ffffff', anchor='w').place(
            x=10, y=60, width=80, height=20)
        self.txt_quant = tk.Entry(self.app)
        self.txt_quant.place(x=100, y=60, width=40, height=20)

        self.lbl_preco = tk.Label(self.app, text='Preço Unit', bg='#1e3743', foreground='#ffffff', anchor='w').place(x=160, y=60, width=70, height=20)
        self.txt_preco = tk.Entry(self.app)
        self.txt_preco.place(x=240, y=60, width=70, height=20)

        self.lbl_total = tk.Label(self.app, text='Total', bg='#1e3743', foreground='#ffffff', anchor='w').place(x=340,y=60,width=60,height=20)
        self.txt_total = tk.Entry(self.app)
        self.txt_total.place(x=390, y=60, width=70, height=20)

        self.lbl_fornc = tk.Label(self.app, text='Fornecedor', bg='#1e3743', foreground='#ffffff', anchor='w').place(
            x=10, y=100, width=80, height=20)
        self.txt_fornec = tk.Entry(self.app)
        self.txt_fornec.place(x=90, y=100, width=370, height=20)

        self.lbl_desc = tk.Label(self.app, text='Descrição', bg='#1e3743', foreground='#ffffff', anchor='w').place(x=10,y=140,width=80,height=20)
        self.txt_desc = tk.Entry(self.app)
        self.txt_desc.place(x=90, y=140, width=240, height=20)

        self.lbl_tipo = tk.Label(self.app, text='Tipo', bg='#1e3743', foreground='#ffffff', anchor='w').place(x=360,y=140,width=40,height=20)
        self.txt_tipo = tk.Entry(self.app)
        self.txt_tipo.place(x=400, y=140, width=60, height=20)

    def criarBotoes(self):
        self.btn_buscar = tk.Button(self.app, text='BUSCAR').place(x=560, y=15, width=100, height=30)
        self.btn_novo = tk.Button(self.app, text='NOVO', command = self.limpaCampos).place(x=705, y=15, width=100,height=30)
        self.btn_gravar = tk.Button(self.app, text='GRAVAR', command = self.salvarRegistro).place(x=560, y=73, width=100,height=30)
        self.btn_editar = tk.Button(self.app, text='EDITAR', command = self.editarRegistro).place(x=705, y=73, width=100,height=30)
        self.btn_excluir = tk.Button(self.app, text='EXCLUIR', command = self.excluirRegistro).place(x=560, y=130,width=100, height=30)
        self.btn_voltar = tk.Button(self.app, text='VOLTAR').place(x=705, y=130, width=100, height=30)

    def criarTabela(self):
        self.lista = ttk.Treeview(self.app, height=3,column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
        self.lista.heading('#0', text='')
        self.lista.heading('#1', text='Código')
        self.lista.heading('#2', text='Data')
        self.lista.heading('#3', text='Quant')
        self.lista.heading('#4', text='Preço')
        self.lista.heading('#5', text='Total')
        self.lista.heading('#6', text='Fornecedor')
        self.lista.heading('#7', text='Descrição')
        self.lista.heading('#8', text='Tipo')

        self.lista.column('#0', width=1)
        self.lista.column('#1', width=50)
        self.lista.column('#2', width=70)
        self.lista.column('#3', width=50)
        self.lista.column('#4', width=50)
        self.lista.column('#5', width=50)
        self.lista.column('#6', width=190)
        self.lista.column('#7', width=190)
        self.lista.column('#8', width=50)

        self.lista.place(x=10, y=180, width=780, height=310)

        self.scrolLista = tk.Scrollbar(self.app, orient='vertical')
        self.lista.configure(yscroll=self.scrolLista.set)
        self.scrolLista.place(x=790, y=180, width=20, height=310)
        self.lista.bind('<Double-1>', self.selecionarRegistro)

Aplicacao()