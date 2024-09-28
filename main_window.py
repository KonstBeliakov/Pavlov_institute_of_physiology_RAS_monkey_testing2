import threading

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QComboBox

from experiment_settings_windows import *
from experiment_windows import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Simple PyQt5 Application')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.combo_box = QComboBox(self)
        self.combo_box.addItems(["DNMS", "Extrapolation", "Memory volume"])
        self.layout.addWidget(self.combo_box)

        self.button = QPushButton('Open settings window', self)
        self.button.clicked.connect(self.open_experiment_settings)
        self.layout.addWidget(self.button)

        self.button_start = QPushButton('Start chosen experiment', self)
        self.button_start.clicked.connect(self.start_experiment)
        self.layout.addWidget(self.button_start)

        self.setLayout(self.layout)

    def start_experiment(self):
        match self.combo_box.currentText():
            case 'DNMS':
                self.experiment_window = ExperimentWindow1()
            case 'Extrapolation':
                self.experiment_window = ExperimentWindow2()
            case 'Memory volume':
                self.experiment_window = ExperimentWindow3()

        t1 = threading.Thread(target=self.experiment_window.main_loop)
        t1.start()

    def open_experiment_settings(self):
        match self.combo_box.currentText():
            case 'DNMS':
                self.experiment_settings_window = ExperimentSettings1()
            case 'Extrapolation':
                self.experiment_settings_window = ExperimentSettings2()
            case 'Memory volume':
                self.experiment_settings_window = ExperimentSettings3()

        self.experiment_settings_window.show()
