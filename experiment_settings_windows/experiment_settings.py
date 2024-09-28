import sys
from dataclasses import astuple, asdict

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QComboBox, QLineEdit, QRadioButton, QApplication, \
    QHBoxLayout, QMainWindow

from settings import Settings, Settings1


class ExperimentSettings(QMainWindow):
    def __init__(self, settings: Settings):
        super().__init__()
        self.settings = settings

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()

        for attr, value in asdict(self.settings).items():
            self.label = QLabel(str(attr), self)
            self.main_layout.addWidget(self.label)

            self.line_edit = QLineEdit(self)
            self.main_layout.addWidget(self.line_edit)

        button_layout = QHBoxLayout()

        self.button_apply = QPushButton("Apply", self)
        self.button_apply.clicked.connect(self.apply_settings)

        self.button_cancel = QPushButton("Cancel", self)
        self.button_cancel.clicked.connect(self.cancel)

        self.button_import = QPushButton("Import", self)
        self.button_import.clicked.connect(self.import_settings)

        self.button_export = QPushButton("Export", self)
        self.button_export.clicked.connect(self.export_settings)

        for button in self.button_apply, self.button_cancel, self.button_import, self.button_export:
            button_layout.addWidget(button)

        self.main_layout.addLayout(button_layout)

        central_widget.setLayout(self.main_layout)

    def cancel(self):
        self.close()

    def apply_settings(self):
        pass

    def import_settings(self):
        pass

    def export_settings(self):
        pass

    def save_settings(self, filename=None):
        self.settings.save(filename)

    def load_settings(self, filename=None):
        self.settings.load(filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExperimentSettings(settings=Settings1())
    window.show()
    sys.exit(app.exec_())