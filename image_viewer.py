import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap

class ImageViewer(QMainWindow):
    def __init__(self, image_path, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.setWindowTitle('Image Viewer')

        # Load the image
        pixmap = QPixmap(image_path)

        # Create a QLabel to display the image
        label = QLabel(self)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)

        # Show the window in fullscreen mode
        self.showFullScreen()

def main(image_path):
    app = QApplication(sys.argv)
    viewer = ImageViewer(image_path)
    sys.exit(app.exec_())

if __name__ == '__main__':
    # Replace 'path/to/your/image.png' with the actual path to the PNG file
    main('/home/kiosk/keogeo1943.png')
