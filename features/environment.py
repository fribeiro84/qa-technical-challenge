import os
import time
from utils.browser import Browser
from pages.funcionario_page import FuncionarioPage
from utils.config import SCREENSHOTS_DIR
from utils.logger import configurar_logger


LOGGER_NAME = 'behave_environment'
logger = configurar_logger(LOGGER_NAME, os.path.join(SCREENSHOTS_DIR, 'behave.log'))


def before_all(context):
    context.browser = Browser()
    context.page = context.browser.new_page()
    context.funcionario_page = FuncionarioPage(context.page)
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


def after_step(context, step):
    if step.status == 'failed' and hasattr(context, 'browser'):
        filename = f"{step.name.replace(' ', '_').replace('/', '_')}_{int(time.time())}.png"
        destination = os.path.join(SCREENSHOTS_DIR, filename)
        context.browser.save_screenshot(destination)
        logger.info('Screenshot salva em: %s', destination)


def after_all(context):
    if hasattr(context, 'browser'):
        context.browser.quit()
