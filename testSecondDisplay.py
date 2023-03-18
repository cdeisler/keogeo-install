from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QProcess, QTextStream, Qt, QObject, pyqtSignal
import sys
import time
import threading


def main():

    print('Step 1')
    print('     Some logic here without QT')

    print('Step 2')
    print('     Launch QT app to run in background')
    myapp = myImageDisplayApp()

    print('Step 3')
    print('     Continue some logic while QT running in background')
    process = QProcess()
    process.setProcessChannelMode(QProcess.MergedChannels)

    process.start("sudo", ["./home/kiosk/retroarch/retroarch", "-L", "-f", "/home/kiosk/libretro-super/dist/unix/fbneo_libretro.so", "/home/kiosk/keogeo/roms/fbneo/kof98.zip"])
    time.sleep(12)

    # print('Step 4')
    # print('     Update the displayed image in the QT app running in background')
    # myapp.emit_image_update('/home/kiosk/keogeo/1943.png')
    # time.sleep(2)

    # print('Step 5')
    # print('     Update displayed image again')
    # myapp.emit_image_update('/home/kiosk/keogeo/1943.png')
    # time.sleep(2)
	
	
class RetroThread(QObject):
    output_received = pyqtSignal(str)
    error_received = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        # Run the libretroarch command
        process = QProcess()
        process.setProcessChannelMode(QProcess.MergedChannels)
        process.readyReadStandardOutput.connect(self.handle_output)
        process.readyReadStandardError.connect(self.handle_error)
        process.start("sudo", ["./home/kiosk/retroarch/retroarch", "-L", "-f", "/home/kiosk/libretro-super/dist/unix/fbneo_libretro.so", "/home/kiosk/keogeo/roms/fbneo/kof98.zip"])

    def handle_output(self):
        output = QTextStream(self.process)
        self.output_received.emit(output.readAll())

    def handle_error(self):
        error = QTextStream(self.process)
        self.error_received.emit(error.readAll())

class myImageDisplayApp (QObject):

    # Define the custom signal
    # https://www.riverbankcomputing.com/static/Docs/PyQt5/signals_slots.html#the-pyqtslot-decorator
    signal_update_image = pyqtSignal(str)

    def __init__ (self):

        super().__init__()

        # Setup the seperate thread 
        # https://stackoverflow.com/a/37694109/4988010
        self.thread = threading.Thread(target=self.run_app_widget_in_background) 
        self.thread.daemon = True
        self.thread.start()

    def run_app_widget_in_background(self):
        self.app = QApplication(sys.argv)
        self.my_bg_qt_app = qtAppWidget(main_thread_object=self)
        self.app.exec_()

    def emit_image_update(self, pattern_file=None):
        print('emit_image_update signal')
        self.signal_update_image.emit(pattern_file)


class qtAppWidget (QLabel):

    def __init__ (self, main_thread_object):

        super().__init__()

        # Connect the singal to slot
        main_thread_object.signal_update_image.connect(self.updateImage)

        self.setupGUI()
        
    def setupGUI(self):

        self.app = QApplication.instance()

        # Get avaliable screens/monitors
        # https://doc.qt.io/qt-5/qscreen.html
        # Get info on selected screen 
        self.selected_screen = 1            # Select the desired monitor/screen

        self.screens_available = self.app.screens()
        self.screen = self.screens_available[self.selected_screen]
        self.screen_width = self.screen.size().width()
        self.screen_height = self.screen.size().height()

        # Create a black image for init 
        self.pixmap = QPixmap(self.screen_width, self.screen_height)
        self.pixmap.fill(QColor('black'))

        # Create QLabel object
        self.app_widget = QLabel()

        # Varioius flags that can be applied to make displayed window frameless, fullscreen, etc...
        # https://doc.qt.io/qt-5/qt.html#WindowType-enum
        # https://doc.qt.io/qt-5/qt.html#WidgetAttribute-enum
        self.app_widget.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowDoesNotAcceptFocus | Qt.WindowStaysOnTopHint)
        # Hide mouse cursor 
        self.app_widget.setCursor(Qt.BlankCursor)       

        monitor = QDesktopWidget().screenGeometry(self.selected_screen)
        #widget.move(monitor.left(), monitor.top())


        self.app_widget.setGeometry(monitor.left(), monitor.top(), monitor.width(), monitor.height())            # Set the size of Qlabel to size of the screen
        self.app_widget.setWindowTitle('myImageDisplayApp')
        self.app_widget.setAlignment(Qt.AlignLeft | Qt.AlignTop) #https://doc.qt.io/qt-5/qt.html#AlignmentFlag-enum                         
        self.app_widget.setPixmap(self.pixmap)
        self.app_widget.show()

        # Set the screen on which widget is on
        self.app_widget.windowHandle().setScreen(self.screen)

        # Make full screen 
        self.app_widget.showFullScreen()


    def updateImage(self, pattern_file=None):
        print('Pattern file given: ', pattern_file)
        self.app_widget.clear()                     # Clear all existing content of the QLabel
        self.pixmap = QPixmap(pattern_file)         # Update pixmap with desired image  
        self.app_widget.setPixmap(self.pixmap)      # Show desired image on Qlabel

if __name__ == "__main__":

    main() 