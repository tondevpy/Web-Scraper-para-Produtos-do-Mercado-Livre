import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup

def salvarProduto(produto, dados):
    with open(f'{produto}.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{dados}\n')

while True:
    produto = input('Informe o nome do produto que deseja buscar: ').strip()

    if produto:
        produto_formatado = produto.replace(' ', '-')
        driver = uc.Chrome()

        driver.get(f'https://lista.mercadolivre.com.br/{produto_formatado}')
        sleep(5)

        source = driver.page_source

        soup = BeautifulSoup(source, 'html.parser')

        todos_dados = ''

        for div in soup.find_all('div', class_='andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated'):
            titulo = div.find('h2').text
            if produto.lower() in titulo.lower():
                    
                # Capturando o preço final com a classe específica
                preco_tag = div.find('span', class_='andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript')
                if preco_tag:
                    preco_final = preco_tag.find('span', class_='andes-money-amount__fraction').text

                # Capturando a URL do produto
                url = div.find('a', class_='ui-search-link__title-card').get('href')

                # Tentando capturar a pontuação do produto
                try:
                    pontuacao_tag = div.find('span', class_='ui-search-reviews__rating-number')
                    if pontuacao_tag:
                        pontuacao = pontuacao_tag.text
                    else:
                        pontuacao = 'Não possui avaliação disponível'
                except:
                    pontuacao = 'Não possui avaliação disponível'
                
                dados = f'\nTitulo: {titulo}\nPreço: {preco_final}\nPontuação: {pontuacao}\nURL: {url}\n===============================================\n'
                
                todos_dados += dados 

        salvarProduto(produto, todos_dados)

        # Fechar o driver para evitar acúmulo de processos
        driver.quit()
        
        sair = input('Caso deseje parar a busca digite (sair): ').lower()

        if 'sair' in sair:
            break
        else:
            continue
    else:
        print('Não informou o nome do produto....')


print('Feito por TonDevPy')