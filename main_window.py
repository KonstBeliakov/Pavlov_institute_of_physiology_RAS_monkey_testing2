from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout

from experiment_settings1 import ExperimentSettings1


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Simple PyQt5 Application')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel('Hello, click the button!', self)
        self.layout.addWidget(self.label)

        self.button = QPushButton('Click Me', self)
        self.button.clicked.connect(self.on_button_click)  # Connect button click to method
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def on_button_click(self):
        self.label.setText('Button Clicked!')
        self.experiment_window = ExperimentSettings1()
        self.experiment_window.show()
