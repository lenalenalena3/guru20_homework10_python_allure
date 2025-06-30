import allure
from selene import browser, be, have


class GitHubPage:
    def __init__(self):
        self.search_icon = browser.element('.search-input')
        self.search_input = browser.element('#query-builder-test')
        self.issues_tab = browser.element('#issues-tab')
        self.issues_tab_input = browser.element("#repository-input")

    def search_result(self, value):
        return browser.element(f'a[href="/{value}"]')

    def issues_result(self, value):
        return browser.element(f'//a[.="{value}"]')

    @allure.step("Открываем главую страницу GitHub")
    def open_github_page(self):
        browser.open('https://github.com')

    @allure.step("Ищем репозиторий {value}")
    def search(self, value):
        self.search_icon.should(be.visible).click()
        self.search_input.should(be.visible).send_keys(value).press_enter()

    @allure.step("Открываем вкладку Issue")
    def open_issues(self):
        self.issues_tab.should(be.visible).click()
        self.issues_tab_input.should(have.value_containing("is:issue"))

    @allure.step("Переходим по ссылке репозитория {value}")
    def open_link(self, value):
        self.search_result(value).should(be.visible).click()

    @allure.step("На вкладке Issue проверяем, что есть {value}")
    def should_issues(self, value):
        self.issues_result(value).should(be.visible)
