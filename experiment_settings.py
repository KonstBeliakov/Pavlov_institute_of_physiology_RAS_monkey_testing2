from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout

from settings import Settings


class ExperimentSettings(QWidget):
    def __init__(self, settings: Settings):
        super().__init__()
        self.settings = settings

    def save_settings(self, filename=None):
        self.settings.save(filename)

    def load_settings(self, filename=None):
        self.settings.load(filename)
