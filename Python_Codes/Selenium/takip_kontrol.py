from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys # space, enter gibi tuşlara tıklamak için.
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
        time.sleep(2)
        sayfaSonu = driver.execute_script(jsKomut)
        if son == sayfaSonu:
            break
  

def login():
    driver.get("http://instagram.com")
    driver.maximize_window()
    time.sleep(1)

    kullanici = driver.find_element(by="xpath", value='//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    parola = driver.find_element(by="xpath", value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input').send_keys(password)
    giris = driver.find_element(by="xpath", value='//*[@id="loginForm"]/div[1]/div[3]/button').click()
    time.sleep(10)

def control():
    def following():
        driver.get(f"https://www.instagram.com/{username}")
        time.sleep(3)
        driver.find_element(by="xpath", value='//*[@id="mount_0_0_Dq"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a').click()
        time.sleep(3)
        
        dialog = driver.find_element(by="css selector", value="div[role=dialog]")
        scrollDown()
        takipciler = dialog.find_elements(by="class name", value="x1dm5mii")

        following1 = []
        for eleman in takipciler:
            link = eleman.find_element(by="css selector", value="span.x1lliihq")
            if link.text != "":
                following1.append(link.text)
            else:
                arr = eleman.find_element(by="css selector", value="a").get_attribute("href").split("/")
                following1.append(arr[3])
        return following1

    def followers():
        takipci = driver.get(f"http://instagram.com/{username}/followers")
        time.sleep(3)

        dialog = driver.find_element(by="css selector", value="div[role=dialog]")
        scrollDown()
        takipciler = dialog.find_elements(by="class name", value="x1dm5mii")

        followers1 = []
        for eleman in takipciler:
            link = eleman.find_element(by="css selector", value="span.x1lliihq")
            if link.text != "":
                followers1.append(link.text)
            else:
                arr = eleman.find_element(by="css selector", value="a").get_attribute("href").split("/")
                followers1.append(arr[3])
        return followers1

    following1 = following()
    followers1 = followers()

    for i in following1:
        if i in followers1:
            continue
        else:
            print(f"{i} kişisini takip etmenize rağmen o sizi takip etmiyor.")
            print("")
    
    for i in followers1:
        if i in following1:
            continue
        else:
            print(f"{i} kişisi sizi takip etmesine rağmen siz onu takip etmiyorsunuz.")
            print("")

username = input("Instagram kullanıcı adınızı giriniz: ")
password = input("Instagram parolanızı giriniz: ")
driver = webdriver.Chrome()

login()
control()