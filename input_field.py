from typing import Optional

from PyQt5.QtWidgets import QLineEdit, QRadioButton, QComboBox, QCheckBox, QWidget
from PyQt5.QtGui import QIntValidator, QDoubleValidator


class InputField:
    """
    Класс для создания различных типов полей ввода в PyQt5.

    Поддерживаемые типы:
    - 'Edit': QLineEdit
    - 'Radiobutton': QRadioButton
    - 'Combobox': QComboBox
    - 'Checkbox': QCheckBox
    """

    def __init__(self, field_type: str, data_type: type, options: Optional[list] = None,
                 parent: Optional[QWidget] = None):
        """
        Инициализатор класса InputField.

        :param field_type: Тип поля ввода ('Edit', 'Radiobutton', 'Combobox', 'Checkbox').
        :param data_type: Ожидаемый тип данных (str, int, float, bool).
        :param options: Список опций для 'Combobox' (только для 'Combobox').
        :param parent: Родительский виджет (опционально).
        """
        self.field_type = field_type
        self.data_type = data_type

        if field_type == 'Edit':
            self.widget = QLineEdit(parent)
            self._setup_edit_validator()
        elif field_type == 'Radiobutton':
            self.widget = QRadioButton(parent)
        elif field_type == 'Combobox':
            self.widget = QComboBox(parent)
            self._setup_combobox(options)
        elif field_type == 'Checkbox':
            self.widget = QCheckBox(parent)
        else:
            raise ValueError(f"Unsupported field_type: {field_type}")

    def _setup_edit_validator(self):
        if self.data_type == int:
            self.widget.setValidator(QIntValidator())
        elif self.data_type == float:
            self.widget.setValidator(QDoubleValidator())

    def _setup_combobox(self, options: Optional[list]):
        if options:
            self.widget.addItems([str(option) for option in options])

    def getValue(self):
        if self.field_type == 'Edit':
            text = self.widget.text()
            if self.data_type == int:
                try:
                    return int(text)
                except ValueError:
                    return None  # Или можно выбросить исключение
            elif self.data_type == float:
                try:
                    return float(text)
                except ValueError:
                    return None
            else:
                return text
        elif self.field_type == 'Radiobutton':
            return self.widget.isChecked()
        elif self.field_type == 'Combobox':
            current_text = self.widget.currentText()
            if self.data_type == int:
                try:
                    return int(current_text)
                except ValueError:
                    return None
            elif self.data_type == float:
                try:
                    return float(current_text)
                except ValueError:
                    return None
            else:
                return current_text
        elif self.field_type == 'Checkbox':
            return self.widget.isChecked()
        else:
            return None

    def setValue(self, value):
        if self.field_type == 'Edit':
            self.widget.setText(str(value))
        elif self.field_type == 'Radiobutton':
            self.widget.setChecked(bool(value))
        elif self.field_type == 'Combobox':
            index = self.widget.findText(str(value))
            if index >= 0:
                self.widget.setCurrentIndex(index)

        elif self.field_type == 'Checkbox':
            self.widget.setChecked(bool(value))
