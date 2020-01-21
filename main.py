import sys  # sys need for import argv in QApplication
import os
import glob
import serial
import design
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # need for access to vars and functions
        # e.t.c in  design.py
        # super(QtWidgets.QMainWindow, self).__init__()
        QtWidgets.QMainWindow.__init__(self)
        design.Ui_MainWindow.__init__(self)
        # super().__init__()
        self.setupUi(self)  # initial our design
        self.setAviablePorts()
        # self.portSelect.addItem("qqqq")
        # self.portSelect.addItem("qqqq4")
        # self.portSelect.addItem("qqqq2")
        # self.portSelect.clicked.connect(self.select_port)

    def setAviablePorts(self):
        ports = self.serial_ports()
        speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']
        for port in ports:
            self.portSelect.addItem(port)
        for speed in speeds:
            self.speedSelect.addItem(speed)
        print ports
        # self.portSelect.addItem("qqqq")
  #       self.listWidget.clear()
  #       directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Open directory")
		# # open dialog window
  #       if directory:
  #           for file_name in os.listdir(directory):
  #               self.listWidget.addItem(file_name)
    def serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

def main():
	app = QtWidgets.QApplication(sys.argv)
	window = ExampleApp()
	window.show()
	app.exec_()  # start app

if __name__ == '__main__': 
	main()  


# pyuic5 untitled.ui -o design.py ui -> py

# pip install pyserial pyqt5
# pip install pyserial