import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message, screen,game, size_text = 90 ):
        self.size_text= size_text
        #screen.fill((0, 0, 0))
        self.draw_background = game.draw_background()
        self.font = pygame.font.Font(FONT_STYLE, size_text)
        self.text = self.font.render(message, True, (204,204,204))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def update(self, game):
        pygame.display.update()
        game.draw_background()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self, screen):
        #screen.fill((0,0,102))
        self.draw_background

    def update_message(self, message,size_text = 50):
        self.font = pygame.font.Font(FONT_STYLE, size_text)
        self.text = self.font.render(message, True, (10,10,10))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)