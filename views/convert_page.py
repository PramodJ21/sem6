from .sidebar import Sidebar
from PySide6.QtWidgets import (QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QComboBox, QFileDialog,QSizePolicy)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

dropdown_stylsheet = """
    QComboBox {
        background-color: #f0f0f0;
        color: #333;
        font-size: 14px;
        padding: 5px;
        border: 1px solid #ccc;
    }
    QComboBox::drop-down {
        background-color: #f0f0f0;
    }
    QComboBox::down-arrow {
        image: url('down_arrow.png');
    }
    QComboBox QAbstractItemView {
        background-color: #f0f0f0;
        color: #333;
        border: 1px solid #ccc;
    }
    QComboBox QAbstractItemView::item:hover {
        background-color: #c62c2c;  /* Change background when hovering over an item */
        color: black;  /* Change text color when hovering */
        border: 1px solid black;
    }
    QComboBox QAbstractItemView::item:selected {
        background-color: #c62c2c;  /* Background when an item is selected */
        color: white;  /* Change text color when selected */
    }
"""
class ConvertPage(QWidget):
    def __init__(self, switch_to_home, switch_to_gallery, switch_to_convert, switch_to_settings, switch_to_profile,switch_to_sign_in):
        super().__init__()
        self.switch_to_gallery = switch_to_gallery
        self.switch_to_home = switch_to_home
        self.switch_to_convert = switch_to_convert
        self.switch_to_settings = switch_to_settings
        self.switch_to_profile = switch_to_profile
        self.switch_to_sign_in = switch_to_sign_in
        
        main_layout = QHBoxLayout(self)
        main_layout.setAlignment(Qt.AlignLeft)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.sidebar = Sidebar(self.switch_to_home, self.switch_to_gallery, self.switch_to_convert, self.switch_to_settings,self.switch_to_profile,self.switch_to_sign_in, "Convert")
        self.sidebar.setFixedWidth(200)
        main_layout.addWidget(self.sidebar)

        # Vertical layout for the convert page content
        content_wrapper = QWidget()
        content_wrapper.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        content_layout = QVBoxLayout(content_wrapper)
        content_layout.setSpacing(20)  # Set spacing between sections
        
        # Heading with bigger and bold font
        convert_text = QLabel("Turn anything into Anime !!!")
        convert_text.setStyleSheet("""
            font-size: 30px;
            font-weight: bold;
            color: #333;
        """)
        content_layout.addWidget(convert_text)
        content_layout.setAlignment(Qt.AlignCenter)
        
        # Create a layout for the image and buttons
        image_button_layout = QVBoxLayout()
        image_button_layout.setAlignment(Qt.AlignCenter)
        image_button_layout.setSpacing(20)  # Set spacing between image and buttons
        
        # Image display area (empty initially)
        self.user_image = QLabel()
        self.user_image.setAlignment(Qt.AlignCenter)
        self.user_image.setFixedSize(400, 400)  # Set a fixed size for the image label
        self.user_image.setStyleSheet("background-color: gray;")
        
        # Set a placeholder image for the image label (before user uploads anything)
        placeholder_pixmap = QPixmap("placeholder.png")
        self.user_image.setPixmap(placeholder_pixmap.scaled(400, 400, Qt.KeepAspectRatio))
        
        image_button_layout.addWidget(self.user_image)
        
        # Upload and Convert buttons side by side
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)  # Add spacing between buttons
        
        # Apply consistent button style
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
                background-color: #a52a2a;
            }
        """
        
        self.upload_button = QPushButton("UPLOAD")
        self.convert_button = QPushButton("CONVERT")
        
        self.upload_button.setStyleSheet(button_style)
        self.convert_button.setStyleSheet(button_style)
        
        button_layout.addWidget(self.upload_button)
        button_layout.addWidget(self.convert_button)
        
        image_button_layout.addLayout(button_layout)
        
        # Create a layout for the dropdowns (style, images, model)
        dropdown_layout = QVBoxLayout()
        dropdown_layout.setSpacing(15)  # Set spacing between the dropdowns

        # Select Style
        style_layout = QHBoxLayout()
        style_layout.setSpacing(15)
        style_text = QLabel("Select Style: ")
        style_text.setStyleSheet("""
            font-size: 14px;
            font-weight: bold;
            color: #333;
        """)
        self.style_dropdown = QComboBox()
        self.style_dropdown.addItems(["Manga", "Shonen", "Seinen", "Kawaii"])
        self.style_dropdown.setStyleSheet(dropdown_stylsheet)

        style_layout.addWidget(style_text)
        style_layout.addWidget(self.style_dropdown)
        
        dropdown_layout.addLayout(style_layout)
        dropdown_layout.setSpacing(60)
        
        # Select No of Images
        images_layout = QHBoxLayout()
        images_layout.setSpacing(15)
        images_text = QLabel("Select No of Images: ")
        images_text.setStyleSheet("""
            font-size: 14px;
            font-weight: bold;
            color: #333;
        """)
        self.images_dropdown = QComboBox()
        self.images_dropdown.addItems([str(i) for i in range(1, 11)])
        self.images_dropdown.setStyleSheet(dropdown_stylsheet)
        images_layout.addWidget(images_text)
        images_layout.addWidget(self.images_dropdown)
        
        dropdown_layout.addLayout(images_layout)
        
        # Select Model
        model_layout = QHBoxLayout()
        model_layout.setSpacing(15)
        model_text = QLabel("Select model: ")
        model_text.setStyleSheet("""
            font-size: 14px;
            font-weight: bold;
            color: #333;
        """)
        self.model_dropdown = QComboBox()
        self.model_dropdown.addItems(["Model A", "Model B", "Model C", "Model D"])
        self.model_dropdown.setStyleSheet(dropdown_stylsheet)
        model_layout.addWidget(model_text)
        model_layout.addWidget(self.model_dropdown)
        
        dropdown_layout.addLayout(model_layout)

        # Add both the image_button_layout and dropdown_layout to the content_layout
        content_layout.addLayout(image_button_layout)
        content_layout.addSpacing(60)  # Space between the image_button_layout and dropdown_layout
        content_layout.addLayout(dropdown_layout)

        # Add the content wrapper to the main layout
        main_layout.addWidget(content_wrapper)

        # Connect the upload button to the method for image upload
        self.upload_button.clicked.connect(self.upload_image)

    def upload_image(self):
        # Open a file dialog to select an image
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")
        
        # Show the dialog and get the selected file path
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            
            # Load the image using QPixmap and display it in the QLabel
            pixmap = QPixmap(file_path)
            self.user_image.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))  # Resize image to fit label
