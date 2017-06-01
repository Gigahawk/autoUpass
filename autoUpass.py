from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import uPassMail
import urllib.request

username = 'yourCwlUsername'
password = 'yourCwlPassword'

attachments = []

school_select_page = 'school_select_page.png'
login_page = 'login_page.png'
checkbox_page = 'checkbox_page.png'
confirmation_page = 'confirmation_page.png'

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)

browser = webdriver.PhantomJS(desired_capabilities=dcap)
browser.set_window_size(1120,550)

browser.implicitly_wait(10)

def wait_for_internet():
    while not checkping():
        print("Error: No internet")
        time.sleep(1)
    print("Internet connection established")

def checkping():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib.error.URLError as err:
        return False

def checklen(array):
    if not len(array):
        print("Error: Element not found, checking internet...")
        wait_for_internet()
        runbrowser()
        quit()


def runbrowser():
    browser.get('https://upassbc.translink.ca/')

    school_dropdown = browser.find_elements_by_xpath("//*[@id=\"PsiId\"]")
    checklen(school_dropdown)

    school_select = Select(school_dropdown[0])
    school_select.select_by_value("ubc")

    browser.execute_script('document.body.style.background = "white"')
    browser.save_screenshot(school_select_page)
    school_select_image = open(school_select_page,'rb')
    attachments.append(school_select_image)

    school_submit = browser.find_elements_by_xpath("//*[@id=\"goButton\"]")
    checklen(school_submit)

    school_submit[0].click()

    username_input = browser.find_elements_by_xpath("//*[@id=\"j_username\"]")
    password_input = browser.find_elements_by_xpath("//*[@id=\"password\"]")
    login_submit = browser.find_elements_by_xpath("//*[@id=\"col2\"]/form/fieldset/input")
    checklen(username_input)
    checklen(password_input)
    checklen(login_submit)

    username_input[0].send_keys(username)
    password_input[0].send_keys(password)

    browser.save_screenshot(login_page)
    login_image = open(login_page,'rb')
    attachments.append(login_image)

    login_submit[0].click()

    checkbox = browser.find_elements_by_xpath("//*[@id=\"chk_0\"]")
    submit = browser.find_elements_by_xpath("//*[@id=\"requestButton\"]")
    # don't check checkbox in case uPass is not available or alreay processed
    # checklen(checkbox)
    checklen(submit)

    if(len(checkbox)):
        checkbox[0].click()

    top_of_screenshot = browser.find_elements_by_xpath("//*[@id=\"home-page\"]/div/div/div[2]/div[1]/div/div/h2")
    browser.execute_script("arguments[0].scrollIntoView();", top_of_screenshot[0])

    browser.execute_script('document.body.style.background = "white"')
    browser.save_screenshot(checkbox_page)
    checkbox_image = open(checkbox_page,'rb')
    attachments.append(checkbox_image)

    submit[0].click()

    time.sleep(10)

    browser.save_screenshot(confirmation_page)
    confirmation_image = open(checkbox_page,'rb')
    attachments.append(confirmation_image)


    uPassMail.sendEmail(server, 'Check screenshots to verify', attachments)

wait_for_internet()

server = uPassMail.initializeEmail()

runbrowser()
