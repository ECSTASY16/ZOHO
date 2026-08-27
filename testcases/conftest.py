import os
import subprocess

import allure
import pytest
from playwright.sync_api import sync_playwright

from pages.LoginPage import LoginPage
from utilities import configReader, dataProvider


# This is for launching single browser for all test cases to reduce the
# memory consumption
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()


@pytest.fixture(scope="class")
def page(browser):
    """Fresh, unauthenticated page — used by login tests that need to
    start at the login screen itself. Not autouse: only runs for tests
    that go through `setup` (which requests `page`)."""
    context = browser.new_context(no_viewport=True)

    # Start tracing before creating the page (recording screenshots,
    # snapshots, and sources)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    try:
        yield page
    finally:
        # Stop tracing and export to a zip file when the test completes
        context.tracing.stop(path="traces/failed_test_trace.zip")
        context.close()


@pytest.fixture(scope="class")
def login_page(setup):

    return LoginPage(setup)


@pytest.fixture(scope="class")
def setup(page):
    base_url = configReader.readConfig("baseurl", "url")
    page.goto(base_url, wait_until="domcontentloaded")
    return page


# ------------------------------------------------------------------
# Logged-in page fixture — for tests that require being logged in but
# are NOT testing the login flow itself (e.g. CRM, AllApps tests).
# Performs a real UI login every time it's used (simple, reliable —
# no storage_state/session sharing, no risk of stale/corrupted state).
# ------------------------------------------------------------------


@pytest.fixture(scope="function")
def logged_in_page(browser):
    context = browser.new_context(no_viewport=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto(configReader.readConfig("baseurl", "url"), wait_until="domcontentloaded")

    email, password = dataProvider.get_data("ValidUser")[0]
    LoginPage(page).click_login_link().enter_email(email).click_next().enter_password(
        password
    ).click_signIn_btn()
    page.wait_for_url("**/home**")

    try:
        yield page
    finally:
        context.tracing.stop(path="traces/failed_test_trace_crm.zip")
        context.close()


# ------------------------------------------------------------------
# Basic shared-login fixture — logs in ONCE per test session and
# saves the state to auth_state.json. Every test that requests
# `authenticated_page` reuses that saved session instead of logging
# in again. No expiry detection — kept intentionally simple.
# ------------------------------------------------------------------


@pytest.fixture(scope="session")
def auth_storage_state(browser):
    context = browser.new_context(no_viewport=True)
    login_page = context.new_page()
    login_page.goto(
        configReader.readConfig("baseurl", "url"), wait_until="domcontentloaded"
    )

    email, password = dataProvider.get_data("ValidUser")[0]
    LoginPage(login_page).click_login_link().enter_email(
        email
    ).click_next().enter_password(password).click_signIn_btn()
    login_page.wait_for_url("**/home**")

    state_path = "auth_state.json"
    context.storage_state(path=state_path)
    context.close()
    return state_path


@pytest.fixture(scope="function")
def authenticated_page(browser, auth_storage_state):
    context = browser.new_context(no_viewport=True, storage_state=auth_storage_state)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto(configReader.readConfig("baseurl", "url"), wait_until="domcontentloaded")

    try:
        yield page
    finally:
        context.tracing.stop(path="traces/failed_test_trace_authenticated.zip")
        context.close()


@pytest.fixture(scope="function")
def capture_screenshot_on_failure(request, page):
    yield
    item = request.node
    # Check if the test failed
    if hasattr(item, "rep_call") and item.rep_call.failed:
        try:
            # Create screenshot directory if it doesn't exist
            os.makedirs("screenshot", exist_ok=True)
            screenshot_data = page.screenshot(path="screenshot/fullpage.png")
            allure.attach(
                screenshot_data,
                name="failurescreenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print(f"Could not capture screenshot: {e}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


def pytest_sessionfinish(session, exitstatus):
    """Generate an Allure report without blocking the test run."""
    if hasattr(session.config, "workerinput"):
        return

    print("\n--- Test session completed. Generating Allure report... ---")

    results_dir = "allure-results"
    output_dir = os.path.join("reports", "allure-report")

    if os.path.exists(results_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
            subprocess.run(
                ["allure", "generate", results_dir, "-o", output_dir, "--clean"],
                shell=True,
                check=False,
                capture_output=True,
                text=True,
            )
            print(f"Allure report generated at {output_dir}")
        except Exception as e:
            print(f"Could not generate Allure report via CLI: {e}")


# END OF LINE
