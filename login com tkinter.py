import tkinter as tk

# Função para fazer login
def fazer_login():
    # Lógica de autenticação aqui
    print("Login realizado com sucesso!")

# Configuração da janela
janela = tk.Tk()
janela.title("Página de Login")
janela.geometry("400x200")  # Tamanho da janela

# Cores
cor_fundo = "#F65B22"  # R: 246, G: 91, B: 34
cor_botao = "#121E72"  # R: 18, G: 30, B: 114

# Configuração do fundo
fundo = tk.Frame(janela, bg=cor_fundo)
fundo.pack(fill="both", expand=True)

# Botão de login
botao_login = tk.Button(fundo, text="Login", command=fazer_login, bg=cor_botao, fg="white")
botao_login.pack(pady=20)

janela.mainloop()
