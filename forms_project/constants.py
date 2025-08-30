from senhas import link_forms, all_analist, products_list, subjects_list

# constants.py
# Constantes e dicionários fixos do projeto

# Simulação dos dados que estariam no arquivo senhas.py
# (Substitua pelos valores reais quando necessário)

# URLs
LINK_FORMS = link_forms  # URL real do projeto

# Dicionário de analistas (email dos analistas)
ALL_ANALYSTS = all_analist

# Produtos disponíveis (senhas.py)
PRODUTO_1 = products_list["produto_1"]
PRODUTO_2 = products_list["produto_2"]  
PRODUTO_3 = products_list["produto_3"]

PRODUTOS = {
    1: PRODUTO_1,
    2: PRODUTO_2, 
    3: PRODUTO_3
}

# Assuntos disponíveis (senhas.py)
ASSUNTO_1 = subjects_list["assunto_1"]
ASSUNTO_2 = subjects_list["assunto_2"]
ASSUNTO_3 = subjects_list["assunto_3"]
ASSUNTO_4 = subjects_list["assunto_4"]
ASSUNTO_5 = subjects_list["assunto_5"]
ASSUNTO_6 = subjects_list["assunto_6"]
ASSUNTO_7 = subjects_list["assunto_7"]
ASSUNTO_8 = subjects_list["assunto_8"]
ASSUNTO_9 = subjects_list["assunto_9"]
ASSUNTO_10 = subjects_list["assunto_10"]
ASSUNTO_11 = subjects_list["assunto_11"]

ASSUNTOS = {
    1: ASSUNTO_1, 2: ASSUNTO_2, 3: ASSUNTO_3, 4: ASSUNTO_4, 
    5: ASSUNTO_5, 6: ASSUNTO_6, 7: ASSUNTO_7, 8: ASSUNTO_8,
    9: ASSUNTO_9, 10: ASSUNTO_10, 11: ASSUNTO_11
}

# Configurações de campos do formulário
FIELDS_CONFIG = {
    'produto': {
        'label': 'Digite o número do produto:\n\n[1] - Credcesta\n[2] - M fácil consignado\n[3] - Empréstimo',
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
        'label': 'Digite o número do Assunto:\n\n[1] - Reembolso - Seguro Prestamista\n[2] - Cancelamento de Seguro Prestamista\n[3] - Reembolso de desconto indevido de Saque\n[4] - Desacordo comercial\n[5] - Baixa de Pagamento (desconto em folha)\n[6] - Cobrança indevida\n\n[7] - Contrato/CCB\n[8] - Criação de conta na Orbitall\n[9] - Voce Pode Saúde\n[10] - Dúvidas sobre desconto em folha\n[11] - Duvidas sobre fatura/cartão',
        'placeholder': 'Digite o assunto...',
        'row_label': 6, 'row_field': 7
    }
}

# Opções de canal de entrada
CANAL_ENTRADA_OPTIONS = [
    "SALESFORCE - (Casos)", 
    "CANAIS CRÍTICOS (SALESFORCE)", 
    "OUVIDORIA (SALESFORCE)"
]

# Configurações de filas
FILAS_CONFIG = [
    ("Backoffice Seguros", 'span[aria-label="Backoffice Seguros"]'),
    ("Backoffice Único", 'span[aria-label="Backoffice Único"]'),
    ("Backoffice Controle Financeiro", 'span[aria-label="Backoffice Controle Financeiro"]'),
    ("Backoffice Conciliação", 'span[aria-label="Backoffice Conciliação"] '),
    ("Monitoramento Corban", 'span[aria-label="Monitoramento Corban"] '),
    ("CAC", 'span[aria-label="CAC"]')
]

# Opções CAC
CAC_OPTIONS = [
    ("Reembolso sem saldo credor", 'input[value="Pedido de reembolso de Seguro ou Cartão em que não há saldo credor a reembolsar na fatura"]'),
    ("Baixa de pagamento sem comprovante", 'input[value^="Pedido de baixa de pagamento sem envio do comprovante de pagamento"]'),
    ("Dentro dos 10 dias", 'input[value="Pedido de reembolso de Saque dentro do prazo de 10 dias corridos para reembolso em lote"]'),
    ("Duplicidade nos casos", 'input[value="Caso aberto em duplicidade quando o caso original ainda está dentro do prazo"]')
]

# Opções de pendências
PENDING_OPTIONS = ["ABERTO >>> PENDENTE", "PENDENTE >>> FINALIZADO"]

# Configurações do navegador
BROWSER_OPTIONS = [
    "--headless=new",
    "--disable-gpu", 
    "--window-size=1920,1080"
]