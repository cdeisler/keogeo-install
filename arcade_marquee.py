import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QDesktopWidget
from PyQt5.QtGui import QPixmap, QPainter, QBrush
from PyQt5.QtCore import Qt
class ArcadeMarquee(QWidget):
    def __init__(self):
        super().__init__()
        
        # Get the geometry of the second screen
        screen_num = 1  # The second screen is index 1
        screen = QDesktopWidget().screenGeometry(screen_num)
        
        # Set the window geometry to the size of the second screen
        self.setGeometry(screen)
        
        # Load the background image and set it as the window's background
        #bg_pixmap = QPixmap('/home/kiosk/keogeo/marquees/neo-geo-marquee.jpg')
        # bg_pixmap = bg_pixmap.scaled(screen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)


        # brush = QBrush(bg_pixmap)
        self.setAutoFillBackground(True)
        # palette = self.palette()
        # palette.setBrush(self.backgroundRole(), brush)
        # self.setPalette(palette)
        
        # Load the background image
        bg_image = QPixmap('/home/kiosk/keogeo/marquees/neo-geo-marquee.jpg')
        bg_image = bg_image.scaled(screen.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        
        bg_label = QLabel(self)
        bg_label.setPixmap(bg_image)
        bg_label.setGeometry(0, 0, screen.size().width(), screen.size().height())

        # Load the three image overlays
        overlay1_image = QPixmap('/home/kiosk/keogeo/marquees/aof.jpg')
        overlay1_label = QLabel(self)
        overlay1_label.setPixmap(overlay1_image)
        overlay1_label.setGeometry(200, 200, 400, 488)

        overlay2_image = QPixmap('/home/kiosk/keogeo/marquees/aof2.jpg')
        overlay2_label = QLabel(self)
        overlay2_label.setPixmap(overlay2_image)
        overlay2_label.setGeometry(600, 200, 400, 488)

        overlay3_image = QPixmap('/home/kiosk/keogeo/marquees/aof3.jpg')
        overlay3_label = QLabel(self)
        overlay3_label.setPixmap(overlay3_image)
        overlay3_label.setGeometry(1000, 200, 400, 416)

        self.showFullScreen()
        #self.show()

    def add_image(self, filename, x, y):
        # Load the image file
        pixmap = QPixmap(filename)
        
        # Draw the image on the painter
        self.painter.drawPixmap(x, y, pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ArcadeMarquee()
    sys.exit(app.exec_())
