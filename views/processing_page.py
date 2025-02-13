from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, 
    QLabel, QFileDialog, QProgressDialog, QDialog, QStackedWidget
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from utils.StyleTransferThread import StyleTransferThread
class ProcessingPage(QWidget):
    def __init__(self, switch_convert_page):
        super().__init__()
        self.switch_convert_page = switch_convert_page

        self.layout = QVBoxLayout()
        self.label = QLabel("Processing Image...")
        self.layout.addWidget(self.label)

        self.progress_dialog = QProgressDialog("Processing...", "Cancel", 0, 100, self)
        self.progress_dialog.setWindowTitle("Loading")
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.layout.addWidget(self.progress_dialog)

        self.setLayout(self.layout)

    def start_processing(self):
        self.thread = StyleTransferThread()
        self.thread.progress.connect(self.progress_dialog.setValue)
        self.thread.completed.connect(self.show_styled_image)
        self.thread.start()

    def show_styled_image(self, image_path):
        self.progress_dialog.close()
        self.popup = ImagePopup(image_path)
        self.popup.exec_()
        self.switch_convert_page()  # Return to Convert Page

class ImagePopup(QDialog):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("Styled Image")
        self.setFixedSize(400, 400)

        layout = QVBoxLayout()
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(350, 350, Qt.KeepAspectRatio))
        layout.addWidget(self.image_label)

        # Download Button
        self.download_button = QPushButton("Download Image", self)
        self.download_button.clicked.connect(lambda: self.download_image(image_path))
        layout.addWidget(self.download_button)

        self.setLayout(layout)