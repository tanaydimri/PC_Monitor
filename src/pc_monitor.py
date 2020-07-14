"""
quthor = Tanay Dimri
created_on = 14-07-2020

This Application was developed as a part of the test during an interview.
"""
# importing builtin modules
import sys

# importing 3rd party modules
from PySide import QtXml  # Need to import this so that the PyInstaller does not fail
from PySide import QtGui, QtCore
from ui.pc_monitor import Ui_PcMonitorUi as ui_class
import psutil


class PcMonitor(QtGui.QWidget, ui_class):
    def __init__(self):
        """
        Init method for the class PcMonitorUI
        """
        super(PcMonitor, self).__init__()
        self.setupUi(self)
        self.show()

        # Populating the CPUs detail view
        self.total_cpus = psutil.cpu_count()
        self.all_cpu_usage = psutil.cpu_percent(percpu=True)
        self.cpu_model = QtGui.QStandardItemModel()
        self.setup_cpus_tree()

        self.get_usage()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)

    @staticmethod
    def get_usage():
        """
        Method responsible for getting and returning the current cpu and ram usage

        :return tuple: (cpu_usage%, ram_usage%)
        """
        return psutil.cpu_percent(), psutil.virtual_memory().percent

    def update_progress(self):
        """
        Method responsible for getting the current usage and updating the progress bars in the UI.
        """
        curr_usage = self.get_usage()
        self.progressBar_cpu_usage.setValue(curr_usage[0])
        self.progressBar_ram_usage.setValue(curr_usage[1])

        self.update_all_cpus_tree()

    def setup_cpus_tree(self):
        """
        Method to setup the initial CPU details view.
        """
        self.listView_individual_logical_cpu.setModel(self.cpu_model)

        for cpu in range(self.total_cpus):
            cpu_name = QtGui.QStandardItem(
                "CPU - {0} Usage :  {1}".format(cpu, str(self.all_cpu_usage[cpu]))
            )
            self.cpu_model.appendRow(cpu_name)

    def update_all_cpus_tree(self):
        """
        Updates the cpu details.
        """
        self.all_cpu_usage = psutil.cpu_percent(percpu=True)

        for cpu in range(self.total_cpus):
            cpu_name = QtGui.QStandardItem(
                "CPU - {0} Usage :  {1}".format(cpu, str(self.all_cpu_usage[cpu]))
            )
            self.cpu_model.setItem(cpu, cpu_name)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWin = PcMonitor()
    sys.exit(app.exec_())
