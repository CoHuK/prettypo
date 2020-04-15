from prettypo import PrettyPageObject

BUTTON_NAME = 'ok'
ELEMENTS_NAME = 'list_items'


class BasePage(PrettyPageObject):
    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.button(BUTTON_NAME, locator='Hello')
        self.elements(ELEMENTS_NAME, locator='locator')


def test_button_methods_present():
    obj = BasePage('driver')
    assert hasattr(obj, BUTTON_NAME)
    assert hasattr(obj, BUTTON_NAME + "_element")


def test_elements_method_present():
    obj = BasePage('driver')
    assert hasattr(obj, ELEMENTS_NAME + "_elements")
