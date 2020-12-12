import pygame, random

pygame.init()
screen_width, screen_height = 1600, 500
screen = pygame.display.set_mode((screen_width, screen_height))
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
suite = "1234"

def display_player_cards(x, y):
    randnum = random.choice(num)
    randsuites = random.choice(suite)
    
    player_card_to_display = pygame.image.load("./images/cards/card_" + str(randnum) + "_" + str(randsuites + ".png"))
    screen.blit(player_card_to_display, (x, y))
    pygame.time.wait(2000)
    
def display_dealer_cards(x, y):
    randnum = random.choice(num)
    randsuites = random.choice(suite)
    
    dealer_card_to_display = pygame.image.load("./images/cards/card_" + str(randnum) + "_" + str(randsuites + ".png"))
    screen.blit(dealer_card_to_display, (x, y))
    pygame.time.wait(2000)
    
def display_card_back(x, y):
    card_back = pygame.image.load("./images/cards/card_back.png")
    screen.blit(card_back, (x, y))
    pygame.time.wait(2000)
    
def blackjack_loop():
    display_player_cards(600, 100)
    display_dealer_cards(600, 400)
    display_player_cards(1000, 100)
    display_card_back(1000, 400)
    
    
while True:
    blackjack_loop()