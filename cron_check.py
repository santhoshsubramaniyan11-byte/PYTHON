from playwright.sync_api import sync_playwright


URL = "http://172.16.16.70/codetrack/Login"


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # ----------------------------------------
    # Open CodeTrack
    # ----------------------------------------

    page.goto(URL)

    print("CodeTrack opened.")
    print("Please login manually.")

    input(
        "After login and home page is visible, "
        "press ENTER..."
    )

    # ----------------------------------------
    # PD Team
    # ----------------------------------------

    page.get_by_role(
        "link",
        name="PD Team"
    ).click()

    print("PD Team clicked.")

    # ----------------------------------------
    # Product Development
    # ----------------------------------------

    page.get_by_role(
        "link",
        name=" Product Development "
    ).click()

    print("Product Development clicked.")

    # ----------------------------------------
    # Cron
    # ----------------------------------------

    page.get_by_role(
        "link",
        name="Cron"
    ).click()

    print("Cron clicked.")

    # ----------------------------------------
    # Wait for Cron page
    # ----------------------------------------

    page.wait_for_load_state(
        "domcontentloaded"
    )

    page.wait_for_timeout(2000)

    print("Cron page loaded.")
    print("Current URL:", page.url)

    # ----------------------------------------
    # Click Apply
    # ----------------------------------------

    page.get_by_role(
        "button",
        name=" Apply"
    ).click()

    print("Apply clicked.")

    # Wait for table/results
    page.wait_for_timeout(3000)

    print("\n========== CRON RESULT ==========")

    # ----------------------------------------
    # Print page text
    # ----------------------------------------

    text = page.locator("body").inner_text()

    print(text)

    input(
        "\nPress ENTER to close the browser..."
    )

    browser.close()