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
    submit.configure(state="disabled")
    progress_bar.grid(row=10, column=0, pady=8, padx=10)
    progress_bar.start()
    threading.Thread(target=forms, daemon=True).start()



def texto_temporario(text_display='', color_display=''):
    texto_original = ''

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
        progress_bar.grid_forget()
        submit.configure(state='normal')
        navegador.quit()
    else:
        try:
            produto = int(campo_produto.get())
            match produto:
                case 1:
                    produto = produto_1
                case 2:
                    produto = produto_2
                case _:
                    invisible_element.configure(text="Opção inválida para o Produto\nInsira novamente!", text_color="red")
                    progress_bar.stop()
                    progress_bar.grid_forget()
                    submit.configure(state='normal')
                    navegador.quit()
        except:
            invisible_element.configure(text="Opção inválida para o Produto\nInsira novamente!", text_color="red")
            progress_bar.stop()
            progress_bar.grid_forget()
            submit.configure(state='normal')
            navegador.quit()


    # Condições e opções para os Assuntos
    

    if assunto == '':
        invisible_element.configure(text="Campo Assunto está em branco!\nDigite novamente!", text_color="red")
        progress_bar.stop()
        progress_bar.grid_forget()
        submit.configure(state='normal')
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
                    progress_bar.grid_forget()
                    submit.configure(state='normal')
                    navegador.quit()
        except:
            invisible_element.configure(text="Opção inválida para o Assunto\nInsira novamente!", text_color="red")
            progress_bar.stop()
            progress_bar.grid_forget()
            submit.configure(state='normal')
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
    sleep(0.5)
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


    # ========================= TRANSFERIR OU FINALIZAR =================

    if especial_radios.get() == "transferido":

        # Clica em transferir para outra fila
        for_transfer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="Transferido para outro Grupo"]')))
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", for_transfer)
        navegador.execute_script("arguments[0].click();", for_transfer)

        # Seleciona as opções de transferência
        select_transfer = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="r99032d47f80f473e9a3974edb4dea644_placeholder_content"]')))
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_transfer)
        navegador.execute_script("arguments[0].click();", select_transfer)

    else:

        # Espera e marca o radio correspondente ao status final
        for_close = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="Finalizado"]')))
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", for_close)
        navegador.execute_script("arguments[0].click();", for_close)

        # Espera e marca o radio correspondente a necessidade de atuação
        precedence = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[value="SIM, demanda dentro do nosso escopo e necessitava de análise em Segundo Nível"]')))
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", precedence)
        navegador.execute_script("arguments[0].click();", precedence)

        # Espera e clica no botão enviar formulário

        submit_button = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="form-main-content1"]/div/div/div[2]/div[4]/div/button')))
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
        # CLICA NO BOTÃO ENVIAR FORMS
        navegador.execute_script("arguments[0].click();", submit_button)

        # confirmação de envio de formulário no display
        try:
            # Tenta localizar elemento após enviar formulário
            WebDriverWait(navegador, 3).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'BackOffice Atendimento agradece!')]"))
            )
            progress_bar.stop() # para progresso da barra
            progress_bar.grid_forget() # oculta a barra        
            texto_temporario("Formulário enviado com sucesso!", "green")
            submit.configure(state='normal') # Habilita botão
            # Armazena o caso na PILHA (Histórico de casos)
            save_case(num_caso)
            navegador.quit() # Fecha nevegador
            
        except: 
            progress_bar.stop() # para progresso da barra
            progress_bar.grid_forget() # oculta a barra        
            texto_temporario("Formulário não foi ENVIADO!", "red")
            # invisible_element.configure(text="Formulário não foi ENVIADO!", text_color="red")
            submit.configure(state='normal') # Habilita botão
            navegador.quit()# Fecha nevegador
            

    

# ========== DISPLAY APP ============

#=============== CONFIGURAÇÕES ===========

# aparencia
ctk.set_appearance_mode('dark')
# Tema
ctk.set_default_color_theme("blue")

# criando o display
app = ctk.CTk()

# Definição do título
app.title('Forms')

# Definição da largura x altura do display
app.geometry("900x650")

# Criando uma fonte para títulos
fonte = ctk.CTkFont(family="Arial", size=15, weight="bold", slant="italic", underline=True)

# ========================================


# =========== BARRA MAIN / CENTRAL  ===========

# Container da barra central do app
box_frame_center = ctk.CTkFrame(master=app, corner_radius=10)
box_frame_center.grid(row=0, column=1, padx=15, pady=10)




# Criando label Produto
label_produto = ctk.CTkLabel(box_frame_center, text='Digite o número do produto:\n\n[1] - Credcesta\n\n[2] - M fácil consignado', font=("Arial", 13, "bold"))
label_produto.grid(row=0, column=0, pady=8, padx=10, sticky="n")

# Campo do Produto
campo_produto = ctk.CTkEntry(box_frame_center, width= 250,placeholder_text='Digite o produto...')
campo_produto.grid(row=1, column=0, pady=8, padx=10, sticky="n")

# ========================================

# Criando label Caso
label_caso = ctk.CTkLabel(box_frame_center, text='Número do Caso: ', font=("Arial", 13, "bold"))
label_caso.grid(row=2, column=0, pady=8, padx=10)

# Campo do Caso
campo_caso = ctk.CTkEntry(box_frame_center, width= 250,placeholder_text='Digite o número do Caso...')
campo_caso.grid(row=3, column=0, pady=8, padx=10)

# ========================================

# Criando label CPF
label_cpf = ctk.CTkLabel(box_frame_center, text='Número do CPF(apenas número): ', font=("Arial", 13, "bold"))
label_cpf.grid(row=4, column=0, pady=8, padx=10)

# Campo do CPF
campo_cpf = ctk.CTkEntry(box_frame_center, width= 250,placeholder_text='Digite o número do CPF...')
campo_cpf.grid(row=5, column=0, pady=8, padx=10)

# ========================================

# Criando label Assunto principal
label_assunto = ctk.CTkLabel(box_frame_center, text='Digite o número do Assunto:\n\n[1] - Reembolso - Seguro Prestamista\n\n[2] - Cancelamento de Seguro Prestamista\n\n[3] - Reembolso de desconto indevido de Saque\n\n[4] - Desacordo comercial', font=("Arial", 13, "bold"))
label_assunto.grid(row=6, column=0, pady=8, padx=10)

campo_assunto = ctk.CTkEntry(box_frame_center,width=250,placeholder_text='Digite o assunto...')
campo_assunto.grid(row=7, column=0, pady=8, padx=10)

# ========================================

# Botão Submit
submit = ctk.CTkButton(box_frame_center, text='ENVIAR', command=load)
submit.grid(row=8, column=0, pady=8, padx=10)

# ========================================
# Campo de barra de progresso
progress_bar = ctk.CTkProgressBar(box_frame_center, width=200, corner_radius=10, progress_color="green", border_width=10, fg_color="blue", height=10)


# ========================================

# campo para controle de retorno e notificações
invisible_element = ctk.CTkLabel(box_frame_center, text='', font=("Arial", 15, "bold"))
invisible_element.grid(row=9, column=0, pady=8, padx=10)



# ============== BARRA LATERAL ESQUERDA  ==============

# Container da barra lateral esquerda
box_frame_left = ctk.CTkFrame(master=app, corner_radius=10)
box_frame_left.grid(row=0, column=0, padx=10, pady=10)

# container filho com ScrollBar para armazenar os casos
box_list_case = ctk.CTkScrollableFrame(box_frame_left, width=180, height=10)
box_list_case.grid(padx=10, pady=10)

# armazenamento dos casos
list_case = []
def save_case(case):
    list_case.insert(0, case)
    label_list_case.configure(text="\n".join(list_case))
    

# Titulo inicial
label_title = ctk.CTkLabel(box_list_case, text='HISTÓRICO DE CASOS', font=fonte)
label_title.grid(row=0, column=0, pady=8, padx=10, sticky="w")

# Label para mostrar os casos armazenados
label_list_case = ctk.CTkLabel(box_list_case, text="", font=("Arial", 13, "bold"))
label_list_case.grid(row=1, column=0, pady=10, sticky="w")


# ============== BARRA LATERAL DIREITA  ==============

# Container da barra lateral direita
box_frame_right = ctk.CTkFrame(app, corner_radius=10)
box_frame_right.grid(row=0, column=3, padx=10, pady=10, sticky="n")

box_frame_right.grid_columnconfigure(0, weight=1 )
box_frame_right.grid_rowconfigure(0, weight=1)
   

# Titulo inicial
label_title_right = ctk.CTkLabel(box_frame_right, text='CONFIGURAÇÕES ESPECIAIS', font=fonte)
label_title_right.grid(row=0, column=0, pady=8, padx=30, sticky="nsew")

box_frame = ctk.CTkFrame(box_frame_right, corner_radius=10)
box_frame.grid(row=1, column=0)


def mostrar_opcao():
    print(especial_radios.get())




especial_radios = ctk.StringVar(value= "finalizado")

# Radios para transferência de filas
especial_status = ctk.CTkRadioButton(box_frame, text="Finalizado", variable= especial_radios, value= "finalizado", font=("Arial", 10, "bold"), command=mostrar_opcao)
especial_status.grid(row=0, column=0, pady=10, padx=10, sticky="nsew" )

especial_transfer = ctk.CTkRadioButton(box_frame, text="Trasferido", variable= especial_radios, value= "transferido", font=("Arial", 10, "bold"), command=mostrar_opcao)
especial_transfer.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")



# Manter display aberto
app.mainloop()









