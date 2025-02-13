from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QFrame, QSizePolicy, QSpacerItem, QGraphicsDropShadowEffect,QMessageBox
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QSettings
from db.database import Database

class SignInPage(QWidget):
    def __init__(self, switch_to_register_callback, switch_to_home_callback):
        super().__init__()
        self.setWindowTitle("Sign In")
        self.showFullScreen()  # Full-screen window
        self.switch_to_register_callback = switch_to_register_callback
        self.switch_to_home_callback = switch_to_home_callback
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: white;")
        # Main Layout (Splitting Left & Right)
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Left Side - Empty Frame (Takes Half the Space)
        left_frame = QFrame(self)
        left_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        left_frame.setStyleSheet('''
                           padding: 0;
                           margin: 0;
                           background-image: url("images/login_bg.jpg");
                           background-repeat: none;
                           background-size: cover;
                           background-position: bottom;
                           ''')
        # Right Side - Form Section
        right_frame = QFrame(self)
        right_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        form_layout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignCenter)  
        form_layout.setSpacing(30)  # Sets equal spacing between all elements

        title = QLabel("Sign In")
        title.setFont(QFont("Arial", 36, QFont.Bold))
        title.setAlignment(Qt.AlignLeft)
        title.setStyleSheet("""
                            color: #3f0106;
                            """)
        
        # Customizing Line Edits
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

        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setFixedHeight(50)  # Increase height
        self.email_input.setFixedWidth(600)
        self.email_input.setStyleSheet(line_edit_style)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(50)  # Increase height
        self.password_input.setFixedWidth(600)
        self.password_input.setStyleSheet(line_edit_style)
        
        # Buttons in Horizontal Layout
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignLeft)
        self.signin_button = QPushButton("SIGN IN")
        self.signin_button.setFixedWidth(300)  
        self.signin_button.setStyleSheet("""
    QPushButton {
        color: black;
        background-color: #c62c2c; 
        height: 45px; 
        font-size: 18px; 
        padding: 10px 20px;
        border: 2px solid black;
    }
    QPushButton:pressed {
        background-color: #a52a2a;  /* Slightly darker gray when pressed */
    }
""")
        
        self.register_button = QPushButton("REGISTER")
        self.register_button.setFixedWidth(300)  # Adjust width
        self.register_button.setStyleSheet("""
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
""")
        

        # Apply shadow effect to buttons
        self.register_button_shadow = QGraphicsDropShadowEffect()
        self.register_button_shadow.setOffset(2,2)
        self.register_button_shadow.setColor(Qt.black)
        self.register_button.setGraphicsEffect(self.register_button_shadow)
        self.register_button.clicked.connect(self.switch_to_register_callback)    
        
        self.signin_button_shadow = QGraphicsDropShadowEffect()
        self.signin_button_shadow.setOffset(2,2)
        self.signin_button_shadow.setColor(Qt.black)
        self.signin_button.setGraphicsEffect(self.signin_button_shadow)    
        self.signin_button.clicked.connect(self.handle_login)

        button_layout.addWidget(self.signin_button)
        button_layout.addWidget(self.register_button)


        # Adding a Spacer at the Top for Extra Padding
        form_layout.addItem(QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Adding Elements to the Layout
        form_layout.addWidget(title)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.password_input)

        # Adding a Spacer Between Inputs and Buttons
        form_layout.addItem(QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Add Button Layout (Side by Side)
        form_layout.addLayout(button_layout)

        # Adding a Spacer at the Bottom for Extra Padding
        form_layout.addItem(QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        right_frame.setLayout(form_layout)

        # Adding Frames to the Main Layout
        main_layout.addWidget(left_frame)  # Empty Left Side
        main_layout.addWidget(right_frame)  # Form on Right Side

        self.setLayout(main_layout)
    def save_login_state(self, username, email):
        settings = QSettings("AnimeStyle", "Pramod")
        settings.setValue("username", username)
        settings.setValue("email", email)
        settings.setValue("login_state", "True")
        settings.sync()

    
    def handle_login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        db = Database()
        valid, user = db.validate_login(email, password)
        print(user)
        if valid:
            print("Logged in successfully")
            QMessageBox.information(self, "Success", "Logged in successfully")
            self.save_login_state(user['username'], user['email'])
            
            self.switch_to_home_callback()
        else:
            print("Invalid credentials")
            QMessageBox.critical(self, "Error", "Invalid credentials")
