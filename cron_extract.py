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

    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2000)

    # ----------------------------------------
    # Apply today's date
    # ----------------------------------------

    page.get_by_role(
        "button",
        name=" Apply"
    ).click()

    print("Apply clicked.")

    page.wait_for_timeout(2000)

    # ----------------------------------------
    # Find table
    # ----------------------------------------

    print("\n========== TABLE ANALYSIS ==========")

    tables = page.locator("table")

    print("Tables found:", tables.count())

    for i in range(tables.count()):

        table = tables.nth(i)

        print(
            f"Table {i} | "
            f"Visible: {table.is_visible()}"
        )

        print(
            "Rows:",
            table.locator("tbody tr").count()
        )

    # ----------------------------------------
    # Use table containing S.NO / JOB NAME
    # ----------------------------------------

    table = page.locator("table").filter(
        has_text="JOB NAME"
    ).first

    rows = table.locator("tbody tr")

    print(
        "\nCron rows found:",
        rows.count()
    )

    # ----------------------------------------
    # Extract rows
    # ----------------------------------------

    failed_jobs = []

    for i in range(rows.count()):

        row = rows.nth(i)

        cells = row.locator("td")

        values = []

        for j in range(cells.count()):

            values.append(
                cells.nth(j).inner_text().strip()
            )

        print(
            f"\nROW {i + 1}:",
            values
        )

        # ------------------------------------
        # Check Status
        # ------------------------------------

        if values and values[-1].strip().lower() == "not completed":

            failed_jobs.append(values)

    # ----------------------------------------
    # Print failed jobs
    # ----------------------------------------

    print("\n========== NOT COMPLETED ==========")

    print(
        "Failed cron count:",
        len(failed_jobs)
    )

    for job in failed_jobs:

        print("\n")

        for index, value in enumerate(job):

            print(
                f"{index}: {value}"
            )

    # ----------------------------------------
    # Keep browser open
    # ----------------------------------------

    input(
        "\nExtraction complete. "
        "Press ENTER to close..."
    )

    browser.close()