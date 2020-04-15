# Python Pretty Page Object Generator
A simple tool to make your page objects pretty and save some time for standard methods implementation.
```python
from prettypo import PrettyPageObject


class BasePage(PrettyPageObject):
    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.button('ok', By.ID, 'ok')
        self.text_field('login', By.XPATH, '//login')
        self.label('welcome_message', locator='welcome_message')
        self.elements('custom_parameters', locator='locator')
        self.element('parent', locator='xxx')
        self.button('button_that_difficult_to_find', By.XPATH, '/a', parent_getter=self.parent_element)

def test_page(driver):
    page = BasePage(driver)
    page.login = 'SuperUser'
    page.ok()
    wait_for_element(page.welcome_message_element())
    assert page.welcome_message == "Welcome SuperUser"
```


## Usage
Just inherit your Base Page class from PrettyPageObject and that's all!

## Features
Prettypo generates several methods for the requested element depending on the type of the element

* self.button('name', by, locator, parent_getter) will generate next methods:
  * **name**() - to call click()
  * **name_element**() - to get full access to WebElement object
* self.text_field('name', by, locator, parent_getter)
  * **name** property to get element's _.text()_
  * **name**=string - setter is reassigned to _.send_keys(string)_
  * **name_element**() - to get full access to WebElement object
* self.elements('name', by, locator, parent_getter)
  * **name_elements**() - get list of WebElement objects
* self.label('name', by, locator, parent_getter)
  * **name** property to get element's _.text()_
  * **name_element**() - to get full access to WebElement object
