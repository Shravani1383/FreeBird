import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import*
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        #navbar
        navbar =QToolBar()
        self.addToolBar(navbar)
        #back button
        #back_btn=   QAction('Back',self)
        back_btn = QAction(QIcon("back-arrow.svg"), "Back", self)
        back_btn.triggered.connect(self.browser.back)
      
        navbar.addAction(back_btn)
        #forward Button
        #next_btn=QAction('Next',self)
        next_btn = QAction(QIcon("forward-arrow.png"), "Next", self)
        next_btn.triggered.connect(self.browser.forward)
        navbar.addAction(next_btn)
        #refresh
        #refresh_btn=QAction('Refresh',self)
        refresh_btn = QAction(QIcon("refresh-icon.png"), "Reload", self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction (refresh_btn)
        #home
        home_btn=QAction(QIcon("home.png"), "home", self)
        home_btn.triggered.connect(self.navigate_home)  #navigate home is user defined
        navbar.addAction(home_btn)
        #url
        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)    #navigate to url is user defined
        navbar.addWidget(self.url_bar)
        
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))      #url for home page
     
    def navigate_to_url(self):
               
        url=self.url_bar.text()                         #updates url when back , forward is released
        self.browser.setUrl(QUrl(url))
        self.browser.urlChanged.connect(self.update_url)
        
    def update_url(self,url):
        self.url_bar.setText(url.toString())
app=QApplication(sys.argv)
QApplication.setApplicationName('FreeBird')
window = MainWindow()
app.exec_()
