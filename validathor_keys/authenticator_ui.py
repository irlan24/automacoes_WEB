import customtkinter as ctk
import threading
import time
from validathor_keys import DataBase


class AuthenticatorUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        

        # Configurações da janela
        self.title("Autenticação")
        self.geometry("350x350")
        self.resizable(True, True)  # Responsivo

        # Fonte padrão para labels
        self.label_font = ctk.CTkFont(family="Arial", size=15, weight="bold")

        # Criar elementos da interface
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Configuração para responsividade
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Label de instrução
        self.label_title = ctk.CTkLabel(
            self.frame, text="Valide sua chave", font=self.label_font
        )
        self.label_title.grid(row=0, column=0, pady=(10, 20), sticky="n")

        # Campo de entrada
        self.entry_key = ctk.CTkEntry(
            self.frame, placeholder_text="Digite a chave", width=200
        )
        self.entry_key.grid(row=1, column=0, pady=10, sticky="n")

        # Botão de envio
        self.btn_submit = ctk.CTkButton(
            self.frame, text="Submit", command=self.submit_key, font=self.label_font
        )
        self.btn_submit.grid(row=2, column=0, pady=10, sticky="n")

        # Label de notificação (inclui loader animado)
        self.label_notification = ctk.CTkLabel(
            self.frame, text="", font=self.label_font
        )
        self.label_notification.grid(row=3, column=0, pady=(20, 0), sticky="n")

    def submit_key(self):
        """Inicia o processo com animação de carregamento"""
        self.btn_submit.configure(state="disabled")  # desabilita botão durante execução
        self.label_notification.configure(text="Carregando")
        threading.Thread(target=self.animar_loader).start()
        threading.Thread(target=self.validar_chave).start()

    def animar_loader(self):
        """Anima o texto 'Carregando...' com pontos"""
        for _ in range(20):  # ~10 segundos de animação
            for pontos in ["", ".", "..", "..."]:
                if self.label_notification.cget("text") not in ["Chave válida e ativa!", "Chave inválida ou inativa!"]:
                    self.label_notification.configure(text=f"Carregando{pontos}", text_color="light blue")
                    time.sleep(0.5)
                else:
                    return  # Para animação se já tiver resultado

    def validar_chave(self):
        """Validação da chave"""
        
        chave = self.entry_key.get().strip()
        
        if DataBase().consultar_chave(chave):
            self.label_notification.configure(text="Chave válida e ativa!", text_color="green")
        else:
            self.label_notification.configure(text="Chave inválida ou inativa!", text_color="red")
        self.btn_submit.configure(state="normal")  # reabilita botão



if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")  # ou "Dark", "Light"
    ctk.set_default_color_theme("blue")

    AuthenticatorUI().mainloop()
    
