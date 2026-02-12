import pytest
from playwright.sync_api import Page, expect
from config import FRANS_API_KEY, FRANS_BASE_URL


def test_frans_ui_has_title(page: Page):
    page.goto(FRANS_BASE_URL)
    
    expect(page).to_have_title("Frank's API test")


def test_create_studen_in_ui(page: Page):
    page.goto(FRANS_BASE_URL)
    page.get_by_placeholder("Enter your API key").fill(FRANS_API_KEY)
    page.get_by_placeholder("Enter name").fill("Test")
    page.get_by_placeholder("Enter age").fill("25")
    page.get_by_placeholder("Enter grade").fill("G")
    page.get_by_role("button", name="Add student").click()