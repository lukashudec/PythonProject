from test_e2e.POM.pages import FaqPage


class DesignCheck:
    ''':cvar
    This will compare website design to saved version to see if its properly displayed (sensoric)
    '''

    def __init__(self, percent_as_succsess = 90):
        self.min = percent_as_succsess

    FAQ_PAGE = {FaqPage, "location"}

    def verify(self, screenshot):
        # take screenshot
        # load file
        # verify result
        # output 1 : true / false
        # output 2 : percentage
        return True

