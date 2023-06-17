# Предварительные действия (Создайте эталонную задачу, заполнив обязательные поля)
# Авторизоваться на сайте https://fix-online.sbis.ru/
# Откройте эталонную задачу по прямой ссылке в новом окне
# Убедитесь, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА",где ДАТА и НОМЕР - это ваши эталонные значения
# Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from atf import log
from atf.ui import *

class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '[name="Login"]', 'логин')
    password = TextField(By.CSS_SELECTOR, '[name="Password"]', 'пароль')

class MainPageSbisRu(Region):

    task = CustomList(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title.NavigationPanels-Accordion__title_level-1', 'Задачи')
    task_my = CustomList(By.CSS_SELECTOR, 'div span.NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with-separator.NavigationPanels-Accordion__prevent-default', 'На мне')

class TaskMenu(Region):
    task_info = Element(By.CSS_SELECTOR, '.controls-Tabs-wrapper.controls-Tabs-wrapper__horizontal', 'Номер')
    task_target = Element(By.CSS_SELECTOR, '.controls-StackTemplate__content-area.controls-StackTemplate_backgroundColor', 'Данные задачи')



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

        log('Откройте эталонную задачу по прямой ссылке в новом окне')
        main_page_online = MainPageSbisRu(self.driver)
        main_page_online.task.item(1).should_be(Visible)
        url = 'https://fix-online.sbis.ru/opendoc.html?guid=9b38d8d2-eee4-4005-a037-73341447f3e6&client=13825325'
        self.browser.create_new_tab(url)
        self.browser.switch_to_opened_window()

        log('Убедитесь, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА",где ДАТА и НОМЕР - это ваши эталонные значения')
        number = '4'
        date = '15 июн, чт'
        task_menu = TaskMenu(self.driver)
        task_menu.task_info.should_be(ExactText(f'Задача\n{date}\n№\n{number}'))

        log('Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениям')
        name = 'Иванов И.И.'
        date_to = 'до 07.07.23'
        target = 'написать автотест'
        autor = 'Иванов И.И.'
        num = '4'
        task_menu.task_target.should_be(ContainsText(name), ContainsText(date_to), ContainsText(target), ContainsText(autor), ContainsText(num))

