# main.py
# Ponto de entrada da aplicação

from ui import FormsApp


def main():
    """Função principal que inicia a aplicação"""
    try:
        app = FormsApp()
        app.run()
    except Exception as e:
        print(f"Erro ao iniciar a aplicação: {e}")
        input("Pressione Enter para sair...")


if __name__ == "__main__":
    main()