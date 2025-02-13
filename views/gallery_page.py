from PySide6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, 
    QScrollArea, QFrame, QSizePolicy, QDialog, QSplitter, 
    QVBoxLayout, QPushButton
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from .sidebar import Sidebar

image_paths = ["images/anime_style1.jpg"] * 16  # Placeholder images

from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QSplitter, QLabel, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class ImagePopup(QDialog):
    def __init__(self, image_path, styles, model, resolution, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Image Details")
        self.setFixedSize(600, 400)
        
        layout = QVBoxLayout(self)
        # Create splitter to divide the window into two sections
        splitter = QSplitter(Qt.Horizontal)
        
        # Left side: Image
        pixmap = QPixmap(image_path).scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        
        # Title for Image
        image_title = QLabel("Generated Anime Image")
        image_title.setAlignment(Qt.AlignCenter)
        image_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #333; padding: 10px;")
        
        # Add image title and image to the left side of the splitter
        left_layout = QVBoxLayout()
        left_layout.addWidget(image_title)
        left_layout.addWidget(image_label)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        splitter.addWidget(left_widget)
        
        # Right side: Styles, Model, and Resolution
        details_label = QLabel(f"Styles:\n{styles}\n\nModel:\n{model}\n\nResolution:\n{resolution} px")
        details_label.setAlignment(Qt.AlignTop)
        details_label.setStyleSheet("""
            font-size: 16px;
            color: #555;
            line-height: 1.5;
            padding: 10px;
        """)
        
        # Add the details label to the right side of the splitter
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(details_label)
        splitter.addWidget(right_widget)

        layout.addWidget(splitter)

        # Close button - positioned at the bottom right
        close_button_layout = QHBoxLayout()
        close_button = QPushButton("Close", self)
        close_button.setStyleSheet("""
            QPushButton{
            background-color: #c62c2c;
            color: black;
            font-size: 18px;
            padding: 10px 20px;
            border: 2px solid black;
            }
            
            QPushButton:pressed {
        background-color: #a52a2a;  /* Darker shade when pressed */
    }
        """)
        close_button.clicked.connect(self.close)
        close_button_layout.addStretch(1)  # Push the button to the right
        close_button_layout.addWidget(close_button)

        layout.addLayout(close_button_layout)

        self.setLayout(layout)

class GalleryPage(QWidget):
    def __init__(self, switch_to_home, switch_to_gallery, switch_to_convert, switch_to_settings,switch_to_profile,switch_to_sign_in):
        super().__init__()
        self.switch_to_gallery = switch_to_gallery
        self.switch_to_home = switch_to_home
        self.switch_to_convert = switch_to_convert
        self.switch_to_settings = switch_to_settings
        self.switch_to_profile = switch_to_profile
        self.switch_to_sign_in =switch_to_sign_in

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)  # Ensures no gap between sidebar and content

        # Sidebar
        sidebar = Sidebar(self.switch_to_home, self.switch_to_gallery, self.switch_to_convert, self.switch_to_settings,self.switch_to_profile,self.switch_to_sign_in, "Gallery")
        sidebar.setFixedWidth(200)  # Ensuring Sidebar is visible
        main_layout.addWidget(sidebar)

        # Content Wrapper
        content_wrapper = QWidget()
        content_layout = QVBoxLayout(content_wrapper)
        content_layout.setAlignment(Qt.AlignTop)
        content_layout.setContentsMargins(10, 20, 10, 10)  # Set top margin to 20 for some spacing
        
        # Heading
        heading = QLabel("User Gallery")
        heading.setAlignment(Qt.AlignLeft)  # Left-align the heading
        heading.setStyleSheet("font-size: 30px; font-weight: bold; color: #333; padding-left: 20px;")  # Bigger, bolder, and left-aligned
        content_layout.addWidget(heading)

        # Horizontal line below the heading
        horizontal_line = QFrame()
        horizontal_line.setFrameShape(QFrame.HLine)
        horizontal_line.setFrameShadow(QFrame.Sunken)
        horizontal_line.setStyleSheet("color: #ccc;")  # Light gray color for the line
        content_layout.addWidget(horizontal_line)

        # Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setStyleSheet("""
    QScrollArea {
        border: none;
    }
    QScrollBar:vertical, QScrollBar:horizontal {
        background-color: #f0f0f0;
        width: 10px;
        height: 10px;
    }
    QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
        background-color: #c62c2c;
        border: 2px solid black;
    }
    QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
        background-color: #a52a2a;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        background-color: transparent;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,
    QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
        background-color: transparent;
    }""")
        # Grid Layout
        grid_widget = QWidget()
        grid_layout = QGridLayout(grid_widget)
        grid_layout.setSpacing(10)

        # Add images to the grid
        row, col = 0, 0
        for path in image_paths:
            pixmap = QPixmap(path).scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            
            # Frame for each image
            frame = QFrame()

            # Image label inside the frame
            label = QLabel()
            label.setPixmap(pixmap)
            label.setAlignment(Qt.AlignCenter)  # Center-align the photo inside the frame
            label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            
            # Define styles (replace with actual styles)
            styles = "Style 1, Style 2, Style 3"
            model = "AnimeGan"
            resolution = "1024"
            
            # When image is clicked, open the popup
            label.mousePressEvent = lambda event, image_path=path, styles=styles: self.open_image_popup(image_path, styles, model, resolution)

            frame_layout = QVBoxLayout(frame)
            frame_layout.setAlignment(Qt.AlignLeft)  # Center the image inside the frame
            frame_layout.addWidget(label)
            frame_layout.setSpacing(0)  # No space between image and frame
            frame_layout.setContentsMargins(0, 0, 0, 0)  # No space around the layout
            grid_layout.addWidget(frame, row, col)
            
            col += 1
            if col == 4:  # 4 images per row
                col = 0
                row += 1

        grid_widget.setLayout(grid_layout)
        scroll_area.setWidget(grid_widget)
        content_layout.addWidget(scroll_area)

        main_layout.addWidget(content_wrapper)
        main_layout.setStretch(1, 4)  # Sidebar takes less space, content takes more

    def open_image_popup(self, image_path, styles,model,resolution):
        popup = ImagePopup(image_path, styles,model,resolution)
        popup.exec_()  # Show the popup as a modal window
