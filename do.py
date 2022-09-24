#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
import sys

# from PySide2.QtWebEngineWidgets import QWebEngineView

from PySide2 import QtCore
from PySide2.QtCore import QSettings
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, \
     QVBoxLayout, QStatusBar, QProgressBar, QToolBar, QTabWidget
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

# --ppapi-flash-path="HCSFP64.dll"
# --register-pepper-plugins="HCSFP64.dll"

# url = "https://google.com"
url='https://darkorbit.com/'
# url="https://flashroom.ru/games1821.html"
# url='https://tankionline.com/play/'

class bview(QWebEngineView):
 def __init__(self, ):
  super(bview, self).__init__()
  self.p=None
#         BigpointClient/1.4.6
  self.page().profile().setHttpUserAgent("BigpointClient/1.6.7")
  self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
  QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
  QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
  QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
  self.urlChanged.connect(self.onUrlChanged)
#   self.showFullScreen()
#   self.settings().setAttribute(WebEngineSettings.PluginsEnabled, True)
 def setFullScreen(self):
  self.showFullScreen()
  
 def onUrlChanged(self, uri):
  if uri=="https://ru6.darkorbit.com/indexInternal.es?action=internalMapRevolution":
      print(2)
  print (uri)    

       

class QDO(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QDO, self).__init__(*args, **kwargs)
        wdg = QWidget()

        lay = QVBoxLayout(wdg)
        lay.setSpacing(0)
        lay.setMargin(0)

        self.setCentralWidget(wdg)
        self.tbb=QTabWidget()

        self.tbb.setTabsClosable(True)
        self.hscale=QProgressBar(self)
        self.hscale.setMaximum(100)
        self.hscale.setMinimum(0)
        # self.hscale.setValue(55)
        self.hscale.setFixedHeight(2)
        self.hscale.setTextVisible(False)

        qs=QSettings('do.ini', 'lv')
        try:
            self.restoreGeometry(qs.value("geometry"))
        except:
            pass
        browser = bview()

        browser.loadStarted.connect(self.loadStartedHandler)
        browser.loadProgress.connect(self.loadProgressHandler)
        browser.loadFinished.connect(self.loadFinishedHandler)
        browser.titleChanged.connect(self.onTitleChanged0)
        self.tbb.addTab(browser, "")
        wdg.setLayout(lay)
        lay.addWidget(self.hscale)
        lay.addWidget(self.tbb)
        self.show()
        browser.load(QUrl(url))

    def onTitleChanged0(self, s):
     try:
      self.tbb.setTabText(0, s)
     except:
      self.tbb.setTabText("0")
  
    def closeEvent(self, event):
        qs=QSettings('do.ini', 'lv')
        qs.setValue("geometry", self.saveGeometry())
        qs.sync()

    def loadStartedHandler(self):
        self.hscale.setValue(0)

    def loadFinishedHandler(self):
        self.hscale.setValue(0)

    def loadProgressHandler(self, prog):
        self.hscale.setValue(prog)
        
if __name__ == '__main__':
  arg=sys.argv
#   a1="--register-pepper-plugins=./HCSFP64.dll"
  a2="--ppapi-flash-path=./HCSFP64.dll"
#   a3='--ppapi-plugin-launcher=./HCSFP64.dll'
#   a1="--register-pepper-plugins=HCSFP64.dll;application/x-shockwave-flash"  
#   a1="--register-pepper-plugins=pepflashplayer.dll;application/x-shockwave-flash"
#   a2="--ppapi-flash-path=pepflashplayer.dll"
  a5="--ppapi-flash-version=26.0.0.137"
#   arg.append(a1)
  arg.append(a2)
#   arg.append(a3)
  arg.append(a5)
#   , '--ppapi-startup-dialog' '-enable-pepper-testing', ,  '--ppapi', '--ppapi-in-process'
  arg.extend(['-platform', 'windows:altgr', 'enable-accelerated-2d-canvas',
              '--default-background-color=000000ff', '--disable-bundled-ppapi-flash', '--ignore-gpu-blacklist',
              '--in-process-gpu'])
#               '--remote-debugging-port=9221'])



  print(arg)
  app = QApplication(arg)
  # app.setStyleSheet("border: 1px solid;")
  ex = QDO()

  sys.exit(app.exec_())