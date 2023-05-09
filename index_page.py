from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from page_base import PageBase

class IndexPage(PageBase):
    #use tuple to store
    #add_to_cart_btn =( (By.XPATH, f"//h2[text()='Album']/ancestor::li/a[text()='Add to cart']") ) 
    #view_cart_btn = ( (By.XPATH, "//h2[text()='Album']/ancestor::li/a[@title='View cart']") )
    #change_qty_btn = ( (By.XPATH, "//a[text()='Album']/ancestor::tr/descendant::input[@title='Qty']") )
    update_cart_btn = ( (By.XPATH, "//button[text()='Update cart']") )
    update_message_btn = ( (By.CLASS_NAME, "woocommerce-message") )

    #def __init__(self,driver):
        #super().＿init__(driver)

    def add_to_cart_btn(self,product_name):
        return (By.XPATH, f"//h2[text()='{product_name}']/ancestor::li/a[text()='Add to cart']")
    
    def view_cart_btn(self,product_name):
        return (By.XPATH, f"//h2[text()='{product_name}']/ancestor::li/a[@title='View cart']")

    def change_qty_btn(self,product_name):
        return (By.XPATH, f"//a[text()='{product_name}']/ancestor::tr/descendant::input[@title='Qty'])

    def click_add_to_cart(self,product_name):
        # Click Add To Cart - Album
        add_to_cart_elem = find_element(self.add_to_cart_btn(product_name))
        add_to_cart_elem.click()
    
    def click_view_cart(self):
        go_to_cart_elem = find_element(self.view_cart_btn))
        go_to_cart_elem.click()
    
    def change_qty(self,qty):
        # Change quantity 
        qty_text_field_elem = find_element(self.change_qty_btn)
        qty_text_field_elem.clear()
        qty_text_field_elem.send_keys(qty)
    
    def click_update_cart(self):
        update_cart_btn_elem = find_element(self.update_cart_btn)
        update_cart_btn_elem.click()
    
    def update_message(self):
        updated_msg_elem = find_element(self.update_message_btn,false)
