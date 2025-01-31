"""This python file provides all the necessary methods (APIs) to perform the testing for the
'https://www.saucedemo.com/' website login page """

"Import all the necessary libraries"

from Config.config import TestData
import pytest
from playwright.sync_api import Playwright, sync_playwright


class LoginPage(TestData):

    def __init__(self, plywr: Playwright, base_url: str, headless=False):
        self.browser = plywr.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    """Go to base-URL"""

    def webPage_Launch(self, url):
        self.page.goto(url=url)

    """Test method to verify the URL title"""

    def urlTitle(self):
        title = self.page.title()
        print("The URL page title is: ", title)
        return title

    """Test teardown method"""
    def close_session(self):
        self.page.close()
        self.context.close()
        self.browser.close()
