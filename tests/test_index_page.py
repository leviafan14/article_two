import pytest
import pages

class TestFooter:
    import pages
    @pytest.mark.case_id(1)
    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.IndexPage.open_index_page(self, page)
        actual_result = pages.index_page.IndexPage.get_text_from_google_search_button(self, page)
        assert actual_result == "Поиск в Google", "Текст в кнопке не соответствует ожидаемомму результату"