from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                               QHBoxLayout, QLabel, QFrame, QScrollArea, QGridLayout, QGraphicsDropShadowEffect,QSizePolicy)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, QSize
from .sidebar import Sidebar

button_style = """
    QPushButton {
        color: black;
        background-color: #c62c2c; 
        height: 45px; 
        font-size: 18px; 
        padding: 10px 20px; 
        border: 2px solid black;
    }
    QPushButton:pressed {
        background-color: #a52a2a;  /* Darker shade when pressed */
    }
"""
default_button_style = """
    QPushButton {
        color: black;
        font-size: 16px;
        height: 45px;
        border : none;
    }
"""
class HomePage(QWidget):
    def __init__(self, switch_to_home, switch_to_gallery,switch_to_convert,switch_to_settings,switch_to_profile,switch_to_sign_in):
        super().__init__()
        self.setWindowTitle("Image Converter App")
        self.setGeometry(100, 100, 1000, 800)
        self.switch_to_gallery = switch_to_gallery
        self.switch_to_home = switch_to_home
        self.switch_to_convert = switch_to_convert
        self.switch_to_settings = switch_to_settings
        self.switch_to_profile = switch_to_profile
        self.switch_to_sign_in = switch_to_sign_in
        
        # Main Layout
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Remove default margins
        
        
        self.sidebar = Sidebar(self.switch_to_home, self.switch_to_gallery, self.switch_to_convert, self.switch_to_settings,self.switch_to_profile,self.switch_to_sign_in, "Home") 
        self.sidebar.setFixedWidth(200)
        
        self.sidebar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        main_layout.addWidget(self.sidebar)
        
        # Main Content Layout
        # Content Wrapper
        content_wrapper = QWidget()
        content_layout = QVBoxLayout(content_wrapper)
        content_layout.setAlignment(Qt.AlignTop)
        content_layout.setContentsMargins(10, 20, 10, 10)  # Set top margin to 20 for some spacing
        
        # Convert Layout (20% height)
        convert_layout = QHBoxLayout()
        
        self.convert_text_label = QLabel("Start Converting by clicking the button")
        self.convert_button = QPushButton("CONVERT")
        
        # Apply CSS styling to the convert text and button
        self.convert_text_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        self.convert_button.setStyleSheet(button_style)
        
        self.convert_button_shadow = QGraphicsDropShadowEffect()
        self.convert_button_shadow.setOffset(2,2)
        self.convert_button_shadow.setColor(Qt.black)
        self.convert_button.setGraphicsEffect(self.convert_button_shadow)
        
        convert_layout.addWidget(self.convert_text_label)
        convert_layout.addWidget(self.convert_button)
        
        # Add the convert_layout inside a QWidget with a border
        convert_widget = QWidget()
        convert_widget.setLayout(convert_layout)
        content_layout.addWidget(convert_widget)
        content_layout.setStretchFactor(convert_widget, 1)  # 20% of the height
        
        # Add spacing after Convert Layout
        content_layout.addSpacing(20)  # Adds 20px of space
        
        # Trending Layout (60% height)
        trending_layout = QVBoxLayout()
        trending_layout.setAlignment(Qt.AlignTop)
        
        self.trending_text = QLabel("Top Trending Images")
        self.trending_text.setStyleSheet("font-size: 24px; font-weight: bold; color: #444; margin-bottom: 15px;")  # Increased font size
        trending_layout.addWidget(self.trending_text)
        
        # Create a scrollable area for the grid of images
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)  # Make the content inside scrollable
        # Apply the button style to the scroll bar of scrollArea
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
    }
""")

        grid_widget = QWidget(self)
        grid_layout = QGridLayout(grid_widget)  # Use QGridLayout for images



        # Array of image paths (increase the number of images for a larger grid)
        images = ["images/anime_style1.jpg", "images/anime_style1.jpg", "images/anime_style1.jpg", "images/anime_style1.jpg",
                "images/anime_style1.jpg", "images/anime_style1.jpg", "images/anime_style1.jpg", "images/anime_style1.jpg",
                "images/anime_style1.jpg", "images/anime_style1.jpg", "images/anime_style1.jpg", "images/anime_style1.jpg",
                "images/anime_style1.jpg", "images/anime_style1.jpg", "images/anime_style1.jpg", "images/anime_style1.jpg"]  # More images

        # Add images to the grid layout
        row = 0
        col = 0
        for image_path in images:
            pixmap = QPixmap(image_path)  # Load image
            pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio)  # Resize image
            
            image_label = QLabel(self)
            image_label.setPixmap(pixmap)
            image_label.setStyleSheet("border: 2px solid #ccc; padding: 5px;")  # Add border to the image
            # Create a frame for each image label to add border
            frame = QFrame(self)
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setFrameShadow(QFrame.Raised)
            frame_layout = QVBoxLayout(frame)
            frame_layout.setAlignment(Qt.AlignLeft)  # Center the content
            frame_layout.setContentsMargins(0, 0, 0, 0)  # No space around the layout
            frame_layout.setSpacing(0)  # No space between image and frame
            frame_layout.addWidget(image_label)
            frame.setLayout(frame_layout)
            
            grid_layout.addWidget(frame, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Set the grid layout inside the scrollable area
        scroll_area.setWidget(grid_widget)

        # Add the scroll_area to your trending layout
        trending_layout.addWidget(scroll_area)
        content_layout.addLayout(trending_layout)
        content_layout.setStretchFactor(trending_layout, 3)  # 60% of the height

        content_layout.addSpacing(20)  # Adds 20px of space
        
        # "How it works" section
        how_it_works_layout = QVBoxLayout()
        how_it_works_layout.setAlignment(Qt.AlignTop)
        
        # Heading
        how_it_works_heading = QLabel("How It Works")
        how_it_works_heading.setStyleSheet("font-size: 24px; font-weight: bold; color: #444; margin-bottom: 15px;")  # Increased font size
        how_it_works_layout.addWidget(how_it_works_heading)
        
        # Steps Layout (QHBoxLayout)
        steps_layout = QHBoxLayout()
        
        # Define the steps
        steps = [
            ("Step 1: Upload Image", "images/upload_icon.png"),
            ("Step 2: Select Style", "images/style_icon.png"),
            ("Step 3: Model Processes", "images/process_icon.png"),
            ("Step 4: Result is Shown", "images/result_icon.png")
        ]
        
        for step_text, icon_path in steps:
            step_box = QFrame(self)
            step_box.setStyleSheet("border: 2px solid #ccc; padding: 10px; margin-right: 10px;")
            step_layout = QVBoxLayout(step_box)
            
            step_icon = QLabel(self)
            step_icon.setPixmap(QPixmap(icon_path).scaled(40, 40, Qt.KeepAspectRatio))
            step_text_label = QLabel(step_text)
            step_text_label.setAlignment(Qt.AlignCenter)
            step_text_label.setStyleSheet("font-size: 12px; font-weight: bold; color: #333; margin-top: 5px;")
            
            step_layout.addWidget(step_icon, alignment=Qt.AlignCenter)
            step_layout.addWidget(step_text_label)
            steps_layout.addWidget(step_box)
        
        how_it_works_layout.addLayout(steps_layout)
        content_layout.addLayout(how_it_works_layout)

        # Final layout
        # content_frame = QFrame(self)
        # content_frame.setLayout(content_layout)
        # content_frame.setStyleSheet("background-color: #e8e8e8; padding: 10px;")
        # main_layout.addWidget(content_frame)
        main_layout.addWidget(content_wrapper)
        # main_layout.setStretch(1, 4)  # Sidebar takes less space, content takes more
