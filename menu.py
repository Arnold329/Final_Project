import pygame, sys, random

# Pygame Setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()


class Game():
    def __init__(self):
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.screen_width, self.screen_height = 1280, 960
        self.TITLE_W, self.TITLE_H = self.screen_width / 2, self.screen_height / 5
        self.display = pygame.Surface((self.screen_width, self.screen_height))
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE (0, 0, 0), (255, 255, 255)
        self.title_size = 80
        
        self.main_menu = MainMenu(self)
        self.game_menu = GameMenu(self)
        self.shooter_game = Shooter(self)
        self.blackjack = Blackjack(self)
        self.curr_menu = self.main_menu
        
    def menu_loop(self):
        while self.playing:
            self.event_loop()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset()
            
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        
class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.TITLE_W, self.game.TITLE_H
        self.run_display = True
        self.cursor_rect = game.Rect(0, 0, 20, 20)
        self.offset = -200
        
    def make_cursor(self):
        self.game.text("*", 40, self.curose_rect.x, self.cursor_rect.y)
        
    def blit_screen(self):
        self.game.screen.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset()
        
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Play"
        self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h + 200)
        
    def display(self):
        self.run = True
        while self.run:
            self.game.event_loop()
            self.inputs()
            self.game.display.fill(self.game.BLACK)
            self.game.text("My game", self.game.title_size, self.game.TITLE_W, self.game.TITLE_H)
            

                
        