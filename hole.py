import pygame

hole_size = 20
flow_speed = 10

class Hole:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.source_x = x
        self.source_y = y + 15
        self.stream_x = self.source_x
        self.stream_y = self.source_y

    def draw_hole(self, window):
        pygame.draw.circle(window, (0, 0, 0), (self.x, self.y), hole_size)

    def update_leakage(self, window):
        if self.stream_y < 700:
            pygame.draw.line(window, (0, 0, 255), (self.source_x, self.source_y), (self.stream_x, self.stream_y + flow_speed), 20)
            self.stream_y += flow_speed
        else:
            pygame.draw.line(window, (0, 0, 255), (self.source_x, self.source_y), (self.stream_x, self.stream_y), 20)