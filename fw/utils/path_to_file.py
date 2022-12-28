

from selene.support.shared import browser
import os


def create_path(selector, file):
    currentDir = os.path.dirname(os.path.abspath(__file__))
    res_dir = os.path.join(currentDir, 'resourses')
    test_file = os.path.join(res_dir, file)
    browser.element(selector).send_keys(test_file)
