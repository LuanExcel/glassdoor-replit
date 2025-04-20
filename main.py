from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime
from time import sleep

# Caminho para salvar o arquivo
download_dir = r"C:\Users\luanr\Downloads"

# ⚙️ Configurações do Firefox
options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # tradicional # Use "--headless" se der erro nessa

# 🔧 Cria o perfil e adiciona as preferências
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", download_dir)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.manager.focusWhenStarting", False)
profile.set_preference("browser.helperApps.alwaysAsk.force", False)

# 🚨 Corrigido: passa o perfil para o options
options.profile = profile

# Inicia o driver com o serviço e opções
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

# Dados de login
email="emanuel.santos@elsanalytics.com.br"
senha="#Tigre!2024"

# Acessa a página de login
driver.get("https://www.glassdoor.com.br/employers/ec/analytics/community-reviews/review-volume-trends.htm?currentPartnerId=211991&selectedEmployerId=600720&profileId=0&overviewStartDate=&graphStartDate=&graphEndDate=")
sleep(3)

# Realiza login
driver.find_element(By.XPATH, "//*[@id='inlineUserEmail']").send_keys(email)
sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/div/div/div/div[1]/div/div/div/div/form/div[2]/div/button").click()
sleep(3)
driver.find_element(By.XPATH, "//*[@id='inlineUserPassword']").send_keys(senha)
sleep(2)
driver.find_element(By.XPATH, "//*[@id='InlineLoginModule']/div/div[1]/div/div/div/div/form/div[2]/div/button").click()
sleep(2)

# Reacessa a página após login
driver.get("https://www.glassdoor.com.br/employers/ec/analytics/community-reviews/review-volume-trends.htm?currentPartnerId=211991&selectedEmployerId=600720&profileId=0&overviewStartDate=&graphStartDate=&graphEndDate=")
sleep(3)

# Coleta os cookies
cookies = driver.get_cookies()
cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}
cookies_string = '; '.join([f"{key}={value}" for key, value in cookie_dict.items()])
user_agent = driver.execute_script("return navigator.userAgent;")

# Print dos cookies
print(cookies_string)

# Fecha o navegador
driver.quit()
