from typing import Callable, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class PrettyPageObject(object):
    ELEMENT_TYPES = {'button',
                     'label',
                     'text_field',
                     'element',
                     'elements'}

    def button(self, name: str,
               by: Optional[By],
               locator: str,
               parent_getter: Optional[Callable[[], WebElement]]) -> None: ...

    def label(self, name: str,
              by: Optional[By],
              locator: str,
              parent_getter: Optional[Callable[[], WebElement]]) -> None: ...

    def text_field(self, name: str,
                   by: Optional[By],
                   locator: str,
                   parent_getter: Optional[Callable[[], WebElement]]) -> None: ...

    def element(self, name: str,
                by: Optional[By],
                locator: str,
                parent_getter: Optional[Callable[[], WebElement]]) -> None: ...

    def elements(self, name: str,
                 by: Optional[By],
                 locator: str,
                 parent_getter: Optional[Callable[[], WebElement]]) -> None: ...

    def __init__(self, driver):
        self.driver = driver

    def __getattribute__(self, name):
        if name in object.__getattribute__(self, 'ELEMENT_TYPES'):
            def temp_func(*args, **kwargs):
                return object.__getattribute__(self, '_add_methods')(*args, **kwargs, element_type=name)

            return temp_func
        return object.__getattribute__(self, name)

    def _add_methods(self, name, by=By.ID, locator=None, parent_getter=None, element_type='element'):
        def getter(self):
            if parent_getter is not None:
                return parent_getter().find_element(by, locator)
            return self.driver.find_element(by, locator)

        def multi_getter(self):
            if parent_getter is not None:
                return parent_getter().find_elements(by, locator)
            return self.driver.find_elements(by, locator)

        def texter(self):
            return getter(self).text

        def writer(self, text):
            getter(self).send_keys(text)

        def clicker(self):
            getter(self).click()

        if element_type == 'elements':
            setattr(PrettyPageObject, f'{name}_elements', multi_getter)
        else:
            setattr(PrettyPageObject, f'{name}_element', getter)
        if element_type == 'button':
            setattr(PrettyPageObject, f'{name}', clicker)
        if element_type == 'label':
            setattr(PrettyPageObject, f'{name}', property(texter))
        if element_type == 'text_field':
            setattr(PrettyPageObject, f'{name}', property(texter, writer))
