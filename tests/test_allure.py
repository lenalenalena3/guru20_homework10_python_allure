import allure
from allure_commons.types import Severity
from selene import browser, be, have

from github_tests.model.pages.application import app


def test1_allure_not():
    search_test = "lenalenalena3/lesson2_python"
    issues = 'Issues 2406'

    browser.open('https://github.com')
    app.github_page.search_icon.should(be.visible).click()
    app.github_page.search_input.should(be.visible).send_keys(search_test).press_enter()
    app.github_page.search_result(search_test).should(be.visible).click()
    app.github_page.issues_tab.should(be.visible).click()
    app.github_page.issues_tab_input.should(have.value_containing("is:issue"))
    app.github_page.issues_result(issues).should(be.visible)


def test2_allure_with():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label("owner", "tinkalyuk")
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Переход по ссылке репозитория")
    allure.dynamic.link("https://github.com", name="Testing")
    allure.dynamic.title("Переход по ссылке репозитория вариант 1 (with)")
    allure.dynamic.description("Тест c использованием with")
    allure.dynamic.epic("Эпик")

    search_test = "lenalenalena3/lesson2_python"
    issues = 'Issues 2406'

    with allure.step("Открываем главую страницу GitHub"):
        browser.open('https://github.com')
    with allure.step(f"Ищем репозиторий {search_test}"):
        app.github_page.search_icon.should(be.visible).click()
        app.github_page.search_input.should(be.visible).send_keys(search_test).press_enter()
    with allure.step(f"Переходим по ссылке репозитория {search_test}"):
        app.github_page.search_result(search_test).should(be.visible).click()
    with allure.step("Открываем вкладку Issue"):
        app.github_page.issues_tab.should(be.visible).click()
        app.github_page.issues_tab_input.should(have.value_containing("is:issue"))
    with allure.step(f"На вкладке Issue проверяем, что есть {issues}"):
        app.github_page.issues_result(issues).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "tinkalyuk")
@allure.feature("Задачи в репозитории")
@allure.story("Переход по ссылке репозитория")
@allure.link("https://github.com", name="Testing")
@allure.title("Переход по ссылке репозитория вариант 2 (@allure.step)")
@allure.description("Тест с использованием @allure.step")
@allure.epic("Эпик")
def test3_allure_step():
    search_test = "lenalenalena3/lesson2_python"
    issues = 'Issues 2406'

    app.github_page.open_github_page()
    app.github_page.search(search_test)
    app.github_page.open_link(search_test)
    app.github_page.open_issues()
    app.github_page.should_issues(issues)