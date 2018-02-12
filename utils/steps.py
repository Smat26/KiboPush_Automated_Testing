from selenium import webdriver
import unicodecsv as csv
import platform
import time
from selenium.webdriver.common.keys import Keys
import os

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

if platform.system() == 'Darwin':
    driver = webdriver.Chrome('../driver/macos/chromedriver', chrome_options=chrome_options)
elif platform.system() == 'Linux':
    driver = webdriver.Chrome('../driver/linux/chromedriver', chrome_options=chrome_options)
elif platform.system() == 'Windows':
    driver = webdriver.Chrome('../driver/windows/chromedriver.exe', chrome_options=chrome_options)

WAIT_TIME = 1# number of seconds to wait after clicking something
# user='maria_rdhorxy_zerosub@tfbnw.net ', pw='cloudkibo123'

def wait(wait_time=WAIT_TIME):
    time.sleep(wait_time)

def open_kibopush():
    try:
        driver.get('https://staging.kibopush.com/')
        wait()
    except Exception, e:
        return "Error: " + str(e)
    return "Success"

# def login(user='mike_vrhkeqg_repeatuser@tfbnw.net', pw='kibo54321'):
#     try:
#         login_button = driver.find_element_by_class_name('btn-brand')
#         login_button.click()
#         time.sleep(WAIT_TIME)
#         if ('facebook' in str(driver.current_url)):
#             email = driver.find_element_by_id('email')
#             password = driver.find_element_by_id('pass')
#             login = driver.find_element_by_id('loginbutton')
#             email.send_keys(user)
#             password.send_keys(pw)
#             login.click()
#         wait()
#     except Exception, e:
#         return "Error: " + str(e)
#     return "Success"

def close_help_popup():
    try:
        driver.switch_to.frame(driver.find_element_by_xpath('.//iframe[@title="fb:customerchat Facebook Social Plugin"]'))
        close_button = driver.find_element_by_class_name('closeButtonContainer')
        close_button.click()
        wait()
        driver.switch_to.default_content()
    except Exception, e:
        return "Error: " + str(e)
    return "Success"

def login(account_type='agent'):
    try:
        team_account = account_type == 'agent' or account_type == 'admin' or account_type == 'buyer'

        pw = 'kibo54321'
        domain = 'fbteser'
        if account_type == 'buyer':
            user = 'a.hsan.tanweer.26@gmail.com'
        elif account_type == 'agent':
            user = 'ah.san.tanweer.26@gmail.com'
        elif account_type == 'admin':
            user = 'ahs.an.tanweer.26@gmail.com'
        elif account_type == 'individual':
            user = 'ahsa.n.tanweer.26@gmail.com'

        if team_account:
            click_on('team account')
        else:
            click_on('individual account')

        login_form = driver.find_element_by_class_name('m-login__wrapper')

        if team_account:
            domain_input = login_form.find_element_by_xpath('.//input[@type="text"]')
        password = login_form.find_element_by_xpath('.//input[@type="password"]')
        email = login_form.find_element_by_xpath('.//input[@type="email"]')

        login_button = login_form.find_element_by_id('m_login_signup_submit')
        
        if team_account:
            domain_input.send_keys(domain) 
        email.send_keys(user)
        password.send_keys(pw)
        login_button.click()
        wait(wait_time=5)
        if verify_failure() == "Success":
            return "Error Invalid Login"        
    except Exception, e:
        return "Error: " + str(e)
    return "Success"

def close_menu(x):
    try:
        exes = driver.find_elements_by_class_name('fa-times')
        num_of_menu_items = len(exes)
        exes[x-1].click()
        wait()
        exes = driver.find_elements_by_class_name('fa-times')
        if (len(exes) >= num_of_menu_items):
            return "Error: menu didn't delete"
    except Exception, e:
        return "Error: " + str(e)
    return "Success"


def add_menu(x):
    try:
        plus = driver.find_element_by_class_name('fa-plus')
        exes = driver.find_elements_by_class_name('fa-times')
        num_of_menu_items = len(exes)
        plus.click()
        wait()
        pluses = driver.find_elements_by_class_name('fa-plus')
        exes = driver.find_elements_by_class_name('fa-times')
        if (len(exes) <= num_of_menu_items):
            return "Error: menu didn't add"
    except Exception, e:
        return "Error: " + str(e)
    return "Success"

def send_broadcast_templates():
    try:
        templates = driver.find_element_by_class_name('m-widget4')
        template_buttons = templates.find_elements_by_class_name('m-btn')
        for i in range(len(template_buttons)):
            templates = driver.find_element_by_class_name('m-widget4')
            button = templates.find_elements_by_class_name('m-btn')[i]
            button.click()
            wait()
            click_on('send')
            if verify_alert() == "Success":
                click_on('back')
            else:
                return "Error: broadcast didn't send"
    except Exception, e:
        return "Error: " + str(e)
    return "Success"

def press_tab(times_to_press=1):
    try:
        for i in range(times_to_press):
            focused_element = driver.switch_to.active_element
            focused_element.send_keys(Keys.TAB)
            wait()
    except Exception, e:
        return "Error: " + str(e)
    return "Success"


# def test_survey_templates():
#     try:
#         templates = driver.find_element_by_class_name('m-widget4')
#         template_buttons = templates.find_elements_by_class_name('m-btn')
#         for i in range(len(template_buttons)):
#             templates = driver.find_element_by_class_name('m-widget4')
#             button = templates.find_elements_by_class_name('m-btn')[i]
#             button.click()
#             wait()
#             click_on('create survey')
#             wait()
#             if verify_alert() == "Success":
#                 click_on('back')
#             else:
#                 return "Error: broadcast didn't send"
#     except Exception, e:
#         return "Error: " + str(e)
#     return "Success"


def click_on(name, scope=driver):
    try:
        #print('click_on')
        name = name.lower().strip()
        links = scope.find_elements_by_xpath(".//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s')]" % (name))
        for element in links:
            if element.is_displayed():
                #driver.execute_script("arguments[0].click();", element)
                element.click()
                #print(element.text)
                wait()
                return "Success"
        
        buttons = scope.find_elements_by_xpath(".//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s')]" % (name))
        for element in buttons:
            if element.is_displayed():
                element.click()
                #print(element.text)
                wait()
                return "Success"

        inputs = scope.find_elements_by_xpath(".//input[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s') or contains(translate(@placeholder, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s') or contains(translate(@value, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s')]" % (name, name, name))
        for element in inputs:
            if element.is_displayed():
                element.click()
                #print(element.text)
                wait()
                return "Success"
        
        remaining_elements = scope.find_elements_by_xpath(".//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s') or contains(translate(@placeholder, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s') or contains(translate(@value, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s')]" % (name, name, name))
        for element in remaining_elements:
            if element.is_displayed():
                #driver.execute_script("arguments[0].click();", element)
                element.click()
                #print(element.text)
                wait()
                return "Success"
        if len(remaining_elements) == 0:
            wait()
            return "Error: no element with text '" + name +"' found"
    except Exception, e:
        wait()
        return "Error: " + str(e)
    return "Error: no element with text '" + name +"' found"

def clear_field():
    try:
        focused_element = driver.switch_to.active_element
        focused_element.clear()
        wait()
    except Exception, e:
        return "Error: " + str(e)
    return "Success"

def click_on_broadcast_title():
    try:
        title = driver.find_element_by_id('convoTitle')
        title.click()
    except Exception, e:
        return "Error: " + str(e)
    return "Success"

def press_enter():
    try:
        focused_element = driver.switch_to.active_element
        focused_element.send_keys(Keys.ENTER)
        wait()
    except Exception, e:
        return "Error: " + str(e)
    return "Success"

def logout():
    try:
        user_pic = driver.find_element_by_class_name('m-topbar__userpic')
        user_pic.click()
        wait()
        click_on('Logout')
        wait()
    except Exception, e:
        return "Error: " + str(e)
    return "Success"


def sidebar_hamburger():
    try:
        sidebar_hamburger = driver.find_element_by_id('m_aside_left_minimize_toggle')
        sidebar_hamburger.click()
        wait()
        collapsed = driver.find_element_by_class_name('m-brand__toggler--active')
    except Exception, e:
        return "Error: " + str(e)
    return "Success"
        

def sidebar_click(sidebar_item):
    #print('sidebar_click')
    sidebar = driver.find_element_by_class_name('m-menu__nav')
    return click_on(sidebar_item, scope=sidebar)

def write(text):
    try:
        focused_element = driver.switch_to.active_element
        focused_element.send_keys(text)
        wait()
    except Exception, e:
        return "Error: " + str(e)
    return "Success"

def choose_select(select_label, select_item=None):
    try:
        if select_item is not None:
            label = driver.find_element_by_xpath("//*[contains(text(), '%s')]" % select_label)
            label_parent = label.find_element_by_xpath("..")
            select = label_parent.find_element_by_tag_name('select')
            select.click()
            click_on(select_item, scope=select)
            wait()
    except Exception, e:
         return "Error: " + str(e)
    return "Success"

def broadcast_upload(type, component_number=None):
    try:
        if component_number == None:
            components = driver.find_elements_by_xpath('//div[@data-id]')
            component_number = len(components)
        component = driver.find_element_by_xpath('//div[@data-rank=%d]' % (component_number-1))
        return upload(type, scope=component)
    except Exception, e:
        return "Error: " + str(e)

def gallery_upload( page_number=None):
    try:
        if page_number == None:
            pages = driver.find_elements_by_xpath('//div[@data-index]')
            page_number = len(pages)
        page_number = int(page_number)
        component = driver.find_element_by_xpath('//div[@data-index=%d]' % (page_number-1))
        return upload('image', scope=component)
    except Exception, e:
        return "Error: " + str(e)

def upload(type, wait_time=10, scope=driver):
    try:
        attachment = scope.find_element_by_xpath('.//input[@type="file"]')
        if type == 'image':
            attachment.send_keys(os.getcwd()+"/sample.jpg")
        elif type == 'audio':
            attachment.send_keys(os.getcwd()+"/sample.mp3")
        elif type == 'video':
            attachment.send_keys(os.getcwd()+"/sample.mp4")
            wait(wait_time)
        elif type == 'file':
            attachment.send_keys(os.getcwd()+"/sample.pdf")
        wait(wait_time)
    except Exception, e:
         return "Error: " + str(e)

    return "Success"

def remove_broadcast_component(component_number=None):
    try:
        if component_number == None:
            components = driver.find_elements_by_xpath('//div[@data-id]')
            component_number = len(components)
        component = driver.find_element_by_xpath('//div[@data-rank=%d]' % (component_number-1))
        remove = component.find_element_by_class_name('fa-stack')
        remove.click()
        wait()
    except Exception, e:
         return "Error: " + str(e)
    return "Success"
    
def click_on_broadcast_component(text, component_number=None):
    try:
        if component_number == None:
            components = driver.find_elements_by_xpath('//div[@data-id]')
            component_number = len(components)
        component = driver.find_element_by_xpath('//div[@data-rank=%d]' % (component_number-1))
        return click_on(text, scope=component)
    except Exception, e:
        return "Error: " + str(e)



def add_broadcast_component(component_name):
    try:
        click_on(component_name)
        wait()
    except Exception, e:
         return "Error: " + str(e)
    return "Success"

def gallery_next():
    try:
        next = driver.find_element_by_class_name('slick-next')
        next.click()
        wait()
    except Exception, e:
         return "Error: " + str(e)
    return "Success"

def gallery_prev():
    try:
        prev = driver.find_element_by_class_name('slick-prev')
        prev.click()
        wait()
    except Exception, e:
         return "Error: " + str(e)
    return "Success"

def select_emoji():
    try:
        emoji_icon = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/div/div/div[2]/div[3]/div/div/div/div/div[5]/div[3]')
        emoji_icon.click()
        emojis = driver.find_elements_by_class_name('emoji-mart-emoji')
        emojis[0].click()
        click_on('type here')
        wait()
    except Exception, e:
         return "Error: " + str(e)
    return "Success"

def send_sticker():
    try:
        sticker_icon = driver.find_element_by_xpath('//*[@data-tip="stickers"]')
        sticker_icon.click()
        wait(wait_time=10)
        sticker_pack = driver.find_element_by_class_name('sticker-pack')
        stickers = sticker_pack.find_elements_by_class_name('sticker')
        src = stickers[0].get_attribute('src')
        sticker_ID = src[src.index('sticker/') + len('sticker/'):]
        sticker_ID = sticker_ID[:sticker_ID.index('_')]
        stickers[0].click()
        wait()
    except Exception, e:
         return "Error: " + str(e)
    if verify_sticker_sent(sticker_ID):
        return "Success"
    else:
        return "Error: sticker wasn't sent"

def remove_autoposting():
    try:
        autopost_delete = driver.find_element_by_class_name('btn-outline-danger')
        autopost_delete.click()
        click_on('delete')
        wait()
    except Exception, e:
        return "Error: " + str(e)
    return "Success"

def autopost_settings():
    try:
        autopost_settings = driver.find_element_by_class_name('btn-outline-brand')
        autopost_settings.click()
        wait()
    except Exception, e:
        return "Error: " + str(e)
    return "Success"

def verify_GIF_sent(gif_ID):
    try:
        messages = driver.find_elements_by_class_name('m-messenger__message-content')
        gif = messages[-1].find_element_by_tag_name('img')
        src = gif.get_attribute('src')
        actual_gif_ID = src[src.index('media/') + len('media/'):]
        actual_gif_ID = actual_gif_ID[:actual_gif_ID.index('/')]
        #print(gif_ID)
        #print(actual_gif_ID)
        return gif_ID == actual_gif_ID
    except Exception, e:
        #print(str(e))
        return False

def verify_sticker_sent(sticker_ID):
    try:
        messages = driver.find_elements_by_class_name('m-messenger__message-content')
        sticker = messages[-1].find_element_by_tag_name('img')
        src = sticker.get_attribute('src')
        actual_sticker_ID = src[src.index('sticker/') + len('sticker/'):]
        actual_sticker_ID = actual_sticker_ID[:actual_sticker_ID.index('_')]
        # print(sticker_ID)
        # print(actual_sticker_ID)
        return sticker_ID == actual_sticker_ID
    except Exception, e:
        #print(str(e))
        return False


def send_GIF():
    try:
        gif_icon = driver.find_element_by_xpath('//*[@data-tip="GIF"]')
        gif_icon.click()
        wait(wait_time=10)
        gifs = driver.find_elements_by_class_name('giphy-gif')
        src = gifs[0].get_attribute('src')
        gif_ID = src[src.index('media/') + len('media/'):]
        gif_ID = gif_ID[:gif_ID.index('/')]
        gifs[0].click()
        wait()
    except Exception, e:
         return "Error: " + str(e)
    if verify_GIF_sent(gif_ID):
        return "Success"
    else:
        return "Error: GIF wasn't sent"

def close_browser():
    driver.close()

def verify_table():
    try:
        table = driver.find_element_by_tag_name('table')
        entries = table.find_elements_by_class_name('m-datatable__row--even')
        if len(entries) > 0:
            return "Success"
        else:
            return "Error: No table entries"
    except Exception, e:
         return "Error: " + str(e)

def verify_alert():
    try:
        success_alert = driver.find_element_by_xpath('//*[@class="css-rr2n0f" or @class="toast-title" or @class="alert-success"]')
        if (success_alert.is_displayed()):
            #wait(7)
            return "Success"
        else:
            return "No Alert detected"
    except Exception, e:
        return "No Alert detected"

def verify_failure():
    try:
        failure_alert = driver.find_element_by_class_name('css-1f1jd2h')
        if (failure_alert.is_displayed()):
            return "Success"
        else:
            return "No Failure Alert"
    except Exception, e:
        return "No Failure Alert"


def download_phone_csv():
    try:
        csv = driver.find_element_by_xpath('//*[@class="fa-download"]')
        csv.click()
        wait(wait_time=10)
    except Exception, e:
         return "Error: " + str(e)
    return "Success"

def download_opdashboard_csv():
    try:
        csv = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[2]')
        csv.click()
        wait(wait_time=10)
    except Exception, e:
         return "Error: " + str(e)
    return "Success"

def send_thumbs_up():
    try:
        thumbs_up = driver.find_element_by_class_name('la-thumbs-o-up')
        thumbs_up.click()
        wait()
    except Exception, e:
         return "Error: " + str(e)
    return "Success"



if __name__ == "__main__":
    try:
        print(open_kibopush())
        print(login(domain='www.kibopush.com', user='mike_vrhkeqg_repeatuser@tfbnw.net', pw='kibo54321'))
        print(sidebar_click('polls'))
        print(click_on('send'))
        print(verify_alert())
        print(click_on('send'))
        print(verify_alert())
        #print(remove_autoposting())
        #print(select_emoji())
    finally:
        close_browser()

