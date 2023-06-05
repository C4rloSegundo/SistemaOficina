from tkinter import * 
from tkinter import Tk, ttk
from tkinter import messagebox
import tkinter as tk
import sqlite3

#----cores
c0 = "#f0f3f5" # Preto
c1 = "#feffff" # Branco 
c2 = "#3fb5a3" # Verde
c3 = "#38576b" # valor 
c4 = "#403d3d" # Letra
c5 = "#0984e3" #azul
c6 = "#f39c12" #laranja
c7 = "#2c3e50"#cinza
  

#-------inicio
class Tela:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry('310x300')
        self.janela.title('Oficina do jailson')
        self.janela.configure(background='#f0f3f5')
        self.janela.resizable(width=FALSE, height=FALSE)

        # ---- dividindo janela       
        self.frame_cima = Frame(self.janela, width=310,height=50, bg=c7, relief='flat')
        self.frame_cima.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

        self.frame_baixo = Frame(self.janela, width=310,height=250, bg=c7, relief='flat')
        self.frame_baixo.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

        # ----- configurando o frame cima 
        self.l_nome = Label(self.frame_cima, text='Oficina Jailson', anchor=NE, font=('sens 25 bold'), bg=c7, fg=c6)
        self.l_nome.place(x=5, y=5)

        self.l_linha = Label(self.frame_cima, text='', width=300, anchor=NW, font=('Ivy 1'), bg=c6, fg=c6)
        self.l_linha.place(x=3, y=45)

        # ----- configurando o frame baixo
        self.l_usuario = Label(self.frame_baixo, text='Usuário *', anchor=NW, font=('Ivy 10'), bg=c7, fg=c6)
        self.l_usuario.place(x=10, y=20)
        self.e_usuario = Entry(self.frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
        self.e_usuario.place(x=14, y=50)

        self.l_senha = Label(self.frame_baixo, text='Senha *', anchor=NW, font=('Ivy 10'), bg=c7, fg=c6)
        self.l_senha.place(x=10, y=95)
        self.e_senha = Entry(self.frame_baixo, width=25, justify='left', show='*',font=("", 15), highlightthickness=1, relief='solid')
        self.e_senha.place(x=14, y=130)

        # ----- botão 
        self.b_confirmar = Button(self.frame_baixo,text='Entrar',width=39,height=2,font=('Ivy 8 bold'), bg=c6, fg=c1, relief=RAISED, overrelief=RIDGE, command=self.verificar_dados)
        self.b_confirmar.place(x=15, y=180)

# ----- função para verificar os dados do usuário
    def verificar_dados(self):
        self.usuario_login = self.e_usuario.get()
        self.senha_login = self.e_senha.get()
            
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("SELECT * FROM funcionarios2 WHERE usuario = ? AND senha = ?", (self.usuario_login, self.senha_login))
        self.func=self.cursor.fetchone()
        if self.func:
            if self.func[4].upper() == "GERENTE":
                self.abrir_janela_gere()

            elif self.func[4].upper() == "RECEPCIONISTA":
                self.abrir_janela_recep()

            elif self.func[4].upper() == "MECANICO" or self.func[4].upper() == "MECÂNICO":
                self.abrir_janela_mec()
            
        else:
            messagebox.showwarning('Erro', 'Usuario ou senha invalidos')
#========
#=======================Janelas=========================
#------ JanelaGerente

    def abrir_janela_gere(self):
        self.janela.destroy()
        self.janela_gere = tk.Tk()
        self.janela_gere.title('Gerente')
        self.janela_gere.geometry('400x300')
        self.janela_gere.resizable(width=FALSE, height=FALSE)
        self.janela_gere.config(bg=c7)
    
        self.label_nome = tk.Label(self.janela_gere, text = 'Gerente', bg=c7, fg=c6, font=('sens 25 bold'))
        self.label_nome.pack(padx=10, pady=10)
        self.btn_gere = tk.Button(self.janela_gere, text='Gerenciar funcionarios',bg=c6, fg='black',height=2, width=20 , command=self.gerenciar_funcionarios)
        self.btn_gere.pack(padx=10, pady=10)
        self.btn_ord = tk.Button(self.janela_gere, text='Ver ordem de serviço',bg=c6, fg='black',height=2, width=20,command= self.ver_ordem)
        self.btn_ord.pack(padx=10, pady=10)
        self.btn_vis = tk.Button(self.janela_gere, text='Vizualizar clientes',bg=c6, fg='black',height=2, width=20, command=self.visualizar_clientes)
        self.btn_vis.pack(padx=10, pady=10)
#=========

#-----janelaRecep
    def abrir_janela_recep(self):
        self.janela.destroy()
        self.janela_recep = tk.Tk()
        self.janela_recep.title('Recepção')
        self.janela_recep.geometry('400x300')
        self.janela_recep.config(bg=c7)
        self.janela_recep.resizable(width=FALSE, height=FALSE)
    
        self.label_nome = tk.Label(self.janela_recep, text = 'Recepcionista', bg=c7, fg=c6, font=('sens 25 bold'))
        self.label_nome.pack(padx=20, pady=20)
        self.btn_recep = tk.Button(self.janela_recep, text='Cadastro de clientes',bg=c6, fg='black',height=2, width=20, command=self.cadastro_cliente)
        self.btn_recep.pack(padx=15, pady=15)
        self.btn_recep = tk.Button(self.janela_recep, text='Ver orçamentos',bg=c6, fg='black',height=2, width=20, command=self.criar_serviço)
        self.btn_recep.pack(padx=15, pady=15)

#====================

#----janelaMec
    def abrir_janela_mec(self):
        self.janela.destroy()
        self.janela_mec = tk.Tk()
        self.janela_mec.title('Mecânico')
        self.janela_mec.geometry('400x300')
        self.janela_mec.resizable(width=FALSE, height=FALSE)
        self.janela_mec.config(bg=c7)
    
        self.label_nome = tk.Label(self.janela_mec, text = 'Mecânico', bg=c7, fg=c6, font=('sens 25 bold'))
        self.label_nome.pack(padx=20, pady=20)
        self.btn_mec = tk.Button(self.janela_mec, text='Cadastro orçamento',bg=c6, fg='black',height=2, width=20, command=self.criar_orçamento)
        self.btn_mec.pack(padx=15, pady=15)
        self.btn_mec = tk.Button(self.janela_mec, text='Vizualizar ordem de serviço',bg=c6, fg='black',height=2, width=20, command=self.visualizar_ordem)
        self.btn_mec.pack(padx=15, pady=15)
#==========
#===================================================
#=============Funções gerente================
    #----Gerenciar funcionarios
    def ver_ordem(self):
        self.janela_ordem=Tk()
        self.janela_ordem.title('Visualizar Ordem de serviço')
        self.janela_ordem.geometry("1000x500")
       
        self.style = ttk.Style()

        self.style.theme_use('default')

        self.style.configure("Visualizar Ordem de serviço", background = "#f39c12", foreground="black", rowheight=25, fieldbackground='#f39c12')

        self.style.map('Treeview', background=[('selected', "#d35400")])

        self.tree_frame = Frame(self.janela_ordem)
        self.tree_frame.pack(pady=10)  

        self.my_tree = ttk.Treeview(self.tree_frame, selectmode="extended")
        self.my_tree.pack()    

        self.my_tree['columns'] = ("cpfc", "cpfm","valor","ser")

        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("cpfc", width=140, anchor=CENTER)
        self.my_tree.column("cpfm", width=140, anchor=CENTER)
        self.my_tree.column("valor", width=140, anchor=CENTER)
        self.my_tree.column("ser", width=140, anchor=CENTER)
      
        
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("cpfc", text="CPF_Cliente", anchor=CENTER)
        self.my_tree.heading("cpfm", text="CPF_Mecanico", anchor=CENTER)
        self.my_tree.heading("valor", text="Valor", anchor=CENTER)
        self.my_tree.heading("ser", text="Serviço", anchor= CENTER)

        
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")

        self.button_frame = LabelFrame(self.janela_ordem, text="Comandos")
        self.button_frame.pack(fill="x", expand="yes", padx=20)

        self.remove_one_button = Button(self.button_frame, text="Remover", command=self.remove_ordem)
        self.remove_one_button.grid(row=0, column=0, padx=10, pady=10)

        self.remove_one_button = Button(self.button_frame, text="Concluir", command=self.concluir_ordem)
        self.remove_one_button.grid(row=0, column=1, padx=10, pady=10)

        self.remove_one_button = Button(self.button_frame, text="Visualizar Concluidas", command=self.concluida_ordem)
        self.remove_one_button.grid(row=0, column=2, padx=10, pady=10)


        self.my_tree.bind("<ButtonRelease-1>", self.select_ordem)
        
        self.servico_database()
#-----selecionar
    def select_ordem(self, event):
        
        global values

        self.selected= self.my_tree.focus()[0]

        self.values = self.my_tree.item(self.selected, 'values')
        

#----Concluir
    def concluir_ordem(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()
        
        self.cursor.execute("INSERT INTO concluido (cpfc, cpfm, valor, ser) SELECT cpfc, cpfm, valor, ser FROM serviço WHERE cpfm= ? AND ser = ?",(self.values[1], self.values[3]))
                                
        self.banco.commit()
        self.remove_ordem()
        self.banco.close()
        
        self.cpfc_entry.delete(0, END)
        self.cpfm_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.ser_entry.delete(0, END)

        self.my_tree.delete(*self.my_tree.get_children())
        self.servico_database()

#-----Visualizar
    def concluida_ordem(self):
        self.janela_concluida=Tk()
        self.janela_concluida.title('Ordem de serviço')
        self.janela_concluida.geometry("1000x500")

        self.style = ttk.Style()

        self.style.theme_use('default')

        self.style.configure("Concluidas", background = "#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")

        self.style.map('Treeview', background=[('selected', "#347083")])

        self.tree_frame = Frame(self.janela_concluida)
        self.tree_frame.pack(pady=10)  

        self.my_tree = ttk.Treeview(self.tree_frame, selectmode="extended")
        self.my_tree.pack()    

        self.my_tree['columns'] = ("cpfc", "cpfm","valor","ser")

        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("cpfc", width=140, anchor=CENTER)
        self.my_tree.column("cpfm", width=140, anchor=CENTER)
        self.my_tree.column("valor", width=140, anchor=CENTER)
        self.my_tree.column("ser", width=140, anchor=CENTER)
      
        
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("cpfc", text="CPF_Cliente", anchor=CENTER)
        self.my_tree.heading("cpfm", text="CPF_Mecanico", anchor=CENTER)
        self.my_tree.heading("valor", text="Valor", anchor=CENTER)
        self.my_tree.heading("ser", text="Serviço", anchor= CENTER)

        
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")

        self.data_frame = LabelFrame(self.janela_concluida, text="Ordens concluidas")
        self.data_frame.pack(fill="x", expand="yes", padx=20)

        self.button_frame = LabelFrame(self.janela_concluida, text="Comandos")
        self.button_frame.pack(fill="x", expand="yes", padx=20)

        self.remove_one_button = Button(self.button_frame, text="Remover selecionado", command=self.remove_ordem)
        self.remove_one_button.grid(row=0, column=0, padx=10, pady=10)

        self.remove_all_button = Button(self.button_frame, text="remover todos", command=self.remove_ordem_all)
        self.remove_all_button.grid(row=0, column=1, padx=10, pady=10)

        self.my_tree.bind("<ButtonRelease-1>", self.select_ordem)
        
        self.concluido_database()

#----remover todas as ordens

    def remove_ordem_all(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()
        
        self.cursor.execute("DELETE from serviço ")

        self.banco.commit()
        self.banco.close()

        messagebox.showinfo("Sucesso", "A ordem de serviço foi deletada ou concluida")
        
        self.my_tree.delete(*self.my_tree.get_children())
        self.servico_database()

#---remover
    def remove_ordem(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()
        
        self.cursor.execute("DELETE from serviço WHERE cpfm=? AND ser=?", (self.values[1], self.values[3]))

        self.banco.commit()
        self.banco.close()

        messagebox.showinfo("Sucesso", "A ordem de serviço foi deletada ou concluida")
        
        self.my_tree.delete(*self.my_tree.get_children())
        self.servico_database()
            
    def gerenciar_funcionarios(self):  
        self.janela_funs=Tk()
        self.janela_funs.title('Gerenciar Funcionarios')
        self.janela_funs.geometry("1000x500")

        self.style = ttk.Style()

        self.style.theme_use('default')

        self.style.configure("Treeview", background = "#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")

        self.style.map('Treeview', background=[('selected', "#347083")])
    
        self.tree_frame = Frame(self.janela_funs)
        self.tree_frame.pack(pady=10)

        self.my_tree = ttk.Treeview(self.tree_frame, selectmode="extended")
        self.my_tree.pack()

        self.my_tree['columns'] = ("Nome", "Senha","Usuario","CPF","Cargo")

        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Nome", width=140, anchor=CENTER)
        self.my_tree.column("Senha", width=140, anchor=CENTER)
        self.my_tree.column("Usuario", width=140, anchor=CENTER)
        self.my_tree.column("CPF", width=140, anchor=CENTER)
        self.my_tree.column("Cargo", width=140, anchor=CENTER)
        

        self.my_tree.heading("#0", text="", anchor=CENTER)
        self.my_tree.heading("Nome", text="Nome", anchor=CENTER)
        self.my_tree.heading("Senha", text="Senha", anchor=CENTER)
        self.my_tree.heading("Usuario", text="Usuario", anchor=CENTER)
        self.my_tree.heading("CPF", text="CPF", anchor= CENTER)
        self.my_tree.heading("Cargo", text="Cargo", anchor=CENTER)
 
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")

        self.data_frame = LabelFrame(self.janela_funs, text="Gerenciamento de funcionarios")
        self.data_frame.pack(fill="x", expand="yes", padx=20)


        self.nome_label = Label(self.data_frame, text="Nome")
        self.nome_label.grid(row=0, column=0, padx=10, pady=10)
        self.nome_entry = Entry(self.data_frame)
        self.nome_entry.grid(row=0, column =1, padx=10, pady=10)

        self.senha_label = Label(self.data_frame, text="Senha")
        self.senha_label.grid(row=0, column=2, padx=10, pady=10)
        self.senha_entry = Entry(self.data_frame)
        self.senha_entry.grid(row=0, column =3, padx=10, pady=10)

        self.usuario_label = Label(self.data_frame, text="Usuario")
        self.usuario_label.grid(row=0, column=4, padx=10, pady=10)
        self.usuario_entry = Entry(self.data_frame)
        self.usuario_entry.grid(row=0, column =5, padx=10, pady=10)

        self.cpf_label = Label(self.data_frame, text="CPF")
        self.cpf_label.grid(row=1, column=0, padx=10, pady=10)
        self.cpf_entry = Entry(self.data_frame)
        self.cpf_entry.grid(row=1, column =1, padx=10, pady=10)

        self.cargo_label = Label(self.data_frame, text="Cargo")
        self.cargo_label.grid(row=1, column=2, padx=10, pady=10)
        self.cargo_entry = Entry(self.data_frame)
        self.cargo_entry.grid(row=1, column =3, padx=10, pady=10)

        self.button_frame = LabelFrame(self.janela_funs, text="Comandos")
        self.button_frame.pack(fill="x", expand="yes", padx=20)

        self.add_button = Button(self.button_frame, text="Adicionar", command=self.add_fun)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.remove_one_button = Button(self.button_frame, text="Remover", command=self.remove_fun)
        self.remove_one_button.grid(row=0, column=3, padx=10, pady=10)


        self.remove_one_button = Button(self.button_frame, text="Limpar campos", command=self.clear_fun)
        self.remove_one_button.grid(row=0, column=5, padx=10, pady=10)

        self.my_tree.bind("<ButtonRelease-1>", self.select_fun)
        
        self.funcionarios_database()
#-----selecionar
    def select_fun(self, event):

        self.nome_entry.delete(0, END)
        self.senha_entry.delete(0, END)
        self.usuario_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.cargo_entry.delete(0, END)
        

        self.selected= self.my_tree.focus()

        self.values = self.my_tree.item(self.selected, 'values')
        
        self.nome_entry.insert(0, self.values[0])
        self.senha_entry.insert(0, self.values[1])
        self.usuario_entry.insert(0, self.values[2])
        self.cpf_entry.insert(0, self.values[3])
        self.cargo_entry.insert(0, self.values[4])
        
    
        
#----adicionar
    def add_fun(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()

        self.cursor.execute("INSERT INTO funcionarios2 VALUES(:nome_, :senha_, :usuario_,:cpf_,:cargo_)",
                            {
        
                                'nome_': self.nome_entry.get(),
                                'senha_': self.senha_entry.get(),
                                'usuario_': self.usuario_entry.get(),
                                'cpf_': self.cpf_entry.get(),
                                'cargo_': self.cargo_entry.get()
                                
                                })
        
        messagebox.showwarning('Bem vindo', 'Novo funcionario cadastrado com sucesso')                
        self.banco.commit()
        self.cursor.close()
        

        self.nome_entry.delete(0, END)
        self.senha_entry.delete(0, END)
        self.usuario_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.cargo_entry.delete(0, END)

        self.my_tree.delete(*self.my_tree.get_children())
        self.funcionarios_database()

#---remover
    def remove_fun(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()

        self.cursor.execute("DELETE from funcionarios2 WHERE cpf=" + self.cpf_entry.get())
                            
        self.banco.commit()
        self.cursor.close()

        self.clear_fun()

        messagebox.showinfo("Apagado", "Funcionario apagado com sucesso")
        
        self.my_tree.delete(*self.my_tree.get_children())
        self.funcionarios_database()


#=================
#visualizar clientes

    def visualizar_clientes(self):

        self.janela_visu=Tk()
        self.janela_visu.title('Visualisar Clientes')
        self.janela_visu.geometry("1000x500")

        self.style = ttk.Style()

        self.style.theme_use('default')

        self.style.configure("Treeview", background = "#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")

        self.style.map('Treeview', background=[('selected', "#347083")])

        self.tree_frame = Frame(self.janela_visu)
        self.tree_frame.pack(pady=10)

        self.my_tree = ttk.Treeview(self.tree_frame, selectmode="extended")
        self.my_tree.pack()

        self.my_tree['columns'] = ("Nome","CPF", "Email","Telefone","Endereço","Placa do carro")

        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Nome", width=140, anchor=CENTER)
        self.my_tree.column("CPF", width=140, anchor=CENTER)
        self.my_tree.column("Email", width=140, anchor=CENTER)
        self.my_tree.column("Telefone", width=140, anchor=CENTER)
        self.my_tree.column("Endereço", width=140, anchor=CENTER)
        self.my_tree.column("Placa do carro", width=140, anchor=CENTER)
        
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("Nome", text="Nome", anchor=CENTER)
        self.my_tree.heading("CPF", text="CPF", anchor=CENTER)
        self.my_tree.heading("Email", text="Email", anchor=CENTER)
        self.my_tree.heading("Telefone", text="Telefone", anchor=CENTER)
        self.my_tree.heading("Endereço", text="Endereço", anchor= CENTER)
        self.my_tree.heading("Placa do carro", text="Placa do carro", anchor=CENTER)

        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")
        
        self.button_frame = LabelFrame(self.janela_visu, text="Comandos")
        self.button_frame.pack(fill="x", expand="yes", padx=20)

        self.add_button = Button(self.button_frame, text="Deletar", command=self.remove_cliente)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.my_tree.bind("<ButtonRelease-1>", self.select_cliente_gere)
        
        self.cliente_database()
        
#-----selecionar
    def select_cliente_gere(self, event):
        global values

        self.itemSelecionado = self.my_tree.selection()[0]
        self.values = self.my_tree.item(self.itemSelecionado, 'values')

        
    def select_cliente(self, event):
        self.nome_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.endereço_entry.delete(0, END)
        self.placa_entry.delete(0, END)

        self.selected= self.my_tree.focus()

        self.values = self.my_tree.item(self.selected, 'values')

        self.nome_entry.insert(0, self.values[1])

        self.cpf_entry.insert(0, self.values[2])

        self.email_entry.insert(0, self.values[3])
 
        self.telefone_entry.insert(0, self.values[4])

        self.endereço_entry.insert(0, self.values[5])

        self.placa_entry.insert(0, self.values[6])


       
#----limpar campos
    def clear_cliente(self):
        self.nome_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.endereço_entry.delete(0, END)
        self.placa_entry.delete(0, END)

    def clear_fun(self):
        self.nome_entry.delete(0, END)
        self.senha_entry.delete(0, END)
        self.usuario_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.cargo_entry.delete(0, END)

    def clear_orçamento(self):
        self.cpfc_entry.delete(0, END)
        self.cpfm_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.ser_entry.delete(0, END)

#-----remover
    def remove_cliente(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()

        self.cursor.execute("DELETE FROM clientes WHERE cpf=  "+ self.values[1])
                            
        self.banco.commit()
        self.cursor.close()

        messagebox.showinfo("Apagado", "O cliente foi removido do banco de dados")
        
        self.my_tree.delete(*self.my_tree.get_children())
        self.cliente_database()

#====================================final gerente==============
#===================funções recep===============
#cadastro cliente
    def cadastro_cliente(self):
        self.janela_cadastro=Tk()
        self.janela_cadastro.title('Cadastrar Clientes')
        self.janela_cadastro.geometry("1000x500")


        self.style = ttk.Style()

        self.style.theme_use('default')

        self.style.configure("Treeview", background = "#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")

        self.style.map('Treeview', background=[('selected', "#347083")])
   
        self.tree_frame = Frame(self.janela_cadastro)
        self.tree_frame.pack(pady=10)

        self.my_tree = ttk.Treeview(self.tree_frame, selectmode="extended")
        self.my_tree.pack()

        self.my_tree['columns'] = ("Nome","CPF", "Email","Telefone","Endereço","Placa do carro")

        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Nome", width=140, anchor=CENTER)
        self.my_tree.column("CPF", width=140, anchor=CENTER)
        self.my_tree.column("Email", width=140, anchor=CENTER)
        self.my_tree.column("Telefone", width=140, anchor=CENTER)
        self.my_tree.column("Endereço", width=140, anchor=CENTER)
        self.my_tree.column("Placa do carro", width=140, anchor=CENTER)
        

        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("Nome", text="Nome", anchor=CENTER)
        self.my_tree.heading("CPF", text="CPF", anchor=CENTER)
        self.my_tree.heading("Email", text="Email", anchor=CENTER)
        self.my_tree.heading("Telefone", text="Telefone", anchor=CENTER)
        self.my_tree.heading("Endereço", text="Endereço", anchor= CENTER)
        self.my_tree.heading("Placa do carro", text="Placa do carro", anchor=CENTER)

        
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")


        self.data_frame = LabelFrame(self.janela_cadastro, text="Cadastro de clientes")
        self.data_frame.pack(fill="x", expand="yes", padx=20)

        self.nome_label = Label(self.data_frame, text="Nome")
        self.nome_label.grid(row=0, column=0, padx=10, pady=10)
        self.nome_entry = Entry(self.data_frame)
        self.nome_entry.grid(row=0, column =1, padx=10, pady=10)

        self.cpf_label = Label(self.data_frame, text="CPF")
        self.cpf_label.grid(row=0, column=2, padx=10, pady=10)
        self.cpf_entry = Entry(self.data_frame)
        self.cpf_entry.grid(row=0, column =3, padx=10, pady=10)

        self.email_label = Label(self.data_frame, text="Email")
        self.email_label.grid(row=0, column=4, padx=10, pady=10)
        self.email_entry = Entry(self.data_frame)
        self.email_entry.grid(row=0, column =5, padx=10, pady=10)

        self.telefone_label = Label(self.data_frame, text="Telefone")
        self.telefone_label.grid(row=1, column=0, padx=10, pady=10)
        self.telefone_entry = Entry(self.data_frame)
        self.telefone_entry.grid(row=1, column =1, padx=10, pady=10)

        self.endereço_label = Label(self.data_frame, text="Endereço")
        self.endereço_label.grid(row=1, column=2, padx=10, pady=10)
        self.endereço_entry = Entry(self.data_frame)
        self.endereço_entry.grid(row=1, column =3, padx=10, pady=10)

        self.placa_label = Label(self.data_frame, text="Placa do carro")
        self.placa_label.grid(row=1, column=4, padx=10, pady=10)
        self.placa_entry = Entry(self.data_frame)
        self.placa_entry.grid(row=1, column =5, padx=10, pady=10)
 
        self.button_frame = LabelFrame(self.janela_cadastro, text="Comandos")
        self.button_frame.pack(fill="x", expand="yes", padx=20)

        self.add_button = Button(self.button_frame, text="Adicionar", command=self.add_cliente)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

    
        self.remove_one_button = Button(self.button_frame, text="Limpar campos", command=self.clear_cliente)
        self.remove_one_button.grid(row=0, column=4, padx=10, pady=10)

        self.my_tree.bind("<ButtonRelease-1>", self.select_cliente)
        
        self.cliente_database()
#-----selecionar
    def select_cliente(self, event):

        self.nome_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.endereço_entry.delete(0, END)
        self.placa_entry.delete(0, END)


        self.selected= self.my_tree.focus()

        self.values = self.my_tree.item(self.selected, 'values')


        self.nome_entry.insert(0, self.values[0])

        self.cpf_entry.insert(0, self.values[1])

        self.email_entry.insert(0, self.values[2])

        self.telefone_entry.insert(0, self.values[3])

        self.endereço_entry.insert(0, self.values[4])

        self.placa_entry.insert(0, self.values[5])

       

#----adicionar
    def add_cliente(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()

        self.cursor.execute("INSERT INTO clientes VALUES(:nome_,:cpf_,:email_,:telefone_,:endereço_,:placa_)",
                            {
                                'nome_': self.nome_entry.get(),
                                'cpf_': self.cpf_entry.get(),
                                'email_': self.email_entry.get(),
                                'telefone_': self.telefone_entry.get(),
                                'endereço_': self.endereço_entry.get(),
                                'placa_': self.placa_entry.get()
                                })
                            
        messagebox.showwarning('Sucesso', 'O novo cliente foi cadastrado com sucesso')
        self.banco.commit()
        self.cursor.close()
        
        self.nome_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.endereço_entry.delete(0, END)
        self.placa_entry.delete(0, END)

        self.my_tree.delete(*self.my_tree.get_children())
        self.cliente_database()


#====================== final cadastro clientes
#ordem de serviço
    def criar_serviço(self):
        self.janela_trans=Tk()
        self.janela_trans.title('Ver orçamento')
        self.janela_trans.geometry("1000x500")

        self.style = ttk.Style()

        self.style.theme_use('default')

        self.style.configure("Treeview", background = "#D3D3D3", foreground="black", rowheight=20, fieldbackground="#D3D3D3")

        self.style.map('Treeview', background=[('selected', "#347083")])

        
        self.tree_frame = Frame(self.janela_trans)
        self.tree_frame.pack(pady=10)

        self.my_tree = ttk.Treeview(self.tree_frame, selectmode="extended")
        self.my_tree.pack()


        self.my_tree['columns'] = ("cpfc","cpfm", "valor","ser")

        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("cpfc", width=100, anchor=CENTER)
        self.my_tree.column("cpfm", width=140, anchor=CENTER)
        self.my_tree.column("valor", width=140, anchor=CENTER)
        self.my_tree.column("ser", width=140, anchor=CENTER)
        

        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("cpfc", text="CPF Cliente", anchor=CENTER)
        self.my_tree.heading("cpfm", text="CPF Mêcanico", anchor=CENTER)
        self.my_tree.heading("valor", text="Valor", anchor=CENTER)
        self.my_tree.heading("ser", text="Serviço", anchor=CENTER)
       
        
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")

        self.button_frame = LabelFrame(self.janela_trans, text="Comandos")
        self.button_frame.pack(fill="x", expand="yes", padx=20)

        self.add_button = Button(self.button_frame, text="Transformar em ordem de serviço", command=self.transformar )
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.remove_one_button = Button(self.button_frame, text="Remover", command=self.remove_orçamento)
        self.remove_one_button.grid(row=0, column=3, padx=10, pady=10)


        self.my_tree.bind("<ButtonRelease-1>", self.select_orçamento_recep)
        

        self.orçamento_database()
#-----selecionar
    def select_orçamento(self, event):
        self.cpfc_entry.delete(0, END)
        self.cpfm_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.ser_entry.delete(0, END)

        self.selected= self.my_tree.focus()

        self.values = self.my_tree.item(self.selected, 'values')
        
        self.cpfc_entry.insert(0, self.values[0])
        self.cpfc_entry.config(state = DISABLED)
        self.cpfm_entry.insert(0, self.values[1])
        self.cpfm_entry.config(state = DISABLED)
        self.valor_entry.insert(0, self.values[2])
        self.valor_entry.config(state = DISABLED)
        self.ser_entry.insert(0, self.values[3])
        self.ser_entry.config(state = DISABLED)
        
    def select_orçamento_recep(self, event):
        global values
        self.itemSelecionado = self.my_tree.selection()[0]
        self.values = self.my_tree.item(self.itemSelecionado, 'values')
        

#----adicionar
    def transformar(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()

        self.cursor.execute("INSERT INTO serviço (cpfc, cpfm, valor, ser) SELECT cpfc, cpfm, valor, ser FROM orçamento WHERE cpfm=? AND ser=?",(self.values[1], self.values[3]))
                                
        self.banco.commit()
        self.remove_orçamento()
        self.banco.close()
        

        self.my_tree.delete(*self.my_tree.get_children())
        self.orçamento_database()

#---remover
    def remove_orçamento(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()

        self.cursor.execute("DELETE FROM orçamento WHERE cpfm=? AND ser=?",(self.values[1], self.values[3]))

        self.banco.commit()


        messagebox.showinfo("Sucesso", "O orçamento foi removido ou alterado")
        
        self.my_tree.delete(*self.my_tree.get_children())
        self.orçamento_database()
#============= final ordem de serviço



#================funções mec==============
#===============Ver Ordem de serviço]
    def visualizar_ordem(self):
        self.janela_mec_visu=Tk()
        self.janela_mec_visu.title('Treeview')
        self.janela_mec_visu.geometry("1000x550")

        self.style = ttk.Style()

        self.style.theme_use('default')

        self.style.configure("Treeview", background = "#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")

        self.style.map('Treeview', background=[('selected', "#347083")])

        
        self.tree_frame = Frame(self.janela_mec_visu)
        self.tree_frame.pack(pady=10)        

        self.my_tree = ttk.Treeview(self.tree_frame, selectmode="extended")
        self.my_tree.pack()
       
        self.my_tree['columns'] = ("cpfc", "cpfm","valor","ser")

        self.my_tree.column("#0", width=0, stretch=NO) 
        self.my_tree.column("cpfc", width=140, anchor=CENTER)
        self.my_tree.column("cpfm", width=140, anchor=CENTER)
        self.my_tree.column("valor", width=140, anchor=CENTER)
        self.my_tree.column("ser", width=140, anchor=CENTER)
        
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("cpfc", text="CPF Cliente", anchor=CENTER)
        self.my_tree.heading("cpfm", text="CPF Mecânico", anchor=CENTER)
        self.my_tree.heading("valor", text="Valor", anchor=CENTER)
        self.my_tree.heading("ser", text="Serviço", anchor= CENTER)
        
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")

        self.button_frame = LabelFrame(self.janela_mec_visu, text="Comandos")
        self.button_frame.pack(fill="x", expand="yes", padx=20)

        self.pesquisar_button = Button(self.button_frame, text="Pesquisar", command=self.pesquisar)
        self.pesquisar_button.grid(row=0, column=0, padx=10, pady=10)

        self.pesquisar_button = Button(self.button_frame, text="Voltar", command=self.voltar_ordem)
        self.pesquisar_button.grid(row=0, column=1, padx=10, pady=10)

        self.servico_database()
        

#----pesquisar
    def pesquisar(self):
        global search_entry, search_janela
        self.search_janela = Toplevel(self.janela_mec_visu)
        self.search_janela.title("Pesquisar Ordem de serviço")
        self.search_janela.geometry("400x200")

        self.search_frame = LabelFrame(self.search_janela, text="CPF do Mêcanico")
        self.search_frame.pack(padx=10, pady=10)

        self.search_entry=Entry(self.search_frame)
        self.search_entry.pack(padx=20, pady=20)

        self.search_button = Button(self.search_janela, text="Ver ordem", command=self.pesquisar_ordem)
        self.search_button.pack(padx=20, pady=20)
        
    def pesquisar_ordem(self):
        self.pesquisar= self.search_entry.get()
        self.search_janela.destroy()
        
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()

        self.cursor.execute("SELECT * from serviço WHERE cpfm = ?", (self.pesquisar,))
       
        self.records = self.cursor.fetchall()

        global count
        self.count = 0


        for self.record in self.records:
            if self.count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3]), tags=('evenrow',))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3]), tags=('oddrow',))

            self.count +=1

        self.banco.commit()
        self.cursor.close()
        
    def voltar_ordem(self):        
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()

        self.cursor.execute("SELECT * from serviço")
       
        self.records = self.cursor.fetchall()

        global count
        self.count = 0

        for self.record in self.records:
            if self.count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3]), tags=('evenrow',))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3]), tags=('oddrow',))

            self.count +=1

        self.banco.commit()
        self.cursor.close()

#===========criar orçamento
    def criar_orçamento(self):
        self.janela_orçamento=Tk()
        self.janela_orçamento.title('Orçamento')
        self.janela_orçamento.geometry("1000x500")

        self.style = ttk.Style()

        self.style.theme_use('default')

        self.style.configure("Treeview", background = "#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")

        self.style.map('Treeview', background=[('selected', "#347083")])

        
        self.tree_frame = Frame(self.janela_orçamento)
        self.tree_frame.pack(pady=10)


        self.my_tree = ttk.Treeview(self.tree_frame, selectmode="extended")
        self.my_tree.pack()


        self.my_tree['columns'] = ("cpfc", "cpfm","valor","ser")

        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("cpfc", width=140, anchor=CENTER)
        self.my_tree.column("cpfm", width=140, anchor=CENTER)
        self.my_tree.column("valor", width=100, anchor=CENTER)
        self.my_tree.column("ser", width=170, anchor=CENTER)

        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("cpfc", text="CPF Cliente", anchor=CENTER)
        self.my_tree.heading("cpfm", text="CPF Mecânico", anchor=CENTER)
        self.my_tree.heading("valor", text="Valor", anchor=CENTER)
        self.my_tree.heading("ser", text="Serviço", anchor= CENTER)
        

        
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")


        self.data_frame = LabelFrame(self.janela_orçamento, text="Cadastrar orçamento")
        self.data_frame.pack(fill="x", expand="yes", padx=20)

        self.cpfc_label = Label(self.data_frame, text="CPF Cliente")
        self.cpfc_label.grid(row=0, column=0, padx=10, pady=10)
        self.cpfc_entry = Entry(self.data_frame)
        self.cpfc_entry.grid(row=0, column =1, padx=10, pady=10)

        self.cpfm_label = Label(self.data_frame, text="CPF Mecanico")
        self.cpfm_label.grid(row=0, column=2, padx=10, pady=10)
        self.cpfm_entry = Entry(self.data_frame)
        self.cpfm_entry.grid(row=0, column =3, padx=10, pady=10)

        self.valor_label = Label(self.data_frame, text="Valor")
        self.valor_label.grid(row=1, column=0, padx=10, pady=10)
        self.valor_entry = Entry(self.data_frame)
        self.valor_entry.grid(row=1, column =1, padx=10, pady=10)

        self.ser_label = Label(self.data_frame, text="Descrição do serviço")
        self.ser_label.grid(row=1, column=2, padx=10, pady=10)
        self.ser_entry = Entry(self.data_frame)
        self.ser_entry.grid(row=1, column =3, padx=10, pady=10)

        self.button_frame = LabelFrame(self.janela_orçamento, text="Comandos")
        self.button_frame.pack(fill="x", expand="yes", padx=20)

        self.add_button = Button(self.button_frame, text="Adicionar", command=self.add_orçamento)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.remove_one_button = Button(self.button_frame, text="Limpar campos", command=self.clear_orçamento)
        self.remove_one_button.grid(row=0, column=4, padx=10, pady=10)

        self.my_tree.bind("<ButtonRelease-1>", self.select_orçamento)
        

        self.orçamento_database()
#-----selecionar
    def select_orçamento(self, event):
        self.cpfc_entry.delete(0, END)
        self.cpfm_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.ser_entry.delete(0, END)


        self.selected= self.my_tree.focus()

        self.values = self.my_tree.item(self.selected, 'values')
        
        self.cpfc_entry.insert(0, self.values[0])
        self.cpfm_entry.insert(0, self.values[1])
        self.valor_entry.insert(0, self.values[2])
        self.ser_entry.insert(0, self.values[3])
        
       


#----adicionar
    def add_orçamento(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()

        self.cursor.execute("INSERT INTO orçamento VALUES(:cpfc_, :cpfm_, :valor_,:ser_)",
                            {
                                'cpfc_': self.cpfc_entry.get(),
                                'cpfm_': self.cpfm_entry.get(),
                                'valor_': self.valor_entry.get(),
                                'ser_': self.ser_entry.get()
                                })
                            


        self.banco.commit()
        self.cursor.close()
        
        self.cpfc_entry.delete(0, END)
        self.cpfm_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.ser_entry.delete(0, END)


        self.my_tree.delete(*self.my_tree.get_children())
        self.orçamento_database()

#================final criar orçamento







#==============banco de dados============
#Bancos de dados(orçamento)
    def orçamento_database(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("SELECT * from orçamento")
        self.records = self.cursor.fetchall()
        global count
        self.count = 0
        for self.record in self.records:
            if self.count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3]), tags=('evenrow',))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3]), tags=('oddrow',))
            self.count +=1
        self.banco.commit()
        self.cursor.close()
#Bancos de dados(clientes)
    def cliente_database(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()  
        self.cursor.execute("SELECT * from clientes")       
        self.records = self.cursor.fetchall()
        global count
        self.count = 0
        for self.record in self.records:
            if self.count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3], self.record[4], self.record[5]), tags=('evenrow',))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3], self.record[4], self.record[5]), tags=('oddrow',))
            self.count +=1
        self.banco.commit()
        self.cursor.close()
#Bancos de dados(funcionarios)
    def funcionarios_database(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()    
        self.cursor.execute("SELECT * from funcionarios2")      
        self.records = self.cursor.fetchall()
        global count
        self.count = 0
        for self.record in self.records:
            if self.count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3], self.record[4]), tags=('evenrow',))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3], self.record[4]), tags=('oddrow',))
            self.count +=1
        self.banco.commit()
        self.cursor.close()
    def concluido_database(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("SELECT * from concluido")
        self.records = self.cursor.fetchall()
        global count
        self.count = 0
        for self.record in self.records:
            if self.count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3]), tags=('evenrow',))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3]), tags=('oddrow',))
            self.count +=1
        self.banco.commit()
        self.cursor.close()
    def servico_database(self):
        self.banco = sqlite3.connect('banco_jailson.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("SELECT * from serviço")
        self.records = self.cursor.fetchall()
        global count
        self.count = 0
        for self.record in self.records:
            if self.count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3]), tags=('evenrow',))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.count, text='', values=(self.record[0], self.record[1], self.record[2], self.record[3]), tags=('oddrow',))
            self.count +=1
        self.banco.commit()
        self.cursor.close()


        mainloop()

t = Tela()
