import datetime
import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from services import TaskService

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1280</width>
    <height>720</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1280</width>
    <height>720</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1280</width>
    <height>720</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalWidget" native="true">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>1280</width>
      <height>669</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QWidget" name="verticalWidget_3" native="true">
       <layout class="QVBoxLayout" name="verticalLayout_3">
        <item>
         <widget class="QLabel" name="label">
          <property name="font">
           <font>
            <pointsize>16</pointsize>
           </font>
          </property>
          <property name="text">
           <string>TODO</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="addTodo">
          <property name="font">
           <font>
            <pointsize>12</pointsize>
           </font>
          </property>
          <property name="text">
           <string>Add</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLineEdit" name="lineEdit">
          <property name="font">
           <font>
            <pointsize>11</pointsize>
           </font>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QListWidget" name="listWidget"/>
        </item>
        <item>
         <widget class="QPushButton" name="delete1">
          <property name="text">
           <string>Delete</string>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
     </item>
     <item>
      <widget class="QWidget" name="verticalWidget" native="true">
       <layout class="QVBoxLayout" name="verticalLayout_4">
        <item>
         <widget class="QPushButton" name="TIn">
          <property name="text">
           <string>-&gt;</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="InT">
          <property name="text">
           <string>&lt;-</string>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
     </item>
     <item>
      <widget class="QWidget" name="verticalWidget_2" native="true">
       <layout class="QVBoxLayout" name="verticalLayout_2">
        <item>
         <widget class="QLabel" name="label_2">
          <property name="font">
           <font>
            <pointsize>16</pointsize>
           </font>
          </property>
          <property name="text">
           <string>IN PROGRESS</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="addProgress">
          <property name="font">
           <font>
            <pointsize>12</pointsize>
           </font>
          </property>
          <property name="cursor">
           <cursorShape>PointingHandCursor</cursorShape>
          </property>
          <property name="text">
           <string>Add</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLineEdit" name="lineEdit_2">
          <property name="font">
           <font>
            <pointsize>11</pointsize>
           </font>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QListWidget" name="listWidget_2"/>
        </item>
        <item>
         <widget class="QPushButton" name="delete2">
          <property name="text">
           <string>Delete</string>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
     </item>
     <item>
      <widget class="QWidget" name="verticalWidget_4" native="true">
       <layout class="QVBoxLayout" name="verticalLayout_5">
        <item>
         <widget class="QPushButton" name="InC">
          <property name="text">
           <string>-&gt;</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="CIn">
          <property name="text">
           <string>&lt;-</string>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
     </item>
     <item>
      <widget class="QWidget" name="verticalWidget" native="true">
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <widget class="QLabel" name="label_3">
          <property name="font">
           <font>
            <pointsize>16</pointsize>
           </font>
          </property>
          <property name="text">
           <string>COMPLETE</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="addComplete">
          <property name="font">
           <font>
            <pointsize>12</pointsize>
           </font>
          </property>
          <property name="cursor">
           <cursorShape>PointingHandCursor</cursorShape>
          </property>
          <property name="text">
           <string>Add</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLineEdit" name="lineEdit_3">
          <property name="font">
           <font>
            <pointsize>11</pointsize>
           </font>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QListWidget" name="listWidget_3"/>
        </item>
        <item>
         <widget class="QPushButton" name="delete3">
          <property name="text">
           <string>Delete</string>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1280</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""


class Kanban(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        tasks = TaskService().findAll()
        for i in tasks:
            el = dict(i)
            if el.get('status') == "TODO":
                self.listWidget.addItem(el.get('title'))
            elif el.get('status') == "PROGRESS":
                self.listWidget_2.addItem(el.get('title'))
            elif el.get('status') == "COMPLETE":
                self.listWidget_3.addItem(el.get('title'))

        self.addTodo.clicked.connect(self.addTodoListener)
        self.addProgress.clicked.connect(self.addProgressListener)
        self.addComplete.clicked.connect(self.addCompleteListener)

        self.delete1.clicked.connect(self.deleteL)
        self.delete2.clicked.connect(self.delete2L)
        self.delete3.clicked.connect(self.delete3L)

        self.TIn.clicked.connect(self.todoProgressL)
        self.InT.clicked.connect(self.progressTodoL)
        self.InC.clicked.connect(self.progressCompleteL)
        self.CIn.clicked.connect(self.completeProgressL)

    def todoProgressL(self):
        try:
            item = self.listWidget.currentItem()
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            TaskService().updateByTitle(item.text(), "PROGRESS")
        except Exception as e:
            with open("logs.txt", "a+") as f:
                f.write(f"{str(datetime.datetime.now()).split('.')[0]} - {e.__class__}: {e}\n")

    def progressTodoL(self):
        try:
            item = self.listWidget_2.currentItem()
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.listWidget.addItem(item.text())
            TaskService().updateByTitle(item.text(), "TODO")
        except Exception as e:
            with open("logs.txt", "a+") as f:
                f.write(f"{str(datetime.datetime.now()).split('.')[0]} - {e.__class__}: {e}\n")

    def progressCompleteL(self):
        try:
            item = self.listWidget_2.currentItem()
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.listWidget_3.addItem(item.text())
            TaskService().updateByTitle(item.text(), "COMPLETE")
        except Exception as e:
            with open("logs.txt", "a+") as f:
                f.write(f"{str(datetime.datetime.now()).split('.')[0]} - {e.__class__}: {e}\n")

    def completeProgressL(self):
        try:
            item = self.listWidget_3.currentItem()
            self.listWidget_3.takeItem(self.listWidget_3.row(item))
            self.listWidget_2.addItem(item.text())
            TaskService().updateByTitle(item.text(), "PROGRESS")
        except Exception as e:
            with open("logs.txt", "a+") as f:
                f.write(f"{str(datetime.datetime.now()).split('.')[0]} - {e.__class__}: {e}\n")

    def deleteL(self):
        try:
            item = self.listWidget.currentItem()
            self.listWidget.takeItem(self.listWidget.row(item))
            TaskService().deleteByTitle(item.text())
        except Exception as e:
            with open("logs.txt", "a+") as f:
                f.write(f"{str(datetime.datetime.now()).split('.')[0]} - {e.__class__}: {e}\n")

    def delete2L(self):
        try:
            item = self.listWidget_2.currentItem()
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            TaskService().deleteByTitle(item.text())
        except Exception as e:
            with open("logs.txt", "a+") as f:
                f.write(f"{str(datetime.datetime.now()).split('.')[0]} - {e.__class__}: {e}\n")

    def delete3L(self):
        try:
            item = self.listWidget_3.currentItem()
            self.listWidget_3.takeItem(self.listWidget_3.row(item))
            TaskService().deleteByTitle(item.text())
        except Exception as e:
            with open("logs.txt", "a+") as f:
                f.write(f"{str(datetime.datetime.now()).split('.')[0]} - {e.__class__}: {e}\n")

    def addTodoListener(self):
        if len(self.lineEdit.text().strip()) != 0:
            self.listWidget.addItem(self.lineEdit.text().strip())
            TaskService().create(self.lineEdit.text(), "TODO")
        self.lineEdit.clear()

    def addProgressListener(self):
        if len(self.lineEdit_2.text().strip()) != 0:
            self.listWidget_2.addItem(self.lineEdit_2.text().strip())
            TaskService().create(self.lineEdit_2.text(), "PROGRESS")
        self.lineEdit_2.clear()

    def addCompleteListener(self):
        if len(self.lineEdit_3.text().strip()) != 0:
            self.listWidget_3.addItem(self.lineEdit_3.text().strip())
            TaskService().create(self.lineEdit_3.text(), "COMPLETE")
        self.lineEdit_3.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    kan = Kanban()
    kan.show()
    sys.exit(app.exec_())
