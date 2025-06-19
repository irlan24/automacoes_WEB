from playwright.sync_api import sync_playwright
from time import sleep
import customtkinter as ctk
import sys
sys.path.append(r'C:\Users\irlan\OneDrive\Documentos\Python_automacao\playwright\aut_in_git')
from senhas import *








def forms():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False) # headless=False
        # context = navegador.new_context(
        #     record_video_dir="videos/",
        #     record_video_size={"width": 1280, "height": 720})
        page =  navegador.new_page()
        page.goto(link_forms, timeout=3000)

        # Caso queira fazer um vídeo do funcionamento
        # page.video.path()

        # Pegando indormações do display
        num_caso = campo_caso.get()
        num_cpf = campo_cpf.get()
        produto = campo_produto.get()
        assunto = campo_assunto.get()
        
        # Condições e opções para os Produtos
        if produto == '':
            invisible_element.configure(text="Campo Produto está em branco!\nDigite novamente!", text_color="red")
        else:
            produto = int(campo_produto.get())
            
            match produto:
                case 1:
                    produto = produto_1
                case 2:
                    produto = produto_2
                case _:
                    invisible_element.configure(text="Nenhuma das opções digitadas para o Produto\nInsira novamente!", text_color="red")

        # Condições e opções para os Assuntos
        if assunto == '':
            invisible_element.configure(text="Campo Assunto está em branco!\nDigite novamente!", text_color="red")
        else:
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
                    invisible_element.configure(text="Nenhuma das opções digitadas para o Assunto\nInsira novamente!", text_color="red")




        # login
        page.fill('id=i0116', login)
        page.click('input[type="submit"]')
        page.fill('id=i0118', senha)
        page.click('input[type="submit"]')

        # botao iniciar agora
        page.click('xpath=//*[@id="form-main-content1"]/div/div[3]/div[4]/button/div')
        
        #Equipe    
        equipe = page.locator('input[value="Eduardo"]')
        equipe.scroll_into_view_if_needed()
        equipe.click()

        # analista
        page.click('input[value="Irlan Silva"]')

        # Produto
        page.click(produto)

        # Canal de entrada
        page.click('input[value="SALESFORCE - (Casos)"]')

        # Numero do Caso
        page.fill('input[data-automation-id="textInput"]', num_caso)
        

        # Selecionar assunto
        page.click('xpath=//*[@id="rc8e46ee7816e47c7aa03ed438808fa9e_placeholder_content"]')
        page.click(assunto)

        # Numero do CPF        
        cpf= page.locator('input[data-automation-id="textInput"]').nth(1)
        cpf.fill(num_cpf)
        

        # Do status
        page.click('input[value="Aberto"]')

        # Para o status
        page.click('input[value="Finalizado"]')

        # Demanda que precisa de nossa atuação
        page.click('input[value="SIM, demanda dentro do nosso escopo e necessitava de análise em Segundo Nível"]')

        # # Clicar no botão enviar
        # page.click('xpath=//*[@id="form-main-content1"]/div/div/div[2]/div[4]/div/button')

        sleep(2)

        # Cria um elemento validador de envio de Forms
        validator_element = page.locator("b", has_text="BackOffice Atendimento agradece!")

        # Condições para o validador retornar uma mensagem no display
        if validator_element.is_visible():
            invisible_element.configure(text="Formulário enviado com sucesso!", text_color="green")
        else:
            invisible_element.configure(text="Formulário não foi ENVIADO!", text_color="red")
            
        
    



# aparencia
ctk.set_appearance_mode('dark')

# criando o display
app = ctk.CTk()

# Definição do título
app.title('Forms')

# Definição da largura x altura do display
app.geometry("350x630")

# ========================================

# Criando label Produto
label_produto = ctk.CTkLabel(app, text='Digite o número do produto:\n\n[1] - Credcesta\n\n[2] - M fácil consignado')
label_produto.pack(pady=10)

# Campo do Produto
campo_produto = ctk.CTkEntry(app, width= 250,placeholder_text='Digite o produto...')
campo_produto.pack(pady=10)

# ========================================

# Criando label Caso
label_caso = ctk.CTkLabel(app, text='Número do Caso: ')
label_caso.pack(pady=10)

# Campo do Caso
campo_caso = ctk.CTkEntry(app, width= 250,placeholder_text='Digite o número do Caso...')
campo_caso.pack(pady=10)

# ========================================

# Criando label CPF
label_cpf = ctk.CTkLabel(app, text='Número do CPF(apenas número): ')
label_cpf.pack(pady=10)

# Campo do CPF
campo_cpf = ctk.CTkEntry(app, width= 250,placeholder_text='Digite o número do CPF...')
campo_cpf.pack(pady=10)

# ========================================

# Criando label Assunto principal
label_assunto = ctk.CTkLabel(app, text='Digite o número do Assunto:\n\n[1] - Reembolso - Seguro Prestamista\n\n[2] - Cancelamento de Seguro Prestamista\n\n[3] - Reembolso de desconto indevido de Saque\n\n[4] - Desacordo comercial')
label_assunto.pack(pady=10)

campo_assunto = ctk.CTkEntry(app,width=250,placeholder_text='Digite o assunto...')
campo_assunto.pack(pady=10)



# Botão Submit
submit = ctk.CTkButton(app, text='Submit', command=forms)
submit.pack(pady=10)

# ========================================

# campo para controle de retorno e notificações
invisible_element = ctk.CTkLabel(app, text='')
invisible_element.pack(pady=10)



# Manter display aberto
app.mainloop()

    






