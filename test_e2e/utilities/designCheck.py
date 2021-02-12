import cv2


from test_e2e.POM.pages import FaqPage, SignInPage


class DesignCheck:
    # This will compare website design to saved version to see if its properly displayed (sensoric)

    def __init__(self, percent_as_succsess=90):
        self.min = percent_as_succsess

    FAQ_PAGE = {FaqPage, "location"}
    SIGN_IN_PAGE = {SignInPage, "login_page.png"}

    @staticmethod
    def verify(screen1 = "pic_50.png", screen2 = "login_page.png"):
        captured = cv2.imread(screen1)
        template = cv2.imread(screen2)
        difference = cv2.subtract(captured, template)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("images are completely Equal")
        else:
            print("images are NOT equal")
            cv2.imwrite("difference.png", difference)
        # verify result
        # output 1 : true / false
        # output 2 : percentage
        return True


