from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from utils.config import BROWSER, BROWSER_ZOOM, CHROMEDRIVER_PATH, EDGEDRIVER_PATH, EDGE_BINARY_PATH, HEADLESS


class Browser:
    def __init__(self):
        if BROWSER == 'edge':
            self.driver = self._build_edge_driver()
        else:
            self.driver = self._build_chrome_driver()

        self._set_zoom(BROWSER_ZOOM)

    def _build_chrome_driver(self):
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-gpu')
        if HEADLESS:
            options.add_argument('--headless=new')
            options.add_argument('--window-size=1920,1080')

        if CHROMEDRIVER_PATH:
            service = ChromeService(CHROMEDRIVER_PATH)
            return webdriver.Chrome(service=service, options=options)

        # Selenium Manager resolves a compatible driver automatically.
        return webdriver.Chrome(options=options)

    def _build_edge_driver(self):
        options = EdgeOptions()
        if EDGE_BINARY_PATH:
            options.binary_location = EDGE_BINARY_PATH
        options.add_argument('--start-maximized')
        options.add_argument('--disable-gpu')
        if HEADLESS:
            options.add_argument('--headless=new')
            options.add_argument('--window-size=1920,1080')

        if EDGEDRIVER_PATH:
            service = EdgeService(EDGEDRIVER_PATH)
            return webdriver.Edge(service=service, options=options)

        # Selenium Manager resolves a compatible driver automatically.
        try:
            return webdriver.Edge(options=options)
        except Exception as edge_error:
            try:
                from webdriver_manager.microsoft import EdgeChromiumDriverManager

                service = EdgeService(EdgeChromiumDriverManager().install())
                return webdriver.Edge(service=service, options=options)
            except Exception as manager_error:
                raise RuntimeError(
                    'Falha ao iniciar Edge WebDriver. Configure EDGEDRIVER_PATH ou EDGE_BINARY_PATH e tente novamente.'
                ) from manager_error

    def _set_zoom(self, zoom_factor):
        if zoom_factor <= 0:
            return
        try:
            self.driver.execute_cdp_cmd('Emulation.setPageScaleFactor', {'pageScaleFactor': zoom_factor})
        except Exception:
            # Ignore zoom failures so tests can continue normally.
            pass

    def new_page(self):
        return self.driver

    def save_screenshot(self, path):
        self.driver.save_screenshot(path)

    def quit(self):
        self.driver.quit()
