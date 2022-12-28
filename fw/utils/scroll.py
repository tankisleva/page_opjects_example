from selene.support.shared import browser
from selene import command


def scroll_to(selector):
    browser.element(selector).perform(command.js.scroll_into_view)