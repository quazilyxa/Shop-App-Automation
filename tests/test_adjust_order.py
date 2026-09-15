import time

from pages.adjustOrder_page import AdjustOrderPage


def test_adjust_order_quantity(driver):

    print("\n🚀 Starting Adjust Order Quantity flow...")

    adjust_order_page = AdjustOrderPage(driver)

    time.sleep(5)

    print("✓ Shop app opened")

    adjust_order_page.adjust_last_order_quantity()

    print(
        "\n🎉 Adjust Order Quantity flow "
        "completed successfully"
    )