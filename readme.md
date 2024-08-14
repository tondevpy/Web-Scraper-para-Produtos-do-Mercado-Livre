# Web Scraper para Produtos do Mercado Livre

Este é um script Python que utiliza `Selenium` e `BeautifulSoup` para realizar scraping de dados de produtos do Mercado Livre. O script permite que o usuário pesquise produtos específicos no Mercado Livre e extraia informações como título, preço, pontuação e URL dos produtos encontrados. Os dados coletados são armazenados em um arquivo de texto para posterior consulta.

## Requisitos

Antes de executar o script, certifique-se de que as seguintes dependências estão instaladas:

- Python 3.6 ou superior
- `undetected-chromedriver` (uma versão modificada do Selenium que evita a detecção pelo Google Chrome)
- `Selenium`
- `BeautifulSoup` (disponível através do pacote `bs4`)

### Instalação das Dependências

Você pode instalar as dependências necessárias usando o `pip`:

```bash
pip install undetected-chromedriver selenium beautifulsoup4


## Como Usar

1. **Execute o Script**: Execute o script `app.py` no seu ambiente Python.

2. **Informe o Nome do Produto**: Quando solicitado, digite o nome do produto que deseja buscar no Mercado Livre.

3. **Aguarde a Coleta de Dados**: O script abrirá uma janela do navegador e buscará os produtos no Mercado Livre. Ele coletará os dados relevantes e os salvará em um arquivo de texto com o nome do produto informado.

4. **Interromper a Busca**: Após a busca, o script perguntará se você deseja parar a busca. Para encerrar o script, digite "sair". Se desejar continuar buscando outros produtos, basta pressionar "Enter" sem digitar nada.

5. **Dados Salvos**: Os dados coletados serão salvos em um arquivo de texto na mesma pasta onde o script está localizado. O arquivo terá o nome do produto como título e conterá todas as informações dos produtos encontrados.

## Estrutura do Código

- **Importação de Bibliotecas**: O script utiliza `undetected_chromedriver` para abrir o navegador e acessar o site do Mercado Livre. `BeautifulSoup` é utilizado para fazer o parsing do conteúdo HTML.

- **Função `salvarProduto`**: Esta função salva os dados extraídos em um arquivo de texto.

- **Loop Principal**: O script entra em um loop onde o usuário pode buscar por diferentes produtos repetidamente. O loop continua até que o usuário digite "sair".

- **Extração de Dados**: Para cada produto encontrado, o script extrai o título, preço, pontuação e URL. Esses dados são então salvos no arquivo de texto correspondente.


Licença
Este projeto é fornecido sob a licença MIT. Sinta-se à vontade para usá-lo, modificá-lo e distribuí-lo conforme necessário.
