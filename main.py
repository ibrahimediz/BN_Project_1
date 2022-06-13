from PyQt5.QtWidgets  import QApplication, QMainWindow, QWidget # Import the PyQt5 modules we'll need
import sys # We need sys so that we can pass argv to QApplication
from PyQt5.uic import loadUi # ui load module from PyQt5.uic
from seleniumbotcore import InstaBotCore

class App(QMainWindow): # Our main window class
    def __init__(self): # Constructor
        super().__init__() # QMainWindow initialization
        loadUi('screens/main.ui', self) # designer ui file loading
        self.botcore = InstaBotCore(username="",password="")
        self.initUI() 

    def initUI(self): 
        self.btnGiris.clicked.connect(self.giris) # button clicked event
        self.btnTakipEt.clicked.connect(self.takipEt) # button clicked event
        self.show() # show mainwindow
    
    def giris(self):
        self.botcore.login(username=self.txtusername.text(),password=self.txtpassword.text())
        # self.lblGiris.setText("Giris yapildi")
   
    def takipEt(self):
        kullaniciAdi = self.txtProfil.text()
        self.botcore.follow(kullanici=kullaniciAdi)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)# A new QApplication
    window = App() # create a new Window
    sys.exit(app.exec_()) # execute the app and wait for it to close before exiting.
    