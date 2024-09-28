from experiment_settings_windows.experiment_settings import ExperimentSettings
import settings


class ExperimentSettings3(ExperimentSettings):
    def __init__(self, settings_=None):
        if settings_ is None:
            settings_ = settings.Settings2()
        super().__init__(settings=settings_)

        self.setWindowTitle('Memory volume experiment settings')
