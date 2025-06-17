from playwright.sync_api import sync_playwright
from time import sleep
from senhas import login, senha



with open("casos_automacao.txt", "r", encoding="utf8") as arquivo1:    
    num_caso = arquivo1.read().split("\n")    

with open("cpf_automacao.txt", "r", encoding="utf8") as arquivo:    
    num_cpf = arquivo.read().split("\n")  


with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) # headless=False
    context = navegador.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720})
    page =  context.new_page()
    page.goto("https://forms.office.com/Pages/ResponsePage.aspx?id=g0JDTVqwv0K-xcZB1cHInb1x76whDHhCnj8r1tIU7QRUQTNJWUgyN1BUT0xBS01KUzc0SlcwWTM2Mi4u", wait_until="load")

    # Caso queira fazer um vídeo do funcionamento
    page.video.path()


    # login
    page.fill('id=i0116', login)
    page.click('input[type="submit"]')
    page.fill('id=i0118', senha)
    page.click('input[type="submit"]')

    # botao iniciar agora
    page.click('xpath=//*[@id="form-main-content1"]/div/div[3]/div[4]/button/div')
    
    for i in range(len(num_caso)):

        #Equipe    
        equipe = page.locator('input[value="Eduardo"]')
        equipe.scroll_into_view_if_needed()
        equipe.click()

        # analista
        page.click('input[value="Irlan Silva"]')

        # Produto
        page.click('input[value="M Fácil Consignado"]')

        # Canal de entrada
        page.click('input[value="SALESFORCE - (Casos)"]')

        # Numero do Caso
        page.fill('input[data-automation-id="textInput"]', num_caso[i])
        

        # Selecionar assunto
        page.click('xpath=//*[@id="rc8e46ee7816e47c7aa03ed438808fa9e_placeholder_content"]')
        page.click('xpath=/html/body/div[2]/div/div[59]/span[2]/span')

        # Numero do CPF        
        cpf= page.locator('input[data-automation-id="textInput"]').nth(1)
        cpf.fill(num_cpf[i])
        

        # Do status
        page.click('input[value="Aberto"]')

        # Para o status
        page.click('input[value="Finalizado por Automação"]')

        # Demanda que precisa de nossa atuação
        page.click('input[value="SIM, demanda dentro do nosso escopo e necessitava de análise em Segundo Nível"]')

        # Clicar no botão enviar
        page.click('xpath=//*[@id="form-main-content1"]/div/div/div[2]/div[4]/div/button')
        sleep(2)

        # Submeter outra resposta        
        page.click('xpath=//*[@id="form-main-content1"]/div/div/div[2]/div[1]/div[2]/div[4]/span')
        
        





    
