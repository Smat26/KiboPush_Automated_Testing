'''
This modules covers the detailed implementation of the functions being used to carry out the test cases.

This modules provides an High level API to selenium way of interacting with the browser.
The functions are general enough to accomodate an array of usage (click_on("String")),
or sometimes designed for a specifc need, to cater a single purpose ( gallery_next() )

The purpose and usage of functions are defined.
'''

from selenium import webdriver
import unicodecsv as csv
import platform
import time
from selenium.webdriver.common.keys import Keys
import os
import config

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


if platform.system() == 'Darwin':
    driver = webdriver.Chrome('driver/macos/chromedriver', chrome_options=chrome_options)
elif platform.system() == 'Linux':
    driver = webdriver.Chrome('driver/linux/chromedriver', chrome_options=chrome_options)
elif platform.system() == 'Windows':
    driver = webdriver.Chrome('driver/windows/chromedriver.exe', chrome_options=chrome_options)

WAIT_TIME = 1# number of seconds to wait after clicking something
# user='maria_rdhorxy_zerosub@tfbnw.net ', pw='cloudkibo123'
driver.implicitly_wait(WAIT_TIME)

def open_new_window():
    """
    Opens a new chrome window
    """
    if platform.system() == 'Darwin':
        new_driver = webdriver.Chrome('driver/macos/chromedriver', chrome_options=chrome_options)
    elif platform.system() == 'Linux':
        new_driver = webdriver.Chrome('driver/linux/chromedriver', chrome_options=chrome_options)
    elif platform.system() == 'Windows':
        new_driver = webdriver.Chrome('driver/windows/chromedriver.exe', chrome_options=chrome_options)
    return new_driver

def wait(wait_time=WAIT_TIME):
    """
    Suspends execution for the given number of seconds
    Keyword arguments:
    wait_time -- number of seconds to wait (default 1.0)
    """
    # time.sleep(wait_time)
    pass

def open_kibopush():
    """
    Opens staging.kibopush.com
    """
    try:
        if config.platform == 'staging':
            driver.get('https://staging.kibopush.com/')
        elif config.platform == 'production':
            driver.get('https://app.kibopush.com/')
        wait()
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def open_facebook(account_type='buyer'):
    """
    Opens Facebook account for a given account type
    Keyword arguments:
    -----------------
    account_type (string): could be 'agent', 'admin', 'buyer' or 'individual' (default 'buyer')
    """
    try:
        facebook_driver = open_new_window()
        facebook_driver.get("https://www.facebook.com/")
       
        email = facebook_driver.find_element_by_id('email')
        password = facebook_driver.find_element_by_id('pass')
        login = facebook_driver.find_element_by_id('loginbutton')

        user_email = config.facebook_accounts[account_type]['facebook_email']
        user_password = config.facebook_accounts[account_type]['password']
        email.send_keys(user_email)
        password.send_keys(user_password)
        login.click()
        wait()
    except Exception as e:
        return "Error: " + str(e)
    return "Success"


def delete_poll_templates():
    """
    Deletes all poll templates from templates page
    """
    try:
        poll_templates = driver.find_element_by_class_name('poll-templates')
        template_rows = poll_templates.find_elements_by_class_name('m-datatable__row--even')
        for row in template_rows:
            click_on('delete', scope=row)
            popup = driver.find_element_by_class_name('narcissus_17w311v')
            click_on('delete', scope=popup)
            if verify_alert() != "Success":
                return "Error: no delete alert"
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def delete_survey_templates():
    """
    Deletes all survey templates from templates page
    """
    try:
        survey_templates = driver.find_element_by_class_name('survey-templates')
        template_rows = poll_templates.find_elements_by_class_name('m-datatable__row--even')
        for row in template_rows:
            click_on('delete', scope=row)
            popup = driver.find_element_by_class_name('narcissus_17w311v')
            click_on('delete', scope=popup)
            if verify_alert() != "Success":
                return "Error: no delete alert"
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def delete_broadcast_templates():
    """
    Deletes all broadcast templates from templates page
    """
    try:
        broadcast_templates = driver.find_element_by_class_name('broadcast-templates')
        template_rows = poll_templates.find_elements_by_class_name('m-datatable__row--even')
        for row in template_rows:
            click_on('delete', scope=row)
            popup = driver.find_element_by_class_name('narcissus_17w311v')
            click_on('delete', scope=popup)
            if verify_alert() != "Success":
                return "Error: no delete alert"
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def verify_poll_templates_table():
    """
    Verifies whether there are entries in poll templates (in templates page)
    """
    try:
        poll_templates = driver.find_element_by_class_name('poll-templates')
        return verify_table(scope=poll_templates)
    except Exception as e:
        return "Error: " + str(e)

def verify_survey_templates_table():
    """
    Verifies whether there are entries in survey templates (in templates page)
    """
    try:
        survey_templates = driver.find_element_by_class_name('survey-templates')
        return verify_table(scope=survey_templates)
    except Exception as e:
        return "Error: " + str(e)

def verify_broadcast_templates_table():
    """
    Verifies whether there are entries in broadcast templates (in templates page)
    """
    try:
        broadcast_templates = driver.find_element_by_class_name('broadcast-templates')
        return verify_table(scope=broadcast_templates)
    except Exception as e:
        return "Error: " + str(e)

def close_help_popup():
    """
    Closes messenger help popup
    """
    try:
        driver.switch_to.frame(driver.find_element_by_xpath('//iframe[contains(@src, "https://www.facebook.com/v2.12/plugins/customerchat")]'))
        close_button = driver.find_element_by_class_name('closeButtonContainer')
        close_button.click()
        wait()
        driver.switch_to.default_content()
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def screenshot(filename):
    """
    Screenshots the webpage
    Parameters:
    ----------
    filename (string) : name which to save the screenshot file.
    """
    try:
        driver.save_screenshot('Screenshots/'+filename+'.png')
    except:
        return "Error: " + str(e)
    return "Screenshot succesfully saved"

def login(account_type='buyer'):
    """
    Logs in a user of a particular account type (from initial login screen of KiboPush)
    Keyword arguments:
    account_type (string) : could be 'agent', 'admin', 'buyer' or 'individual' (default 'buyer')
    """
    try:
        click_on('login')
        team_account = account_type == 'agent' or account_type == 'admin' or account_type == 'buyer'

        user_email = config.facebook_accounts[account_type]['login_email']
        user_password = config.facebook_accounts[account_type]['password']


        if team_account:
            user_domain = config.facebook_accounts[account_type]['domain']
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
            domain_input.send_keys(user_domain) 
        email.send_keys(user_email)
        password.send_keys(user_password)
        login_button.click()
        wait(wait_time=5)
        if verify_failure() == "Success":
            return "Error Invalid Login"        
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def close_menu(x):
    """
    Closes the xth menu (from top to down including submenus and nested menus) (from persistent menu page)
    Parameters:
    ----------
    x (string) : number of the menu from top to bottom (starting from 1)
    """
    try:
        x = int(x)
        exes = driver.find_elements_by_class_name('fa-times')
        num_of_menu_items = len(exes)
        exes[x-1].click()
        wait()
        exes = driver.find_elements_by_class_name('fa-times')
        if (len(exes) >= num_of_menu_items):
            return "Error: menu didn't delete"
    except Exception as e:
        return "Error: " + str(e)
    return "Success"


def add_menu():
    """
    Adds a menu item (from persistent menu page)
    """
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
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def send_broadcast_templates():
    """
    Sends all broadcast templates
    """
    try:
        templates = driver.find_element_by_class_name('m-widget4')
        template_buttons = templates.find_elements_by_class_name('m-btn')
        for i in range(len(template_buttons)):
            templates = driver.find_element_by_class_name('m-widget4')
            button = templates.find_elements_by_class_name('m-btn')[i]
            button.click()
            wait()
            click_on('next')
            click_on('send')
            if verify_alert() == "Success":
                driver.execute_script("window.history.go(-1)")
                wait()
            else:
                return "Error: broadcast didn't send"
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def press_tab(times_to_press="1"):
    """
    Presses tab the specified number of times
    Keyword Arguments:
    -----------------
    times_to_press (string): number of times to press tab (default '1')
    """
    try:
        for i in range(int(times_to_press)):
            focused_element = driver.switch_to.active_element
            focused_element.send_keys(Keys.TAB)
            wait()
    except Exception as e:
        return "Error: " + str(e)
    return "Success"



def click_on(name, scope=driver):
    """
    Clicks on the element with specified text.
    Preference is in the following order: anchor links, buttons, input placeholders, and then remaining element from the top of the page
    Parameters:
    ----------
    name (string) : the text of what to click on

    Keyword Arguments
    -----------------
    scope (WebElement): which element to search inside (default driver which is the entire page)
    """
    try:
        #print('click_on')
        name = name.lower().strip()
        links = scope.find_elements_by_xpath(".//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s')]" % (name))
        for element in links:
            if element.is_displayed():
                try:
                    element.click()
                except:
                    driver.execute_script("arguments[0].click();", element)
                #element.click()
                #print(element.text)
                wait()
                #print("Link")
                return "Success"
        
        buttons = scope.find_elements_by_xpath(".//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s')]" % (name))
        for element in buttons:
            if element.is_displayed():
                try:
                    element.click()
                except:
                    driver.execute_script("arguments[0].click();", element)
                #element.click()
                #print(element.text)
                wait()
                #print("Button")
                return "Success"

        inputs = scope.find_elements_by_xpath(".//input[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s') or contains(translate(@placeholder, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s') or contains(translate(@value, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s')]" % (name, name, name))
        for element in inputs:
            if element.is_displayed():
                try:
                    element.click()
                except:
                    driver.execute_script("arguments[0].click();", element)
                #element.click()
                #print(element.text)
                wait()
                #print("Input")
                return "Success"
        
        remaining_elements = scope.find_elements_by_xpath(".//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s') or contains(translate(@placeholder, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s') or contains(translate(@value, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s')]" % (name, name, name))
        for element in remaining_elements:
            if element.is_displayed():
                try:
                    element.click()
                except:
                    driver.execute_script("arguments[0].click();", element)
                #element.click()
                #print(element.text)
                wait()
                #print("Remaining")
                return "Success"
        if len(remaining_elements) == 0:
            wait()
            return "Error: no element with text '" + name +"' found"
    except Exception as e:
        wait()
        return "Error: " + str(e)
    return "Error: no element with text '" + name +"' found"

def clear_field():
    """
    Clears the content from the currently focused input field
    """
    try:
        focused_element = driver.switch_to.active_element
        focused_element.clear()
        wait()
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def click_on_broadcast_title():
    """
    Clicks on the edit broadcast title icon
    """
    try:
        title = driver.find_element_by_id('convoTitle')
        title.click()
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def press_enter():
    """
    Presses enter on the currently focused element
    """
    try:
        focused_element = driver.switch_to.active_element
        focused_element.send_keys(Keys.ENTER)
        wait()
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def logout():
    """
    Logs out the currently logged in user
    """
    try:
        user_pic = driver.find_element_by_class_name('m-topbar__userpic')
        user_pic.click()
        wait()
        click_on('Logout')
        wait()
    except Exception as e:
        return "Error: " + str(e)
    return "Success"


def sidebar_hamburger():
    """
    Clicks on the collapse/expand icon at the top of the sidebar
    """
    try:
        collapsed = driver.find_element_by_class_name('m-aside-left--minimize')
        collapsed = True
    except Exception as e:
        collapsed = False

    try:
        sidebar_hamburger = driver.find_element_by_id('m_aside_left_minimize_toggle')
        sidebar_hamburger.click()
        wait()
        if collapsed:
            try:
                driver.find_element_by_class_name('m-aside-left--minimize')
            except Exception as e:
                return "Success"
        else:
            driver.find_element_by_class_name('m-aside-left--minimize')
            return "Success"    
    except Exception as e:
        return "Error: " + str(e)
    return "Success"
        

def sidebar_click(sidebar_item):
    """
    Clicks on an element with a certain text in the sidebar

    Parameters
    ----------
    sidebar_item (string) : the text of the element to click on
    """
    #print('sidebar_click')
    sidebar = driver.find_element_by_class_name('m-menu__nav')
    return click_on(sidebar_item, scope=sidebar)

def write(text):
    """
    writes text on the currently selected element

    Parameters
    ----------
    text (string): the text to write
    """
    try:
        focused_element = driver.switch_to.active_element
        focused_element.send_keys(text)
        wait()
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def choose_select(select_label, select_item=None):
    """
    Clicks on the select element with a certain label and selects a certain option from the select dropdown

    Parameters:
    ----------
    select_label (string): the label associated with the select element

    Keyword Arguments:
    -----------------
    select_item (string): the option inside the select dropdown (default will select first item)
    """
    try:
        if select_item is not None:
            label = driver.find_element_by_xpath("//*[contains(text(), '%s')]" % select_label)
            label_parent = label.find_element_by_xpath("..")
            select = label_parent.find_element_by_tag_name('select')
            select.click()
            click_on(select_item, scope=select)
            wait()
    except Exception as e:
         return "Error: " + str(e)
    return "Success"

def broadcast_upload(type, component_number=None):
    """
    Uploads a file to particular broadcast component (in broadcast creation)

    Keyword Arguments:
    -----------------
    component_number (string): the component number (from top to bottom starting from 1)
    """
    try:
        broadcast_components = driver.find_elements_by_class_name('broadcast-component')
        if component_number == None:
            component_number = len(broadcast_components)-1
        else:
            component_number = int(component_number)-1
        component = broadcast_components[component_number]
        while not component.is_displayed() and component_number >= 0:
            component_number -= 1
            component = broadcast_components[component_number]
        return upload(type, scope=component)
    except Exception as e:
        return "Error: " + str(e)

def gallery_upload(page_number=None):
    """
    Uploads a file to a particular page in a gallery component (in broadcast creation)

    Keyword Arguments:
    -----------------
    page_number (string) : the page number which to upload a file
    """
    try:
        if page_number == None:
            pages = driver.find_elements_by_xpath('//div[@data-index]')
            page_number = len(pages)
        else:
            page_number = int(page_number)
        page_number = int(page_number)
        component = driver.find_element_by_xpath('//div[@data-index=%d]' % (page_number-1))
        return upload('image', scope=component)
    except Exception as e:
        return "Error: " + str(e)

def upload(type, wait_time=10, scope=driver):
    """
    Uploads a file to the first file input component on the page

    Parameters:
    ----------
    type (string) : can be 'image', 'audio', 'video', 'file'

    Keyword Arguments:
    -----------------
    wait_time (int): number of seconds to wait after hitting upload (default 10 seconds)
    scope (WebElement): which element to search inside (default driver which is the entire page)
    """
    try:
        attachment = scope.find_element_by_xpath('.//input[@type="file"]')
        if type == 'image':
            attachment.send_keys(os.getcwd()+"/Uploads/sample.jpg")
        elif type == 'audio':
            attachment.send_keys(os.getcwd()+"/Uploads/sample.mp3")
        elif type == 'video':
            attachment.send_keys(os.getcwd()+"/Uploads/sample.mp4")
            wait(wait_time)
        elif type == 'file':
            attachment.send_keys(os.getcwd()+"/Uploads/sample.pdf")
        wait(wait_time)
    except Exception as e:
         return "Error: " + str(e)

    return "Success"

def remove_broadcast_component(component_number=None):
    """
    Removes a particular broadcast component
     Keyword Arguments:
    -----------------
    component_number (string): the component number (from top to bottom starting from 1)
    """
    try:
        if component_number == None:
            broadcast_components = driver.find_elements_by_class_name('broadcast-component')
            component_number = len(broadcast_components)-1
        else:
            component_number = int(component_number)-1
        component = broadcast_components[component_number]
        remove = component.find_element_by_class_name('fa-stack')
        remove.click()
        wait()
    except Exception as e:
         return "Error: " + str(e)
    return "Success"
    
def click_on_broadcast_component(text, component_number=None):
    """
    Clicks on the text of a particular broadcast component

    Parameters:
    ----------
    text: the text of which to click on

    Keyword Arguments:
    -----------------
    component_number (string): the component number (from top to bottom starting from 1)
    """
    try:
        broadcast_components = driver.find_elements_by_class_name('broadcast-component')
        if component_number == None:
            component_number = len(broadcast_components)-1
        else:
            component_number = int(component_number)-1
        component = broadcast_components[component_number]
        while not component.is_displayed() and component_number >= 0:
            component_number -= 1
            component = broadcast_components[component_number]
        return click_on(text, scope=component)
        
    except Exception as e:
        return "Error: " + str(e)



def add_broadcast_component(component_name):
    """
    add broadcast component of a particular type

    Parameters:
    ----------
    component_name (string): the content type to add (e.g text, image, card, etc.)
    """
    try:
        click_on(component_name)
        wait()
    except Exception as e:
         return "Error: " + str(e)
    return "Success"

def gallery_next():
    """
    Goes to the next page of the gallery component
    """
    try:
        next = driver.find_element_by_class_name('slick-next')
        next.click()
        wait()
    except Exception as e:
         return "Error: " + str(e)
    return "Success"

def gallery_prev():
    """
    Goes to the previous page of the gallery component
    """
    try:
        prev = driver.find_element_by_class_name('slick-prev')
        prev.click()
        wait()
    except Exception as e:
         return "Error: " + str(e)
    return "Success"

def select_emoji():
    """Selects an emoji and puts it in the input box (Live Chat)"""
    Selects
    try:
        emoji_icon = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/div/div/div[2]/div[3]/div/div/div/div/div[5]/div[3]')
        emoji_icon.click()
        emojis = driver.find_elements_by_class_name('emoji-mart-emoji')
        emojis[0].click()
        click_on('type here')
        wait()
    except Exception as e:
         return "Error: " + str(e)
    return "Success"

def send_sticker():
    """Sends the first sticker in the sticker menu""" 
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
    except Exception as e:
         return "Error: " + str(e)
    if verify_sticker_sent(sticker_ID):
        return "Success"
    else:
        return "Error: sticker wasn't sent"

def remove_autoposting():
    """Removes the first autoposting channel"""
    try:
        autopost_delete = driver.find_element_by_class_name('btn-outline-danger')
        autopost_delete.click()
        click_on('delete')
        wait()
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def autopost_settings():
    """Clicks on the edit settings of the first autoposting channel"""
    try:
        autopost_settings = driver.find_element_by_class_name('btn-outline-brand')
        autopost_settings.click()
        wait()
    except Exception as e:
        return "Error: " + str(e)
    return "Success"

def verify_GIF_sent(gif_ID):
    """
    Verifies whether the GIF was sent

    Parameters:
    ----------
    gid_ID: the id of the GIF
    """
    try:
        messages = driver.find_elements_by_class_name('m-messenger__message-content')
        gif = messages[-1].find_element_by_tag_name('img')
        src = gif.get_attribute('src')
        actual_gif_ID = src[src.index('media/') + len('media/'):]
        actual_gif_ID = actual_gif_ID[:actual_gif_ID.index('/')]
        #print(gif_ID)
        #print(actual_gif_ID)
        return gif_ID == actual_gif_ID
    except Exception as e:
        #print(str(e))
        return False

def verify_sticker_sent(sticker_ID):
    """
    Verifies whether the sticker was sent

    Parameters:
    ----------
    gid_ID: the id of the sticker
    """
    try:
        messages = driver.find_elements_by_class_name('m-messenger__message-content')
        sticker = messages[-1].find_element_by_tag_name('img')
        src = sticker.get_attribute('src')
        actual_sticker_ID = src[src.index('sticker/') + len('sticker/'):]
        actual_sticker_ID = actual_sticker_ID[:actual_sticker_ID.index('_')]
        # print(sticker_ID)
        # print(actual_sticker_ID)
        return sticker_ID == actual_sticker_ID
    except Exception as e:
        #print(str(e))
        return False


def send_GIF():
    """
    Sends a GIF (Live Chat)
    """
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
    except Exception as e:
         return "Error: " + str(e)
    if verify_GIF_sent(gif_ID):
        return "Success"
    else:
        return "Error: GIF wasn't sent"

def close_browser():
    """
    Closes the currently running browser
    """
    driver.close()

def verify_table(scope=driver):
    """
    Verifies if the table element has entries

    Keyword Arguments:
    -----------------
    scope (WebElement): which element to search inside (default driver which is the entire page)
    """
    try:
        table = scope.find_element_by_tag_name('table')
        entries = table.find_elements_by_class_name('m-datatable__row--even')
        if len(entries) > 0:
            return "Success"
        else:
            return "Error: No table entries"
    except Exception as e:
         return "Error: " + str(e)

def num_of_broadcast_components():
    """
    Returns the number of broadcast components currently being used
    """
    try:
        broadcast_components = driver.find_elements_by_class_name('broadcast-component')
        return len(broadcast_components)
    except Exception as e:
        return "No Broadcast components"

def verify_alert():
    """
    Checks if a successful alert is being shown
    """
    try:
        success_alert = driver.find_element_by_xpath('//*[@class="css-rr2n0f" or @class="toast-title" or @class="alert-success"]')
        if (success_alert.is_displayed()):
            #wait(7)
            return "Success"
        else:
            return "No Alert detected"
    except Exception as e:
        return "No Alert detected"

def verify_failure():
    """
    Checks if a failure alert is being shown
    """
    try:
        failure_alert = driver.find_element_by_class_name('css-1f1jd2h')
        if (failure_alert.is_displayed()):
            return "Success"
        else:
            return "No Failure Alert"
    except Exception as e:
        return "No Failure Alert"


def download_phone_csv():
    """
    Downloads csv of phone numbers (in Invite using Phone Numebers)
    """
    try:
        csv = driver.find_element_by_xpath('//*[@class="fa-download"]')
        csv.click()
        wait(wait_time=10)
    except Exception as e:
         return "Error: " + str(e)
    return "Success"

def download_opdashboard_csv():
    """
    Downloads csv of users (in Operational Dashboard)
    """
    try:
        csv = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[2]')
        csv.click()
        wait(wait_time=10)
    except Exception as e:
         return "Error: " + str(e)
    return "Success"

def send_thumbs_up():
    """
    Sends a thumbs up in Live Chat
    """
    try:
        thumbs_up = driver.find_element_by_class_name('la-thumbs-o-up')
        thumbs_up.click()
        wait()
    except Exception as e:
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


