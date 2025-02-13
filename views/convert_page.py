from .sidebar import Sidebar
from PySide6.QtWidgets import (QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QComboBox, QFileDialog,QSizePolicy)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

button_stylesheet = """
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
convert_button_stylesheet = """
QPushButton {
    color: black;
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 1,
        stop: 0 #b03030, stop: 0.1 #a22222,
        stop: 0.2 #c03838, stop: 0.3 #a22222,
        stop: 0.4 #b03030, stop: 0.5 #a22222,
        stop: 0.6 #c03838, stop: 0.7 #a22222,
        stop: 0.8 #b03030, stop: 0.9 #a22222,
        stop: 1 #b03030
    );
    height: 45px;
    font-size: 18px;
    padding: 10px 20px;
    border: 2px solid black;
}

QPushButton:pressed {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 1,
        stop: 0 #8a1e1e, stop: 0.1 #7a1a1a,
        stop: 0.2 #9c2828, stop: 0.3 #7a1a1a,
        stop: 0.4 #8a1e1e, stop: 0.5 #7a1a1a,
        stop: 0.6 #9c2828, stop: 0.7 #7a1a1a,
        stop: 0.8 #8a1e1e, stop: 0.9 #7a1a1a,
        stop: 1 #8a1e1e
    );
}

"""
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
    def __init__(self, switch_to_home, switch_to_gallery, switch_to_convert, switch_to_settings, switch_to_profile,switch_to_sign_in, switch_to_processing_page):
        super().__init__()
        self.switch_to_gallery = switch_to_gallery
        self.switch_to_home = switch_to_home
        self.switch_to_convert = switch_to_convert
        self.switch_to_settings = switch_to_settings
        self.switch_to_profile = switch_to_profile
        self.switch_to_sign_in = switch_to_sign_in
        self.switch_to_processing_page = switch_to_processing_page

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
        
        image_layout = QHBoxLayout()
        content_image_layout = QVBoxLayout() 
        content_image_layout.setAlignment(Qt.AlignCenter)

        # Image display area (empty initially)
        self.content_image = QLabel()
        self.content_image.setAlignment(Qt.AlignCenter)
        self.content_image.setFixedSize(300, 300)  # Set a fixed size for the image label
        self.content_image.setStyleSheet("background-color: gray;")
        content_image_layout.addWidget(self.content_image)
        
        # Content Image Upload button
        self.content_upload_button = QPushButton("UPLOAD CONTENT IMAGE")
        self.content_upload_button.setStyleSheet(button_stylesheet)
        self.content_upload_button.clicked.connect(self.upload_content_image)
        content_image_layout.addWidget(self.content_upload_button)
        
        # Style Image Layout
        style_image_layout = QVBoxLayout()

        # Style Image upload button
        self.upload_style_button = QPushButton("UPLOAD STYLE IMAGE")
        self.upload_style_button.setStyleSheet(button_stylesheet)
        self.upload_style_button.setVisible(False)  # Hidden initially
        self.upload_style_button.clicked.connect(self.upload_style_image)

        # Style Image Display Area (Initially hidden)
        self.style_image_label = QLabel()
        self.style_image_label.setAlignment(Qt.AlignCenter)
        self.style_image_label.setFixedSize(300, 300)  
        self.style_image_label.setStyleSheet("background-color: gray;")
        self.style_image_label.setVisible(False)  # Hidden initially

        # Add the style image button and label to the style_image_layout
        style_image_layout.addWidget(self.style_image_label)
        style_image_layout.addWidget(self.upload_style_button)

        # Add the content image layout and style image layout to image layout
        image_layout.addLayout(content_image_layout)
        image_layout.addLayout(style_image_layout)

        # Add the image layout to image_button layout
        image_button_layout.addLayout(image_layout)

        # Convert button for converting the image
        self.convert_button = QPushButton("CONVERT")
        self.convert_button.setStyleSheet(convert_button_stylesheet)
        self.convert_button.clicked.connect(self.start_conversion)
        # Add the convert button to image_button layout
        image_button_layout.addWidget(self.convert_button)

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
        self.model_dropdown.addItems(["AnimeGanV2", "StyleDiffusion", "NST", "INST"])
        self.model_dropdown.setStyleSheet(dropdown_stylsheet)
        model_layout.addWidget(model_text)
        model_layout.addWidget(self.model_dropdown)
        self.model_dropdown.currentIndexChanged.connect(self.handle_model_change)
        
        dropdown_layout.addLayout(model_layout)

        # Add both the image_button_layout and dropdown_layout to the content_layout
        content_layout.addLayout(image_button_layout)
        content_layout.addSpacing(60)  # Space between the image_button_layout and dropdown_layout
        content_layout.addLayout(dropdown_layout)

        # Add the content wrapper to the main layout
        main_layout.addWidget(content_wrapper)

        # Connect the upload button to the method for image upload

     

    def upload_content_image(self, widget):
        # Open a file dialog to select an image
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")
        
        # Show the dialog and get the selected file path
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            
            # Load the image using QPixmap and display it in the QLabel
            pixmap = QPixmap(file_path)
            self.content_image.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))  # Resize image to fit label
    
    def upload_style_image(self, widget):
        # Open a file dialog to select an image
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")
        
        # Show the dialog and get the selected file path
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            
            # Load the image using QPixmap and display it in the QLabel
            pixmap = QPixmap(file_path)
            self.style_image_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))  # Resize image to fit label

    def handle_model_change(self):
        """ Show style image upload option for NST and INST models """
        selected_model = self.model_dropdown.currentText()
        
        if selected_model in ["NST", "INST"]:
            self.upload_style_button.setVisible(True)
            self.style_image_label.setVisible(True)
        else:
            self.upload_style_button.setVisible(False)
            self.style_image_label.setVisible(False)

    def start_conversion(self):
        self.switch_to_processing_page()  # Navigate to ProcessingPage