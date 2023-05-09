

class PageBase:

    def __init__(self,driver):
        self.driver = driver

    def find_element(self,locator,clickable = true):
        if clickable:
            elem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            return elem
        else:
            elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return elem
