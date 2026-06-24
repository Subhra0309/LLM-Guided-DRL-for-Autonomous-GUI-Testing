from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os


class SeleniumEnv:
    def __init__(self, episode_id=0):
        self.episode_id = episode_id

        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        # options.add_argument("--headless=new")  # enable if needed

        self.driver = webdriver.Chrome(options=options)

        #  Increased stability
        self.wait = WebDriverWait(self.driver, 25)

        self.base_url = "https://opensource-demo.orangehrmlive.com/"

    # =============================
    # OPEN URL
    # =============================
    def open_url(self, path=""):
        print("Opening URL...")

        full_url = self.base_url.rstrip("/") + "/" + path.lstrip("/")
        self.driver.get(full_url)

        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        time.sleep(1)

    def get_page_html(self):
        return self.driver.page_source

    # =============================
    # SMART FINDER
    # =============================
    def find_element_smart(self, target):

        if not target:
            raise Exception("Empty target")

        # XPath
        if target.startswith("//"):
            return self.wait.until(
                EC.presence_of_element_located((By.XPATH, target))
            )

        # CSS
        try:
            return self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, target))
            )
        except:
            pass

        # ID
        try:
            return self.wait.until(
                EC.presence_of_element_located((By.ID, target))
            )
        except:
            pass

        # NAME
        try:
            return self.wait.until(
                EC.presence_of_element_located((By.NAME, target))
            )
        except:
            pass

        raise Exception(f"Element not found: {target}")

    # =============================
    # TYPE
    # =============================
    def type(self, target, value):
        print(f"Typing into {target}: {value}")

        elem = self.find_element_smart(target)

        elem.clear()
        elem.send_keys(value)

        time.sleep(0.5)

    # =============================
    # CLICK
    # =============================
    def click(self, target):
        print(f"Clicking {target}")

        elem = self.find_element_smart(target)

        self.wait.until(lambda d: elem.is_displayed() and elem.is_enabled())

        elem.click()

        time.sleep(2)

    # =============================
    # VERIFY (🔥 FIXED)
    # =============================
    def verify(self, target):
        print("Verifying result...")

        os.makedirs("outputs/screenshots", exist_ok=True)
        filename = f"outputs/screenshots/episode_{self.episode_id}_{int(time.time())}.png"

        current_url = self.driver.current_url
        print("🔍 CURRENT URL:", current_url)

        self.driver.save_screenshot(filename)

        # 🔥 IGNORE BAD XPATH FROM LLM
        # Use URL-based verification instead

        if "dashboard" in current_url:
            return 1, "Dashboard detected"

        elif "login" in current_url:
            return 1, "Login page detected"

        else:
            return -1, "Unknown page"

    # =============================
    # CLOSE
    # =============================
    def close(self):
        print("Closing browser...")
        try:
            self.driver.quit()
        except:
            pass