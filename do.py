import sys

# from PySide2.QtWebEngineWidgets import QWebEngineView

from PySide2 import QtCore
from PySide2.QtCore import QSettings
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, \
     QVBoxLayout, QStatusBar, QProgressBar, QToolBar, QTabBar
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView

    

# url = "https://google.com"
url='https://ru6.darkorbit.com/'

class QDO(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QDO, self).__init__(*args, **kwargs)
        browser = QWebEngineView()
        browser.load(QUrl(url))

        wdg = QWidget()
        self.setCentralWidget(wdg)
        lay = QVBoxLayout(wdg)
        tbb=QTabBar(wdg)
        tbb.addTab("1")
        tbb.addTab("2")
        lay.addWidget(tbb)
        lay.addWidget(browser)
        # self.sb=QStatusBar(self)
        # self.setStatusBar(self.sb)
        self.hscale=QProgressBar()
        self.hscale.setMaximum(100)
        self.hscale.setMinimum(0)
        self.hscale.setValue(55)
        self.hscale.setFixedHeight(5)
        self.hscale.setTextVisible(False)
#         self.hscale.setVisible(False)
#         self.hscale.setTickInterval(10);
#         self.hscale.setSingleStep(1);
        self.ptToolbar=QToolBar("play")
        #ptToolbar.setIconSize(QtCore.QSize(16, 16))
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.ptToolbar)
        self.ptToolbar.addWidget(self.hscale)
        self.ptToolbar.setVisible(False)
        qs=QSettings('do.ini', 'lv')
        try:
            self.restoreGeometry(qs.value("geometry"))
        except:
            pass
        self.show()
        
    def closeEvent(self, event):
        qs=QSettings('do.ini', 'lv')
        qs.setValue("geometry", self.saveGeometry())
        qs.sync()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = QDO()

  sys.exit(app.exec_())