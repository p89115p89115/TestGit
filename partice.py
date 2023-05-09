from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from .index_page import IndexPage

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()
    driver.get("http://demostore.supersqa.com/")

    index_page = IndexPage(driver)
    product_name = 'Album'
    # Click Add To Cart - Album
    index_page.click_to_add_cart(product_name)

    # Click view cart element
    index_page.click_view_cart()

    # Change quantity to 2
    qty = 2
    index_page.change_qty(qty)

    # Click Update Cart Button
    index_page.click_update_cart()

    # Wait for Update Success Message
    updated_msg_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "woocommerce-message"))
    )

    # Get Unit Price Value
    unit_price_elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Album']/ancestor::tr/descendant::span[contains(@class, 'amount')]/bdi"))
    )

    # Get Subtotal Value
    subtotal_text_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located( (By.XPATH, "//td[@data-title='Subtotal']/descendant::bdi"))
    )

    expect_subtotal = float(unit_price_elem.text[1:]) * qty

    assert float(subtotal_text_elem.text[1:]) == float(unit_price_elem.text[1:]) * qty, \
        f"Expected: {expect_subtotal}, Actual: {float(subtotal_text_elem.text[1:])}"

finally:
    driver.quit()
