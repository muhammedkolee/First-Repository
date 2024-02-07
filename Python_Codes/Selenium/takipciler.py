from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def scrollDown():
    jsKomut = """
        sayfa = document.querySelector("._aano");
        sayfa.scrollTo(0, sayfa.scrollHeight);
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu;
    """
    sayfaSonu = driver.execute_script(jsKomut)
    while True:
        son = sayfaSonu
        time.sleep(1)
        sayfaSonu = driver.execute_script(jsKomut)
        if son == sayfaSonu:
            break

def followers():
    takipci = driver.get(f"http://instagram.com/{username}/followers")
    time.sleep(3)

    dialog = driver.find_element(by="css selector", value="div[role=dialog]")
    scrollDown()
    takipciler = dialog.find_elements(by="class name", value="x1dm5mii")

    for eleman in takipciler:
        link = eleman.find_element(by="css selector", value="a").get_attribute("href")
        file.write(link + "\n")

def login():
    driver.get("http://instagram.com")
    driver.maximize_window()
    time.sleep(1)

    kullanici = driver.find_element(by="xpath", value='//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    parola = driver.find_element(by="xpath", value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(password)
    giris = driver.find_element(by="xpath", value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button").click()
    time.sleep(5)
    followers()

file = open("takipciler.txt", "w+", encoding="UTF-8")

username = input("Instagram kullanıcı adınızı giriniz: ")
password = input("Instagram parolanızı giriniz: ")
driver = webdriver.Chrome()
login()

file.close()
time.sleep(3)