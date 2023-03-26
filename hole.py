import pygame

class Hole:
    def __init__(self, x, y, difficulty):
        self.x = x
        self.y = y
        self.source_x = x
        self.source_y = y + 15
        self.stream_x = self.source_x
        self.stream_y = self.source_y
        self.difficulty = difficulty
        self.leak_rate = 0.2 * self.difficulty
        self.progress = 0
        self.clock = pygame.time.Clock()
        self.hole_size = 20 * self.difficulty
        self.flow_speed = 10 * self.difficulty

    def draw_hole(self, window):
        r = 255 * self.progress if 255 * self.progress <= 255 else 255
        g = 215 * self.progress if 215 * self.progress <= 215 else 215
        pygame.draw.circle(window, (r, g, 0, 255), (self.x, self.y), 20)

    def update_leakage(self, window, screen, water_level):
        # flow stream
        if self.stream_y < window.get_height() - water_level:
            pygame.draw.line(screen, (0, 0, 255, 125), (self.source_x, self.source_y), (self.stream_x, self.stream_y + self.flow_speed), 20)
            self.stream_y += self.flow_speed
            return False
        # stop stream
        elif self.progress < 1:
            pygame.draw.line(screen, (0, 0, 255, 125), (self.source_x, self.source_y), (self.stream_x, self.stream_y + self.flow_speed), 20)
            return True
        # clear stream
        else:
            pygame.draw.line(screen, (255, 255, 255, 0), (self.source_x, self.source_y), (self.stream_x, self.stream_y + self.flow_speed), 20)
            return False

    def is_inside_hole(self, finger_x, finger_y):
        if (finger_x - self.x) ** 2 + (finger_y - self.y) ** 2 <= self.hole_size ** 2:
            return True
        else:
            return False

    def is_under_water(self, window, water_level):
        return self.source_y >= window.get_height() - water_level
