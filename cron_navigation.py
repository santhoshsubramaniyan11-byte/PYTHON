from playwright.sync_api import sync_playwright


URL = "http://172.16.16.70/codetrack/Login"


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    # ----------------------------------------
    # Open CodeTrack
    # ----------------------------------------

    page.goto(URL)

    print("CodeTrack opened.")

    print("Please login manually.")

    input(
        "After login and the home page is visible, "
        "press ENTER..."
    )

    print("Current URL:", page.url)

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
    # Verify Cron page
    # ----------------------------------------

    page.wait_for_load_state("domcontentloaded")

    print("\n========== RESULT ==========")

    print("URL:", page.url)

    print(
        "Cron Management visible:",
        page.get_by_text(
            "CRON Management",
            exact=False
        ).is_visible()
    )

    input(
        "\nNavigation test completed. "
        "Press ENTER to close..."
    )

    context.close()

    browser.close()