from dataclasses import astuple, asdict

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QComboBox, QLineEdit, QRadioButton

from settings import Settings


class ExperimentSettings(QWidget):
    def __init__(self, settings: Settings):
        super().__init__()
        self.settings = settings

        self.layout = QVBoxLayout()

        for attr, value in asdict(self.settings).items():
            self.label = QLabel(str(attr), self)
            self.layout.addWidget(self.label)

            self.line_edit = QLineEdit(self)
            self.layout.addWidget(self.line_edit)

        self.setLayout(self.layout)

        self.button_apply = QPushButton("OK", self)
        self.button_apply.clicked.connect(self.save_settings)
        self.layout.addWidget(self.button_apply)

    def save_settings(self, filename=None):
        self.settings.save(filename)

    def load_settings(self, filename=None):
        self.settings.load(filename)
