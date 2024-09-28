from experiment_settings_windows.experiment_settings import ExperimentSettings
from settings import *


class ExperimentSettings2(ExperimentSettings):
    def __init__(self):
        super().__init__(settings=Settings2())

        self.setWindowTitle('Extrapolation experiment settings')
