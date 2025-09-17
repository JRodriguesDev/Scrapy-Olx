from .settings import randomAgent, randomTimezone
from playwright.sync_api import sync_playwright
import time

products = []
errors = []

input = 'teclado'

def olxScrapy():
    with sync_playwright() as pw:
        print("Abrindo navegador")
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent=randomAgent(),
            viewport={'width': 1366, 'height': 720},
            locale='pt-BR',
            timezone_id=randomTimezone(),
            extra_http_headers={
                'Accept-Language': 'pt-BR,pt;q=0.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            })
        page = context.new_page()
        print("Navegando ate a pagina da OLX...")
        page.goto(url='https://www.olx.com.br/', wait_until='load', timeout=60000)

        print("Iniciando Busca do Produto: " + input)
        searchInput = page.locator('input#oraculo-23-input')
        searchInput.fill(input)
        page.locator('button.ajfs2S').click()
        print("Carregando a lista de Anunciantes")
        time.sleep(5)
        def moreAds():
            ads = page.locator('section.olx-adcard.olx-adcard__horizontal.undefined').all()
            for ad in ads:
                try:
                    name = ad.locator('a.olx-adcard__link').get_attribute('title')
                    link = ad.locator('a.olx-adcard__link').get_attribute('href')
                    location = ad.locator('p.olx-text.olx-text--caption.olx-text--block.olx-text--regular.olx-adcard__location').inner_text()
                    day = ad.locator('div.olx-adcard__location-date').locator('p').nth(1).inner_text()
                    picture = ad.locator('div.olx-adcard__media picture img').get_attribute('src')
                    price =  price = ad.locator('div.olx-adcard__mediumbody h3.olx-text.olx-text--body-large.olx-text--block.olx-text--semibold.olx-adcard__price').inner_text()
                    installment = '-'
                    extra = []
                    tags = ad.locator('span.olx-badge.olx-badge--secondary.olx-badge--small.olx-badge--pill').all()
                    for tag in tags:
                        extra.append(tag.inner_text())
                    if (ad.locator('div.olx-adcard__price-info').count() > 0):
                        installment = ad.locator('div.olx-adcard__price-info span.olx-text.olx-text--caption.olx-text--inline.olx-text--bold').inner_text()
                    products.append({'name': name, 
                                    'link': link, 
                                    'price': price, 
                                    'location' :location,
                                    'picture': picture,
                                    'installment': installment,
                                    'extra': extra,
                                    'day': day,
                                    'site': 'OLX'
                                    })
                    print(name + " Adicionado a lista")
                except Exception as erro:
                    print(f"Error no Anuncio: {name}")
                    errors.append({'Produto': name, 'Link': link, 'location': location, 'day': day, 'error': erro})
                    continue
            if (page.locator('div.sc-5ebad952-1.iWtTZK').locator('button.olx-core-button.olx-core-button--link.olx-core-button--small').nth(-2).get_attribute('aria-disabled') != 'true'):
                print("Navegando ate a Proxima Lista de Anuncios")
                page.locator('div.sc-5ebad952-1.iWtTZK').locator('button').nth(-2).click()
                time.sleep(3)
                moreAds()
        moreAds()
        print("Fechando o Navegador")
        browser.close()
    return [products, errors]