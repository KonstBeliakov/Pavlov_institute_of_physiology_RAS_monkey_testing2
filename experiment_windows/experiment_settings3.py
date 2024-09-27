from experiment_windows.experiment_settings import ExperimentSettings
from settings import *


class ExperimentSettings3(ExperimentSettings):
    def __init__(self):
        super().__init__(settings=Settings3())

        self.setWindowTitle('Memory volume experiment settings')
