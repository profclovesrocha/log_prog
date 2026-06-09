import tkinter as tk
from tkinter import messagebox
import random

MAX_CHANCES = 5

numero_secreto = random.randint(1, 100)
chances = MAX_CHANCES

def novo_jogo():
    global numero_secreto, chances

    numero_secreto = random.randint(1, 100)
    chances = MAX_CHANCES

    entrada.config(state="normal")
    entrada.delete(0, tk.END)

    lbl_resultado.config(
        text="Digite um número entre 1 e 100",
        fg="#7fb3ff"
    )

    lbl_vidas.config(
        text="♥ ♥ ♥ ♥ ♥"
    )

    lista_palpites.delete(0, tk.END)

def verificar():
    global chances

    try:
        palpite = int(entrada.get())

        if palpite < 1 or palpite > 100:
            messagebox.showwarning(
                "Aviso",
                "Digite um número entre 1 e 100!"
            )
            return

        lista_palpites.insert(tk.END, palpite)

        if palpite == numero_secreto:

            lbl_resultado.config(
                text=f"🏆 Você acertou! O número era {numero_secreto}",
                fg="#2ecc71"
            )

            messagebox.showinfo(
                "Parabéns!",
                "Você venceu!"
            )

            entrada.config(state="disabled")
            return

        chances -= 1

        if palpite < numero_secreto:
            lbl_resultado.config(
                text="⬆️ O número é MAIOR",
                fg="#2ecc71"
            )
        else:
            lbl_resultado.config(
                text="⬇️ O número é MENOR",
                fg="#ff5c5c"
            )

        lbl_vidas.config(
            text=("♥ " * chances) +
                 ("♡ " * (MAX_CHANCES - chances))
        )

        if chances == 0:

            lbl_resultado.config(
                text=f"💀 Você perdeu! O número era {numero_secreto}",
                fg="#ff5c5c"
            )

            messagebox.showinfo(
                "Fim de jogo",
                f"O número era {numero_secreto}"
            )

            entrada.config(state="disabled")

        entrada.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um número válido!"
        )

# ===== JANELA =====

janela = tk.Tk()
janela.title("Adivinhe o Número")
janela.state("zoomed")
janela.configure(bg="#06142b")

# ===== TÍTULO =====

titulo = tk.Label(
    janela,
    text="🎯 ADIVINHE O NÚMERO",
    font=("Arial", 28, "bold"),
    bg="#06142b",
    fg="#66b3ff"
)
titulo.pack(pady=20)

subtitulo = tk.Label(
    janela,
    text="Descubra o número secreto entre 1 e 100",
    font=("Arial", 14),
    bg="#06142b",
    fg="white"
)
subtitulo.pack()

# ===== VIDAS =====

lbl_vidas = tk.Label(
    janela,
    text="♥ ♥ ♥ ♥ ♥",
    font=("Arial", 24, "bold"),
    fg="red",
    bg="#06142b"
)
lbl_vidas.pack(pady=20)

# ===== ENTRADA =====

entrada = tk.Entry(
    janela,
    font=("Arial", 20),
    justify="center",
    width=10
)
entrada.pack(pady=20)

# ===== BOTÃO =====

btn = tk.Button(
    janela,
    text="VERIFICAR",
    font=("Arial", 14, "bold"),
    bg="#1a6fff",
    fg="white",
    padx=20,
    pady=10,
    command=verificar
)
btn.pack()

# ===== RESULTADO =====

lbl_resultado = tk.Label(
    janela,
    text="Digite um número entre 1 e 100",
    font=("Arial", 16),
    bg="#06142b",
    fg="#7fb3ff"
)
lbl_resultado.pack(pady=25)

# ===== HISTÓRICO =====

titulo_hist = tk.Label(
    janela,
    text="📜 Histórico de Palpites",
    font=("Arial", 14, "bold"),
    bg="#06142b",
    fg="white"
)
titulo_hist.pack()

lista_palpites = tk.Listbox(
    janela,
    width=20,
    height=8,
    font=("Arial", 12)
)
lista_palpites.pack(pady=10)

# ===== NOVO JOGO =====

btn_novo = tk.Button(
    janela,
    text="🔄 NOVO JOGO",
    font=("Arial", 12, "bold"),
    bg="#0d4fd4",
    fg="white",
    padx=15,
    pady=8,
    command=novo_jogo
)
btn_novo.pack(pady=20)

janela.mainloop()
