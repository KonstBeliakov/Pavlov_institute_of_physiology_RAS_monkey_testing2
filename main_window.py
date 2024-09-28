from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QComboBox

from experiment_settings_windows import ExperimentSettings1, ExperimentSettings2, ExperimentSettings3


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
        self.button.clicked.connect(self.on_button_click)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def on_button_click(self):
        match self.combo_box.currentText():
            case 'DNMS':
                self.experiment_window = ExperimentSettings1()
            case 'Extrapolation':
                self.experiment_window = ExperimentSettings2()
            case 'Memory volume':
                self.experiment_window = ExperimentSettings3()

        self.experiment_window.show()
