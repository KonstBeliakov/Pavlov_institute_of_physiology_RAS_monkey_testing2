import sys
from copy import deepcopy
from dataclasses import astuple, asdict

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QComboBox, QLineEdit, QRadioButton, QApplication, \
    QHBoxLayout, QMainWindow, QFileDialog, QGridLayout

import settings
from settings import Settings, Settings1, Settings2, Settings3, CommonSettings


class ExperimentSettings(QMainWindow):
    def __init__(self, settings: Settings):
        super().__init__()
        self.settings = settings

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()

        self.line_edit = []

        grid_layout = QGridLayout()

        for i, (attr, value) in enumerate(asdict(self.settings).items()):
            if str(attr) in self.settings.settings_names:
                self.label = QLabel(self.settings.settings_names[str(attr)], self)
                grid_layout.addWidget(self.label, i, 0)

                self.line_edit.append(QLineEdit(self))
                grid_layout.addWidget(self.line_edit[-1], i, 1)

        self.main_layout.addLayout(grid_layout)

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
        print('apply settings method was called')
        for i, (attr, value) in enumerate(asdict(self.settings).items()):
            # Should check type of value and transform string to it somehow
            self.settings.__dict__[attr] = self.line_edit[i].text()
            # break the for loop if values are wrong
        else:
            match type(self.settings):
                case settings.Settings1:
                    settings.current_settings1 = deepcopy(self.settings)
                case settings.Settings2:
                    settings.current_settings2 = deepcopy(self.settings)
                case settings.Settings3:
                    settings.current_settings3 = deepcopy(self.settings)
                case settings.CommonSettings:
                    settings.current_common_settings = deepcopy(self.settings)

    def update_data(self):
        items_with_descriptions = [(i, j) for i, j in asdict(self.settings).items() if str(i) in self.settings.settings_names]
        for i, (attr, value) in enumerate(items_with_descriptions):
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