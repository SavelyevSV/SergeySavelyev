import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

s = Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)


#Открыть сайт и залогиниться
driver.get("https://qa.neapro.site/login")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("savelev_sv_1982@mail.ru")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)

#Заполнение паспорта
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
driver.find_element(By.ID, "surname").send_keys("Савельев")
driver.find_element(By.ID, "name").send_keys("Сергей")
driver.find_element(By.ID, "patronymic").send_keys("Владимирович")

driver.find_element(By.XPATH, '//*[@id="birthday"]/div/input').send_keys("15.08.1982")
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/table/tbody/tr[3]/td[5]").click()
time.sleep(1)

driver.find_element(By.ID, 'passportSeries').clear()
driver.find_element(By.ID, 'passportSeries').send_keys("1234")
driver.find_element(By.ID, 'passportNumber').clear()
driver.find_element(By.ID, 'passportNumber').send_keys("567890")

driver.find_element(By.XPATH, '//*[@id="dateOfIssue"]/div/input').send_keys("25.10.2005")

driver.find_element(By.ID, 'code').send_keys(Keys.CONTROL + "a")
driver.find_element(By.ID, 'code').send_keys(Keys.DELETE)
driver.find_element(By.ID, 'code').send_keys("123456")
driver.find_element(By.ID, 'cardId').clear()
driver.find_element(By.ID, 'cardId').send_keys("12345678910")

driver.find_element(By.ID, 'issued').send_keys("УВД г.Рыбинска")

driver.find_element(By.ID, 'phone').send_keys(Keys.CONTROL + "a")
driver.find_element(By.ID, 'phone').send_keys(Keys.DELETE)
driver.find_element(By.ID, 'phone').send_keys("9991234567")

driver.find_element(By.CSS_SELECTOR, "#address > div > div > input").send_keys(Keys.CONTROL + "a")
driver.find_element(By.CSS_SELECTOR, "#address > div > div > input").send_keys(Keys.DELETE)
time.sleep(1)

address = driver.find_element(By.XPATH, "//*[@id='address']/div/div/input")
address.send_keys("г Рыбинск, ул 50 Лет Влксм, д 42")
address.click()
wait = WebDriverWait(driver, 2)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vue-dadata__suggestions')))
address.send_keys(Keys.ARROW_DOWN)
address.send_keys(Keys.ENTER)
time.sleep(4)

#Прикрепление файла паспорта
filePath ='C:\\Users\\savel\\Desktop\\1.jpg'
driver.find_element(By.CSS_SELECTOR, '#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div.form.passport-form.document-form > div.body > div.upload-widget.upload-widget > input[type=file]').send_keys(filePath)
time.sleep(5)
driver.find_element(By.XPATH, "//div[@id='__layout']/div/div[3]/div/div/div[3]/div/div/div[2]/div[3]/div[9]/button[2]").click()

#Подтверждение паспорта в админке
driver.get("https://adminqa.neapro.site/login")
driver.find_element(By.ID, "admin_email").send_keys(" moderat@neapro.ru")
driver.find_element(By.ID, "admin_password").send_keys("Aa123456")
driver.find_element(By.NAME, "commit").click()

driver.find_element(By.XPATH, "//*[@id='students']/a").click()
driver.find_element(By.XPATH, "//*[@id='documents']/a").click()
driver.get("https://adminqa.neapro.site/documents?q%5Buser_id_eq%5D=1974&commit=%D0%A4%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C&order=id_desc")
driver.find_element(By.XPATH, "/html/body/div/div[4]/div[1]/div/form/div[2]/div[1]/div/div/table/tbody/tr[1]/td[6]/div/div[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)

#Вход студента, изменение номера телефона и выход
driver.get("https://qa.neapro.site/login")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("savelev_sv_1982@mail.ru")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)
driver.get("https://qa.neapro.site/cabinet/setting")
driver.get("https://qa.neapro.site/cabinet/security")
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/div/input").click()
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/div/input").send_keys(Keys.CONTROL + "a")
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/div/input").send_keys(Keys.DELETE)
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/div/input").send_keys("9996663311")
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/button").click()
time.sleep(3)
driver.find_element(By.XPATH, ".//*[@id='__layout']/div/div[1]/div/div[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[1]/div[1]/div/div").click()

#Удаление паспорта в админке
driver.get("https://adminqa.neapro.site/documents?q%5Buser_id_eq%5D=1974&commit=%D0%A4%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C&order=id_desc")
driver.find_element(By.XPATH, "/html/body/div/div[4]/div[1]/div/form/div[2]/div[1]/div/div/table/tbody/tr[1]/td[7]/div/a[3]").click()
driver.switch_to.alert.accept()


