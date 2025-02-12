# main.py
import sys
from PySide6.QtWidgets import QApplication, QStackedWidget
from views.register_page import RegisterPage
from views.sign_in_page import SignInPage
from views.home_page import HomePage
from views.gallery_page import GalleryPage
from views.convert_page import ConvertPage
from views.settings_page import SettingsPage
from views.profile_page import UserProfilePage
from PySide6.QtCore import QSettings

class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.showFullScreen()
        # Create RegisterPage and SignInPage
        self.register_page = RegisterPage(self.switch_to_sign_in)
        self.sign_in_page = SignInPage(self.switch_to_register, self.switch_to_home)
        self.home_page = HomePage(self.switch_to_home,self.switch_to_gallery,self.switch_to_convert, self.switch_to_settings,self.switch_to_profile,self.switch_to_sign_in)
        self.gallery_page = GalleryPage(self.switch_to_home,self.switch_to_gallery,self.switch_to_convert, self.switch_to_settings, self.switch_to_profile,self.switch_to_sign_in)
        self.convert_page = ConvertPage(self.switch_to_home,self.switch_to_gallery,self.switch_to_convert, self.switch_to_settings, self.switch_to_profile,self.switch_to_sign_in)
        self.settings_page = SettingsPage(self.switch_to_home,self.switch_to_gallery,self.switch_to_convert, self.switch_to_settings, self.switch_to_profile,self.switch_to_sign_in)
        self.profile_page = UserProfilePage(self.switch_to_home,self.switch_to_gallery,self.switch_to_convert, self.switch_to_settings, self.switch_to_profile,self.switch_to_sign_in)
        
        # Add pages to the stacked widget
        self.addWidget(self.register_page)
        self.addWidget(self.sign_in_page)
        self.addWidget(self.home_page)
        self.addWidget(self.gallery_page)
        self.addWidget(self.convert_page)
        self.addWidget(self.settings_page)
        self.addWidget(self.profile_page)

        # Show RegisterPage by default
        print(QSettings("AnimeStyle","Pramod").value("login_state", "True"))
        login_state = QSettings("AnimeStyle", "Pramod").value("login_state", False, type=bool)

        if login_state:
            self.setCurrentWidget(self.home_page)
        else:
            self.setCurrentWidget(self.register_page)

        
        self.setStyleSheet("background-color: white;")

    def switch_to_sign_in(self):
        self.setCurrentWidget(self.sign_in_page)

    def switch_to_register(self):
        self.setCurrentWidget(self.register_page)
    
    def switch_to_home(self):
        self.setCurrentWidget(self.home_page)
    
    def switch_to_gallery(self):
        self.setCurrentWidget(self.gallery_page)
    
    def switch_to_convert(self):
        self.setCurrentWidget(self.convert_page)
    
    def switch_to_settings(self):
        self.setCurrentWidget(self.settings_page)
    
    def switch_to_profile(self):
        self.setCurrentWidget(self.profile_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and show the main window with the stacked widget
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
