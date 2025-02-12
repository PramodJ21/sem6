import sys
from PySide6.QtCore import Qt, QSettings
from PySide6.QtWidgets import QGraphicsDropShadowEffect,QSizePolicy, QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QGroupBox, QPushButton, QHBoxLayout,QFileDialog
from PySide6.QtGui import QIcon,QPixmap,QBrush,QPainter,QPalette
from .sidebar import Sidebar

line_edit_style = """
            QLineEdit {
                background-color: #f3f3f3; /* White background */
                color: black; /* Dark gray text */
                padding: 10px; /* Padding inside the line edit */
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #000; /* Purple border when focused */
            }
           
        """
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

alt_button_style = """
    QPushButton {
    color: black;
        background-color: white; 
        height: 45px; 
        font-size: 18px; 
        padding: 10px 20px; 
        border: 2px solid black;
    }
    QPushButton:pressed {
        background-color: #f0f0f0;  /* Darker shade when pressed */
    }
"""    
class UserProfilePage(QWidget):
    def __init__(self, switch_to_home, switch_to_gallery, switch_to_convert, switch_to_settings, switch_to_profile,switch_to_sign_in):
        super().__init__()

        self.setWindowTitle("User Profile")
        self.setWindowIcon(QIcon("app_icon.png"))  # Add your icon if available
        
        self.switch_to_gallery = switch_to_gallery
        self.switch_to_home = switch_to_home
        self.switch_to_convert = switch_to_convert
        self.switch_to_settings = switch_to_settings
        self.switch_to_profile = switch_to_profile
        self.switch_to_sign_in = switch_to_sign_in
        # Main layout
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Sidebar (assuming Sidebar is imported and implemented in sidebar.py)
        self.sidebar = Sidebar(self.switch_to_home, self.switch_to_gallery, self.switch_to_convert, self.switch_to_settings, self.switch_to_profile,self.switch_to_sign_in, "Profile")
        self.sidebar.setFixedWidth(200)
        main_layout.addWidget(self.sidebar)
        
        # Content Layout for Profile Page
        content_wrapper = QWidget()
        content_layout = QVBoxLayout(content_wrapper)
        content_layout.setAlignment(Qt.AlignCenter)  # Center align the entire content
        content_layout.setSpacing(50)
        
        palette = QPalette()
        background = QPixmap("./images/cover_img.jpg").scaled(content_wrapper.size())  # Scale to fit
        palette.setBrush(QPalette.Window, QBrush(background))
        content_wrapper.setPalette(palette)


        # Profile Image Label
        user_img_wrapper = QWidget()
        user_img_layout = QVBoxLayout(user_img_wrapper)
        self.user_img_label = QLabel("Profile Image")
        self.user_img_label.setFixedSize(250, 250)  # Increased size
        self.user_img_label.setStyleSheet("background-color: grey; border-radius: 125px")  # Added border and adjusted style
        self.user_img_label.setAlignment(Qt.AlignCenter)
        
        # Upload image button
        self.upload_button = QPushButton("UPLOAD")
        self.upload_button.setFixedWidth(200)  # Increased button width
        self.upload_button.setFixedHeight(50)  # Increased button height
        self.upload_button.setStyleSheet(button_style)  # Added background color and rounded corners
        self.upload_button.clicked.connect(self.upload_image)
        
        self.upload_button_shadow = QGraphicsDropShadowEffect()
        self.upload_button_shadow.setOffset(2,2)
        self.upload_button_shadow.setColor(Qt.black)
        self.upload_button.setGraphicsEffect(self.upload_button_shadow)
        
        # Ensuring the label itself is centered
        user_img_layout.addWidget(self.user_img_label, alignment=Qt.AlignCenter)
        user_img_layout.addWidget(self.upload_button, alignment=Qt.AlignCenter)
        user_img_layout.setSpacing(20)
        content_layout.addWidget(user_img_wrapper)

        # Input Section (Centered)
        input_wrapper = QWidget()
        input_wrapper.setFixedWidth(1200)  # Increased width
        input_layout = QVBoxLayout(input_wrapper)
        input_layout.setAlignment(Qt.AlignCenter)  # Center align input section
        
        username_layout = QHBoxLayout()
        username_layout.setAlignment(Qt.AlignCenter)
        username_text = QLabel("Enter username: ")
        username_text.setFixedWidth(120)  # Increased width
        username_text.setStyleSheet("padding: 5px; font-size: 16px;")
        username_input = QLineEdit()
        username_input.setText(QSettings().value("username", ""))
        username_input.setFixedWidth(400)  # Increased width
        username_input.setStyleSheet(line_edit_style)  # Added padding and border
        username_layout.addWidget(username_text)
        username_layout.addWidget(username_input)
        input_layout.addLayout(username_layout)
        
        email_layout = QHBoxLayout()
        email_layout.setAlignment(Qt.AlignCenter)
        email_text = QLabel("Enter Email: ")
        email_text.setFixedWidth(120)  # Increased width
        email_text.setStyleSheet("padding: 5px; font-size: 16px;")
        email_input = QLineEdit()
        email_input.setText(QSettings().value("email", ""))
        email_input.setFixedWidth(400)  # Increased width
        email_input.setStyleSheet(line_edit_style)  # Added padding and border
        email_layout.addWidget(email_text)
        email_layout.addWidget(email_input)
        input_layout.addLayout(email_layout)
        
        # password_layout = QHBoxLayout()
        # password_layout.setAlignment(Qt.AlignCenter)
        # password_text = QLabel("Enter Password: ")
        # password_text.setFixedWidth(120)  # Increased width
        # password_text.setStyleSheet("padding: 5px; font-size: 16px;")
        # password_input = QLineEdit()
        # password_input.setFixedWidth(400)  # Increased width
        # password_input.setStyleSheet(line_edit_style)  # Added padding and border
        # password_layout.addWidget(password_text)
        # password_layout.addWidget(password_input)
        # input_layout.addLayout(password_layout)
        
        content_layout.addWidget(input_wrapper)
        
        # Centering the update button using a horizontal layout
        update_button_layout = QHBoxLayout()
        update_button_layout.setAlignment(Qt.AlignCenter)  # Center the button
        
        update_button = QPushButton("UPDATE")
        update_button.setFixedWidth(250)  # Increased button width
        update_button.setFixedHeight(50)  # Increased button height
        update_button.setStyleSheet(button_style)  # Added background color and rounded corners
        
        self.update_button_shadow = QGraphicsDropShadowEffect()
        self.update_button_shadow.setOffset(2,2)
        self.update_button_shadow.setColor(Qt.black)
        update_button.setGraphicsEffect(self.update_button_shadow)
        
        discard_button = QPushButton("DISCARD")
        discard_button.setFixedWidth(250)  # Increased button width
        discard_button.setFixedHeight(50)  # Increased button height
        discard_button.setStyleSheet(alt_button_style)  # Added background color and rounded corners
        
        self.discard_button_shadow = QGraphicsDropShadowEffect()
        self.discard_button_shadow.setOffset(2,2)
        self.discard_button_shadow.setColor(Qt.black)
        discard_button.setGraphicsEffect(self.discard_button_shadow)
        
        update_button_layout.addWidget(update_button)
        update_button_layout.addWidget(discard_button)
        content_layout.addLayout(update_button_layout)
        
        main_layout.addWidget(content_wrapper)

    def upload_image(self):
        # Open file dialog to select an image
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileusername(self, "Select Profile Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")

        if file_path:  # If a file is selected
            pixmap = QPixmap(file_path)
            pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Scale image
            
            # Apply a circular mask to make the image round
            circular_pixmap = self.make_circle_pixmap(pixmap)
            
            # Set the processed circular image to QLabel
            self.user_img_label.setPixmap(circular_pixmap)

    def make_circle_pixmap(self, pixmap):
        """Creates a circular cropped version of the given QPixmap"""
        size = min(pixmap.width(), pixmap.height())  # Ensure it's a square crop
        cropped_pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        circular_pixmap = QPixmap(size, size)
        circular_pixmap.fill(Qt.transparent)  # Transparent background

        painter = QPainter(circular_pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)

        brush = QBrush(cropped_pixmap)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        # Draw a circular clip
        painter.drawEllipse(0, 0, size, size)
        painter.end()

        return circular_pixmap