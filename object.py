import pygame
## object klass som alla objekt ärver ifrån
class object :
    speed_x = 3 ## hastigheten på x-led och är statisk
    speed_y = 3 ## hastigheten på y-led och är statisk
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
    def draw(self, screen):
        
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])
    
    def update(self):
        self.x += speed_x
        self.y += speed_y
