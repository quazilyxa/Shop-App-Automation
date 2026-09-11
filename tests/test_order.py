import time

from pages import order_page
from pages.order_page import OrderPage




def test_preparing_order_flow(driver):

    order_page = OrderPage(driver)

    print("\n🚀 Starting Preparing Order flow...")

    # App is already logged in
    time.sleep(5)

    print("✓ Shop app opened")

    # Start directly from OrderPage
    order_page.click_preparing()
    print("✓ Preparing tab clicked")
    
    order_page.click_random_order()
    print("✓ Random order card clicked")
# --------------------------------------------------
    # Wait for Order Summary
    # --------------------------------------------------

    order_page.wait_for_order_summary()

    # --------------------------------------------------
    # Get first product name
    # --------------------------------------------------

    first_product_name = (
        order_page.get_first_product_name()
    )

    # --------------------------------------------------
    # View Barcode
    # --------------------------------------------------

    order_page.click_view_barcode()
    print("✓ Barcode opened")
    # Close barcode popup
    order_page.close_barcode_popup()

    # --------------------------------------------------
    # Open first product image
    # --------------------------------------------------

    order_page.open_first_product_image()
    print("✓ Open image popup")
    # --------------------------------------------------
    # Go back to Order Summary
    # --------------------------------------------------

    order_page.go_back_from_product_image()

    # --------------------------------------------------
    # Search first product
    # --------------------------------------------------

    order_page.search_product(
        first_product_name
    )

    # Give search result time to appear
    time.sleep(3)
    print("✓ Search result appeared")
    # --------------------------------------------------
    # Clear search
    # --------------------------------------------------

    order_page.clear_search()

    # --------------------------------------------------
    # Select all available
    # --------------------------------------------------

    order_page.select_all_available()
    print("✓ All available products selected")
    # --------------------------------------------------
    # Ready for pick-up
    # --------------------------------------------------

    order_page.click_ready_for_pickup()
    print("✓ Ready for pick-up button clicked")
    # --------------------------------------------------
    # Confirm
    # --------------------------------------------------

    order_page.confirm_ready_for_pickup()

    print("✓ Preparing order flow completed successfully")