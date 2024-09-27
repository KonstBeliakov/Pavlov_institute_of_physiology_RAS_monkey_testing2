from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

from experiment_settings import ExperimentSettings
from settings import *


class ExperimentSettings1(ExperimentSettings):
    def __init__(self):
        super().__init__(settings=Settings1)

        self.setWindowTitle('This is the experiment window')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel('Text', self)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    def on_button_click(self):
        self.label.setText('Button Clicked!')
