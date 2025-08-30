# Sistema de Autenticação de Chaves

## 📋 Descrição

Este é um sistema de autenticação desenvolvido em Python que permite validar chaves de licença através de uma interface gráfica moderna. O sistema utiliza o Google Sheets como banco de dados para armazenar e verificar o status das chaves, oferecendo uma solução simples e eficiente para controle de licenças.

## 🎯 Funcionalidades

- **Interface Gráfica Moderna**: Utiliza CustomTkinter para uma experiência visual aprimorada
- **Validação de Chaves**: Verifica se a chave inserida existe e está ativa
- **Gerador de Chaves**: Ferramenta para gerar chaves aleatórias no formato padrão
- **Integração com Google Sheets**: Utiliza planilhas do Google como banco de dados
- **Feedback Visual**: Animações de carregamento e notificações coloridas
- **Interface Responsiva**: Layout adaptável com suporte a redimensionamento

## 🏗️ Estrutura do Projeto

```
projeto/
├── authenticator_ui.py      # Interface principal do sistema
├── validathor_keys.py       # Módulo de validação e acesso ao banco de dados
├── gerar_keys.py           # Gerador de chaves aleatórias
├── file_keys.json          # Credenciais da API do Google (não incluído)
└── README.md               # Este arquivo
```

## 🛠️ Tecnologias e Dependências

### Bibliotecas Python Necessárias

```bash
pip install customtkinter
pip install gspread
pip install oauth2client
```

### Dependências do Sistema

- **CustomTkinter**: Framework moderno para interfaces gráficas baseado no Tkinter
- **gspread**: Biblioteca para interação com Google Sheets
- **oauth2client**: Autenticação OAuth2 para APIs do Google
- **secrets**: Geração segura de números aleatórios (nativa do Python)
- **string**: Manipulação de strings (nativa do Python)
- **threading**: Execução de tarefas em paralelo (nativa do Python)

## ⚙️ Configuração

### 1. Configuração do Google Sheets

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Ative as APIs:
   - Google Sheets API
   - Google Drive API
4. Crie credenciais de conta de serviço:
   - Vá para "Credenciais" → "Criar credenciais" → "Conta de serviço"
   - Baixe o arquivo JSON das credenciais
   - Renomeie para `file_keys.json` e coloque na raiz do projeto

### 2. Configuração da Planilha

1. Crie uma planilha no Google Sheets chamada "Licenças"
2. Configure as colunas na primeira linha:
   - Coluna A: `chave`
   - Coluna B: `status`
3. Compartilhe a planilha com o email da conta de serviço (encontrado no arquivo JSON)
4. Adicione as chaves com status "Ativa" ou "Inativa"

Exemplo da planilha:
| chave    | status |
|----------|--------|
| ABCD123  | Ativa  |
| EFGH456  | Inativa|

## 🚀 Como Usar

### Executar o Sistema de Autenticação

```bash
python authenticator_ui.py
```

### Gerar Novas Chaves

```bash
python gerar_keys.py
```

## 📱 Interface do Usuário

A interface apresenta:

- **Campo de entrada**: Para inserir a chave de licença
- **Botão Submit**: Inicia o processo de validação
- **Animação de carregamento**: Feedback visual durante a verificação
- **Mensagens de status**: Confirmação se a chave é válida (verde) ou inválida (vermelha)

## 🔧 Personalização

### Modificar Aparência

No arquivo `authenticator_ui.py`, você pode alterar:

```python
ctk.set_appearance_mode("Dark")  # "Dark", "Light" ou "System"
ctk.set_default_color_theme("blue")  # "blue", "green" ou "dark-blue"
```

### Formato das Chaves

No arquivo `gerar_keys.py`, modifique o método `gerar_chave()` para alterar o padrão:

```python
# Padrão atual: 4 letras + 3 números (ex: ABCD123)
self.letras = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(4))
self.numeros = ''.join(secrets.choice(string.digits) for _ in range(3))
```

## 🔒 Segurança

- As chaves são geradas usando o módulo `secrets` para garantir aleatoriedade criptográfica
- A autenticação com Google Sheets utiliza OAuth2 para acesso seguro
- O arquivo `file_keys.json` deve ser mantido em segurança e não versionado

## ⚠️ Observações Importantes

1. **Arquivo de Credenciais**: O arquivo `file_keys.json` não está incluído no repositório por questões de segurança
2. **Conexão com Internet**: O sistema requer conexão para acessar o Google Sheets
3. **Permissões**: A conta de serviço deve ter acesso de leitura à planilha
4. **Nome da Planilha**: Certifique-se de que a planilha se chama exatamente "Licenças"

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no repositório do projeto.
