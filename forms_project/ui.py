# ui.py
# Interface gráfica com CustomTkinter

import customtkinter as ctk
import threading
import webbrowser
from constants import (
    ALL_ANALYSTS, PRODUTOS, ASSUNTOS, FIELDS_CONFIG, 
    CANAL_ENTRADA_OPTIONS, FILAS_CONFIG, CAC_OPTIONS, PENDING_OPTIONS
)
from automation import WebAutomation


class FormsApp:
    def __init__(self):
        self.setup_ui()
        self.automation = WebAutomation()
        
    def setup_ui(self):
        """Configura a interface do usuário"""
        # Configurações básicas
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme("green")
        
        self.app = ctk.CTk()
        self.app.title('Forms')
        self.app.geometry("1210x685")
        
        self.fonte = ctk.CTkFont(family="Arial", size=15, weight="bold", slant="italic", underline=True)
        
        # Cria os containers principais
        self.create_main_containers()
        self.create_form_fields()
        self.create_history_section()
        self.create_login_section()
        self.create_entry_section()
        self.create_special_configs()
        self.create_pending_section()
        self.select_button_pending()
        self.create_signature()
        self.create_version()
        
    def create_main_containers(self):
        """Cria os containers principais da interface"""
        self.box_frame_center = ctk.CTkFrame(master=self.app, corner_radius=10)
        self.box_frame_center.grid(row=1, column=1, padx=15, pady=10, sticky='ns')
        
        self.box_frame_left = ctk.CTkFrame(master=self.app, corner_radius=10)
        self.box_frame_left.grid(row=1, column=0, padx=10, pady=10, sticky='ns')
        
        self.box_frame_right = ctk.CTkFrame(self.app, corner_radius=10)
        self.box_frame_right.grid(row=1, column=3, padx=10, pady=10, sticky="ns")
        
        self.box_pending = ctk.CTkFrame(self.app, corner_radius=10)
        self.box_pending.grid(row=1, column=4, padx=10, pady=10, sticky="ns")

    def create_signature(self):
        """Cria assinatura do desenvolvedor"""
        self.assinatura = ctk.CTkLabel(self.app, text="Desenvolvido por: Irlan Nonato (Click para conhecer)", 
                                     font=("Arial", 11, "bold"), text_color="red", cursor="hand2")
        self.assinatura.grid(row=0, column=0, padx=5, pady=2, sticky="w")

        self.assinatura.bind("<Button-1>", self.link_external)
        self.assinatura.bind("<Enter>", self.link_external_on)
        self.assinatura.bind("<Leave>", self.link_external_off)

    def create_version(self):
        """Cria label da versão"""
        self.version = ctk.CTkLabel(self.app, text="Version: v2.0", font=("Arial", 11, "bold"), text_color="red")
        self.version.grid(row=0, column=4, padx=10, pady=2, sticky="e")
        
    def create_form_fields(self):
        """Cria os campos do formulário principal"""
        self.campos = {}
        
        for field_name, config in FIELDS_CONFIG.items():
            # Label
            label = ctk.CTkLabel(self.box_frame_center, text=config['label'], font=("Arial", 13, "bold"))
            label.grid(row=config['row_label'], column=0, pady=3, padx=10, sticky="n")
            
            # Campo de entrada
            campo = ctk.CTkEntry(self.box_frame_center, width=250, placeholder_text=config['placeholder'])
            campo.grid(row=config['row_field'], column=0, pady=5, padx=10, sticky="n")
            
            self.campos[field_name] = campo
        
        # Botão e elementos de controle
        self.submit = ctk.CTkButton(self.box_frame_center, text='ENVIAR', command=self.load)
        self.submit.grid(row=8, column=0, pady=8, padx=10)
        
        self.progress_bar = ctk.CTkProgressBar(self.box_frame_center, width=200, corner_radius=10, 
                                             progress_color="green", border_width=10, fg_color="blue", height=10)
        
        self.invisible_element = ctk.CTkLabel(self.box_frame_center, text='', font=("Arial", 15, "bold"))
        self.invisible_element.grid(row=9, column=0, pady=4, padx=10, sticky="ns")
        
    def create_history_section(self):
        """Cria a seção de histórico de casos"""
        self.box_history_section = ctk.CTkFrame(self.box_frame_left, corner_radius=10, width=210, height=180)
        self.box_history_section.grid(padx=10, pady=10)
        self.box_history_section.grid_propagate(False)

        label_title = ctk.CTkLabel(self.box_history_section, text='HISTÓRICO DE CASOS', font=self.fonte)
        label_title.grid(row=0, column=0, pady=2, padx=10, sticky="nswe")

        # Quantificador de casos realizados
        self.list_quantificador = []
        font_quantificador = ctk.CTkFont(family="Arial", size=12, weight="bold", slant="italic", underline=False)

        self.label_quant_case = ctk.CTkLabel(self.box_history_section, 
                                           text=f'Nº de casos concluídos: {len(self.list_quantificador)}', 
                                           font=font_quantificador)
        self.label_quant_case.grid(row=1, column=0, pady=1, padx=10, sticky="nswe")

        box_list_case = ctk.CTkScrollableFrame(self.box_history_section, width=180)
        box_list_case.grid(row=2, column=0, padx=2, pady=3, sticky="n")

        # Botão para limpar histórico
        ctk.CTkButton(self.box_frame_left, text="Limpar histórico", 
                     command=self.delete_historic_case).grid(row=1, column=0, pady=5, padx=15, sticky="nsew")
        
        self.entry_list_case = ctk.CTkTextbox(box_list_case, font=("Arial", 13, "bold"), state="disabled")
        self.entry_list_case.grid(row=0, column=0, pady=10, sticky="w")
        
    def create_login_section(self):
        """Cria a seção de login"""
        box_frame_login = ctk.CTkFrame(self.box_frame_left, corner_radius=10)
        box_frame_login.grid(row=2, column=0, padx=10, pady=5, sticky='s')
        
        label_title_login = ctk.CTkLabel(box_frame_login, text='ACESSO DO ANALISTA', font=self.fonte)
        label_title_login.grid(row=0, column=0, pady=8, padx=10, sticky="n")
        
        self.box_login = ctk.CTkFrame(box_frame_login, corner_radius=10)
        self.box_login.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        
        # Email
        ctk.CTkLabel(self.box_login, text="Email:", font=("Arial", 11, "bold")).grid(row=0, column=0, pady=8, padx=5, sticky="w")
        self.campo_email = ctk.CTkEntry(self.box_login, placeholder_text='Digite seu email...')
        self.campo_email.grid(row=0, column=1, pady=8, padx=5, sticky="w")
        
        # Senha
        ctk.CTkLabel(self.box_login, text="Senha:", font=("Arial", 11, "bold")).grid(row=1, column=0, pady=8, padx=5, sticky="w")
        self.campo_senha = ctk.CTkEntry(self.box_login, placeholder_text='Digite sua senha...', show="*")
        self.campo_senha.grid(row=1, column=1, pady=8, padx=5, sticky="w")
        
        self.label_invisible_login = ctk.CTkLabel(box_frame_login, text='', font=("Arial", 15, "bold"))
        self.label_invisible_login.grid(row=2, column=0, pady=8, padx=5, sticky="w")

    def create_entry_section(self):
        """Cria a seção do canal de entrada"""        
        ctk.CTkLabel(self.box_frame_left, text='CANAL DE ENTRADA', font=self.fonte).grid(row=3, column=0, pady=2, padx=10, sticky="nswe")

        self.box_entry_section = ctk.CTkFrame(self.box_frame_left, corner_radius=10)
        self.box_entry_section.grid(row=4, column=0, pady=1, padx=20, sticky="nsew")

        self.opcao_selecionada = None
        self.botoes = {}

        for i, opcao in enumerate(CANAL_ENTRADA_OPTIONS):
            botao = ctk.CTkButton(self.box_entry_section, text=opcao, command=lambda o=opcao: self.selecionar(o))
            botao.grid(row=i, column=0, padx=10, pady=4, sticky='nswe')
            self.botoes[opcao] = botao

    def selecionar(self, opcao):
        """Seleciona opção de canal de entrada"""
        self.opcao_selecionada = opcao
        for chave, valor in self.botoes.items():
            if chave == opcao:
                valor.configure(fg_color="green")
            else:
                valor.configure(fg_color="gray")
        self.canal_entrada = self.opcao_selecionada
        
    def create_special_configs(self):
        """Cria a seção de configurações especiais"""
        ctk.CTkLabel(self.box_frame_right, text='CONFIGURAÇÕES ESPECIAIS', font=self.fonte).grid(row=0, column=0, pady=8, padx=30)
        
        # Container principal para radios
        box_frame = ctk.CTkFrame(self.box_frame_right, corner_radius=10)
        box_frame.grid(row=1, column=0)
        
        # Radios principais
        self.especial_radios = ctk.StringVar(value="finalizado")
        
        ctk.CTkRadioButton(box_frame, text="Finalizado", variable=self.especial_radios, 
                          value="finalizado", command=self.handle_status_change).grid(row=0, column=0, pady=10, padx=10)
        
        ctk.CTkRadioButton(box_frame, text="Transferido", variable=self.especial_radios, 
                          value="transferido", command=self.handle_status_change).grid(row=0, column=1, pady=10, padx=10)

        # Container para filas
        self.box_frame_1 = ctk.CTkFrame(self.box_frame_right, corner_radius=10)
        self.filas = ctk.StringVar(value='')
        
        for i, (text, value) in enumerate(FILAS_CONFIG):
            radio = ctk.CTkRadioButton(self.box_frame_1, text=text, variable=self.filas, 
                                     value=value, command=self.handle_fila_change)
            radio.grid(row=i, column=0, pady=10, padx=10, sticky="w")

        # Container para opções CAC
        self.box_frame_2 = ctk.CTkFrame(self.box_frame_right, corner_radius=10)
        self.option_resolution = ctk.StringVar(value='')
        
        for i, (text, value) in enumerate(CAC_OPTIONS):
            radio = ctk.CTkRadioButton(self.box_frame_2, text=text, variable=self.option_resolution, value=value)
            radio.grid(row=i, column=0, pady=10, padx=10, sticky="w")
    
    def handle_status_change(self):
        """Gerencia mudanças no status (finalizado/transferido)"""
        if self.especial_radios.get() == "transferido":
            self.box_frame_1.grid(row=2, column=0, pady=20, sticky="nsew")
            self.box_select_pending.grid_forget()
            self.pending_radios.set("Não")
            self.radio_yes.configure(state="disabled")
        else:
            self.radio_yes.configure(state="normal")
            self.box_frame_1.grid_forget()
            self.box_frame_2.grid_forget()
            
    def handle_fila_change(self):
        """Gerencia mudanças na seleção de fila"""
        if self.filas.get() == 'span[aria-label="CAC"]':
            self.box_frame_2.grid(row=3, column=0, pady=10, sticky="nsew")
        else:
            self.box_frame_2.grid_forget()

    def create_pending_section(self):
        """Cria a seção de configurações de pendências do caso"""
        ctk.CTkLabel(self.box_pending, text='PENDÊNCIAS DE CASOS', font=self.fonte).grid(row=0, column=0, pady=8, padx=30)

        # Container para Pendentes
        box_pending = ctk.CTkFrame(self.box_pending, corner_radius=10)
        box_pending.grid(row=1, column=0, pady=3, padx=4)

        # Radios pending
        self.pending_radios = ctk.StringVar(value="Não")
        
        ctk.CTkRadioButton(box_pending, text="Não", variable=self.pending_radios, 
                          value="Não", command=self.handle_pending_change).grid(row=0, column=0, pady=2, padx=(4, 5))
        
        self.radio_yes = ctk.CTkRadioButton(box_pending, text="Sim", variable=self.pending_radios, 
                          value="Sim", command=self.handle_pending_change)
        self.radio_yes.grid(row=0, column=1, pady=2, padx=(5, 4))

        # Box das seleções de pendências dos casos
        self.box_select_pending = ctk.CTkFrame(self.box_pending, corner_radius=10)

    def select_button_pending(self):
        """Cria botões para seleção de pendências"""
        self.selected_option = None
        self.buttons_pending = {}

        for i, opcao in enumerate(PENDING_OPTIONS):
            botao = ctk.CTkButton(self.box_select_pending, text=opcao, command=lambda o=opcao: self.select(o))
            botao.grid(row=i, column=0, padx=10, pady=4, sticky='nswe')
            self.buttons_pending[opcao] = botao

    def select(self, opcao):
        """Seleciona opção de pendência"""
        self.selected_option = opcao
        for chave, valor in self.buttons_pending.items():
            if chave == opcao:
                valor.configure(fg_color="green")
            else:
                valor.configure(fg_color="gray")
        self.pending_value = self.selected_option

    def handle_pending_change(self):
        """Gerencia mudanças no status (Pendente/Finalizado)"""
        if self.pending_radios.get() == "Sim":
            self.box_select_pending.grid(row=2, column=0, pady=5, padx=5, sticky="nsew")
        else:
            self.box_select_pending.grid_forget()

    def get_analista_name(self, email):
        """Retorna o nome do analista baseado no email"""
        return ALL_ANALYSTS.get(email, "")
    
    def validate_and_get_options(self, produto_val, assunto_val):
        """Valida e retorna as opções de produto e assunto"""
        try:
            produto_num = int(produto_val)
            assunto_num = int(assunto_val)
            
            if produto_num not in PRODUTOS:
                raise ValueError("Produto inválido")
            if assunto_num not in ASSUNTOS:
                raise ValueError("Assunto inválido")
                
            return PRODUTOS[produto_num], ASSUNTOS[assunto_num]
            
        except (ValueError, KeyError):
            return None, None
    
    def show_error(self, message):
        """Exibe mensagem de erro e reabilita interface"""
        self.invisible_element.configure(text=message, text_color="red")
        self.progress_bar.stop()
        self.progress_bar.grid_forget()
        self.submit.configure(state='normal')
        self.automation.quit_browser()
    
    def show_success(self, message, num_caso):
        """Exibe mensagem de sucesso e salva caso"""
        self.progress_bar.stop()
        self.progress_bar.grid_forget()
        self.box_frame_1.grid_forget()
        self.box_frame_2.grid_forget()
        self.especial_radios.set("finalizado")
        self.texto_temporario(message, "green")
        self.submit.configure(state='normal')
        self.save_case(num_caso)
        self.pending_radios.set("Não")
        self.automation.quit_browser()
    
    def load(self):
        """Inicia o processo de carregamento"""
        self.invisible_element.configure(text='CARREGANDO...', text_color="green")
        self.submit.configure(state="disabled")
        self.progress_bar.grid(row=10, column=0, pady=4, padx=7, sticky="ns")
        self.progress_bar.start()
        threading.Thread(target=self.forms, daemon=True).start()
    
    def texto_temporario(self, text_display='', color_display=''):
        """Exibe texto temporário"""
        self.invisible_element.configure(text=text_display, text_color=color_display)
        self.app.after(7000, lambda: self.invisible_element.configure(text=''))
    
    def save_case(self, case):
        """Salva o caso no histórico"""
        self.entry_list_case.configure(state="normal")
        self.entry_list_case.insert("1.0", case + "\n")
        self.entry_list_case.configure(state="disabled")

        # Incrementa o quantificador de casos
        self.list_quantificador.append(case)
        self.label_quant_case.configure(text=f'Nº de casos concluídos: {len(self.list_quantificador)}')

    def delete_historic_case(self):
        """Deleta o histórico dos casos"""
        self.entry_list_case.configure(state="normal")
        self.entry_list_case.delete("1.0", "end")
        self.entry_list_case.configure(state="disabled")

        # Atualiza o quantificador dos casos
        self.list_quantificador.clear() 
        self.label_quant_case.configure(text=f'Nº de casos concluídos: {len(self.list_quantificador)}')

    def link_external(self, event=None):
        """Abre link externo"""
        webbrowser.open("https://www.linkedin.com/in/irlan24/")

    def link_external_on(self, event):
        """Evento mouse enter"""
        self.assinatura.configure(text_color="light blue")
    
    def link_external_off(self, event):
        """Evento mouse leave"""
        self.assinatura.configure(text_color="red")

    def handle_case_flow(self, data):
        """Decide se o caso é Transferido, Pendente ou Finalizado"""
        try:
            if self.especial_radios.get() == "transferido":
                self.automation.handle_transfer(
                    self.filas.get(), 
                    self.option_resolution.get() if self.filas.get() == 'span[aria-label="CAC"]' else None
                )
            elif self.pending_radios.get() == "Sim":
                self.automation.handle_pending(self.pending_value)
            else:
                self.automation.handle_close()
            
            # Submete o formulário
            if self.automation.submit_form():
                self.show_success("Formulário enviado com sucesso!", data["num_caso"])
            else:
                self.show_error("Formulário não foi ENVIADO!")
                
        except Exception as e:
            self.show_error(f"Erro durante processamento: {str(e)}")
    
    def forms(self):
        """Função principal que executa todo o processo"""
        # Coleta dados dos campos
        num_caso = self.campos['caso'].get()
        num_cpf = self.campos['cpf'].get()
        email_analista = self.campo_email.get()
        
        # Validações básicas
        if not all([num_caso, num_cpf, email_analista]):
            self.show_error("Preencha todos os campos obrigatórios!")
            return
        
        # Valida produto e assunto
        produto, assunto = self.validate_and_get_options(
            self.campos['produto'].get(), 
            self.campos['assunto'].get()
        )
        
        if not produto or not assunto:
            self.show_error("Opções inválidas para Produto ou Assunto!")
            return
        
        analista_nome = self.get_analista_name(email_analista)
        if not analista_nome:
            self.show_error("Email de analista não encontrado!")
            return
        
        if not hasattr(self, 'canal_entrada') or not self.canal_entrada:
            self.show_error("Selecione um canal de entrada!")
            return
        
        # Configura navegador e executa automação
        try:
            self.automation.setup_browser()
            self.automation.navigate_to_forms()
            
            # Realiza login
            if not self.automation.perform_login(email_analista, self.campo_senha.get()):
                self.show_error("Erro no login! Verifique email e senha.")
                return
            
            # Atualiza interface após login bem-sucedido
            self.label_invisible_login.configure(text=f'Logado como {analista_nome}', text_color='green')
            self.box_login.grid_forget()
            
            # Prepara dados para o formulário
            form_data = {
                "num_caso": num_caso,
                "num_cpf": num_cpf,
                "analista_nome": analista_nome,
                "produto": produto,
                "assunto": assunto,
                "canal_entrada": self.canal_entrada
            }
            
            # Preenche formulário
            self.automation.fill_form(form_data)
            
            # Gerencia fluxo do caso
            self.handle_case_flow(form_data)
            
        except Exception as e:
            self.show_error(f"Erro durante execução: {str(e)}")
    
    def run(self):
        """Executa a aplicação"""
        self.app.mainloop()