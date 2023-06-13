# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys
import datetime


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://fix-online.sbis.ru/")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '[name="Login"]').clear()
driver.find_element(By.CSS_SELECTOR, '[name="Login"]').send_keys('sv.savelev.ip', Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, '[name="Password"]').clear()
driver.find_element(By.CSS_SELECTOR, '[name="Password"]').send_keys('Qwerty123', Keys.ENTER)
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title.NavigationPanels-Accordion__title_level-1').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'div span.NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with-separator.NavigationPanels-Accordion__prevent-default').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'span i.controls-Button__icon.controls-BaseButton__icon.controls-icon_size-m.controls-icon_style-default.controls-icon.icon-RoundPlus').click()
time.sleep(5)
selector = '[name="ws-input_'+datetime.datetime.now().strftime('%Y-%m-%d')+'"]'
driver.find_element(By.CSS_SELECTOR, selector).send_keys('Иванов Иван')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, selector).send_keys(Keys.ENTER)
time.sleep(4)
letter = "sv.savelev.ip"
driver.find_element(By.CSS_SELECTOR, 'div p.textEditor_Viewer__Paragraph').send_keys(letter, Keys.CONTROL + Keys.ENTER)
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, 'div.msg-dialogs-item__title.ws-flexbox.ws-justify-content-start.ws-flex-nowrap.ws-align-items-baseline').click()
time.sleep(5)
assert letter == str(driver.find_element(By.CSS_SELECTOR, 'div div.msg-entity-layout__message-content.ws-flexbox.ws-flex-column.msg-entity-templates-content.msg-entity-layout__message-content_padding-right_default.msg-entity-templates-content_rounded.msg-entity-templates-content_background_blue p').get_attribute('textContent')), 'письмо не ровно'
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'span i.controls-Button__icon.controls-BaseButton__icon.controls-icon_size-m.controls-icon_style-danger.controls-icon.icon-Erase').click()
time.sleep(4)
