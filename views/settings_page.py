from .sidebar import Sidebar
from PySide6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QGraphicsDropShadowEffect,
    QComboBox, QSpinBox, QCheckBox
)
from PySide6.QtCore import Qt

class SettingsPage(QWidget):
    def __init__(self, switch_to_home, switch_to_gallery, switch_to_convert, switch_to_settings, switch_to_profile,switch_to_sign_in):
        super().__init__()
        self.switch_to_gallery = switch_to_gallery
        self.switch_to_home = switch_to_home
        self.switch_to_convert = switch_to_convert
        self.switch_to_settings = switch_to_settings
        self.switch_to_profile = switch_to_profile
        self.switch_to_sign_in = switch_to_sign_in
        
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Sidebar
        self.sidebar = Sidebar(self.switch_to_home, self.switch_to_gallery, self.switch_to_convert, self.switch_to_settings, self.switch_to_profile,self.switch_to_sign_in, "Settings")
        self.sidebar.setFixedWidth(200)
        main_layout.addWidget(self.sidebar)

        # Content Wrapper for Settings
        content_wrapper = QWidget()
        content_layout = QVBoxLayout(content_wrapper)
        content_layout.setAlignment(Qt.AlignTop)
        content_layout.setContentsMargins(10, 20, 10, 10)
        # Title
        title_label = QLabel("Settings")
        title_label.setStyleSheet("font-size: 36px; font-weight: bold; color: #333;")

        # Model Selection
        model_label = QLabel("Select AI Model:")
        self.model_dropdown = QComboBox()
        self.model_dropdown.addItems(["AnimeGANv2", "StyleGAN", "DeepAnime"])
        self.model_dropdown.setStyleSheet(self.combo_style)

        # Style Selection
        style_label = QLabel("Anime Style:")
        self.style_dropdown = QComboBox()
        self.style_dropdown.addItems(["Classic", "Modern", "Watercolor", "Sketch"])
        self.style_dropdown.setStyleSheet(self.combo_style)

        # Output Resolution
        resolution_label = QLabel("Output Resolution (px):")
        self.resolution_box = QSpinBox()
        self.resolution_box.setRange(256, 4096)
        self.resolution_box.setValue(1024)
        self.resolution_box.setStyleSheet(self.spin_style)

        # Storage Option
        self.storage_checkbox = QCheckBox("Save images automatically")
        self.storage_checkbox.setStyleSheet(self.checkbox_style)

        # Theme Selection
        self.theme_checkbox = QCheckBox("Enable Dark Mode")
        self.theme_checkbox.setStyleSheet(self.checkbox_style)

        # Reset Button
        reset_button = QPushButton("Reset to Defaults")
        reset_button.setStyleSheet(self.button_style)
        reset_button.clicked.connect(self.reset_settings)
        
        self.reset_button_shadow = QGraphicsDropShadowEffect()
        self.reset_button_shadow.setOffset(2,2)
        self.reset_button_shadow.setColor(Qt.black)
        reset_button.setGraphicsEffect(self.reset_button_shadow)

        # Add widgets to layout
        content_layout.addWidget(title_label)
        content_layout.addWidget(model_label)
        content_layout.addWidget(self.model_dropdown)
        content_layout.addWidget(style_label)
        content_layout.addWidget(self.style_dropdown)
        content_layout.addWidget(resolution_label)
        content_layout.addWidget(self.resolution_box)
        content_layout.addWidget(self.storage_checkbox)
        content_layout.addWidget(self.theme_checkbox)
        content_layout.addWidget(reset_button)

        main_layout.addWidget(content_wrapper)
        main_layout.setStretch(1, 4)  # Content takes more space

    def reset_settings(self):
        """Reset settings to default values."""
        self.model_dropdown.setCurrentIndex(0)
        self.style_dropdown.setCurrentIndex(0)
        self.resolution_box.setValue(1024)
        self.storage_checkbox.setChecked(False)
        self.theme_checkbox.setChecked(False)

    # Button Style
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

    # ComboBox Style (Background color of dropdown changed)
    combo_style = """
        QComboBox {
            height: 35px;
            font-size: 16px;
            padding: 5px;
            border: 1px solid #c62c2c;
            background-color: #f1f1f1;  /* Light background for combobox */
        }
        QComboBox::drop-down {
            background-color: #c62c2c;  /* Dropdown background color */
            border: none;
        }
        QComboBox QAbstractItemView {
            background-color: #f1f1f1;  /* Dropdown item background */
            selection-background-color: #c62c2c;
        }
        QComboBox QAbstractItemView::item:hover {
        background-color: #c62c2c;  /* Change background when hovering over an item */
        color: black;  /* Change text color when hovering */
        border: 1px solid black;
    }
    """

    # SpinBox Style
    spin_style = """
        QSpinBox {
            height: 35px;
            font-size: 16px;
            padding: 5px;
            border: 1px solid #c62c2c;
        }
    """

    # CheckBox Style
    checkbox_style = """
        QCheckBox {
            font-size: 16px;
            color: #333;
            padding: 5px;
        }
        QCheckBox::indicator {
            width: 20px;
            height: 20px;
        }
        QCheckBox::indicator:checked {
            background-color: #c62c2c;
        }
    """
