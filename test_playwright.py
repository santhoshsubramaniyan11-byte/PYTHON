from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open CodeTrack
    page.goto("http://172.16.16.70/codetrack/Login")

    print("CodeTrack opened.")
    print("Please enter username/password and click SignIn or else.")

    # Wait for manual login
    page.wait_for_timeout(10000)

    print("Current URL:", page.url)

    # Click PD Team
    page.get_by_text("PD Team", exact=True).click()
    print("PD Team clicked successfully.")

    # Wait for PD Team menu
    page.wait_for_timeout(3000)

    # Click Cron
    page.locator('a[href="Cron_controller"]').first.click()
    print("Cron clicked successfully.")

    # Wait for Cron page
    page.wait_for_timeout(5000)

    print("Cron page URL:", page.url)

    input("Press ENTER to close the browser...")

    browser.close()