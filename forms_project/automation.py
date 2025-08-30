# automation.py
# Módulo de automação com Selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from constants import LINK_FORMS, BROWSER_OPTIONS


class WebAutomation:
    def __init__(self):
        self.navegador = None
        self.wait = None
    
    def setup_browser(self):
        """Configura e inicializa o navegador"""
        options = Options()
        for option in BROWSER_OPTIONS:
            options.add_argument(option)
        
        self.navegador = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.navegador, 7)
        return self.wait
    
    def navigate_to_forms(self):
        """Navega para a página de formulários"""
        self.navegador.get(LINK_FORMS)
    
    def perform_login(self, email, senha):
        """Realiza o processo de login"""
        try:
            # Primeira tentativa - usuario já logado
            try:
                usuario = self.wait.until(EC.presence_of_element_located((By.XPATH, f'//small[contains(text(), "{email}")]')))
                self.navegador.execute_script("arguments[0].click();", usuario)

                password = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"]')))
                password.send_keys(senha)
                
                sleep(0.5)
                self.navegador.find_element("css selector", 'input[type="submit"]').click()
                
                WebDriverWait(self.navegador, 3).until(
                    EC.presence_of_element_located((By.XPATH,'//*[@id="form-main-content1"]/div/div[3]/div[4]/button/div'))
                )
                return True
            except:
                # Segunda tentativa - login completo
                usuario = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="email"]')))
                usuario.send_keys(email)
                
                sleep(0.5)
                self.navegador.find_element("css selector", 'input[type="submit"]').click()
                
                WebDriverWait(self.navegador, 3).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Insira a senha')]"))
                )
                
                password = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"]')))
                password.send_keys(senha)
                
                sleep(0.5)
                self.navegador.find_element("css selector", 'input[type="submit"]').click()
                
                WebDriverWait(self.navegador, 3).until(
                    EC.presence_of_element_located((By.XPATH,'//*[@id="form-main-content1"]/div/div[3]/div[4]/button/div'))
                )
                return True
                
        except Exception as e:
            return False
    
    def fill_form(self, data):
        """Preenche o formulário com os dados"""
        # Clica em iniciar
        iniciar_agora = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="form-main-content1"]/div/div[3]/div[4]/button/div')))
        iniciar_agora.click()
        
        # Seleciona equipe Eduardo
        equipe = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="radio"][value="Eduardo"]')))
        self.navegador.execute_script("arguments[0].click();", equipe)
        
        # Seleciona analista
        analista = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,f'input[value="{data["analista_nome"]}"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", analista)
        self.navegador.execute_script("arguments[0].click();", analista)
        
        # Seleciona produto
        select_produt = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, data["produto"])))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_produt)
        self.navegador.execute_script("arguments[0].click();", select_produt)
        
        # Seleciona canal de entrada
        canal_entrada = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,f'input[value="{data["canal_entrada"]}"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", canal_entrada)
        self.navegador.execute_script("arguments[0].click();", canal_entrada)
        
        # Preenche número do caso
        numero_caso = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[data-automation-id="textInput"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", numero_caso)
        numero_caso.send_keys(data["num_caso"])
        
        # Seleciona assunto
        click_assunto = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="rc8e46ee7816e47c7aa03ed438808fa9e_placeholder_content"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", click_assunto)
        self.navegador.execute_script("arguments[0].click();", click_assunto)        
        
        select_assunto = self.navegador.find_element("css selector", data["assunto"])
        self.navegador.execute_script("arguments[0].click();", select_assunto)
        
        # Preenche CPF
        numero_cpf = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="question-list"]/div[7]/div[2]/div/span/input')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", numero_cpf)
        numero_cpf.send_keys(data["num_cpf"])

        # Status aberto
        of_open = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="Aberto"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", of_open)
        self.navegador.execute_script("arguments[0].click();", of_open)
    
    def handle_pending(self, pending_type):
        """Gerencia casos pendentes"""
        if pending_type == "ABERTO >>> PENDENTE":
            # Status pendente
            for_pending = self.wait.until(EC.presence_of_element_located((By.XPATH,'(//input[@value="Pendente informações"])[2]')))
            self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", for_pending)
            self.navegador.execute_script("arguments[0].click();", for_pending)

            precedence = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="SIM, demanda dentro do nosso escopo e necessitava de análise em Segundo Nível"]')))
            self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", precedence)
            self.navegador.execute_script("arguments[0].click();", precedence)

        elif pending_type == "PENDENTE >>> FINALIZADO":
            # Status pendente para finalizado
            for_pending = self.wait.until(EC.presence_of_element_located((By.XPATH,'(//input[@value="Pendente informações"])[1]')))
            self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", for_pending)
            self.navegador.execute_script("arguments[0].click();", for_pending)

            # Finaliza o caso após marcar como pendente
            self.handle_close()
    
    def handle_transfer(self, fila_selector, option_resolution=None):
        """Gerencia casos transferidos"""        
        # Marca como transferido
        for_transfer = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="Transferido para outro Grupo"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", for_transfer)
        self.navegador.execute_script("arguments[0].click();", for_transfer)
        
        # Seleciona fila
        option_filas = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="r99032d47f80f473e9a3974edb4dea644_placeholder_content"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", option_filas)
        self.navegador.execute_script("arguments[0].click();", option_filas)
        
        select_filas = self.navegador.find_element(By.CSS_SELECTOR, fila_selector)
        self.navegador.execute_script("arguments[0].click();", select_filas)
        
        # Lógica específica para CAC
        if fila_selector == 'span[aria-label="CAC"]' and option_resolution:
            no_precedence = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value^="SIM, demanda dentro do nosso escopo, mas"]')))
            self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", no_precedence)
            self.navegador.execute_script("arguments[0].click();", no_precedence)
            
            first_level_resolution = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, option_resolution)))
            self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_level_resolution)
            self.navegador.execute_script("arguments[0].click();", first_level_resolution)
        else:
            precedence = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="SIM, demanda dentro do nosso escopo e necessitava de análise em Segundo Nível"]')))
            self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", precedence)
            self.navegador.execute_script("arguments[0].click();", precedence)
    
    def handle_close(self):
        """Gerencia casos finalizados"""
        for_close = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="Finalizado"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", for_close)
        self.navegador.execute_script("arguments[0].click();", for_close)
        
        precedence = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="SIM, demanda dentro do nosso escopo e necessitava de análise em Segundo Nível"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", precedence)
        self.navegador.execute_script("arguments[0].click();", precedence)
    
    def submit_form(self):
        """Submete o formulário e verifica confirmação"""
        submit_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-automation-id="submitButton"]')))
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
        self.navegador.execute_script("arguments[0].click();", submit_button)
        
        try:
            WebDriverWait(self.navegador, 3).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'BackOffice Atendimento agradece!')]"))
            )
            return True
        except:
            return False
    
    def quit_browser(self):
        """Fecha o navegador"""
        if self.navegador:
            self.navegador.quit()