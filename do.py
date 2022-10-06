#!/usr/bin/env python
#-*- coding: UTF-8 -*-
try:
 from functools import cached_property
 print('functools')
except:
 from django.utils.functional import cached_property
 print('django.utils.functional')
import sys
#~ import conf
#~ import math

# from PySide2 import QtCore

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, \
     QVBoxLayout, QProgressBar,  QTabWidget, QShortcut
from PySide2.QtCore import QUrl, QSettings
from PySide2.QtGui import QKeySequence 
from PySide2 import QtWebEngineWidgets
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

#~ url='https://darkorbit.com/'
url="https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_a_target"
uri2="https://%s.darkorbit.com/indexInternal.es?action=internalMapRevolution"
serv='ru6'

# j_str='function f(){document.getElementById("bgcdw_login_form_username").value="21";getElementById("bgcdw_login_form_password").value="qwe";}'
# j_str='document.write("121");'
j_str='document.getElementById("bgcdw_login_form_username").value="%s";'
j_str+='document.getElementById("bgcdw_login_form_password").value="%s"';
ini_f='./do.ini'

login=""
passw=""

class bview(QWebEngineView):    
 def createWindow(self, type_):
  if not isinstance(self.window(), QMain):
   return
  if type_ == QtWebEngineWidgets.QWebEnginePage.WebBrowserTab:
   return self.window().tab_widget.create_tab()

 def __init__(self, parent=None ):
  super(bview, self).__init__(parent)
  # m_fullScreenWindow=None
  self.p=None
#         BigpointClient/1.4.6
  self.page().profile().setHttpUserAgent("BigpointClient/1.6.7")
  self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
  QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
  QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
  QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
  QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
  fs=QShortcut(QKeySequence("F11"), self)
  fs.activated.connect(self.setFullScreen)
  self.isFullScreen=False

 def setFullScreen(self):
  print('setFullScreen', self.isFullScreen)
  if self.isFullScreen:
    print(1)
    self.showNormal()
    self.isFullScreen=False
  else:
    print(2)
    self.showFullScreen()
    self.isFullScreen=True

  # self.page().onFullScreenRequested.
#   self.urlChanged.connect(self.onUrlChanged)
#   self.page().linkHovered.connect(self.onLinkHovered)


#   self.showFullScreen()
  

class TabWidget(QTabWidget):
    def create_tab(self):
        view = bview()

        index = self.addTab(view, "(Untitled)")
        self.setTabIcon(index, view.icon())
        view.titleChanged.connect(
            lambda title, view=view: self.update_title(view, title)
        )
        view.iconChanged.connect(lambda icon, view=view: self.update_icon(view, icon))
        self.setCurrentWidget(view)
        return view

    def update_title(self, view, title):
        index = self.indexOf(view)
        self.setTabText(index, title)

    def update_icon(self, view, icon):
        index = self.indexOf(view)
        self.setTabIcon(index, icon)


class QMain(QMainWindow):
 def __init__(self, parent=None):
  super(QMain, self).__init__(parent)
  wdg = QWidget()
  self.hscale=QProgressBar(self)
  lay = QVBoxLayout(wdg)
  lay.addWidget(self.hscale)
  wdg.setLayout(lay)
  lay.setSpacing(0)
  lay.setMargin(0)
  self.tbb=self.tab_widget
  lay.addWidget(self.tbb)
  self.setCentralWidget(wdg)
  self.tbb.setTabsClosable(True)
#   self.tbb.setIconSize(QSize(10, 10))
  self.tbb.tabCloseRequested.connect(self.onTabCloseRequest)
  
  self.hscale.setMaximum(100)
  self.hscale.setMinimum(0)
  self.hscale.setFixedHeight(2)
  self.hscale.setTextVisible(False)
  qs=QSettings(ini_f, QSettings.IniFormat)
  try:
   self.restoreGeometry(qs.value("geometry"))
  except:
   pass
  view = self.tab_widget.create_tab()

  view.loadStarted.connect(self.loadStartedHandler)
  view.loadProgress.connect(self.loadProgressHandler)
  view.loadFinished.connect(self.loadFinishedHandler)
  view.setZoomFactor(0.9)
  view.setFocus()
  try:
   with open('./do.qss', "r") as h:
    self.setStyleSheet(h.read())
  except:
    pass
  view.load(QUrl(url))
  
 @cached_property
 def tab_widget(self):
  return TabWidget() 

 #~ def putAutoFill(self):
  #~ w = self.tbb.widget(0)   
  #~ w.page().runJavaScript(j_str%(login, passw));   

#  def onCurrentChanged(self, i):
#   w=self.tbb.widget(i)
#   if w!=None:
#    z=w.zoomFactor()
#    try:
#     z=str(int(math.ceil(100*z)))
#    except ValueError:
#     z='100'
#   else:
#    z='100'
#   z=conf.scale_list.index(z)
#   self.cb.setCurrentIndex(z)


#  def onSelectionChange(self, i):
  # w=self.tbb.widget(self.tbb.currentIndex())
  # if w!= None:
  #  w.setZoomFactor(int(conf.scale_list[i])/100)

#  def onConfig(self):
  # d=conf.Conf()
  # ok, a,b,c=d.getConf()

#  def setFullScreen(self):
  # print('setFullScreen')
  # self.showFullScreen()
        
 def onTabCloseRequest(self, index):
  self.tbb.widget(index).close()  
  self.tbb.removeTab(index)
  if self.tbb.count()<=0:
   self.close()

    
 #~ def onTitleChanged0(self, s):
  #~ try:
   #~ self.tbb.setTabText(0, s)
  #~ except:
   #~ self.tbb.setTabText("")
  
 def closeEvent(self, event):
  qs=QSettings(ini_f, QSettings.IniFormat)
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
 strs=[ 'enable-accelerated-2d-canvas',
        '--default-background-color=000000ff', '--disable-bundled-ppapi-flash',
        '--ignore-gpu-blacklist',
        '--in-process-gpu', '--enable-smooth-scrolling']
 if sys.platform.startswith('win'):
  strs.extend(['-platform', 'windows:altgr', "--ppapi-flash-path=./HCSFP64.dll",
               "--ppapi-flash-version=26.0.0.137"])
 else:
  strs.extend([ "--ppapi-flash-version=32.0.0.137",
         "--ppapi-flash-path=./libpepfplashplayer.so"])

 arg.extend(strs)
 app = QApplication(arg)
 ex = QMain()
 ex.show()
 sys.exit(app.exec_())