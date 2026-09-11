# from appium.webdriver.common.appiumby import AppiumBy
# import time
# from pages.base_page import BasePage


# class HomePage(BasePage):

#     NEW_TAB = (
#         AppiumBy.XPATH,
#         '//android.view.ViewGroup[@content-desc="New"]'
#     )

#     ORDER_CARD = (
#         AppiumBy.XPATH,
#         '//android.view.ViewGroup[contains(@content-desc, "Total") and contains(@content-desc, "LBP")]'
#     )
    
#     REJECT_ORDER_TEXT = (
#     AppiumBy.XPATH,
#     '//android.widget.TextView[@text="Reject Order"]'
#     )

#     def is_new_tab_displayed(self):
#         return self.is_visible(self.NEW_TAB)

#     def click_any_lbp_order(self):
#         if not self.is_new_tab_displayed():
#             raise AssertionError(
#                 "New tab is not displayed. Cannot select an order."
#             )

#         print("✓ New tab is displayed")

#         order_cards = self.driver.find_elements(*self.ORDER_CARD)

#         if not order_cards:
#             raise AssertionError(
#                 "No order card containing Total and LBP was found"
#             )

#         print(f"✓ Found {len(order_cards)} order card(s) with LBP total")

#         # Click the first matching order
#         order_cards[0].click()

#         print("✓ Order card clicked")
        
        
#     def reject_order(self):
#         print("→ Rejecting order...")

#         # Click Reject Order
#         reject_buttons = self.driver.find_elements(*self.REJECT_ORDER_TEXT)

#         if not reject_buttons:
#             raise AssertionError("Reject Order button was not found")

#         # There can be multiple "Reject Order" TextViews.
#         # The last one is the button at the bottom of the sheet.
#         reject_buttons[-1].click()

#         print("✓ Reject Order clicked")

#         time.sleep(1)

#         # Select rejection reason
#         # Bounds: [90,809][990,960]
#         reason_x = 540
#         reason_y = 884

#         self.driver.execute_script(
#             "mobile: clickGesture",
#             {
#                 "x": reason_x,
#                 "y": reason_y
#             }
#         )

#         print("✓ Rejection reason selected")

#         time.sleep(0.5)

#         # Click bottom "Reject Order" button
#         # Bounds: [101,1678][979,1741]
#         confirm_x = 540
#         confirm_y = 1709

#         self.driver.execute_script(
#             "mobile: clickGesture",
#             {
#                 "x": confirm_x,
#                 "y": confirm_y
#             }
#         )

#         print("✓ Order rejection confirmed")

from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class HomePage(BasePage):

    NEW_TAB = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[contains(@content-desc, "New")]'
    )

    ORDER_CARD = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[contains(@content-desc, "Total") and contains(@content-desc, "LBP")]'
    )

    REJECT_ORDER_TEXT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Reject Order"]'
    )
    
    ACCEPT_BUTTON = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Accept"]'
    )

    def is_new_tab_displayed(self):
        """
        Quick check only.
        Does not wait for a long time.
        """
        try:
            return self.driver.find_element(
                *self.NEW_TAB
            ).is_displayed()
        except Exception:
            return False

    def wait_for_new_tab(self, timeout=15):
        """
        Wait for New tab to appear after login.
        """
        try:
            WebDriverWait(
                self.driver,
                timeout
            ).until(
                EC.visibility_of_element_located(self.NEW_TAB)
            )

            return True

        except TimeoutException:
            return False

    def click_any_lbp_order(self):
        if not self.is_new_tab_displayed():
            raise AssertionError(
                "New tab is not displayed. Cannot select an order."
            )

        print("✓ New tab is displayed")

        order_cards = self.driver.find_elements(
            *self.ORDER_CARD
        )

        if not order_cards:
            raise AssertionError(
                "No order card containing Total and LBP was found"
            )

        print(
            f"✓ Found {len(order_cards)} "
            f"order card(s) with LBP total"
        )

        order_cards[0].click()

        print("✓ Order card clicked")

    def reject_order(self):
        print("→ Rejecting order...")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    self.REJECT_ORDER_TEXT
                )
            )
        except TimeoutException:
            raise AssertionError(
                "Reject Order button was not displayed within 10 seconds"
            )

        reject_buttons = self.driver.find_elements(
            *self.REJECT_ORDER_TEXT
        )


        if not reject_buttons:
            raise AssertionError(
                "Reject Order button was not found"
            )

        reject_buttons[-1].click()

        print("✓ Reject Order clicked")

        time.sleep(1)

        # Select rejection reason
        # Bounds: [90,809][990,960]
        self.driver.execute_script(
            "mobile: clickGesture",
            {
                "x": 540,
                "y": 884
            }
        )

        print("✓ Rejection reason selected")

        time.sleep(0.5)

        # Confirm rejection
        # Bounds: [101,1678][979,1741]
        self.driver.execute_script(
            "mobile: clickGesture",
            {
                "x": 540,
                "y": 1709
            }
        )

        print("✓ Order rejection confirmed")
        time.sleep(3)
        
    
    
    
    
    def click_another_lbp_order(self):
        """
        Find another available LBP order after returning to New orders.
        """
        time.sleep(2)

        order_cards = self.driver.find_elements(*self.ORDER_CARD)

        if not order_cards:
            raise AssertionError(
                "No LBP order cards were found after returning to New orders"
            )

        print(
            f"✓ Found {len(order_cards)} LBP order card(s) after returning"
        )

        # Click the first currently available card
        order_cards[0].click()

        print("✓ Another order card clicked")

    def wait_for_order_details_and_accept(self, timeout=30):
        """
        Give the order details page time to load,
        then wait for Accept button and click it.
        """

        print("→ Waiting for order details to load...")
        time.sleep(3)

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.ACCEPT_BUTTON)
            )
        except TimeoutException:
            raise AssertionError(
                f"Accept button was not displayed within {timeout} seconds"
            )

        print("✓ Order details loaded")
        print("✓ Accept button displayed")

        self.driver.find_element(*self.ACCEPT_BUTTON).click()

        print("✓ Order accepted")