from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame,QSizePolicy,QGraphicsDropShadowEffect
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt, QSettings


button_style = """
    QPushButton {
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
        font-size: 16px;
        height: 45px;
        border: none;
    }
"""
class Sidebar(QWidget):
    def __init__(self,switch_to_home, switch_to_gallery,switch_to_convert,switch_to_settings,switch_to_profile,switch_to_sign_in, current_page):
        super().__init__()
        self.switch_to_gallery = switch_to_gallery
        self.switch_to_home = switch_to_home
        self.switch_to_convert = switch_to_convert
        self.switch_to_settings = switch_to_settings
        self.switch_to_profile = switch_to_profile
        self.switch_to_sign_in = switch_to_sign_in
        
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.current_page = current_page
        # Sidebar Layout
        sidebar_layout = QVBoxLayout(self)
        sidebar_layout.setSpacing(20)
        sidebar_layout.setAlignment(Qt.AlignTop)

        self.app_name = QLabel("Anime Style", self)
        self.app_name.setAlignment(Qt.AlignCenter)
        self.app_name.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px; color:black;")
        sidebar_layout.addWidget(self.app_name)
        buttons = [
            ("Home", "images/home_icon.png", self.switch_to_home,self.give_style("Home")),
            ("Gallery", "images/gallery_icon.png",self.switch_to_gallery,self.give_style("Gallery")),
            ("Convert", "images/convert_icon.png", self.switch_to_convert,self.give_style("Convert")),
            ("Settings", "images/settings_icon.png", self.switch_to_settings,self.give_style("Settings")),
        ]
        
        for btn_text, icon_path, switch_fn, btn_style in buttons:
            btn = QPushButton(self)
            btn.setIcon(QIcon(icon_path))  # Set icon for each button
            btn.setIconSize(QSize(20, 20))  # Adjust icon size
            btn.clicked.connect(switch_fn)
            btn.setStyleSheet(btn_style)  # Apply the button style to each
            btn.setFixedSize(60, 60)  # Button size to match icon size
            sidebar_layout.addWidget(btn, alignment=Qt.AlignCenter)  # Center-align buttons
            sidebar_layout.addStretch()

        sidebar_layout.addStretch()

        # Profile and Sign Out
        profile_btn = QPushButton("Profile", self)
        profile_btn.setFixedHeight(50)
        logout_btn = QPushButton("Sign Out", self)
        logout_btn.setFixedHeight(50)
        profile_btn.setStyleSheet("""
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
        """)
        profile_btn.clicked.connect(self.switch_to_profile)
        
        logout_btn.setStyleSheet("""
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
        """)
        
        self.logout_button_shadow = QGraphicsDropShadowEffect()
        self.logout_button_shadow.setOffset(2,2)
        self.logout_button_shadow.setColor(Qt.black)
        logout_btn.clicked.connect(self.handle_logout)
        logout_btn.setGraphicsEffect(self.logout_button_shadow)
        
        self.profile_button_shadow = QGraphicsDropShadowEffect()
        self.profile_button_shadow.setOffset(2,2)
        self.profile_button_shadow.setColor(Qt.black)
        profile_btn.setGraphicsEffect(self.profile_button_shadow)
        
        sidebar_layout.addWidget(profile_btn)
        sidebar_layout.addWidget(logout_btn)

        # Frame to hold the sidebar content
        sidebar_frame = QFrame(self)
        sidebar_frame.setLayout(sidebar_layout)
        sidebar_frame.setFixedWidth(200)
        sidebar_frame.setStyleSheet("background-color: #e8e8e8; padding: 10px;")

    def give_style(self, button_name):
        if button_name == self.current_page:
            return button_style
        return default_button_style
    
    def handle_logout(self):
        QSettings("AnimeStyle", "Pramod").clear()
        QSettings("AnimeStyle", "Pramod").sync()
        self.switch_to_sign_in()