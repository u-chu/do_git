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
url='https://ru6.darkorbit.com/'
# url="https://flashroom.ru/games1821.html"

class bview(QWebEngineView):
 def __init__(self):
  super(bview, self).__init__()
#   self.b=QWebEngineView()
  self.page().profile().setHttpUserAgent("BigpointClient/1.6.7")
  self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
       
       

class QDO(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QDO, self).__init__(*args, **kwargs)
        
#         BigpointClient/1.4.6
        wdg = QWidget()
        # wdg.setStyleSheet("border:50ps solid red")
#         self.setCentralWidget(wdg)
        lay = QVBoxLayout(wdg)
#         lay.setStyleSheet("border:10")
        self.setCentralWidget(wdg)
        tbb=QTabWidget()
        tbb.setStyleSheet("border:0px")

        self.hscale=QProgressBar(self)
        self.hscale.setMaximum(100)
        self.hscale.setMinimum(0)
        # self.hscale.setValue(55)
        self.hscale.setFixedHeight(1)
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
        tbb.addTab(browser, "")
        wdg.setLayout(lay)
        lay.addWidget(self.hscale)
        lay.addWidget(tbb)        
        self.show()
        browser.load(QUrl(url))
        
    def closeEvent(self, event):
        qs=QSettings('do.ini', 'lv')
        qs.setValue("geometry", self.saveGeometry())
        qs.sync()
        
#     @QtCore.pyqtSlot()
    def loadStartedHandler(self):
        self.hscale.setValue(0)
#         self.ptToolbar.setVisible(True)

#     @QtCore.pyqtSlot()
    def loadFinishedHandler(self):
        self.hscale.setValue(0)
#         self.ptToolbar.setVisible(False)

#     @QtCore.pyqtSlot(int)
    def loadProgressHandler(self, prog):
        self.hscale.setValue(prog)
        

if __name__ == '__main__':
  arg=sys.argv[1:]
  a1="--register-pepper-plugins=./HCSFP64.dll"
  a2="--ppapi-flash-path=./HCSFP64.dll"
#   a3="--register-pepper-plugins=pepflashplayer.dll;application/x-shockwave-flash"
#   a4="--ppapi-flash-path=./pepflashplayer.dll"
  a5="--ppapi-flash-version=26.0.0.137"
#   arg.append(a1)
  arg.append(a2)
  arg.append(a5)
  arg.extend(['-platform', 'windows:altgr', 'enable-accelerated-2d-canvas', '--default-background-color=000000ff', '--disable-bundled-ppapi-flash', '--ignore-gpu-blacklist', '--in-process-gpu'])

  print(arg)
  app = QApplication(arg)
  ex = QDO()

  sys.exit(app.exec_())