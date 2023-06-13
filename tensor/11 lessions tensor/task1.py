# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

sbis_site = "https://sbis.ru"
tensor_site = "https://tensor.ru/about"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(sbis_site)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item.sbisru-Header__menu-item-1.mh-8.s-Grid--hide-sm').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'div.sbisru-Contacts__border-left.pl-20.pv-12 > a.sbisru-Contacts__logo-tensor.mb-8 > img').click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[1])
target = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')
ActionChains(driver).scroll_to_element(target).perform()
assert "Сила в людях" in str(target.get_attribute('textContent'))
driver.find_element(By.CSS_SELECTOR, 'div.tensor_ru-Index__block4-content.tensor_ru-Index__card p a').click()
assert driver.current_url == tensor_site
time.sleep(3)




