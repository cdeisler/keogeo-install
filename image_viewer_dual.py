import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageViewer(QMainWindow):
    def __init__(self, image_path, screen_geometry, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.setWindowTitle('Image Viewer')

        # Load the image
        pixmap = QPixmap(image_path)

        # Create a QLabel to display the image
        label = QLabel(self)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)

        # Set the window geometry based on the secondary monitor
        self.setGeometry(screen_geometry)

        # Show the window in fullscreen mode
        self.showFullScreen()

def main(image_path):
    app = QApplication(sys.argv)

    # Get a list of connected screens
    screens = app.screens()

    if len(screens) >= 2:
        # Use the secondary monitor (connected via HDMI)
        secondary_screen = screens[1]
        screen_geometry = secondary_screen.availableGeometry()
    else:
        print("Secondary monitor not found. Using the primary monitor.")
        # Use the primary monitor as a fallback
        primary_screen = screens[0]
        screen_geometry = primary_screen.availableGeometry()

    viewer = ImageViewer(image_path, screen_geometry)
    sys.exit(app.exec_())

if __name__ == '__main__':
    # Replace 'path/to/your/image.png' with the actual path to the PNG file
    main('path/to/your/image.png')
