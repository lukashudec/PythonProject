import time


class Growler:

    def __init__(self, driver):
        self.driver = driver

    def inject_js_libraries(self):
        simple_notify_js = 'https://drewdulz.github.io/simpleNotify-js/inc/simpleNotify.js'
        simple_notify_css = 'https://drewdulz.github.io/simpleNotify-js/inc/simpleNotifyStyle.css'
        # inject simpleNotify javascript
        self.driver.execute_script("var element = document.createElement('script'); "
                                   "element.src = '" + simple_notify_js + "';" +
                                   "document.getElementsByTagName('head')[0].appendChild(element);")
        time.sleep(1)
        # inject simpleNotify css
        self.driver.execute_script("var element = document.createElement('link'); "
                                   "element.rel = 'stylesheet';" +
                                   "element.href = '" + simple_notify_css + "';" +
                                   "document.getElementsByTagName('head')[0].appendChild(element);")

    def growl(self, message, level):
        """
        :param message: message that will be displayed
        :param level: color of notification, attention / danger / warning / good
        :return: nothing
        known issue > notification can be rendered behind another element so it will be invisible / partly invisible
        """
        self.inject_js_libraries()
        self.driver.execute_script("simpleNotify.notify({ message:'" + message + "', level: '" + level + "'});")
