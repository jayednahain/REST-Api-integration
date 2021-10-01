from selenium import webdriver
import time
import requests
import json



option = webdriver.ChromeOptions()
option.add_argument(r'--user-data-dir=C:\Users\Jayed Nahian\AppData\Local\Google\Chrome\User Data\Default')
option.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='WebDriver/chromedriver.exe',options=option)
whats_app_path = 'https://web.whatsapp.com/'
driver.get(whats_app_path)



"""whatsapp functions"""

lock = 5

data = int(input("unlock !: "))


if data==lock:
    name = input("enter name: ")

    api_request = requests.get("http://127.0.0.1:8000/contact_list/"+name+"")
    raw_json_data = json.loads(api_request.content)
    user_number = raw_json_data.get('numbers')
    search_box = driver.find_element_by_css_selector("._13NKt ")
    search_box.send_keys(user_number)
    time.sleep(5)
    print(user_number)