from selene import have
from selene.support.shared import browser


def checkHobby(selector, value):
    browser.all(selector).element_by(have.text(value)).click()