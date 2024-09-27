import json
import pickle
from dataclasses import dataclass, field, astuple, asdict
from enum import Enum
from datetime import datetime
import os


@dataclass
class Settings:
    filename: str = field(init=False, default=f'settings/default_settings.json')

    def __post_init__(self):
        if os.path.exists(self.filename):
            if self.filename:
                self.load()
        else:
            self.save(self.filename)

    def load(self, filename=None):
        if filename is not None:
            self.filename = filename

        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'rb') as file:
                    loaded_settings = pickle.load(file)

                for attr, value in loaded_settings.__dict__.items():
                    self.__dict__[attr] = value

                #with open(self.filename, 'r') as file:
                #    data = json.load(file)

                #for key, value in data:
                #    self.__dict__[key] = value
            except:
                raise ValueError('При записи файла произошла ошибка')
        else:
            raise ValueError('Файл не найден!')

    def save(self, filename=None):
        if filename is not None:
            self.filename = filename

        os.makedirs('settings', exist_ok=True)
        with open(self.filename, 'wb') as file:
            pickle.dump(self, file)

        #data = asdict(self)

        #os.makedirs('settings', exist_ok=True)
        #with open(filename, 'w') as file:
        #    json.dump(data, file, indent=4)


@dataclass
class CommonSettings(Settings):
    filename: str = field(init=False, default=f'settings/default_common_settings.json')
    fullscreen_mode: bool = True
    bg_color: str = '#fff'
    monitor_copy_size: float = 0.1
    move_cursor: bool = False
    escape_key: str = 't'
    drink_delay: float = 1.0
    autosave_period: int = 5  # in minutes
    captured_monitor: int = 2
    selected_period_start: datetime = None
    selected_period_end: datetime = None

    # arduino params
    port: str = 'COM3'
    baud_rate: int = 9600
    arduino_script_filename: str = '24-07-18.ino'
    barrier_working_time: float = 0.4

    # sounds
    using_sounds: bool = True
    experiment_start_sound_filename: str = 'sounds/start.mp3'
    test_start_sound_filename: str = 'sounds/start.mp3'
    right_answer_sound: str = 'sounds/right_answer_sound.mp3'
    wrong_answer_sound: str = 'sounds/wrong_answer_sound.wav'

    # click parametres
    mouse_click_circle_radius: int = 20
    click_circle_color: str = '#fff'
    click_circle_width: int = 5
    click_circle_time: float = 1.0


class UsedImagesBehavior(Enum):
    DELETE = 0
    IGNORE = 1
    MOVE = 2


class RightImage(Enum):
    OLD_IMAGE = 0
    NEW_IMAGE = 1


@dataclass
class Settings1(Settings):
    filename: str = field(init=False, default=f'settings/default_experiment1_settings.json')
    delays: list[str] = field(default_factory=lambda: [1.0, [1.0], 1.0, 0.0, 5.0, 0, 0])
    barrier_delay: float = 0.0
    session_number: int = 1
    repeat_number: int = 5
    restart_after_answer: bool = False
    image_size: int = 100
    distance_between_images: int = 100
    display_target_image_twice: bool = False
    mix_delays: bool = False
    correct_answer_percentage: int = 50
    equalize_correct_answers_by_delays: bool = False
    right_image: RightImage = RightImage.OLD_IMAGE
    experiment_directory: str = ''
    log_header: list[str] = field(
        default_factory=lambda: ['Номер', 'Время с начала эксперимента', 'Время реакции', 'Ответ', 'Правильный ответ',
                                 'Файл 1', 'Файл 2', 'Дата', 'Время', 'Ответ справа', 'Ответ слева', 'Текущая отсрочка',
                                 'Предыдущая отсрочка', 'Правильным считается', 'Отказ от ответа',
                                 'Файл настроек эксперимента'])
    current_log_header: list[str] = None
    used_images_behaviour: UsedImagesBehavior = UsedImagesBehavior.IGNORE
    used_images_directory: str = 'used_images'


class MovementDirection(Enum):
    LEFT = 0
    RIGHT = 1


@dataclass
class Settings2(Settings):
    filename: str = field(init=False, default=f'settings/default_experiment2_settings.json')
    image_min_speed: int = 50
    image_max_speed: int = 75
    barrier_width: int = 100
    barrier_color: str = '#f00'
    barrier_dist: int = 150
    image_number: int = 5
    session_delay: float = 1.0
    straight_movement: bool = True
    repeat_number: int = 3
    image_size: int = 100
    image_filename: str = 'pictograms/no.png'
    movement_direction: MovementDirection = MovementDirection.RIGHT
    log_header: list[str] = field(default_factory=lambda: ['Номер', 'Время с начала эксперимента', 'Время реакции',
                                                           'Ответ', 'Правильный ответ', 'Файлы', 'Дата', 'Время',
                                                           'Текущая отсрочка', 'Предыдущая отсрочка', 'Отказ от ответа',
                                                           'Файл настроек эксперимента'])
    current_log_header: list[str] = None


@dataclass
class Settings3(Settings):
    filename: str = field(init=False, default=f'settings/default_experiment3_settings.json')
    min_image_number: int = 2
    max_image_number: int = 4
    shuffle_images: bool = True
    image_size: int = 128
    delays: list[float] = field(default_factory=lambda: [1.0, 1.0, 1.0, 0.5])
    stop_after_error: bool = True
    grid_size: list[float, float] = field(default_factory=lambda: [5, 5])
    log_header: list[str] = field(default_factory=lambda: ['Номер', 'Время с начала эксперимента', 'Время реакции',
                                                           'Ответ', 'Правильный ответ', 'Файлы', 'Дата', 'Время',
                                                           'Текущая отсрочка', 'Предыдущая отсрочка', 'Отказ от ответа',
                                                           'Файл настроек эксперимента'])
    current_log_header: list[str] = None


if __name__ == '__main__':
    common_settings = CommonSettings()
    s1 = Settings1()
    s2 = Settings2()
    s3 = Settings3()

    print('-----CommonSettings-----')
    print(common_settings)
    print('------------------------')
    print()
    print('-----Settings1-----')
    print(s1)
    print('-------------------')
    print()
    print('-----Settings2-----')
    print(s2)
    print('-------------------')
    print()
    print('-----Settings3-----')
    print(s3)
    print('-------------------')

