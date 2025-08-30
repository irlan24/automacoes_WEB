# Forms Project

Aplicação para automação de formulários usando CustomTkinter e Selenium.

## Estrutura do Projeto

```
forms_project/
│── ui.py              # Interface gráfica (CustomTkinter)
│── automation.py       # Automação (Selenium)
│── constants.py        # Constantes e dicionários fixos
│── main.py             # Ponto de entrada (roda o app)
│── README.md           # Este arquivo
```

## Descrição dos Módulos

### 1. `main.py`
- **Responsabilidade**: Ponto de entrada da aplicação
- **Função**: Inicializa e executa a aplicação principal
- **Dependências**: `ui.py`

### 2. `ui.py` 
- **Responsabilidade**: Interface gráfica completa
- **Funcionalidades**:
  - Criação de todos os elementos visuais (CustomTkinter)
  - Gerenciamento de eventos da interface
  - Validação de dados de entrada
  - Controle de fluxo da aplicação
  - Integração com o módulo de automação
- **Dependências**: `constants.py`, `automation.py`

### 3. `automation.py`
- **Responsabilidade**: Automação web com Selenium
- **Funcionalidades**:
  - Configuração do navegador
  - Processo de login automatizado
  - Preenchimento de formulários
  - Gerenciamento de casos (finalizado/transferido/pendente)
  - Submissão e validação de formulários
- **Dependências**: `constants.py`

### 4. `constants.py`
- **Responsabilidade**: Armazenamento de dados fixos
- **Conteúdo**:
  - URLs e links
  - Dicionários de analistas, produtos e assuntos
  - Configurações de interface
  - Seletores CSS/XPath
  - Opções de configuração do navegador

## Instalação e Configuração

### Dependências Necessárias
```bash
pip install selenium customtkinter webdriver-manager
```

### Configuração Inicial

1. **Edite o arquivo `constants.py`**:
   - `LINK_FORMS` URL real do formulário
   - Atualizações do dicionário `ALL_ANALYSTS` com os dados reais dos analistas
   - Ajustes dos seletores CSS/XPath conforme necessário

2. **ChromeDriver**:
   - Certifique-se de ter o ChromeDriver instalado e no PATH
   - Ou use `webdriver-manager` para download automático

## Como Usar

1. Execute o arquivo principal:
   ```bash
   python main.py
   ```

2. A interface será aberta com as seguintes seções:
   - **Formulário Principal**: Campos para produto, caso, CPF e assunto
   - **Histórico**: Lista de casos processados
   - **Login**: Credenciais do analista
   - **Canal de Entrada**: Seleção da origem do caso
   - **Configurações Especiais**: Status do caso (finalizado/transferido)
   - **Pendências**: Gerenciamento de casos pendentes

3. Preencha todos os campos obrigatórios e clique em "ENVIAR"

## Funcionalidades Principais

### Processamento de Casos
- **Finalizado**: Marca o caso como concluído
- **Transferido**: Move o caso para outra fila/equipe
- **Pendente**: Coloca o caso em status de espera

### Validações
- Verificação de campos obrigatórios
- Validação de produtos e assuntos
- Autenticação de analistas
- Verificação de canal de entrada
- Verificação de escolha individual"transferido/pendente"

### Histórico
- Contador de casos processados
- Lista de casos com timestamps
- Função para limpar histórico

## Personalização

### Adicionando Novos Produtos
Edite o arquivo `constants.py`:
```python
PRODUTO_4 = 'input[value="Novo Produto"]'
PRODUTOS[4] = PRODUTO_4
```

### Adicionando Novos Analistas
```python
ALL_ANALYSTS["novo_analista@email.com"] = "Nome do Analista"
```

### Modificando Seletores
Atualize os seletores CSS/XPath no arquivo `constants.py` conforme mudanças no formulário web.

## Estrutura de Classes

### FormsApp (ui.py)
- Classe principal da interface
- Gerencia todos os elementos visuais
- Controla o fluxo da aplicação

### WebAutomation (automation.py)
- Classe para automação web
- Encapsula todas as operações do Selenium
- Métodos independentes para cada ação

## Tratamento de Erros

A aplicação inclui tratamento de erros para:
- Falhas de login
- Problemas de conexão
- Elementos não encontrados
- Validações de dados

## Logs e Debug

Para debug, você pode adicionar prints ou usar o módulo `logging` nos pontos críticos do código.

## Contribuição

Para contribuir com o projeto:
1. Mantenha a separação de responsabilidades entre módulos
2. Adicione validações adequadas
3. Documente novas funcionalidades
4. Teste todas as modificações

## Versão

Versão atual: v3.0

## Screenshots das funcionalidades

Primeiro módulo funcional desenvolvida na interface gráfica (erro campo em branco)
![Campo em branco](https://github.com/irlan24/automacoes_WEB/blob/master/forms_project/funcionamento_img/coluna_final_pending.png)