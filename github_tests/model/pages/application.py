from github_tests.model.pages.github_page import GitHubPage


class Application:
    def __init__(self):
        self.github_page = GitHubPage()


app = Application()
