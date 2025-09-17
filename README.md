# Web Scraping com Scrapy e Playwright | OLX - Placas de Vídeo

Este projeto é um web scraper construído com a combinação do **Scrapy** e do **Playwright**, projetado para navegar e extrair dados de **placas de vídeo** da página da OLX. A ferramenta navega por múltiplas páginas, coletando informações relevantes e salvando-as de forma estruturada para análise.

### Funcionalidades

* **Navegação Inteligente:** Utiliza o Playwright para simular a interação de um navegador real, permitindo a navegação por páginas dinâmicas.
* **Extração de Dados:** Coleta informações detalhadas sobre **placas de vídeo** (preço, modelo, link, etc.).
* **Armazenamento Estruturado:** Os dados extraídos são organizados e salvos utilizando a biblioteca Pandas, facilitando a análise posterior.

### Tecnologias Utilizadas

* **Playwright:** Usado para renderizar páginas JavaScript e lidar com conteúdo dinâmico.
* **Pandas:** Para o tratamento e manipulação dos dados extraídos.
* **Python:** A linguagem de programação base do projeto.

### Como Rodar o Projeto

Para executar o web scraper, siga os passos abaixo:

1.  **Crie e ative o ambiente virtual** (recomendado).
2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *Certifique-se de que a Playwright também esteja instalada: `playwright install`*

3.  **Execute o crawler:**
    ```bash
    py index.py
    ```
