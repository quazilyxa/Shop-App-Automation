import re
import time
import random
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class OrderPage(BasePage):
    
    PREPARING_TAB = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Preparing"]'
    )

    ORDER_CARD = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[contains(@content-desc, "Total") and contains(@content-desc, "LBP")]'
    )
    
    ORDER_SUMMARY = (
        AppiumBy.XPATH,
        '//android.widget.TextView[contains(@text, "Order Summary")]'
    )

    VIEW_BARCODE = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="View Barcode"]'
    )

    BARCODE_CLOSE_BUTTON = (
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().className("com.horcrux.svg.PathView")'
    )

    PRODUCT_IMAGE = (
        AppiumBy.XPATH,
        '(//android.widget.ImageButton[@content-desc="View product image"])[1]/android.view.ViewGroup/android.widget.ImageView'
    )

    SEARCH_FIELD = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@text="Search"]'
    )
    
    SEARCH_FIELD_2 = (
    AppiumBy.XPATH,
    '//android.widget.EditText[@text and string-length(@text) > 0]'
    )

    READY_FOR_PICKUP = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Ready for pick-up"]'
    )

    CONFIRM_BUTTON = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Confirm"]'
    )
    
    def click_preparing(self):
        print("→ Looking for Preparing tab...")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.PREPARING_TAB)
        )

        self.driver.find_element(*self.PREPARING_TAB).click()

        print("✓ Preparing tab clicked")

        # Give Preparing orders time to load
        time.sleep(3)

        print("✓ Preparing orders loaded")
    
    
    
    
    def click_random_order(self):
        print("→ Looking for Preparing order cards...")

        # Give the order list time to load
        time.sleep(3)

        order_cards = self.driver.find_elements(
            *self.ORDER_CARD
        )

        if not order_cards:
            raise AssertionError(
                "No order cards were found in Preparing"
            )

        print(
            f"✓ Found {len(order_cards)} order card(s)"
        )

        # Select a random order
        random_card = random.choice(order_cards)

        print("✓ Random order selected")

        # --------------------------------------------------
        # Delay selected order
        # --------------------------------------------------

        print("→ Looking for Delay Order button...")

        delay_button = random_card.find_element(
            AppiumBy.XPATH,
            './/android.widget.TextView[@text="Delay Order"]'
        )

        delay_button.click()

        print("✓ Delay Order clicked")
        

        
        print("→ Waiting for 20 Min option...")

        WebDriverWait(
            self.driver, 20
        ).until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="20 Min"]'
                )
            )
        )

        self.driver.find_element(
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="20 Min"]'
        ).click()

        print("✓ 20 Min selected")

 
        # --------------------------------------------------
        # First popup
        # --------------------------------------------------

        print("→ Waiting for Done button...")

        WebDriverWait(
            self.driver, 20
        ).until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Done"]'
                )
            )
        )

        self.driver.find_element(
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Done"]'
        ).click()

        print("✓ Done clicked")

        # --------------------------------------------------
        # Second popup
        # --------------------------------------------------

        print("→ Waiting for Ok button...")

        WebDriverWait(
            self.driver, 20
        ).until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@text="Ok"]'
                )
            )
        )

        self.driver.find_element(
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Ok"]'
        ).click()

        print("✓ Ok clicked")

        # --------------------------------------------------
        # Wait for order list to reload
        # --------------------------------------------------

        print("→ Waiting for order list to reload...")

        time.sleep(5)

        print("✓ Order list reloaded")

        # --------------------------------------------------
        # Open the selected order
        # --------------------------------------------------

        print("→ Opening selected order...")

        # Refresh the order cards because the UI changed
        order_cards = self.driver.find_elements(
            *self.ORDER_CARD
        )

        if not order_cards:
            raise AssertionError(
                "No order cards found after delay operation"
            )

        print(
            f"✓ Found {len(order_cards)} order card(s) after delay"
        )

        # For now, click the first available card
        order_cards[0].click()

        print("✓ Order card clicked")

        # Give order details time to open
        time.sleep(5)

        print("✓ Waiting for order details...")
    
    
    

    def wait_for_order_summary(self, timeout=30):
        print("→ Waiting for order summary to load...")

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(
                    self.ORDER_SUMMARY
                )
            )

            print("✓ Order summary loaded")

        except TimeoutException:
            raise AssertionError(
                "Order summary was not loaded"
            )

    def click_view_barcode(self):
        print("→ Looking for View Barcode...")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.VIEW_BARCODE)
        )

        self.driver.find_element(
            *self.VIEW_BARCODE
        ).click()

        print("✓ View Barcode clicked")

        # Give barcode popup time to load
        time.sleep(3)

        print("✓ Barcode popup loaded")

    def close_barcode_popup(self):
        print("→ Waiting for barcode popup close icon...")

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    self.BARCODE_CLOSE_BUTTON
                )
            )

            close_buttons = self.driver.find_elements(
                *self.BARCODE_CLOSE_BUTTON
            )

            visible_buttons = []

            for button in close_buttons:
                try:
                    if button.is_displayed():
                        visible_buttons.append(button)
                except Exception:
                    continue

            if not visible_buttons:
                raise AssertionError(
                    "Barcode popup close icon was not visible"
                )

            # Click the last visible PathView
            visible_buttons[-1].click()

            print("✓ Barcode popup closed")

        except TimeoutException:
            raise AssertionError(
                "Barcode popup close icon was not found"
            )

        # Give the underlying page time to become active
        time.sleep(3)

        print("✓ Returned to order summary")

    def get_first_product_name(self):
        print("→ Looking for products...")

        first_product_container = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]'
            '/android.widget.FrameLayout'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup[2]'
            '/android.widget.ScrollView'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup[4]'
            '/android.widget.ScrollView'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup[6]'
        )

        try:
            container = WebDriverWait(
                self.driver, 30
            ).until(
                EC.presence_of_element_located(
                    first_product_container
                )
            )

            print("✓ Product container found")

            text_views = container.find_elements(
                AppiumBy.XPATH,
                './/android.widget.TextView'
            )

            print(
                f"→ Found {len(text_views)} text element(s)"
            )

            for element in text_views:
                text = element.get_attribute("text")

                if not text:
                    continue

                print(f"   → {text}")

                # Match product name followed by quantity
                # Example: Carrot x2
                match = re.match(
                    r'^(.+?)\s+x\d+\b',
                    text.strip()
                )

                if match:
                    product_name = match.group(1).strip()

                    print(
                        f"✓ First product name: {product_name}"
                    )

                    return product_name

            raise AssertionError(
                "No product name with quantity was found"
            )

        except TimeoutException:
            raise AssertionError(
                "Product container was not found"
            )
    
    
    def open_first_product_image(self):
        print("→ Looking for first product image...")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                self.PRODUCT_IMAGE
            )
        )

        self.driver.find_element(
            *self.PRODUCT_IMAGE
        ).click()

        print("✓ First product image opened")

        # Give image viewer time to load
        time.sleep(3)

    def go_back_from_product_image(self):
        print("→ Going back from product image...")

        self.driver.back()

        # Give Order Summary time to return
        time.sleep(3)

        self.wait_for_order_summary()

        print("✓ Returned to Order Summary")

    def search_product(self, product_name):
        print(
            f"→ Searching for product: {product_name}"
        )

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.SEARCH_FIELD
            )
        )

        search_field = self.driver.find_element(
            *self.SEARCH_FIELD
        )

        search_field.click()
        search_field.send_keys(product_name)

        self.driver.hide_keyboard()

        print(
            f"✓ Searched for: {product_name}"
        )

        # Give search results time to appear
        time.sleep(3)

    def clear_search(self):
        print("→ Looking for search field...")

        search_field = WebDriverWait(
            self.driver, 20
        ).until(
            EC.presence_of_element_located(
                self.SEARCH_FIELD_2
            )
        )

        print(
            f"✓ Search field found: "
            f"{search_field.get_attribute('text')}"
        )

        search_field.clear()
        self.driver.hide_keyboard()

        print("✓ Search field cleared")

        time.sleep(2)
        
        
    def select_all_available(self):
        print("→ Selecting all available products...")

        product_container = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]'
            '/android.widget.FrameLayout'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup[2]'
            '/android.widget.ScrollView'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup[4]'
            '/android.widget.ScrollView'
            '/android.view.ViewGroup'
            '/android.view.ViewGroup[6]'
        )

        container = WebDriverWait(
            self.driver, 20
        ).until(
            EC.presence_of_element_located(product_container)
        )

        print("✓ Product container found")

        # Unselected check marks have this structure:
        #
        # SvgView
        #   └── GroupView
        #       └── PathView
        #
        unchecked_marks = container.find_elements(
            AppiumBy.XPATH,
            './/com.horcrux.svg.SvgView'
            '/com.horcrux.svg.GroupView'
            '/com.horcrux.svg.PathView'
        )

        print(
            f"→ Found {len(unchecked_marks)} "
            "unselected product check mark(s)"
        )

        if not unchecked_marks:
            print("✓ All products are already selected")
            return

        for index, mark in enumerate(unchecked_marks, start=1):
            try:
                if mark.is_displayed():
                    mark.click()

                    print(
                        f"✓ Selected available product #{index}"
                    )

                    time.sleep(1)

            except Exception as e:
                print(
                    f"⚠ Could not select product #{index}: {e}"
                )

        print("✓ All available products selected")

    def click_ready_for_pickup(self):
        print("→ Looking for Ready for pick-up...")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                self.READY_FOR_PICKUP
            )
        )

        self.driver.find_element(
            *self.READY_FOR_PICKUP
        ).click()

        print("✓ Ready for pick-up clicked")

        # Give confirmation popup time to load
        time.sleep(3)

        print("✓ Confirmation popup loaded")

    def confirm_ready_for_pickup(self):
        print("→ Looking for Confirm...")

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.CONFIRM_BUTTON
            )
        )

        self.driver.find_element(
            *self.CONFIRM_BUTTON
        ).click()

        print("✓ Confirm clicked")