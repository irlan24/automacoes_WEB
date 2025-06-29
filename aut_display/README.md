
# FORMS com selenium

## O que faz?

Foi desenvolvido uma interface gráfica para preenchimento de um formulário, que contabiliza a produtividade (resolução no dia) da empresa na qual eu trabalho atualmente.

## Qual o objetivo?

Esse projeto tem por finalidade reduzir o tempo gasto em que levaria para o preenchimento manual do fomulário, mantendo o preenchimento padrão e alterando, de forma mais ágil, apenas as informações variáveis.

Também possui como objetivo masterizar os conhecimentos recem adquiridos no ramo de automação e python.

## O que é necessário utilizar para rodar o projeto?

1 - Necessário ter o python instalado, recomendo a versão mais recente (V 3.13.15 / download: https://www.python.org/downloads/);
2 - necessário importações de:
```bash
  from selenium import webdriver # Webdrive selenium
  from selenium.webdriver.chrome.options import Options # Nesse projeto, foi utilizado para ocultar a interface gráfica do selenium
  from selenium.webdriver.common.by import By # Usado para criar os seletores
  from selenium.webdriver.support.ui import WebDriverWait # Usado para criar tempos de esperas para os seletores
  from selenium.webdriver.support import expected_conditions as EC # Usado para criar condições em conjunto com o WebDriverWait
  from senhas import * # Arquivo com senhas de acesso e links
  from time import sleep # Pequenas pausas na automação  
  import customtkinter as ctk # Desenvolvimento da interface gráfica (necessário instalação)
  import threading # Usado para execução de multiplas telas em simultâneo 
```
3 - Toda automação foi desenvolvida com a biblioteca Selenium (documentação: https://www.selenium.dev/pt-br/documentation/)
4 - A interface gráfica foi desenvolvida com o customtkinter (necessário instalação prévia)
5 - Para converter em executável, recomendo o pyinstaller ou o cx_freeze (alguns casos, pyinstaller pode ser identificado como vírus pelo antivírus instalado, mas não é prejudicial ao sistema)

## Instalação

Instale my-project com terminal/VScode

```bash
  pip install selenium
  pip install cx_freeze
  pip install pyinstaller
  pip install customtkinter
```
    
## Screenshots funcionalidades
Primeiro módulo funcional desenvolvida na interface gráfica (erro campo em branco)
![Campo em branco](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/campo_em_branco.png)

Primeiro módulo funcional desenvolvida na interface gráfica (erro opção inválida)
![Opção inválida](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/opcao_invalida.png)

Primeiro módulo funcional desenvolvida na interface gráfica (Tela de carregamento durante funcionamento)
![Thread carregamento](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/thread_carregamento.png)

Primeiro módulo funcional desenvolvida na interface gráfica (erro no preenchimento do formulário)
![forms não enviado](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/forms_nao_enviado.png)

Primeiro módulo funcional desenvolvida na interface gráfica (Sucesso no preenchimento do formulário)
![forms enviado](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/forms_enviado.png)

Segundo módulo funcional desenvolvida na interface gráfica (Armazenamento do campo "Número do caso")
![forms enviado](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/att_segunda_coluna_0.png)

Terceiro módulo funcional desenvolvida na interface gráfica (Condições para envio do forms)
![forms enviado](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/att_terceira_coluna_0.png)

Terceiro módulo funcional desenvolvida na interface gráfica (Possibilidades de transferências para: )
![forms enviado](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/att_terceira_coluna_1.png)

Terceiro módulo funcional desenvolvida na interface gráfica (Condições de transferência para o CAC)
![forms enviado](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/att_terceira_coluna_2.png)

Implantação de bloco no segundo módulo da interface gráfica (Acesso do analista utilizando)
![forms enviado](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/att_segunda_coluna_1.png)

Implantação de bloco no segundo módulo da interface gráfica (Sucesso ao logar-se)
![forms enviado](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/att_segunda_coluna_2.png)

Implantação de bloco no segundo módulo da interface gráfica (Erro no e-mail)
![forms enviado](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/att_segunda_coluna_3.png)

Implantação de bloco no segundo módulo da interface gráfica (Erro na senha)
![forms enviado](https://github.com/irlan24/automacoes_WEB/blob/master/aut_display/funcionamento_img/att_segunda_coluna_4.png)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/irlan24?tab=repositories)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/irlan24/)


