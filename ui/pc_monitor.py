# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Works\Programming\Developments\PC_Monitor\ui\pc_monitor.ui'
#
# Created: Tue Jul 14 17:11:58 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PcMonitorUi(object):
    def setupUi(self, PcMonitorUi):
        PcMonitorUi.setObjectName("PcMonitorUi")
        PcMonitorUi.resize(520, 301)
        self.gridLayout = QtGui.QGridLayout(PcMonitorUi)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(PcMonitorUi)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.progressBar_cpu_usage = QtGui.QProgressBar(PcMonitorUi)
        self.progressBar_cpu_usage.setObjectName("progressBar_cpu_usage")
        self.horizontalLayout.addWidget(self.progressBar_cpu_usage)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(PcMonitorUi)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.progressBar_ram_usage = QtGui.QProgressBar(PcMonitorUi)
        self.progressBar_ram_usage.setObjectName("progressBar_ram_usage")
        self.horizontalLayout_2.addWidget(self.progressBar_ram_usage)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listView_individual_logical_cpu = QtGui.QListView(PcMonitorUi)
        self.listView_individual_logical_cpu.setObjectName("listView_individual_logical_cpu")
        self.verticalLayout.addWidget(self.listView_individual_logical_cpu)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(PcMonitorUi)
        QtCore.QMetaObject.connectSlotsByName(PcMonitorUi)

    def retranslateUi(self, PcMonitorUi):
        PcMonitorUi.setWindowTitle(QtGui.QApplication.translate("PcMonitorUi", "PC Monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PcMonitorUi", "Total CPU USAGE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PcMonitorUi", "Total RAM USAGE", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PcMonitorUi = QtGui.QWidget()
    ui = Ui_PcMonitorUi()
    ui.setupUi(PcMonitorUi)
    PcMonitorUi.show()
    sys.exit(app.exec_())

