import time
import random
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductSetPage:

    # --------------------------------------------------
    # Locators
    # --------------------------------------------------

    MENU_BUTTON = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Menu"])'
    )


    OUT_OF_STOCK_OPTION = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Out of Stock"]'
    )

    POPUP_CLOSE_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("com.horcrux.svg.PathView")'
    )

    OK_BUTTON = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Ok"]'
    )

    OUT_OF_STOCK_TAB = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Out of stock"])[1]'
    )

    IN_STOCK_OPTION = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="In Stock"]'
    )
    
    
    FIRST_CHECK_MARK = (
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().resourceId("product_item_checkbox_0")'
    )   
    
    
    PROFILE_BUTTON = (
    AppiumBy.XPATH,
    '//android.view.View[@content-desc="Profile"]'
    )

    PAST_ORDER = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[contains(@content-desc, "Total")]'
    )

    PAYOUT_BUTTON = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Payout"]'
    )

    REVIEW_ORDER_CARDS = (
    AppiumBy.XPATH,
    '//android.view.ViewGroup[@content-desc and string-length(@content-desc) > 0]'
    )
    
    OUT_OF_STOCK_TAB = (
    AppiumBy.XPATH,
    '//android.widget.TextView[@text="Out of stock"]'
    )

    IN_STOCK_OPTION = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="In Stock"]'
    )

    # --------------------------------------------------
    # Initialization
    # --------------------------------------------------

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # --------------------------------------------------
    # Menu
    # --------------------------------------------------

    def click_menu(self):
        print("→ Looking for Menu button...")

        self.wait.until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        )

        self.driver.find_element(
            *self.MENU_BUTTON
        ).click()

        print("✓ Menu clicked")

        time.sleep(2)

    # --------------------------------------------------
    # Select product
    # --------------------------------------------------
    def click_checkbox(self):
        print("→ Looking for first product check mark...")

        checkbox_locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("product_item_checkbox_0")'
        )

        self.wait.until(
            EC.presence_of_element_located(checkbox_locator)
        )

        checkboxes = self.driver.find_elements(*checkbox_locator)

        visible_checkboxes = [c for c in checkboxes if c.is_displayed()]

        if not visible_checkboxes:
            raise AssertionError("No visible product checkboxes found")

        print(f"✓ Found {len(visible_checkboxes)} visible checkbox(es)")

        visible_checkboxes[0].click()

        print("✓ First product check mark clicked")
        time.sleep(2)
    # --------------------------------------------------
    # Mark Out of Stock
    # --------------------------------------------------

    def click_out_of_stock(self):
        print("→ Waiting for Out of Stock option...")

        self.wait.until(
            EC.element_to_be_clickable(self.OUT_OF_STOCK_OPTION)
        )

        self.driver.find_element(
            *self.OUT_OF_STOCK_OPTION
        ).click()

        print("✓ Out of Stock clicked")

        time.sleep(2)

    # --------------------------------------------------
    # Close popup
    # --------------------------------------------------

    def close_popup(self):
        print("→ Waiting for popup close button...")

        self.wait.until(
            EC.presence_of_element_located(
                self.POPUP_CLOSE_BUTTON
            )
        )

        close_buttons = self.driver.find_elements(
            *self.POPUP_CLOSE_BUTTON
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
                "Popup close button was not visible"
            )

        visible_buttons[-1].click()

        print("✓ Popup closed")

        time.sleep(2)

    # --------------------------------------------------
    # Confirm Out of Stock
    # --------------------------------------------------

    def click_ok(self):
        print("→ Waiting for Ok button...")

        self.wait.until(
            EC.element_to_be_clickable(self.OK_BUTTON)
        )

        self.driver.find_element(
            *self.OK_BUTTON
        ).click()

        print("✓ Ok clicked")

        time.sleep(5)

        print("✓ Product page loaded")

    # --------------------------------------------------
    # Open Out of Stock
    # --------------------------------------------------

    def click_out_of_stock_tab(self):
        print("→ Looking for Out of stock tab...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.OUT_OF_STOCK_TAB
            )
        )

        self.driver.find_element(
            *self.OUT_OF_STOCK_TAB
        ).click()

        print("✓ Out of stock tab clicked")

        time.sleep(2)

    # --------------------------------------------------
    # Select product again
    # --------------------------------------------------




















    def select_out_of_stock_product(self):
        print("→ Selecting the out-of-stock product...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.FIRST_CHECK_MARK
            )
        )
        time.sleep(2)

        self.driver.find_element(
            *self.FIRST_CHECK_MARK
        ).click()

        print("✓ Out-of-stock product selected")

        time.sleep(2)

    # --------------------------------------------------
    # Change back to In Stock
    # --------------------------------------------------

    def click_in_stock(self):
        print("→ Waiting for Out of stock tab...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.OUT_OF_STOCK_TAB
            )
        )

        self.driver.find_element(
            *self.OUT_OF_STOCK_TAB
        ).click()

        print("✓ Out of stock tab clicked")

        time.sleep(2)

        print("→ Waiting for product selection...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.FIRST_CHECK_MARK
            )
        )

        self.driver.find_element(
            *self.FIRST_CHECK_MARK
        ).click()

        print("✓ Product selected")

        time.sleep(2)

        print("→ Waiting for In Stock button...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.IN_STOCK_OPTION
            )
        )

        self.driver.find_element(
            *self.IN_STOCK_OPTION
        ).click()

        print("✓ In Stock clicked")



        time.sleep(2)

    # --------------------------------------------------
    # Full Product Set flow
    # --------------------------------------------------

    def make_product_out_of_stock(self):
        self.click_menu()
        self.click_checkbox()
        self.click_out_of_stock()
        self.close_popup()
        self.click_ok()

    def make_product_in_stock(self):
        self.click_out_of_stock_tab()
        self.select_out_of_stock_product()
        self.click_in_stock()

        time.sleep(2)

        self.click_menu()

        print("✓ Product Set flow completed")
        
        
    def click_profile(self):
        print("→ Looking for Profile...")

        self.wait.until(
            EC.element_to_be_clickable(self.PROFILE_BUTTON)
        )

        self.driver.find_element(
            *self.PROFILE_BUTTON
        ).click()

        print("✓ Profile clicked")

        time.sleep(3)

        print("✓ Profile page loaded")
        
    
    def click_random_past_order(self):
        print("→ Looking for past orders...")

        time.sleep(2)

        orders = self.driver.find_elements(
            *self.PAST_ORDER
        )

        if not orders:
            raise AssertionError(
                "No past orders were found"
            )

        print(f"✓ Found {len(orders)} past order(s)")

        random_order = random.choice(orders)

        random_order.click()

        print("✓ Random past order clicked")

        # Give order details time to load
        time.sleep(5)

        print("✓ Past order details loaded")

        # Additional 2 second wait
        time.sleep(2)

        # Go back to Profile
        self.driver.back()

        print("✓ Returned to Profile")

        time.sleep(3)


    def click_payout(self):
        print("→ Looking for Payout...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.PAYOUT_BUTTON
            )
        )

        self.driver.find_element(
            *self.PAYOUT_BUTTON
        ).click()

        print("✓ Payout clicked")

        time.sleep(4)

        print("✓ Payout page loaded")
       
       
        
    def click_review(self):
        print("→ Looking for Review...")

        REVIEW_BUTTON = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Review"]'
        )

        self.wait.until(
            EC.element_to_be_clickable(REVIEW_BUTTON)
        )

        self.driver.find_element(
            *REVIEW_BUTTON
        ).click()

        print("✓ Review clicked")

        time.sleep(3)

        print("✓ Review page loaded")


    def click_random_review_order(self):
        print("→ Looking for review orders...")
        time.sleep(3)

        elements = self.driver.find_elements(
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc and string-length(@content-desc) > 0]'
        )

        review_orders = []

        for element in elements:
            try:
                desc = element.get_attribute("contentDescription")
                bounds = element.get_attribute("bounds")

                if not desc or not bounds:
                    continue

                # Ignore the top tabs/buttons
                if desc in ["Past Orders", "Payout", "Review"]:
                    continue

                # Review order cards are below the tab section.
                # Their bounds start around y >= 500.
                if bounds.startswith("[45,"):
                    review_orders.append(element)

            except Exception:
                continue

        if not review_orders:
            raise AssertionError("No review orders were found")

        print(f"✓ Found {len(review_orders)} review order(s)")

        for i, order in enumerate(review_orders):
            print(
                f"   [{i}] {order.get_attribute('contentDescription')}"
            )

        random_order = random.choice(review_orders)

        print(
            f"→ Selecting review order: "
            f"{random_order.get_attribute('contentDescription')}"
        )

        random_order.click()

        print("✓ Random review order clicked")

        time.sleep(5)

        print("✓ Review order details loaded")
        time.sleep(3)
        self.driver.back()
        time.sleep(2)
        
        
    
    
    def toggle_rider_note_setting(self):
        print("→ Looking for Settings...")

        SETTINGS_BUTTON = (
            AppiumBy.XPATH,
            '//android.view.View[@content-desc="Settings"]'
        )

        GENERAL_BUTTON = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="General"]'
        )

        RIDER_NOTE_SWITCH = (
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
            '/android.widget.ScrollView'
            '/android.view.ViewGroup'
            '/android.widget.Switch[2]'
            '/android.view.ViewGroup'
        )

        RIDER_NOTE_FIELD = (
            AppiumBy.XPATH,
            '//android.widget.EditText'
        )

        SAVE_BUTTON = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Save"]'
        )

        # ---------------------------------------------------------
        # 1. Open Settings
        # ---------------------------------------------------------
        print("→ Looking for bottom Settings...")

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.view.View[@content-desc="Settings"]')
            )
        )

        settings_button = self.driver.find_element(
            AppiumBy.XPATH,
            '//android.view.View[@content-desc="Settings"]'
        )

        print("✓ Bottom Settings found")

        settings_button.click()

        print("✓ Settings clicked")

        time.sleep(3)

        # ---------------------------------------------------------
        # 2. Open General
        # ---------------------------------------------------------
        print("→ Looking for General...")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(GENERAL_BUTTON)
        )

        self.driver.find_element(*GENERAL_BUTTON).click()
        print("✓ General clicked")

        time.sleep(4)
        print("✓ General page loaded")

        # ---------------------------------------------------------
        # 3. Turn ON Rider Note switch
        # ---------------------------------------------------------
        print("→ Looking for Rider Note switch...")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(RIDER_NOTE_SWITCH)
        )

        self.driver.find_element(*RIDER_NOTE_SWITCH).click()
        print("✓ Rider Note switch turned ON")

        time.sleep(2)

        # ---------------------------------------------------------
        # 4. Enter Rider Note
        # ---------------------------------------------------------
        print("→ Looking for Rider Note field...")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(RIDER_NOTE_FIELD)
        )

        rider_note_field = self.driver.find_element(*RIDER_NOTE_FIELD)
        rider_note_field.click()

        rider_note_field.send_keys(
            "Please contact the shop if you have any issue with the order."
        )

        print("✓ Rider Note entered")

        # ---------------------------------------------------------
        # 5. Hide keyboard
        # ---------------------------------------------------------
        self.driver.hide_keyboard()
        print("✓ Keyboard hidden")

        time.sleep(1)

        # ---------------------------------------------------------
        # 6. Save
        # ---------------------------------------------------------
        print("→ Looking for Save...")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(SAVE_BUTTON)
        )

        self.driver.find_element(*SAVE_BUTTON).click()
        print("✓ Settings saved")

        time.sleep(4)
        print("✓ General tab closed")

        # ---------------------------------------------------------
        # 7. Open General again
        # ---------------------------------------------------------
        print("→ Opening General again...")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(GENERAL_BUTTON)
        )

        self.driver.find_element(*GENERAL_BUTTON).click()
        print("✓ General opened again")

        time.sleep(4)
        print("✓ General page loaded again")

        # ---------------------------------------------------------
        # 8. Turn OFF Rider Note switch
        # ---------------------------------------------------------
        print("→ Looking for Rider Note switch again...")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(RIDER_NOTE_SWITCH)
        )

        self.driver.find_element(*RIDER_NOTE_SWITCH).click()
        print("✓ Rider Note switch turned OFF")

        time.sleep(2)

        # ---------------------------------------------------------
        # 9. Save again
        # ---------------------------------------------------------
        print("→ Looking for Save...")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(SAVE_BUTTON)
        )

        self.driver.find_element(*SAVE_BUTTON).click()
        print("✓ Rider Note setting disabled and saved")

        time.sleep(4)

        print("✓ Rider Note setting flow completed")
        
        
        
        
        
        
        
        
    def toggle_sunday_opening_hours(self):

        OPENING_HOURS_BUTTON = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Opening Hours"]'
        )

        SUNDAY_CLOSED = (
            AppiumBy.XPATH,
            '//android.widget.RadioButton[@content-desc="Sunday Closed"]'
            '/android.view.ViewGroup[2]'
        )

        SUNDAY_24_HOURS = (
            AppiumBy.XPATH,
            '//android.widget.RadioButton[@content-desc="Sunday 24 Hours"]'
            '/android.view.ViewGroup[2]'
        )

        SUNDAY_SPECIFIC_HOURS = (
            AppiumBy.XPATH,
            '//android.widget.RadioButton[@content-desc="Sunday Specific hours"]'
            '/android.view.ViewGroup[1]'
        )

        CONFIRM_BUTTON = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Confirm"]'
        )

        # ---------------------------------------------------------
        # 1. Open Opening Hours
        # ---------------------------------------------------------
        print("→ Looking for Opening Hours...")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(OPENING_HOURS_BUTTON)
        )

        self.driver.find_element(*OPENING_HOURS_BUTTON).click()

        print("✓ Opening Hours clicked")

        time.sleep(4)

        print("✓ Opening Hours page loaded")

        # ---------------------------------------------------------
        # 2. Check current Sunday selection
        # ---------------------------------------------------------
        print("→ Checking Sunday opening hour selection...")

        closed_radio = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SUNDAY_CLOSED)
        )

        hours_24_radio = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SUNDAY_24_HOURS)
        )

        specific_hours_radio = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SUNDAY_SPECIFIC_HOURS)
        )

        closed_selected = (
            closed_radio.get_attribute("selected") == "true"
        )

        hours_24_selected = (
            hours_24_radio.get_attribute("selected") == "true"
        )

        specific_hours_selected = (
            specific_hours_radio.get_attribute("selected") == "true"
        )

        print(f"   → Sunday Closed selected: {closed_selected}")
        print(f"   → Sunday 24 Hours selected: {hours_24_selected}")
        print(f"   → Sunday Specific hours selected: {specific_hours_selected}")

        # ---------------------------------------------------------
        # 3. Apply the required logic
        # ---------------------------------------------------------
        if closed_selected:
            print("→ Sunday is currently Closed")
            print("→ Changing Sunday to 24 Hours...")

            self.driver.find_element(*SUNDAY_24_HOURS).click()

            print("✓ Sunday changed to 24 Hours")

        elif hours_24_selected:
            print("→ Sunday is currently 24 Hours")
            print("→ Changing Sunday to Closed...")

            self.driver.find_element(*SUNDAY_CLOSED).click()

            print("✓ Sunday changed to Closed")

        elif specific_hours_selected:
            print("→ Sunday is currently Specific hours")
            print("→ Changing Sunday to Closed...")

            self.driver.find_element(*SUNDAY_CLOSED).click()

            print("✓ Sunday changed to Closed")

        else:
            raise AssertionError(
                "Could not determine the current Sunday opening hour selection"
            )

        time.sleep(2)

        # ---------------------------------------------------------
        # 4. Confirm
        # ---------------------------------------------------------
        print("→ Looking for Confirm...")

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(CONFIRM_BUTTON)
        )

        self.driver.find_element(*CONFIRM_BUTTON).click()

        print("✓ Confirm clicked")

        time.sleep(4)

        print("✓ Sunday Opening Hours setting saved")
        
        
        
        
        
        
        
        
        
    MENU_BUTTON_FIRST = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Menu"])[1]'
    )

    HIDE_OPTION = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Hide"]'
    )

    HIDDEN_ITEMS_TAB = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Hidden items"]'
    )

    UNHIDE_OPTION = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Unhide"]'
    )

    PRODUCT_CHECKBOX = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("product_item_checkbox_0")'
    )

    def hide_and_unhide_product(self):

        # --------------------------------------------------
        # 1. Wait for page to load
        # --------------------------------------------------
        print("→ Waiting for product page to load...")
        time.sleep(1)
        
        
        # --------------------------------------------------
        # 2. Click Menu
        # --------------------------------------------------
        print("→ Waiting for Menu...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.MENU_BUTTON_FIRST
            )
        )

        self.driver.find_element(
            *self.MENU_BUTTON_FIRST
        ).click()

        print("✓ Menu clicked")

        time.sleep(2)


        # --------------------------------------------------
        # 3. Select product
        # --------------------------------------------------
        print("→ Waiting for product checkbox...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.PRODUCT_CHECKBOX
            )
        )

        self.driver.find_element(
            *self.PRODUCT_CHECKBOX
        ).click()

        print("✓ Product selected")

        time.sleep(2)

        # --------------------------------------------------
        # 4. Click Hide
        # --------------------------------------------------
        print("→ Waiting for Hide option...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.HIDE_OPTION
            )
        )

        self.driver.find_element(
            *self.HIDE_OPTION
        ).click()

        print("✓ Hide clicked")

        time.sleep(3)

        # --------------------------------------------------
        # 5. Open Hidden Items
        # --------------------------------------------------
        print("→ Waiting for Hidden items...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.HIDDEN_ITEMS_TAB
            )
        )

        self.driver.find_element(
            *self.HIDDEN_ITEMS_TAB
        ).click()

        print("✓ Hidden items clicked")

        time.sleep(3)

        # --------------------------------------------------
        # 6. Select hidden product
        # --------------------------------------------------
        print("→ Waiting for hidden product checkbox...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.PRODUCT_CHECKBOX
            )
        )

        self.driver.find_element(
            *self.PRODUCT_CHECKBOX
        ).click()

        print("✓ Hidden product selected")

        time.sleep(2)

        # --------------------------------------------------
        # 7. Click Unhide
        # --------------------------------------------------
        print("→ Waiting for Unhide option...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.UNHIDE_OPTION
            )
        )

        self.driver.find_element(
            *self.UNHIDE_OPTION
        ).click()

        print("✓ Unhide clicked")

        time.sleep(3)

        # --------------------------------------------------
        # 8. Go to Menu again
        # --------------------------------------------------
        print("→ Waiting for Menu again...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.MENU_BUTTON_FIRST
            )
        )

        self.driver.find_element(
            *self.MENU_BUTTON_FIRST
        ).click()

        print("✓ Menu clicked again")

        time.sleep(2)

        print("✓ Hide and Unhide product flow completed")
        
    EDIT_PRODUCT_BUTTON = (
    AppiumBy.XPATH,
    '//android.widget.FrameLayout[@resource-id="android:id/content"]'
    '/android.widget.FrameLayout/android.view.ViewGroup'
    '/android.view.ViewGroup/android.view.ViewGroup'
    '/android.view.ViewGroup[2]/android.widget.ScrollView'
    '/android.view.ViewGroup/android.view.ViewGroup'
    '/android.view.ViewGroup[1]/android.widget.FrameLayout'
    '/android.view.ViewGroup/android.view.ViewGroup'
    '/android.view.ViewGroup[10]/android.widget.ScrollView'
    '/android.view.ViewGroup/android.view.ViewGroup'
    '/android.view.ViewGroup[3]/com.horcrux.svg.SvgView'
    '/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'
    )

    PRODUCT_UNIT_G = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="g"]'
    )

    PRODUCT_PRICE_FIELD = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@text and string-length(@text) > 0]'
    )

    UPDATE_BUTTON = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Update"]'
    )
    
    def edit_product_price(self):

        print("→ Waiting for product Edit icon...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.EDIT_PRODUCT_BUTTON
            )
        )

        self.driver.find_element(
            *self.EDIT_PRODUCT_BUTTON
        ).click()

        print("✓ Product Edit icon clicked")

        time.sleep(4)

        print("✓ Edit Product page loaded")

        # =========================================================
        # CHECK PRODUCT UNIT
        # =========================================================

        print("→ Checking product unit...")

        try:
            self.wait.until(
                EC.presence_of_element_located(
                    self.PRODUCT_UNIT_G
                )
            )

            print("✓ Product unit is g")
            print("→ Continuing with product price update...")

        except Exception:
            print("⚠ Product unit is not g")
            print("⚠ Product price update will be skipped")

            pytest.skip(
                "Product unit is not g. Product price update skipped."
            )

        # =========================================================
        # GET CURRENT PRICE
        # =========================================================

        print("→ Looking for product price field...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.PRODUCT_PRICE_FIELD
            )
        )

        price_field = self.driver.find_element(
            *self.PRODUCT_PRICE_FIELD
        )

        current_price_text = price_field.get_attribute("text")

        print(
            f"→ Current price displayed: "
            f"{current_price_text}"
        )

        # =========================================================
        # CONVERT CURRENT PRICE TO NUMBER
        # =========================================================

        try:
            current_price = float(
                current_price_text
                .replace("$", "")
                .strip()
            )

        except (ValueError, AttributeError):
            raise AssertionError(
                f"Could not read current product price: "
                f"{current_price_text}"
            )

        print(
            f"✓ Current product price: "
            f"${current_price:.2f}"
        )

        # =========================================================
        # GENERATE RANDOM PRICE ± $2
        # =========================================================

        min_price = max(
            0,
            current_price - 2
        )

        max_price = current_price + 2

        new_price = round(
            random.uniform(
                min_price,
                max_price
            ),
            2
        )

        print(
            f"→ Allowed price range: "
            f"${min_price:.2f} - ${max_price:.2f}"
        )

        print(
            f"→ Generated new random price: "
            f"${new_price:.2f}"
        )

        # =========================================================
        # UPDATE PRICE
        # =========================================================

        print("→ Updating product price...")

        price_field.click()

        price_field.clear()

        price_field.send_keys(
            f"{new_price:.2f}"
        )

        print(
            f"✓ New price entered: "
            f"${new_price:.2f}"
        )

        # =========================================================
        # HIDE KEYBOARD
        # =========================================================

        self.driver.hide_keyboard()

        time.sleep(1)

        # =========================================================
        # CLICK UPDATE
        # =========================================================

        print("→ Waiting for Update button...")

        self.wait.until(
            EC.element_to_be_clickable(
                self.UPDATE_BUTTON
            )
        )

        self.driver.find_element(
            *self.UPDATE_BUTTON
        ).click()

        print("✓ Update button clicked")

        # =========================================================
        # WAIT FOR UPDATE TO COMPLETE
        # =========================================================

        time.sleep(4)

        print(
            f"✓ Product price updated successfully "
            f"from ${current_price:.2f} "
            f"to ${new_price:.2f}"
        )