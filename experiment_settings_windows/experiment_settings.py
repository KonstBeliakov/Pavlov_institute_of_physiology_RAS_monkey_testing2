import sys
from dataclasses import astuple, asdict

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QComboBox, QLineEdit, QRadioButton, QApplication, \
    QHBoxLayout, QMainWindow, QFileDialog

from settings import Settings, Settings1


class ExperimentSettings(QMainWindow):
    def __init__(self, settings: Settings):
        super().__init__()
        self.settings = settings

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()

        self.line_edit = []

        for attr, value in asdict(self.settings).items():
            self.label = QLabel(str(attr), self)
            self.main_layout.addWidget(self.label)

            self.line_edit.append(QLineEdit(self))
            self.main_layout.addWidget(self.line_edit[-1])

        self.update_data()

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

    def update_data(self):
        for i, (attr, value) in enumerate(asdict(self.settings).items()):
            self.line_edit[i].setText(str(value))

    def import_settings(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Открыть файл",
                                                  "",
                                                  "Все файлы (*.*);;Текстовые файлы (*.txt)",
                                                  options=options)
        self.load_settings(filename)
        self.update_data()

    def export_settings(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self,
                                                  "Сохранить файл как",
                                                  "",
                                                  "Текстовые файлы (*.txt);;Все файлы (*.*)",
                                                  options=options)
        self.save_settings(filename=filename)

    def save_settings(self, filename=None):
        self.settings.save(filename)

    def load_settings(self, filename=None):
        self.settings.load(filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExperimentSettings(settings=Settings1())
    window.show()
    sys.exit(app.exec_())
