from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Login(link, user, password):
   
    web = webdriver.Chrome()
    
   
    web.get(link)
    
 
    user_fields = ["user", "username", "name", "email", "gmail", "mail"]
    
  
    password_fields = ["password", "pass", "pwd"]
    
   
    button_texts = ["Login", "Submit", "Signup", "Start","Get Started"]
    button_attributes = ['type="submit"', 'id="submit"','class="submit"']

  
    username_input = None
    for field in user_fields:
        try:
            username_input = web.find_element(By.NAME, field)
            break
        except:
            try:
                username_input = web.find_element(By.ID, field)
                break
            except:
                try:
                    username_input = web.find_element(By.CLASS_NAME, field)
                    break
                except:
                    pass
    if username_input:
        username_input.send_keys(user)
  
    password_input = None
    for field in password_fields:
        try:
            password_input = web.find_element(By.NAME, field)
            break
        except:
            try:
                password_input = web.find_element(By.ID, field)
                break
            except:
                try:
                    password_input = web.find_element(By.CLASS_NAME, field)
                    break
                except:
                    pass
    if password_input:
        password_input.send_keys(password)
 
    submit_button = None
    for text in button_texts:
        try:
            submit_button = web.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
            break
        except:
            pass
    
    if not submit_button:
        for attribute in button_attributes:
            try:
                submit_button = web.find_element(By.XPATH, f"//*[@{attribute}]")
                break
            except:
                pass
    
    if submit_button:
        submit_button.click()
    else:
        print("Submit button not found.")

Login('https://example.com/login', 'your_username', 'your_password')
