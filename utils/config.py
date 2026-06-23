import os

BASE_URL = os.getenv('BASE_URL', 'http://analista-teste.seatecnologia.com.br/')
SCREENSHOTS_DIR = os.getenv('SCREENSHOTS_DIR', os.path.join(os.path.dirname(os.path.dirname(__file__)), 'evidencias'))
WARNING_LOG_FILE = os.getenv('WARNING_LOG_FILE', os.path.join(os.path.dirname(os.path.dirname(__file__)), 'evidencias', 'warnings.log'))
HEADLESS = os.getenv('HEADLESS', 'false').lower() in ('1', 'true', 'yes')
BROWSER = os.getenv('BROWSER', 'chrome').strip().lower()
CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')
EDGEDRIVER_PATH = os.getenv('EDGEDRIVER_PATH')

_DEFAULT_EDGE_PATHS = [
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
]
_detected_edge_path = next((path for path in _DEFAULT_EDGE_PATHS if os.path.exists(path)), '')
EDGE_BINARY_PATH = os.getenv('EDGE_BINARY_PATH', _detected_edge_path)

try:
    BROWSER_ZOOM = float(os.getenv('BROWSER_ZOOM', '1.0'))
except ValueError:
    BROWSER_ZOOM = 1.0
