from playwright.sync_api import sync_playwright

def auto_book():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False so you SEE it working
        page = browser.new_page()

        # Step 1: Go to site
        page.goto("https://www.txdpsscheduler.com")

        # Step 2: Click on "Schedule an Appointment"
        page.click("text=Schedule an Appointment")

        # Step 3: Select service type (example: driver license)
        page.select_option("select#ServiceType", "DL")

        # Step 4: Enter ZIP code and search
        page.fill("input#zipCode", "75001")  # CHANGE TO YOUR ZIP
        page.click("button#searchBtn")

        # Step 5: Wait for available slots
        page.wait_for_selector("div.results")
        slots = page.query_selector_all("div.slot")

        if slots:
            print("🎉 Appointment found! Trying to book...")

            # Step 6: Click first slot
            slots[0].click()

            # Step 7: Fill in details (YOU must provide real info here)
            page.fill("input#firstName", "John")   # CHANGE TO YOUR FIRST NAME
            page.fill("input#lastName", "Doe")     # CHANGE TO YOUR LAST NAME
            page.fill("input#dob", "01/01/1990")   # CHANGE TO YOUR DOB
            page.fill("input#phone", "1234567890") # CHANGE TO YOUR PHONE
            page.fill("input#email", "your@email.com")

            # Some sites ask for Driver License Number
            # page.fill("input#dlNumber", "12345678")

            # Step 8: Confirm booking
            page.click("button#confirmAppointment")

            print("✅ Appointment booked successfully!")
        else:
            print("😢 No slots available right now.")

        browser.close()

if __name__ == "__main__":
    auto_book()
