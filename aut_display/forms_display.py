from playwright.sync_api import sync_playwright
from time import sleep
import customtkinter as ctk
import sys
sys.path.append(r'C:\Users\irlan\OneDrive\Documentos\Python_automacao\playwright\aut_forms')
from senhas import login, senha







def forms():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False) # headless=False
        context = navegador.new_context(
            record_video_dir="videos/",
            record_video_size={"width": 1280, "height": 720})
        page =  context.new_page()
        page.goto("https://forms.office.com/Pages/ResponsePage.aspx?id=g0JDTVqwv0K-xcZB1cHInb1x76whDHhCnj8r1tIU7QRUQTNJWUgyN1BUT0xBS01KUzc0SlcwWTM2Mi4u", wait_until="load")

        # Caso queira fazer um vídeo do funcionamento
        # page.video.path()

        num_caso = campo_caso.get()
        num_cpf = campo_cpf.get()
        produto = int(campo_produto.get())

        match produto:
            case 1:
                produto = 'input[value="Credcesta"]'
            case 2:
                produto = 'input[value="M Fácil Consignado"]'
            case _:
                produto = 'input[value="Credcesta"]'



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
        page.click('xpath=/html/body/div[2]/div/div[59]/span[2]/span')

        # Numero do CPF        
        cpf= page.locator('input[data-automation-id="textInput"]').nth(1)
        cpf.fill(num_cpf)
        

        # Do status
        page.click('input[value="Aberto"]')

        # Para o status
        page.click('input[value="Finalizado por Automação"]')

        # Demanda que precisa de nossa atuação
        page.click('input[value="SIM, demanda dentro do nosso escopo e necessitava de análise em Segundo Nível"]')

        # Clicar no botão enviar
        # page.click('xpath=//*[@id="form-main-content1"]/div/div/div[2]/div[4]/div/button')
        sleep(15)

        # # Submeter outra resposta        
        # page.click('xpath=//*[@id="form-main-content1"]/div/div/div[2]/div[1]/div[2]/div[4]/span')
    



# aparencia
ctk.set_appearance_mode('dark')

# criando o display
app = ctk.CTk()

# Definição do título
app.title('Forms')

# Definição do tamanho do display
app.geometry("350x550")

# ========================================

# Criando label Caso
label_caso = ctk.CTkLabel(app, text='Número do Caso')
label_caso.pack(pady=10)

# Campo do caso
campo_caso = ctk.CTkEntry(app, width= 250,placeholder_text='Digite o número do Caso')
campo_caso.pack(pady=10)

# ========================================

# Criando label CPF
label_cpf = ctk.CTkLabel(app, text='Número do CPF')
label_cpf.pack(pady=10)

# Campo do caso
campo_cpf = ctk.CTkEntry(app, width= 250,placeholder_text='Digite o número do CPF')
campo_cpf.pack(pady=10)

# ========================================

# Criando label Produto
label_produto = ctk.CTkLabel(app, text='Digite o número do produto:\n\n[1] - Credcesta\n\n[2] - M fácil consignado')
label_produto.pack(pady=10)

# Campo do caso
campo_produto = ctk.CTkEntry(app, width= 250,placeholder_text='Digite o produto...')
campo_produto.pack(pady=10)

# ========================================

# Botão Submit
submit = ctk.CTkButton(app, text='Submit', command=forms)
submit.pack(pady=10)


# Manter display aberto
app.mainloop()

    






