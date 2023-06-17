# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from atf import log
from atf.ui import *
import datetime


class MainPageSbisRu(Region):

    contact = CustomList(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title.NavigationPanels-Accordion__title_level-1', 'Контакты')
    contact1 = CustomList(By.CSS_SELECTOR, 'div span.NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with-separator.NavigationPanels-Accordion__prevent-default', 'Контакты')


class ContactDialog(Region):
    plus = Button(By.CSS_SELECTOR, 'span i.controls-Button__icon.controls-BaseButton__icon.controls-icon_size-m.controls-icon_style-default.controls-icon.icon-RoundPlus', 'Плюс')
    sotrud = CustomList(By.CSS_SELECTOR, '.ws-align-self-center.addressee-selector-popup__browser-tab-caption.controls-Tabs__item_overflow', 'Сотрудники')
    selector = '[name="ws-input_' + datetime.datetime.now().strftime('%Y-%m-%d') + '"]'
    name = TextField(By.CSS_SELECTOR, selector, 'Имя')
    user_mail = CustomList(By.CSS_SELECTOR, '.controls-fontsize-l.ws-ellipsis', 'Иванов Иван')
    letter_field = TextField(By.CSS_SELECTOR, 'div p.textEditor_Viewer__Paragraph', 'Письмо')
    letter = CustomList(By.CSS_SELECTOR, 'div.msg-dialogs-item__title.ws-flexbox.ws-justify-content-start.ws-flex-nowrap.ws-align-items-baseline', 'Письмо')
    letter_read = Element(By.CSS_SELECTOR, 'div div.msg-entity-layout__message-content.ws-flexbox.ws-flex-column.msg-entity-templates-content.msg-entity-layout__message-content_padding-right_default.msg-entity-templates-content_rounded.msg-entity-templates-content_background_blue p', 'Прочитанное письмо')
    letter_del = Button(By.CSS_SELECTOR, 'span i.controls-Button__icon.controls-BaseButton__icon.controls-icon_size-m.controls-icon_style-danger.controls-icon.icon-Erase', 'Удалить')
    empty_list = CustomList(By.CSS_SELECTOR, '.hint-Template__text_message.hint-Template__text_message_m', 'Пустой список')

class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '[name="Login"]', 'логин')
    password = TextField(By.CSS_SELECTOR, '[name="Password"]', 'пароль')


class Test(TestCaseUI):

    def test(self):
        sbis_site = self.config.get('SBIS_SITE')

        self.browser.open(sbis_site)

        log('Авторизоваться')
        user_login, user_password = self.config.get('USER_LOGIN'), self.config.get('USER_PASSWORD')
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER)
        auth_page.login.should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER)

        log('Перейти в реестр Контакты')
        main_page_online = MainPageSbisRu(self.driver)
        main_page_online.contact.item(1).scroll_into_view().click()
        main_page_online.contact1.item(1).scroll_into_view().click()

        log('Отправить сообщение самому себе')
        contact_dialog = ContactDialog(self.driver)
        contact_dialog.plus.mouse_click()
        contact_dialog.sotrud.should_be(Visible)
        contact_dialog.name.type_in('Иванов Иван' + Keys.ENTER)
        contact_dialog.user_mail.should_be(ExactText('Иванов Иван')).mouse_click()
        contact_dialog.letter_field.type_in(' Это текст письма' + Keys.CONTROL + Keys.ENTER)

        log('Убедиться, что сообщение появилось в реестре')
        contact_dialog.letter.should_be(Visible)
        contact_dialog.letter.item(1).click()
        contact_dialog.letter_read.should_be(ExactText('Это текст письма'))

        log('Удалить это сообщение и убедиться, что удалили')
        contact_dialog.letter_del.mouse_click()
        contact_dialog.empty_list.should_be(Visible)

