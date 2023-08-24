import webbrowser
from config import load_config

config = load_config('.env')
homepage = config.browser.homePage
webbrowser.register('browser',
                    None,
                    webbrowser.BackgroundBrowser(
                        config.browser.browserPath))


def start_browser():
    webbrowser.get('browser').open_new_tab(homepage)


def open_youtube():
    webbrowser.get('browser').open_new_tab('youtube.com')
