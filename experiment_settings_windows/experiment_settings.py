import sys
from copy import deepcopy
from dataclasses import asdict
from typing import Any, Optional

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QGridLayout, QPushButton, QFileDialog, QMessageBox, QLineEdit, QRadioButton,
    QComboBox, QCheckBox
)
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import Qt

import settings
from input_field import InputField


class ExperimentSettings(QMainWindow):
    """
    Окно для настройки параметров эксперимента.

    Attributes:
        settings (Settings): Объект настроек для редактирования.
        input_fields (dict): Словарь, сопоставляющий атрибутам настроек с объектами InputField.
    """

    def __init__(self, settings: settings.Settings):
        super().__init__()
        self.setWindowTitle("Experiment Settings")
        self.settings = settings
        self.input_fields = {}
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

        grid_layout = self.create_settings_grid()
        self.main_layout.addLayout(grid_layout)

        button_layout = self.create_buttons()
        self.main_layout.addLayout(button_layout)

        self.update_data()

    def create_settings_grid(self) -> QGridLayout:
        grid = QGridLayout()
        settings_dict = asdict(self.settings)
        for i, (attr, value) in enumerate(settings_dict.items()):
            if attr in self.settings.settings_names:
                label = QLabel(self.settings.settings_names[attr], self)
                grid.addWidget(label, i, 0)

                # Определение типа данных и типа виджета
                expected_type = type(value)
                if expected_type == bool:
                    field = InputField(field_type='Checkbox', data_type=bool, parent=self)
                elif attr.lower().find('enable') != -1 or attr.lower().find('is_') != -1:
                    field = InputField(field_type='Checkbox', data_type=bool, parent=self)
                elif expected_type == int:
                    field = InputField(field_type='Edit', data_type=int, parent=self)
                elif expected_type == float:
                    field = InputField(field_type='Edit', data_type=float, parent=self)
                elif attr.lower().find('country') != -1:
                    # Пример использования Combobox
                    countries = ["USA", "Canada", "UK", "Germany", "France", "Other"]
                    field = InputField(field_type='Combobox', data_type=str, options=countries, parent=self)
                else:
                    field = InputField(field_type='Edit', data_type=str, parent=self)

                self.input_fields[attr] = field
                grid.addWidget(field.widget, i, 1)

        return grid

    def create_buttons(self) -> QHBoxLayout:
        button_layout = QHBoxLayout()

        self.button_apply = QPushButton("Apply", self)
        self.button_apply.clicked.connect(self.apply_settings)

        self.button_cancel = QPushButton("Cancel", self)
        self.button_cancel.clicked.connect(self.cancel)

        self.button_import = QPushButton("Import", self)
        self.button_import.clicked.connect(self.import_settings)

        self.button_export = QPushButton("Export", self)
        self.button_export.clicked.connect(self.export_settings)

        for button in [self.button_apply, self.button_cancel, self.button_import, self.button_export]:
            button_layout.addWidget(button)

        return button_layout

    def apply_settings(self):
        try:
            for attr, field in self.input_fields.items():
                value = field.getValue()
                if value is None and isinstance(field.widget, QLineEdit):
                    raise ValueError(f"Invalid input for {self.settings.settings_names[attr]}")
                setattr(self.settings, attr, value)

            match type(self.settings):
                case settings.Settings1:
                    settings.current_settings1 = deepcopy(self.settings)
                case settings.Settings2:
                    settings.current_settings2 = deepcopy(self.settings)
                case settings.Settings3:
                    settings.current_settings3 = deepcopy(self.settings)
                case settings.CommonSettings:
                    settings.current_common_settings = deepcopy(self.settings)
            self.close()
        except ValueError as e:
            self.show_error_message("Не получилось применить настройки", str(e))

    def cancel(self):
        self.close()

    def import_settings(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Открыть файл настроек",
            "",
            "JSON Files (*.json);;All Files (*)",
            options=options
        )
        if filename:
            self.load_settings(filename)
            self.update_data()

    def export_settings(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить настройки как",
            "",
            "JSON Files (*.json);;All Files (*)",
            options=options
        )
        if filename:
            self.save_settings(filename)

    def save_settings(self, filename: Optional[str] = None):
        try:
            self.settings.save(filename)
        except Exception as e:
            self.show_error_message("Ошибка при сохранении настроек", str(e))

    def load_settings(self, filename=None):
        try:
            self.settings.load(filename)
        except Exception as e:
            self.show_error_message("Ошибка при загрузке настроек", str(e))

    def update_data(self):
        for attr, field in self.input_fields.items():
            value = getattr(self.settings, attr, None)
            field.setValue(value)

    def show_error_message(self, title: str, message: str):
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText(title)
        error_dialog.setInformativeText(message)
        error_dialog.setWindowTitle(title)
        error_dialog.exec_()
