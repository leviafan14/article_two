from playwright.sync_api import Page
import config
import qase

class IndexPage:
    @qase.step(
        action = "Open the Index page",
        data = config.url.DOMAIN,
        expected_result  = "The page opened"
    )
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    @qase.step(
        action = "Check the text in the Google Search",
        expected_result = "The test os equal Google Search"
    )
    def get_text_from_google_search_button(self, page: Page) -> None:
        self.BUTTON_GOOGLE_SEARCH = ".gNO89b"
        return page.locator(self.BUTTON_GOOGLE_SEARCH).first.get_attribute("value")