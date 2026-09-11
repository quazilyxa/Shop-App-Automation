import time

from pages import product_set_page
from pages.product_set_page import ProductSetPage


def test_product_set(driver):

    print("\n🚀 Starting Product Set flow...")

    product_set_page = ProductSetPage(driver)

    time.sleep(5)

    print("✓ Shop app opened")

    # --------------------------------------------------
    # Make product Out of Stock
    # --------------------------------------------------

    # print("\n→ Making product Out of Stock...")

    # product_set_page.make_product_out_of_stock()

    # print("✓ Product marked as Out of Stock")

    # # # --------------------------------------------------
    # # # Make the same product In Stock
    # # # --------------------------------------------------

    # print("\n→ Making product In Stock...")

    # product_set_page.click_in_stock()

    # print("✓ Product marked as In Stock")

    print("\n→ Hiding and Unhiding product...")

    product_set_page.hide_and_unhide_product()

    print("✓ Product successfully hidden and unhidden")
    
    
    
    #NEED TO FIX THIS TEST CASE, IT IS NOT WORKING AS EXPECTED
    
    # product_set_page.edit_product_price()
    # print("✓ Product price successfully updated")

    
    # product_set_page.click_profile()

    # print("✓ Successfully navigated to Profile")
    
    
    # product_set_page.click_random_past_order()
    # print("✓ Successfully navigated to a random past order")
    # # --------------------------------------------------
    # # Open Payout
    # # --------------------------------------------------

    # product_set_page.click_payout()
    # print("✓ Successfully navigated to Payout")
    # # --------------------------------------------------
    # # Open Review
    # # --------------------------------------------------
    
    # product_set_page.click_review()

    # print("✓ Successfully navigated to Review")

    # # --------------------------------------------------
    # # Open random review order
    # # --------------------------------------------------

    # product_set_page.click_random_review_order()

    # print("\n🎉 Profile flow completed successfully")
    
    print("\n🚀 Starting Rider Note Settings flow...")

    product_set_page.toggle_rider_note_setting()

    print("\n🎉 Rider Note Settings flow completed successfully")
    
    product_set_page.toggle_sunday_opening_hours()

    print("\n🎉 Opening Hours flow completed successfully")