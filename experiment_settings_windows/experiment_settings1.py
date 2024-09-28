import sys
from PyQt5.QtWidgets import QApplication

import settings
from experiment_settings_windows.experiment_settings import ExperimentSettings


class ExperimentSettings1(ExperimentSettings):
    def __init__(self, settings_=None):
        if settings_ is None:
            settings_ = settings.Settings1()
        super().__init__(settings=settings_)

        self.setWindowTitle('DNMS experiment settings')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExperimentSettings1(settings.Settings1())
    window.show()
    sys.exit(app.exec_())
