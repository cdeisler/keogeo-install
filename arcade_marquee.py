import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QDesktopWidget
from PyQt5.QtGui import QPixmap, QPainter

class ArcadeMarquee(QWidget):
    def __init__(self):
        super().__init__()
        
        # Get the geometry of the second screen
        screen_num = 1  # The second screen is index 1
        screen = QDesktopWidget().screenGeometry(screen_num)
        
        # Set the window geometry to the size of the second screen
        self.setGeometry(screen)
        
        # Load the background image and set it as the window's background
        bg_image = QPixmap('/home/kiosk/keogeo/marquees/neo-geo-marquee.jpg')
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(self.backgroundRole(), bg_image)
        self.setPalette(palette)
        
        # Create a painter to draw the images on top of the background
        self.painter = QPainter(self)
        
        # Add the images to the painter
        self.add_image('/home/kiosk/keogeo/marquees/aof.jpg', 100, 50)
        self.add_image('/home/kiosk/keogeo/marquees/aof2.jpg', 200, 50)
        self.add_image('/home/kiosk/keogeo/marquees/aof3.jpg', 300, 50)
        
        # Show the window on the second screen
        self.move(screen.left(), screen.top())
        self.show()
        
    def add_image(self, filename, x, y):
        # Load the image file
        pixmap = QPixmap(filename)
        
        # Draw the image on the painter
        self.painter.drawPixmap(x, y, pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ArcadeMarquee()
    sys.exit(app.exec_())
