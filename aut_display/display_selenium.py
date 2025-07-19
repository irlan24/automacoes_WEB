from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from senhas import *
from time import sleep
import customtkinter as ctk
import threading

class FormsApp:
    def __init__(self):
        self.setup_ui()
        self.navegador = None
        
    def setup_ui(self):
        """Configura a interface do usuário"""
        # Configurações básicas
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme("green")
        
        self.app = ctk.CTk()
        self.app.title('Forms')
        self.app.geometry("940x650")
        
        self.fonte = ctk.CTkFont(family="Arial", size=15, weight="bold", slant="italic", underline=True)
        
        # Chama os containers principais
        self.create_main_containers()
        self.create_form_fields()
        self.create_history_section()
        self.create_login_section()
        self.create_special_configs()
        self.create_entry_section()
        

        
    def create_main_containers(self):
        """Cria os containers principais da interface"""
        self.box_frame_center = ctk.CTkFrame(master=self.app, corner_radius=10)
        self.box_frame_center.grid(row=0, column=1, padx=15, pady=10)
        
        self.box_frame_left = ctk.CTkFrame(master=self.app, corner_radius=10)
        self.box_frame_left.grid(row=0, column=0, padx=10, pady=10, sticky='n')
        
        self.box_frame_right = ctk.CTkFrame(self.app, corner_radius=10)
        self.box_frame_right.grid(row=0, column=3, padx=10, pady=10, sticky="n")
        
    def create_form_fields(self):
        """Cria os campos do formulário principal"""
        # Dicionário com configurações dos campos
        fields_config = {
            'produto': {
                'label': 'Digite o número do produto:\n\n[1] - Credcesta\n[2] - M fácil consignado',
                'placeholder': 'Digite o produto...',
                'row_label': 0, 'row_field': 1
            },
            'caso': {
                'label': 'Número do Caso:',
                'placeholder': 'Digite o número do Caso...',
                'row_label': 2, 'row_field': 3
            },
            'cpf': {
                'label': 'Número do CPF(apenas número):',
                'placeholder': 'Digite o número do CPF...',
                'row_label': 4, 'row_field': 5
            },
            'assunto': {
                'label': 'Digite o número do Assunto:\n\n[1] - Reembolso - Seguro Prestamista\n[2] - Cancelamento de Seguro Prestamista\n[3] - Reembolso de desconto indevido de Saque\n[4] - Desacordo comercial\n[5] - Baixa de Pagamento (desconto em folha)\n[6] - Cobrança indevida\n\n[7] - Contrato/CCB\n[8] - Criação de conta na Orbitall',
                'placeholder': 'Digite o assunto...',
                'row_label': 6, 'row_field': 7
            }
        }
        
        self.campos = {}
        
        for field_name, config in fields_config.items():
            # Label
            label = ctk.CTkLabel(self.box_frame_center, text=config['label'], font=("Arial", 13, "bold"))
            label.grid(row=config['row_label'], column=0, pady=8, padx=10, sticky="n")
            
            # Campo de entrada
            campo = ctk.CTkEntry(self.box_frame_center, width=250, placeholder_text=config['placeholder'])
            campo.grid(row=config['row_field'], column=0, pady=8, padx=10, sticky="n")
            
            self.campos[field_name] = campo
        
        # Botão e elementos de controle
        self.submit = ctk.CTkButton(self.box_frame_center, text='ENVIAR', command=self.load)
        self.submit.grid(row=8, column=0, pady=8, padx=10)
        
        self.progress_bar = ctk.CTkProgressBar(self.box_frame_center, width=200, corner_radius=10, 
                                             progress_color="green", border_width=10, fg_color="blue", height=10)
        
        self.invisible_element = ctk.CTkLabel(self.box_frame_center, text='', font=("Arial", 15, "bold"))
        self.invisible_element.grid(row=9, column=0, pady=8, padx=10)
        
    def create_history_section(self):
        """Cria a seção de histórico de casos"""
        self.box_history_section = ctk.CTkFrame(self.box_frame_left, corner_radius=10, width=210, height=180)
        self.box_history_section.grid(padx=10, pady=10)
        self.box_history_section.grid_propagate(False)

        label_title = ctk.CTkLabel(self.box_history_section, text='HISTÓRICO DE CASOS', font=self.fonte)
        label_title.grid(row=0, column=0, pady=5, padx=10, sticky="nswe")

        box_list_case = ctk.CTkScrollableFrame(self.box_history_section, width=180)
        box_list_case.grid(row=1, column=0, padx=5, pady=5, sticky="n")
                
        

        # Botão para limpar histórico (clear_historic)
        ctk.CTkButton(self.box_frame_left, text= "Limpar histórico", command=self.delete_historic_case).grid(row=1, column=0, pady=5, padx=15, sticky="nsew")
        
        
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
        """Cria a seção do canal de entrada """        
        ctk.CTkLabel(self.box_frame_left, text='CANAL DE ENTRADA', font=self.fonte).grid(row=3, column=0, pady=2, padx=10, sticky="nswe")

        self.box_entry_section = ctk.CTkFrame(self.box_frame_left, corner_radius=10)
        self.box_entry_section.grid(row=4, column=0, pady=1, padx=20, sticky="nsew")

        # Variável de controle para armazenar a opção selecionada
        self.opcao_selecionada = None

        # Lista para armazenar os botões
        self.botoes = {}

        # Criando botões como opções
        opcoes = ["SALESFORCE - (Casos)", "CANAIS CRÍTICOS (SALESFORCE)", "OUVIDORIA (SALESFORCE)"]
        for i, opcao in enumerate(opcoes):
            botao = ctk.CTkButton(self.box_entry_section, text=opcao, command=lambda o=opcao: self.selecionar(o))
            botao.grid(row=i, column=0, padx=10, pady=10, sticky='nswe')
            self.botoes[opcao] = botao

    def selecionar(self, opcao):
        self.opcao_selecionada = opcao
        for chave, valor in self.botoes.items():
            if chave == opcao:
                valor.configure(fg_color="green")  # botão ativo
            else:
                valor.configure(fg_color="gray")   # desativa os outros

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
        
        filas_config = [
            ("Backoffice Seguros", 'span[aria-label="Backoffice Seguros"]'),
            ("Backoffice Único", 'span[aria-label="Backoffice Único"]'),
            ("Backoffice Controle Financeiro", 'span[aria-label="Backoffice Controle Financeiro"]'),
            ("CAC", 'span[aria-label="CAC"]')
        ]
        
        for i, (text, value) in enumerate(filas_config):
            radio = ctk.CTkRadioButton(self.box_frame_1, text=text, variable=self.filas, 
                                     value=value, command=self.handle_fila_change)
            radio.grid(row=i, column=0, pady=10, padx=10, sticky="w")
        
        # Container para opções CAC
        self.box_frame_2 = ctk.CTkFrame(self.box_frame_right, corner_radius=10)
        self.option_resolution = ctk.StringVar(value='')
        
        cac_options = [
            ("Reembolso sem saldo credor", 'input[value="Pedido de reembolso de Seguro ou Cartão em que não há saldo credor a reembolsar na fatura"]'),
            ("Baixa de pagamento sem comprovante", 'input[value^="Pedido de baixa de pagamento sem envio do comprovante de pagamento"]'),
            ("Dentro dos 10 dias", 'input[value="Pedido de reembolso de Saque dentro do prazo de 10 dias corridos para reembolso em lote"]'),
            ("Duplicidade nos casos", 'input[value="Caso aberto em duplicidade quando o caso original ainda está dentro do prazo"]')
        ]
        
        for i, (text, value) in enumerate(cac_options):
            radio = ctk.CTkRadioButton(self.box_frame_2, text=text, variable=self.option_resolution, value=value)
            radio.grid(row=i, column=0, pady=10, padx=10, sticky="w")
    
    def handle_status_change(self):
        """Gerencia mudanças no status (finalizado/transferido)"""
        if self.especial_radios.get() == "transferido":
            self.box_frame_1.grid(row=2, column=0, pady=30, sticky="nsew")
        else:
            self.box_frame_1.grid_forget()
            self.box_frame_2.grid_forget()
    
    def handle_fila_change(self):
        """Gerencia mudanças na seleção de fila"""
        if self.filas.get() == 'span[aria-label="CAC"]':
            self.box_frame_2.grid(row=3, column=0, pady=20, sticky="nsew")
        else:
            self.box_frame_2.grid_forget()

    def get_analista_name(self, email):
        """Retorna o nome do analista baseado no email"""

        analistas = all_analist # variavel com dicionário de todos os emails

        return analistas.get(email, "")
    
    
    def validate_and_get_options(self, produto_val, assunto_val):
        """Valida e retorna as opções de produto e assunto"""
        try:
            produto_num = int(produto_val)
            assunto_num = int(assunto_val)
            
            produtos = {1: produto_1, 2: produto_2}
            assuntos = {1: assunto_1, 2: assunto_2, 3: assunto_3, 4: assunto_4, 5: assunto_5, 6: assunto_6, 7: assunto_7, 8: assunto_8}
            
            if produto_num not in produtos:
                raise ValueError("Produto inválido")
            if assunto_num not in assuntos:
                raise ValueError("Assunto inválido")
                
            return produtos[produto_num], assuntos[assunto_num]
            
        except (ValueError, KeyError):
            return None, None
    
    def show_error(self, message):
        """Exibe mensagem de erro e reabilita interface"""
        self.invisible_element.configure(text=message, text_color="red")
        self.progress_bar.stop()
        self.progress_bar.grid_forget()
        self.submit.configure(state='normal')
        if self.navegador:
            self.navegador.quit()
    
    def show_success(self, message, num_caso):
        """Exibe mensagem de sucesso e salva caso"""
        self.progress_bar.stop()
        self.progress_bar.grid_forget()
        self.texto_temporario(message, "green")
        self.submit.configure(state='normal')
        self.save_case(num_caso)
        if self.navegador:
            self.navegador.quit()
    
    def load(self):
        """Inicia o processo de carregamento"""
        self.invisible_element.configure(text='CARREGANDO...', text_color="green")
        self.submit.configure(state="disabled")
        self.progress_bar.grid(row=10, column=0, pady=5, padx=7)
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

    def delete_historic_case(self):
        """Deleta o histórico dos casos """
        self.entry_list_case.configure(state="normal")
        self.entry_list_case.delete("1.0", "end")
        self.entry_list_case.configure(state="disabled")
    
    def setup_browser(self):
        """Configura e inicializa o navegador"""
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        
        self.navegador = webdriver.Chrome(options=options)
        return WebDriverWait(self.navegador, 7)
    
    def perform_login(self, wait, email, senha):
        """Realiza o processo de login"""
        try:
            # Campo email
            usuario = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="email"]')))
            usuario.send_keys(email)
            
            sleep(0.5)
            self.navegador.find_element("css selector", 'input[type="submit"]').click()
            
            WebDriverWait(self.navegador, 3).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Insira a senha')]"))
            )
            
            # Campo senha
            password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"]')))
            password.send_keys(senha)
            
            sleep(0.5)
            self.navegador.find_element("css selector", 'input[type="submit"]').click()
            
            WebDriverWait(self.navegador, 3).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="form-main-content1"]/div/div[3]/div[4]/button/div'))
            )
            
            return True
            
        except Exception as e:
            return False
    
    def fill_form(self, wait, data):
        """Preenche o formulário com os dados"""
        # Clica em iniciar
        iniciar_agora = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="form-main-content1"]/div/div[3]/div[4]/button/div')))
        iniciar_agora.click()
        
        # Seleciona equipe Eduardo
        equipe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="radio"][value="Eduardo"]')))
        self.navegador.execute_script("arguments[0].click();", equipe)
        
        # Seleciona analista
        analista = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,f'input[value="{data["analista_nome"]}"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", analista)
        self.navegador.execute_script("arguments[0].click();", analista)
        
        # Seleciona produto
        select_produt = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, data["produto"])))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_produt)
        self.navegador.execute_script("arguments[0].click();", select_produt)
        
        # Seleciona canal de entrada
        canal_entrada = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,f'input[value="{self.canal_entrada}"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", canal_entrada)
        self.navegador.execute_script("arguments[0].click();", canal_entrada)
        
        # Preenche número do caso
        numero_caso = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[data-automation-id="textInput"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", numero_caso)
        numero_caso.send_keys(data["num_caso"])
        
        # Seleciona assunto
        click_assunto = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="rc8e46ee7816e47c7aa03ed438808fa9e_placeholder_content"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", click_assunto)
        self.navegador.execute_script("arguments[0].click();", click_assunto)        
        
        select_assunto = self.navegador.find_element("css selector", data["assunto"])
        self.navegador.execute_script("arguments[0].click();", select_assunto)
        

        # Preenche CPF
        numero_cpf = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="question-list"]/div[7]/div[2]/div/span/input')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", numero_cpf)
        numero_cpf.send_keys(data["num_cpf"])
        
        # Status aberto
        of_open = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="Aberto"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", of_open)
        self.navegador.execute_script("arguments[0].click();", of_open)
    
    def handle_transfer_or_close(self, wait, data):
        """Gerencia transferência ou finalização"""
        if self.especial_radios.get() == "transferido":
            self.handle_transfer(wait, data)
        else:
            self.handle_close(wait, data)
    
    def handle_transfer(self, wait, data):
        """Gerencia casos transferidos"""
        # Marca como transferido
        for_transfer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="Transferido para outro Grupo"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", for_transfer)
        self.navegador.execute_script("arguments[0].click();", for_transfer)
        
        # Seleciona fila
        option_filas = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="r99032d47f80f473e9a3974edb4dea644_placeholder_content"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", option_filas)
        self.navegador.execute_script("arguments[0].click();", option_filas)
        
        select_filas = self.navegador.find_element(By.CSS_SELECTOR, self.filas.get())
        self.navegador.execute_script("arguments[0].click();", select_filas)
        
        # Lógica específica para CAC
        if self.filas.get() == 'span[aria-label="CAC"]':
            no_precedence = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value^="SIM, demanda dentro do nosso escopo, mas"]')))
            self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", no_precedence)
            self.navegador.execute_script("arguments[0].click();", no_precedence)
            
            first_level_resolution = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.option_resolution.get())))
            self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_level_resolution)
            self.navegador.execute_script("arguments[0].click();", first_level_resolution)
        else:
            precedence = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="SIM, demanda dentro do nosso escopo e necessitava de análise em Segundo Nível"]')))
            self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", precedence)
            self.navegador.execute_script("arguments[0].click();", precedence)
        
        self.submit_form(wait, data["num_caso"])
    
    def handle_close(self, wait, data):
        """Gerencia casos finalizados"""
        for_close = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="Finalizado"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", for_close)
        self.navegador.execute_script("arguments[0].click();", for_close)
        
        precedence = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="SIM, demanda dentro do nosso escopo e necessitava de análise em Segundo Nível"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", precedence)
        self.navegador.execute_script("arguments[0].click();", precedence)
        
        self.submit_form(wait, data["num_caso"])
    
    def submit_form(self, wait, num_caso):
        """Submete o formulário e verifica confirmação"""
        submit_button = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="form-main-content1"]/div/div/div[2]/div[4]/div/button')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
        self.navegador.execute_script("arguments[0].click();", submit_button)
        
        try:
            WebDriverWait(self.navegador, 3).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'BackOffice Atendimento agradece!')]"))
            )
            self.show_success("Formulário enviado com sucesso!", num_caso)
        except:
            self.show_error("Formulário não foi ENVIADO!")
    
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
        
        # Configura navegador
        try:
            wait = self.setup_browser()
            self.navegador.get(link_forms)
            self.navegador.maximize_window()
            
            # Realiza login
            if not self.perform_login(wait, email_analista, self.campo_senha.get()):
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
                "assunto": assunto
            }
            
            # Preenche formulário
            self.fill_form(wait, form_data)
            
            # Gerencia transferência ou fechamento
            self.handle_transfer_or_close(wait, form_data)
            
        except Exception as e:
            self.show_error(f"Erro durante execução: {str(e)}")
    
    def run(self):
        """Executa a aplicação"""
        self.app.mainloop()

# Execução
if __name__ == "__main__":
    app = FormsApp()
    app.run()