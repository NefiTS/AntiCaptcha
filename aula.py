from anticaptchaofficial.recaptchav2proxyless import *

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

from selenium import webdriver

from selenium.webdriver.common.by import By

import time

import chave_api

import os

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link = "https://www.google.com/recaptcha/api2/demo"
navegador.get(link)

get_captcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')

resolvedor_captcha = recaptchaV2Proxyless()

# 0 ou 1, normalmente como 1 vai mostrando o status do serviço, teste
resolvedor_captcha.set_verbose(1)

resolvedor_captcha.set_key(chave_api) #Colocar a chave da API

resolvedor_captcha.set_website_url(link) # Referenciando o site/link

resolvedor_captcha.set_website_key(get_captcha) # Referenciando o local do captcha

resposta = resolvedor_captcha.solve_and_return_solution()

if resposta != 0 :
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
    navegador.find_element(By.ID, 'recaptcha-demo-submit').click()
else:
    print(resolvedor_captcha.err_string)


time.sleep(100)
