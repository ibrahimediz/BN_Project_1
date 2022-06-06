from PyQt5.QtWidgets  import QApplication, QMainWindow, QWidget
import sys
from PyQt5.uic import loadUi
from selenium import webdriver
import os 
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/ibrahimediz/Documents/GitHub/BN_Project_1/drivers/chromedriver")
import time

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('screens/main.ui', self)
        self.initUI()

    def initUI(self):
        self.btnGiris.clicked.connect(self.giris)
        self.show()
    
    def giris(self):
        self.tarayici = webdriver.Chrome(executable_path=DRIVER_BIN)
        self.tarayici.get("https://www.instagram.com")
        time.sleep(3)
        kullanicAdi = self.txtusername.text()
        sifre = self.txtpassword.text()
        self.tarayici.find_element_by_xpath("//input[@name='username']").send_keys(kullanicAdi)
        self.tarayici.find_element_by_xpath("//input[@name='password']").send_keys(sifre)
        self.tarayici.find_element_by_xpath("//button[@type='submit']").click()
        self.tarayici.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
        time.sleep(2)
        print("Giriş Yapıldı")
        # username
        # password


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
    