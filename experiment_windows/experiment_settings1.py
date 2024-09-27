from experiment_windows.experiment_settings import ExperimentSettings
from settings import *


class ExperimentSettings1(ExperimentSettings):
    def __init__(self):
        super().__init__(settings=Settings1())

        self.setWindowTitle('DNMS experiment settings')
