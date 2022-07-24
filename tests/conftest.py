import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", action="store", default="chrome", help="Invocation the browser"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("--browser-name")
    if browser == "chrome":
        s = Service(executable_path="c:\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)

    elif browser == "firefox":
        s = Service(executable_path="c:\\geckodriver.exe")
        driver = webdriver.Firefox(service=s)
    elif browser == "ie":
        s = Service(executable_path="c:\\IEDriverServer.exe")
        driver = webdriver.ie(service=s)
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver  # Up to here precondition
    yield
    driver.quit()  # post condition


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
