from playwright.sync_api import Page
import config

class IndexPage:

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def get_text_from_google_search_button(self, page: Page) -> None:
        self.BUTTON_GOOGLE_SEARCH = ".gNO89b"
        return page.locator(self.BUTTON_GOOGLE_SEARCH).first.get_attribute("value")