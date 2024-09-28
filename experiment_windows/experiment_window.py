import time
from dataclasses import dataclass
import pygame


@dataclass
class ClickCircle:
    position: pygame.Vector2
    radius: int
    time: float

    def __post_init__(self):
        self.start_time = time.perf_counter()

    def draw(self, screen):
        circle_surface = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)

        pygame.draw.circle(circle_surface, (255, 0, 0, self.brightness * 255),
                           (self.radius, self.radius), self.radius)

        screen.blit(circle_surface, self.position)

    @property
    def brightness(self):
        return 1 - max(0.0, time.perf_counter() - self.start_time) / self.time


class ExperimentWindow:
    def __init__(self):
        width, height = 800, 600
        self.screen = pygame.display.set_mode((width, height))
        self.running = True

        self.circles: list[ClickCircle] = []

    def main_loop(self):
        while self.running:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.circles.append(ClickCircle(event.pos, 20, 1))

            for circle in self.circles:
                circle.draw(self.screen)

            for i in range(len(self.circles)-1, -1, -1):
                if self.circles[i].brightness <= 0:
                    del self.circles[i]

            pygame.display.flip()
        self.close()

    def close(self):
        pygame.quit()


if __name__ == '__main__':
    pygame.init()
    window = ExperimentWindow()
    window.main_loop()
