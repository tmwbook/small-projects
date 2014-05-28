from time import time
import threading
import os
#hh:mm:ss
movie1Time = "00:00:00"
movie2Time = "00:00:00"
movie3Time = "00:00:00"
movie4Time = "00:00:00"
movie5Time = "00:00:00"

timer1Start = None
timer1Time = "00:00:00"
timer1Running = False
timer2Start = None
timer2Time = "00:00:00"
timer2Running = False
timer3Start = None
timer3Time = "00:00:00"
timer3Running = False
timer4Start = None
timer4Time = "00:00:00"
timer4Running = False
timer5Start = None
timer5Time = "00:00:00"
timer5Running = False

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed May 21 20:35:02 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class TestThread(QtCore.QThread):
    index_finished = QtCore.pyqtSignal([str, QtCore.QObject])

    def __init__(self, timerStart, timerRunning, timerNumber, movieTime, textBrowser, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.timerStart = timerStart
        self.timerRunning = timerRunning
        self.timerNumber = timerNumber
        self.textBrowser = textBrowser
        self.movieTime = movieTime

    def run(self):
        self.incrememnt(self.timerStart, self.timerRunning, self.timerNumber, self.movieTime)

    def formatTime(self, time):
        formattedTime = ''
        hours = time / 3600
        minutes = time / 60
        seconds = time % 60
        if hours == 0:
            formattedTime += "00:"
        elif len(str(hours)) == 1:
            formattedTime += '0' + str(hours) + ':'
        else:
            formattedTime += str(hours)
        if minutes == 0:
            formattedTime += "00:"
        elif minutes > 60:
            newMinutes = minutes
            while minutes > 60:
                newMinutes -= 60
            if len(newMinutes) == 1:
                formattedTime += '0' + str(newMinutes) + ':'
            else:
                formattedTime += str(newMinutes)
        else:
            if len(str(minutes)) == 1:
                formattedTime += '0' + str(minutes) + ':'
            else:
                formattedTime += str(minutes)
        if len(str(seconds)) == 1:
            formattedTime += '0' + str(seconds)
        else:
            formattedTime += str(seconds)
        return formattedTime

    def deformatTime(self, time):
        timeInSecs = 0
        timeInSecs += int(time[0:2]) * 3600  # hours
        timeInSecs += int(time[3:5]) * 60    # minutes
        timeInSecs += int(time[6:8])         # seconds
        return timeInSecs

    def incrememnt(self, timerStart, timerRunning, timerNumber, movieTime):
        global timer1Time, timer2Time, timer3Time, timer4Time, timer5Time
        if timerRunning:
            convertedTime = self.deformatTime(movieTime)
            timerTime = self.formatTime(int(time()) - int(timerStart) + convertedTime)
            if timerNumber == 1:
                timer1Time = timerTime
                self.index_finished.emit(timer1Time, self.textBrowser)
            elif timerNumber == 2:
                timer2Time = timerTime
                self.index_finished.emit(timer2Time, self.textBrowser)
            elif timerNumber == 3:
                timer3Time = timerTime
                self.index_finished.emit(timer3Time, self.textBrowser)
            elif timerNumber == 4:
                timer4Time = timerTime
                self.index_finished.emit(timer4Time, self.textBrowser)
            elif timerNumber == 5:
                timer5Time = timerTime
                self.index_finished.emit(timer5Time, self.textBrowser)
        else:
            timerStart = None
            self.index_finished.emit('none')
            return timerStart


class Ui_Form1(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        if os.path.exists(os.getcwd() + '\\settings.ini') and os.path.getsize(os.getcwd() + '\\settings.ini') > 0:
            with open(os.getcwd() + '\\settings.ini', 'r') as var:
                global movie1Time, movie2Time, movie3Time, movie4Time, movie5Time
                movie1Time = var.readline().strip()
                self.updateGUITimers(movie1Time, self.textBrowser_6)
                movie2Time = var.readline().strip()
                self.updateGUITimers(movie2Time, self.textBrowser_2)
                movie3Time = var.readline().strip()
                self.updateGUITimers(movie3Time, self.textBrowser_5)
                movie4Time = var.readline().strip()
                self.updateGUITimers(movie4Time, self.textBrowser_3)
                movie5Time = var.readline().strip()
                self.updateGUITimers(movie5Time, self.textBrowser_4)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 289)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(611, 289))
        Form.setMaximumSize(QtCore.QSize(611, 289))
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 61, 261))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.movieOne = QtGui.QLabel(self.verticalLayoutWidget)
        self.movieOne.setObjectName(_fromUtf8("movieOne"))
        self.verticalLayout.addWidget(self.movieOne)
        self.movieTwo = QtGui.QLabel(self.verticalLayoutWidget)
        self.movieTwo.setObjectName(_fromUtf8("movieTwo"))
        self.verticalLayout.addWidget(self.movieTwo)
        self.movieThree = QtGui.QLabel(self.verticalLayoutWidget)
        self.movieThree.setObjectName(_fromUtf8("movieThree"))
        self.verticalLayout.addWidget(self.movieThree)
        self.movieFour = QtGui.QLabel(self.verticalLayoutWidget)
        self.movieFour.setObjectName(_fromUtf8("movieFour"))
        self.verticalLayout.addWidget(self.movieFour)
        self.movieFive = QtGui.QLabel(self.verticalLayoutWidget)
        self.movieFive.setObjectName(_fromUtf8("movieFive"))
        self.verticalLayout.addWidget(self.movieFive)
        self.DesignedBy = QtGui.QLabel(Form)
        self.DesignedBy.setGeometry(QtCore.QRect(440, 40, 111, 31))
        self.DesignedBy.setAlignment(QtCore.Qt.AlignCenter)
        self.DesignedBy.setObjectName(_fromUtf8("DesignedBy"))
        self.sourceAt = QtGui.QLabel(Form)
        self.sourceAt.setGeometry(QtCore.QRect(440, 170, 111, 20))
        self.sourceAt.setObjectName(_fromUtf8("sourceAt"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(580, 270, 31, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 40, 101, 261))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.startTwo = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.startTwo.setObjectName(_fromUtf8("startTwo"))
        self.verticalLayout_2.addWidget(self.startTwo)
        self.startOne = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.startOne.setObjectName(_fromUtf8("startOne"))
        self.verticalLayout_2.addWidget(self.startOne)
        self.startThree = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.startThree.setObjectName(_fromUtf8("startThree"))
        self.verticalLayout_2.addWidget(self.startThree)
        self.startFour = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.startFour.setObjectName(_fromUtf8("startFour"))
        self.verticalLayout_2.addWidget(self.startFour)
        self.startFive = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.startFive.setObjectName(_fromUtf8("startFive"))
        self.verticalLayout_2.addWidget(self.startFive)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(400, 230, 160, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.save = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.save.setObjectName(_fromUtf8("save"))
        self.horizontalLayout.addWidget(self.save)
        self.settings = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.settings.setObjectName(_fromUtf8("settings"))
        self.horizontalLayout.addWidget(self.settings)
        self.textBrowser_2 = QtGui.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(90, 110, 113, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(113)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(113, 20))
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setReadOnly(False)
        self.textBrowser_2.setUndoRedoEnabled(True)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser_5 = QtGui.QTextBrowser(Form)
        self.textBrowser_5.setGeometry(QtCore.QRect(90, 160, 113, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(113)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.textBrowser_5.sizePolicy().hasHeightForWidth())
        self.textBrowser_5.setSizePolicy(sizePolicy)
        self.textBrowser_5.setMinimumSize(QtCore.QSize(113, 20))
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setReadOnly(False)
        self.textBrowser_5.setUndoRedoEnabled(True)
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        self.textBrowser_4 = QtGui.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(90, 260, 113, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(113)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.textBrowser_4.sizePolicy().hasHeightForWidth())
        self.textBrowser_4.setSizePolicy(sizePolicy)
        self.textBrowser_4.setMinimumSize(QtCore.QSize(113, 20))
        self.textBrowser_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setReadOnly(False)
        self.textBrowser_4.setUndoRedoEnabled(True)
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.textBrowser_3 = QtGui.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(90, 210, 113, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(113)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy)
        self.textBrowser_3.setMinimumSize(QtCore.QSize(113, 20))
        self.textBrowser_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setReadOnly(False)
        self.textBrowser_3.setUndoRedoEnabled(True)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.textBrowser_6 = QtGui.QTextBrowser(Form)
        self.textBrowser_6.setGeometry(QtCore.QRect(90, 60, 113, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(113)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.textBrowser_6.sizePolicy().hasHeightForWidth())
        self.textBrowser_6.setSizePolicy(sizePolicy)
        self.textBrowser_6.setMinimumSize(QtCore.QSize(113, 20))
        self.textBrowser_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_6.setReadOnly(False)
        self.textBrowser_6.setUndoRedoEnabled(True)
        self.textBrowser_6.setObjectName(_fromUtf8("textBrowser_6"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(340, 50, 20, 211))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(430, 190, 151, 20))
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(420, 80, 161, 91))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("logo.jpg")))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.textBrowser_6, QtCore.SIGNAL(_fromUtf8("textChanged()")), Form.changeMovie1)
        QtCore.QObject.connect(self.textBrowser_2, QtCore.SIGNAL(_fromUtf8("textChanged()")), Form.changeMovie2)
        QtCore.QObject.connect(self.textBrowser_5, QtCore.SIGNAL(_fromUtf8("textChanged()")), Form.changeMovie3)
        QtCore.QObject.connect(self.textBrowser_3, QtCore.SIGNAL(_fromUtf8("textChanged()")), Form.changeMovie4)
        QtCore.QObject.connect(self.textBrowser_4, QtCore.SIGNAL(_fromUtf8("textChanged()")), Form.changeMovie5)
        QtCore.QObject.connect(self.startTwo, QtCore.SIGNAL(_fromUtf8("pressed()")), Form.changeTimer1State)
        QtCore.QObject.connect(self.startOne, QtCore.SIGNAL(_fromUtf8("pressed()")), Form.changeTimer2State)
        QtCore.QObject.connect(self.startThree, QtCore.SIGNAL(_fromUtf8("pressed()")), Form.changeTimer3State)
        QtCore.QObject.connect(self.startFour, QtCore.SIGNAL(_fromUtf8("pressed()")), Form.changeTimer4State)
        QtCore.QObject.connect(self.startFive, QtCore.SIGNAL(_fromUtf8("pressed()")), Form.changeTimer5State)
        QtCore.QObject.connect(self.save, QtCore.SIGNAL(_fromUtf8("pressed()")), Form.saveChanges)
        QtCore.QObject.connect(self.settings, QtCore.SIGNAL(_fromUtf8("pressed()")), Form.reset)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Multiple Movie Timer", None))
        self.movieOne.setText(_translate("Form", "Movie 1", None))
        self.movieTwo.setText(_translate("Form", "Movie 2", None))
        self.movieThree.setText(_translate("Form", "Movie 3", None))
        self.movieFour.setText(_translate("Form", "Movie 4", None))
        self.movieFive.setText(_translate("Form", "Movie 5", None))
        self.DesignedBy.setText(_translate("Form", "This program was\n"
"designed by:", None))
        self.sourceAt.setText(_translate("Form", " Source is available at:", None))
        self.label.setText(_translate("Form", "V 1.0", None))
        self.startTwo.setText(_translate("Form", "Start / Stop", None))
        self.startOne.setText(_translate("Form", "Start / Stop", None))
        self.startThree.setText(_translate("Form", "Start / Stop", None))
        self.startFour.setText(_translate("Form", "Start / Stop", None))
        self.startFive.setText(_translate("Form", "Start / Stop", None))
        self.save.setToolTip(_translate("Form", "<html><head/><body><p>Save all the current times</p></body></html>", None))
        self.save.setText(_translate("Form", "Save", None))
        self.settings.setText(_translate("Form", "Reset timers", None))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">00:00:00</span></p></body></html>", None))
        self.textBrowser_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">00:00:00</span></p></body></html>", None))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">00:00:00</span></p></body></html>", None))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">00:00:00</span></p></body></html>", None))
        self.textBrowser_6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">00:00:00</span></p></body></html>", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><a href=\"https://github.com/tmwbook/small-projects/tree/Master/MultipleMovieTimer\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/tmwbook</span></a></p></body></html>", None))


    def changeMovie1(self):
        pass
    def changeMovie2(self):
        pass
    def changeMovie3(self):
        pass
    def changeMovie4(self):
        pass
    def changeMovie5(self):
        pass

    def changeTimer1State(self):
        global movie1Time, timer1Running, timer1Start, timer1Time
        if not timer1Running:
            timer1Running = True
            timer1Start = time()
            self.thread1 = TestThread(timer1Start, timer1Running, 1, movie1Time, self.textBrowser_6)
            self.thread1.index_finished.connect(self.updateGUITimers)

            def loopThread():
                if timer1Running:
                    self.thread1.start()
                    threading.Timer(1, loopThread).start()
            loopThread()
        elif timer1Running:
            timer1Running = False
            movie1Time = timer1Time

    def changeTimer2State(self):
        global movie2Time, timer2Running, timer2Start, timer2Time
        if not timer2Running:
            timer2Running = True
            timer2Start = time()
            self.thread2 = TestThread(timer2Start, timer2Running, 2, movie2Time, self.textBrowser_2)
            self.thread2.index_finished.connect(self.updateGUITimers)

            def loopThread():
                if timer2Running:
                    self.thread2.start()
                    threading.Timer(1, loopThread).start()
            loopThread()
        elif timer2Running:
            timer2Running = False
            movie2Time = timer2Time

    def changeTimer3State(self):
        global movie3Time, timer3Running, timer3Start, timer3Time
        if not timer3Running:
            timer3Running = True
            timer3Start = time()
            self.thread3 = TestThread(timer3Start, timer3Running, 3, movie3Time, self.textBrowser_5)
            self.thread3.index_finished.connect(self.updateGUITimers)

            def loopThread():
                if timer3Running:
                    self.thread3.start()
                    threading.Timer(1, loopThread).start()
            loopThread()
        elif timer3Running:
            timer3Running = False
            movie3Time = timer3Time

    def changeTimer4State(self):
        global movie4Time, timer4Running, timer4Start, timer4Time
        if not timer4Running:
            timer4Running = True
            timer4Start = time()
            self.thread4 = TestThread(timer4Start, timer4Running, 4, movie4Time, self.textBrowser_3)
            self.thread4.index_finished.connect(self.updateGUITimers)

            def loopThread():
                if timer4Running:
                    self.thread4.start()
                    threading.Timer(1, loopThread).start()
            loopThread()
        elif timer4Running:
            timer4Running = False
            movie4Time = timer4Time

    def changeTimer5State(self):
        global movie5Time, timer5Running, timer5Start, timer5Time
        if not timer5Running:
            timer5Running = True
            timer5Start = time()
            self.thread5 = TestThread(timer5Start, timer5Running, 5, movie5Time, self.textBrowser_4)
            self.thread5.index_finished.connect(self.updateGUITimers)

            def loopThread():
                if timer5Running:
                    self.thread5 .start()
                    threading.Timer(1, loopThread).start()
            loopThread()
        elif timer5Running:
            timer5Running = False
            movie5Time = timer5Time

    def reset(self):
        global movie1Time, movie2Time, movie3Time, movie4Time, movie5Time
        global timer1Time, timer2Time, timer3Time, timer4Time, timer5Time
        self.updateGUITimers('00:00:00', self.textBrowser_2)
        self.updateGUITimers('00:00:00', self.textBrowser_3)
        self.updateGUITimers('00:00:00', self.textBrowser_4)
        self.updateGUITimers('00:00:00', self.textBrowser_5)
        self.updateGUITimers('00:00:00', self.textBrowser_6)
        timerStartingValue = '00:00:00'
        movie1Time = timerStartingValue
        movie2Time = timerStartingValue
        movie3Time = timerStartingValue
        movie4Time = timerStartingValue
        movie5Time = timerStartingValue
        timer1Time = timerStartingValue
        timer2Time = timerStartingValue
        timer3Time = timerStartingValue
        timer4Time = timerStartingValue
        timer5time = timerStartingValue

    def saveChanges(self):
        cwd = os.getcwd()
        with open(cwd + '\\settings.ini', 'w') as var:
            toWrite = [movie1Time, movie2Time, movie3Time, movie4Time, movie5Time]
            for i in toWrite:
                var.write(i + '\n')

    def updateGUITimers(self, time, textBrowser):
        if time != 'none':
            textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">" + str(time) + "</span></p></body></html>", None))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form1()
    ex.show()
    sys.exit(app.exec_())