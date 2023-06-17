# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Задачи на вкладку "В работе"
# Убедиться, что выделена папка "Входящие" и стоит маркер.
# Убедиться, что папка не пустая (в реестре есть задачи)
# Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
# Создать новую папку и перейти в неё
# Убедиться, что она пустая
# Удалить новую папку, проверить, что её нет в списке папок
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from atf import log
from atf.ui import *


class MainPageSbisRu(Region):

    task = CustomList(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title.NavigationPanels-Accordion__title_level-1', 'Задачи')
    task_my = CustomList(By.CSS_SELECTOR, 'div span.NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with-separator.NavigationPanels-Accordion__prevent-default', 'На мне')


class TaskMenu(Region):
    incoming = CustomList(By.CSS_SELECTOR, '.ws-flexbox.ws-flex-nowrap.ws-flex-grow-1.ws-ellipsis.ws-align-items-center', 'Входящие')
    highlighted_marker = Element(By.CSS_SELECTOR, '.controls-StickyBlock__content', 'Маркер выделения')
    marker = Element(By.CSS_SELECTOR, '.controls-ListView__itemV_marker.controls-ListView__itemV_marker_size_content-xs.controls-ListView__itemV_marker-master_topPadding-default.controls-ListView__baseline_font-size.controls-Grid__row-cell__content_baseline_default', 'Маркер')
    task_list = CustomList(By.CSS_SELECTOR, '.controls-air-m.controls-BaseControl.controls_list_theme-default.controls_toggle_theme-default.edo3-Browser-view.controls-air-m.Hint-ListWrapper_list', 'Список задач')
    plus = Button(By.CSS_SELECTOR, 'span i.controls-Button__icon.controls-BaseButton__icon.controls-icon_size-m.controls-icon_style-default.controls-icon.icon-RoundPlus', 'Плюс')
    plus_menu = CustomList(By.CSS_SELECTOR,'.controls-Menu__content_baseline', 'Создать')
    name = TextField(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-InputBase__nativeField_caretFilled.controls-InputBase__nativeField_caretFilled_theme_default.controls-InputBase__nativeField_hideCustomPlaceholder', 'Имя папки')
    folder = TextField(By.CSS_SELECTOR, '.hint-Template__imageWrapper.controls_Hint_theme-default.hint-Template__imageWrapper_m_emptyView.hint-Template-HelpPersonImage-Common_wow_nothing_new.hint-EmptyView__imageWrapper_columnLayout_bottom', 'Задачи0')
    del_folder = Button(By.CSS_SELECTOR, '.controls-icon_size-m.controls-icon_style-danger.icon-24.icon-Erase.icon-error.controls-icon.controls-Menu__icon.controls-Menu__icon_m-left', 'удалить')
    confirm_body = CustomList(By.CSS_SELECTOR, '.controls-ConfirmationTemplate__body', 'потверждение')
    confirm = Button(By.CSS_SELECTOR, '.controls-BaseButton__wrapper.controls-Button__wrapper_viewMode-outlined.controls-BaseButton__wrapper_captionPosition_end.controls-Button_textAlign-center.controls-Button__wrapper_padding-default.controls-Button__wrapper_mode-button.controls-Button__wrapper_inline-height_default','ДА')



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

        log('Перейти в реестр Задачи на вкладку "В работе"')
        main_page_online = MainPageSbisRu(self.driver)
        main_page_online.task.item(2).scroll_into_view().click()
        main_page_online.task_my.item(1).scroll_into_view().click()

        log('Убедиться, что выделена папка "Входящие" и стоит маркер')
        task_menu = TaskMenu(self.driver)
        task_menu.incoming.item(1).should_be(ExactText('Входящие'))
        task_menu.incoming.item(1).element(task_menu.highlighted_marker.should_be(Enabled))
        task_menu.incoming.item(1).element(task_menu.marker.should_be(Enabled))

        log('Убедиться, что папка не пустая (в реестре есть задачи)')
        task_menu.task_list.should_be(Visible)

        log('Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято)')
        task_menu.incoming.item(2).mouse_click()
        task_menu.incoming.item(2).element(task_menu.highlighted_marker.should_be(Enabled))
        task_menu.incoming.item(1).should_not_be(CssClass(task_menu.highlighted_marker))
        task_menu.folder.should_be(Visible)

        log('Создать новую папку и перейти в неё')
        task_menu.incoming.item(1).mouse_click()
        task_menu.plus.mouse_click()
        task_menu.plus_menu.item(2).mouse_click()
        task_menu.name.should_be(Visible)
        task_menu.name.type_in(' Новая Папка' + Keys.CONTROL + Keys.ENTER)
        task_menu.incoming.item(3).mouse_click()

        log('Убедиться, что она пустая')
        task_menu.folder.should_be(Visible)

        log('Удалить новую папку, проверить, что её нет в списке папок')
        task_menu.incoming.item(3).context_click()
        task_menu.del_folder.mouse_click()
        task_menu.confirm_body.should_be(Visible)
        task_menu.confirm.mouse_click()
        task_menu.incoming.item(3).should_not_be(Visible)
