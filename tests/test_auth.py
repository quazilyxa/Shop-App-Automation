from pages.login_page import LoginPage
from pages.home_page import HomePage
import time

from config.test_data import SHOP_EMAIL, SHOP_PASSWORD


def test_shop_login(driver):

    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    time.sleep(3)

    assert login_page.is_login_page_displayed(), \
        "Shop login page was not displayed"

    print("✓ Shop login page displayed")

    login_page.login(
        SHOP_EMAIL,
        SHOP_PASSWORD
    )

    print("✓ Shop login submitted")

    assert home_page.wait_for_new_tab(timeout=15), \
        "New tab was not displayed after login"

    print("✓ New tab displayed")

    home_page.click_any_lbp_order()

    print("✓ Order selected")

    home_page.reject_order()

    print("✓ Order rejected successfully")
    
    home_page.click_another_lbp_order()

    # Wait for order details to load and accept
    home_page.wait_for_order_details_and_accept(timeout=30)

    print("✓ Second order accepted successfully")