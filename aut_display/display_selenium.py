from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from senhas import *
from time import sleep
import customtkinter as ctk
import threading


def load():
    invisible_element.configure(text='CARREGANDO...', text_color="green")
    progress_bar.pack(pady=8)
    progress_bar.start()
    threading.Thread(target=forms, daemon=True).start()



def texto_temporario(text_display='', color_display=''):
    texto_original = invisible_element.cget("text")

    invisible_element.configure(text=text_display, text_color=color_display)

    app.after(7000, lambda: invisible_element.configure(text=texto_original))



def forms():    


    # Pegando indormações do display
    num_caso = campo_caso.get()
    num_cpf = campo_cpf.get()
    produto = campo_produto.get()
    assunto = campo_assunto.get()
    
    # Condições e opções para os Produtos
    if produto == '':
        invisible_element.configure(text="Campo Produto está em branco!\nDigite novamente!", text_color="red")
        progress_bar.stop()
        progress_bar.pack_forget()
        navegador.quit()
    else:
        produto = int(campo_produto.get())
        try:
            match produto:
                case 1:
                    produto = produto_1
                case 2:
                    produto = produto_2
                case _:
                    invisible_element.configure(text="Opção inválida para o Produto\nInsira novamente!", text_color="red")
                    progress_bar.stop()
                    progress_bar.pack_forget()
                    navegador.quit()
        except:
            invisible_element.configure(text="Opção inválida para o Produto\nInsira novamente!", text_color="red")
            progress_bar.stop()
            progress_bar.pack_forget()
            navegador.quit()


    # Condições e opções para os Assuntos
    

    if assunto == '':
        invisible_element.configure(text="Campo Assunto está em branco!\nDigite novamente!", text_color="red")
        progress_bar.stop()
        progress_bar.pack_forget()
        navegador.quit()
    else:
        try:
            assunto = int(campo_assunto.get())
        
            match assunto:
                case 1:
                    assunto = assunto_1
                case 2:
                    assunto = assunto_2
                case 3:
                    assunto = assunto_3
                case 4:
                    assunto = assunto_4
                case _:
                    invisible_element.configure(text="Opção inválida para o Assunto\nInsira novamente!", text_color="red")
                    progress_bar.stop()
                    progress_bar.pack_forget()
                    navegador.quit()
        except:
            invisible_element.configure(text="Opção inválida para o Assunto\nInsira novamente!", text_color="red")
            progress_bar.stop()
            progress_bar.pack_forget()
            navegador.quit()



    
    options = Options()
    options.add_argument("--headless")  # Ativa o modo headless
    options.add_argument("--disable-gpu")  # Recomendado para Windows
    options.add_argument("--window-size=1920,1080")  # Tamanho fixo da janela (evita erros de renderização)

    # inicia o navegador
    navegador = webdriver.Chrome(options=options)

    
    navegador.get(link_forms)
    wait = WebDriverWait(navegador, 7)

    # coloca em tela cheia
    navegador.maximize_window()

    # ================ login ==========
    # Espera o campo usuario aparecer e digita nele
    usuario = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="email"]')))
    usuario.send_keys(login)

    # clica no botão avançar
    navegador.find_element("css selector", 'input[type="submit"]').click()

    # Espera o campo senha aparecer e digita nele
    password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"]')))
    password.send_keys(senha)

    sleep(0.5)
    # clica no botão Submit
    navegador.find_element("css selector", 'input[type="submit"]').click()

    # Espera o botao "iniciar agora" aparecer e clica nele 
    iniciar_agora = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="form-main-content1"]/div/div[3]/div[4]/button/div')))
    iniciar_agora.click()

    # ===================== FORMS ==============

    # Espera e marca o radio correspondente a equipe    
    equipe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="radio"][value="Eduardo"]')))

    navegador.execute_script("arguments[0].click();", equipe) 



    # Espera e marca o radio correspondente ao analista
    analista = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="Irlan Silva"]')))
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", analista)
    navegador.execute_script("arguments[0].click();", analista)


    # Espera e marca o radio correspondente ao Produto
    select_produt = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,produto)))
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_produt)
    navegador.execute_script("arguments[0].click();", select_produt)


    # Espera e marca o radio correspondente ao canal de entrada

    canal_entrada = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="SALESFORCE - (Casos)"]')))
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", canal_entrada)
    navegador.execute_script("arguments[0].click();", canal_entrada)


    # Numero do Caso
    numero_caso = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[data-automation-id="textInput"]')))
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", numero_caso)
    navegador.execute_script("arguments[0].click();", numero_caso)

    # Insere valor no campo
    numero_caso.send_keys(num_caso)


    # Abre opções do campo assunto
    click_assunto = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="rc8e46ee7816e47c7aa03ed438808fa9e_placeholder_content"]')))
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", click_assunto)
    navegador.execute_script("arguments[0].click();", click_assunto)

    # Escolhe o assunto
    select_assunto = navegador.find_element("css selector", assunto)
    navegador.execute_script("arguments[0].click();", select_assunto)

    # Número do CPF

    numero_cpf = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="question-list"]/div[7]/div[2]/div/span/input')))
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", numero_cpf)
    navegador.execute_script("arguments[0].click();", numero_cpf)

    # Insere valor no campo
    numero_cpf.send_keys(num_cpf)


    # Espera e marca o radio correspondente ao status atual

    of_open = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="Aberto"]')))
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", of_open)
    navegador.execute_script("arguments[0].click();", of_open)


    # Espera e marca o radio correspondente ao status final
    for_close = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="Finalizado"]')))
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", for_close)
    navegador.execute_script("arguments[0].click();", for_close)

    # Espera e marca o radio correspondente a necessidade de atuação
    precedence = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="SIM, demanda dentro do nosso escopo e necessitava de análise em Segundo Nível"]')))
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", precedence)
    navegador.execute_script("arguments[0].click();", precedence)

    # Espera e clica no botão enviar formulário

    submit = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="form-main-content1"]/div/div/div[2]/div[4]/div/button')))
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit)
    # CLICA NO BOTÃO ENVIAR FORMS
    # navegador.execute_script("arguments[0].click();", submit)

    # confirmação de envio de formulário no display
    try:
        validator_element = WebDriverWait(navegador, 3).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'BackOffice Atendimento agradece!')]"))
        )
        progress_bar.stop()
        progress_bar.pack_forget()
        invisible_element.configure(text='')
        texto_temporario("Formulário enviado com sucesso!", "green")
        navegador.quit()
    except: 
        progress_bar.stop()
        progress_bar.pack_forget()
        invisible_element.configure(text='')
        texto_temporario("Formulário não foi ENVIADO!", "red")
        # invisible_element.configure(text="Formulário não foi ENVIADO!", text_color="red")
        navegador.quit()  

    

# ========== DISPLAY APP ============


# aparencia
ctk.set_appearance_mode('dark')

# criando o display
app = ctk.CTk()

# Definição do título
app.title('Forms')

# Definição da largura x altura do display
app.geometry("350x650")

# ========================================

# Criando label Produto
label_produto = ctk.CTkLabel(app, text='Digite o número do produto:\n\n[1] - Credcesta\n\n[2] - M fácil consignado', font=("Arial", 13, "bold"))
label_produto.pack(pady=8)

# Campo do Produto
campo_produto = ctk.CTkEntry(app, width= 250,placeholder_text='Digite o produto...')
campo_produto.pack(pady=8)

# ========================================

# Criando label Caso
label_caso = ctk.CTkLabel(app, text='Número do Caso: ', font=("Arial", 13, "bold"))
label_caso.pack(pady=8)

# Campo do Caso
campo_caso = ctk.CTkEntry(app, width= 250,placeholder_text='Digite o número do Caso...')
campo_caso.pack(pady=8)

# ========================================

# Criando label CPF
label_cpf = ctk.CTkLabel(app, text='Número do CPF(apenas número): ', font=("Arial", 13, "bold"))
label_cpf.pack(pady=8)

# Campo do CPF
campo_cpf = ctk.CTkEntry(app, width= 250,placeholder_text='Digite o número do CPF...')
campo_cpf.pack(pady=8)

# ========================================

# Criando label Assunto principal
label_assunto = ctk.CTkLabel(app, text='Digite o número do Assunto:\n\n[1] - Reembolso - Seguro Prestamista\n\n[2] - Cancelamento de Seguro Prestamista\n\n[3] - Reembolso de desconto indevido de Saque\n\n[4] - Desacordo comercial', font=("Arial", 13, "bold"))
label_assunto.pack(pady=8)

campo_assunto = ctk.CTkEntry(app,width=250,placeholder_text='Digite o assunto...')
campo_assunto.pack(pady=8)

# ========================================

# Botão Submit
submit = ctk.CTkButton(app, text='Submit', command=load)
submit.pack(pady=8)

# ========================================
# Campo de barra de progresso
progress_bar = ctk.CTkProgressBar(app, width=200, corner_radius=10, progress_color="green", border_width=10, fg_color="blue", height=10)


# ========================================

# campo para controle de retorno e notificações
invisible_element = ctk.CTkLabel(app, text='', font=("Arial", 15, "bold"))
invisible_element.pack(pady=8)


# Manter display aberto
app.mainloop()









