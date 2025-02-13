import time
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QThread, Signal

# Worker Thread for Style Transfer
class StyleTransferThread(QThread):
    progress = Signal(int)  # Signal for updating progress
    completed = Signal(str)  # Signal when done

    def run(self):
        for i in range(1, 101):  # Simulating image processing
            time.sleep(0.05)  # Simulate processing delay
            self.progress.emit(i)
        self.completed.emit("images/anime_style1.jpg")  # Example output file