import gspread
from oauth2client.service_account import ServiceAccountCredentials



class DataBase():
    def __init__(self):
        # Escopo da API (Sheets + Drive)
        self.scope = ["https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive.file",
                "https://www.googleapis.com/auth/drive"]

        # Credenciais do arquivo JSON baixado
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("file_keys.json", self.scope)
        
        self.authenticator()
        


    def authenticator(self):
        # Autenticar e abrir a planilha
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("Licenças").sheet1  # primeira aba

    def consultar_chave(self, chave):
        self.dados = self.sheet.get_all_records()
        for registro in self.dados:
            if registro["chave"] == chave:
                return registro["status"] == "Ativa"
        return False


