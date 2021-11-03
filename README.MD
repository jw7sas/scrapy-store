# Instalar Python - https://www.python.org/  - instalar pip -> se selecciona en la instalación de python.
Python 3.8.3
pip 20.3.3

# Instalar el ambiente virtual
pip install virtualenv
virtualenv venv

# Activar el entorno virtual en Windows
venv\Scripts\activate

# Instalación de dependencias
pip install -r requirements.txt

# Verificar si scrapy se instalo
scrapy version

# consola de Scrapy
    Listado de tiendas
        scrapy shell "https://jw7sas.github.io/tshops/index.html"
        response.xpath('//div[contains(@class, "content-panel")]//a[contains(@class, "panel-block")]/@href').getall()
    Listado titulos de tiendas
        response.xpath('//div[contains(@class, "asgeek-container")]//h1[contains(@class, "asgeek-title")]/text()').get()

# comandos scrapy
    scrapy startproject as_g_store
    scrapy crawl as_stores