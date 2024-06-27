#!/usr/bin/env python
# coding: utf-8

# # Como instalar/configurar/usar o `MathPix` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para instalar/configurar/usar o `MathPix` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and configurations for installing/configuring/using `MathPix` on `Linux Ubuntu`._

# ## Descrição
# 
# 
# O `MathPix` é uma ferramenta que utiliza tecnologia de reconhecimento óptico de caracteres (OCR) especializada em equações matemáticas. Ele permite aos usuários capturar equações matemáticas a partir de imagens ou documentos em formato PDF e convertê-las automaticamente em texto digital editável. Essa funcionalidade é especialmente útil para estudantes, professores e profissionais que precisam trabalhar com fórmulas matemáticas de maneira rápida e precisa.

# ### Construído com
# 
# Esta seção deve listar todas as principais estruturas/bibliotecas usadas para inicializar seu projeto, bem como a sequência de instalação. Deixe quaisquer complementos/plugins para a seção de agradecimentos. Aqui estão alguns exemplos.
# 
# * [![Texlive](https://img.shields.io/badge/Texlive-3776AB?style=flat-square&logo=latex&logoColor=white)](https://tug.org/texlive/)
# * [![JabRef](https://img.shields.io/badge/JabRef-44A833?style=flat-square&logo=latex&logoColor=white)](https://www.jabref.org/)
# * [![Texstudio](https://img.shields.io/badge/Texstudio-008080?style=flat-square&logo=latex&logoColor=white)](https://www.texstudio.org/)
# * [![MathPix](https://img.shields.io/badge/MathPix-008080?style=flat-square&logo=MathPix&logoColor=white)](https://mathpix.com/)
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# ## 1. Obtendo o aplicativo `Snip` e iniciando-o em seu Terminal (Avançado) [1]
# 
# Para instalar o `MathPix` no `Linux Ubuntu`, você pode seguir os seguintes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. Execute o comando: `cd ~/Downloads`
# 
# 4. Execute o comando: `wget https://download.mathpix.com/linux/Mathpix_Snipping_Tool-x86_64.v03.00.0050.AppImage -O Mathpix_Snipping_Tool.AppImage`
# 
# - (Nota: O link pode mudar, verifique https://mathpix.com/)
# 
# 5. Execute o comando: `chmod 777 ./Mathpix_Snipping_Tool-x86_64.v03.00.0104.AppImage`
# 
# 6. Execute o comando: `./Mathpix_Snipping_Tool-x86_64.v03.00.0104.AppImage`

# ## 1.1 Código completo para configurar/instalar
# 
# Para instalar o `MathPix` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```

# ## Referências
# 
# [1] MATHPIX. ***Snip for linux.*** Disponível em: <https://mathpix.com/docs/snip/linux-overview> (texto adaptado). Acessado em: 29/09/2023 22:41.
# 
# [2] OPENAI. ***VS code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 14/11/2023 18:56.
# 
