import pygame, sys, math, time, random
from dice import roll_dice
from blackjack_final import Blackjack

pygame.init()
#Player
player_x, player_y = 80, 140
player_icon = pygame.image.load("./images/character.png")
player_dice_x, player_dice_y = 250, 50
player_move = 0
player_health = 4
player_steps = 200
player_dice = "123"
player_die_roll = 0
reached_finish = False

#Computer
computer_x, computer_y = 80, 200
computer_icon = pygame.image.load("./images/enemy.png")
computer_move = 0
computer_steps = 200
computer_dice_x, computer_dice_y = 650, 50
computer_dice = "123456"
computer_die_roll = 0
collision = False

#Background
background = pygame.image.load("./images/board.png")

#Board Specs
screen_width, screen_height = 1600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
turn = 0
end_of_board = 1480
message_font = pygame.font.Font("./fonts/Square.ttf", 40)
winner = ""


#States
fight = False
running, playing = True, False
START_KEY = False
health_x, health_y = 410, 50
blackjack_game = Blackjack()



def draw_player():
    screen.blit(player_icon, (player_x, player_y))
        
def draw_computer():
    screen.blit(computer_icon, (computer_x, computer_y))
        
def lose_health():
    player_health = player_health - 1
    display_player_health()
        
def display_player_health():
    health_icon = pygame.image.load("./images/health.png")
    count = 0
    while count < player_health:
        screen.blit(health_icon, (health_x + (count * 45), health_y))
        count += 1

    
def is_collision():
    if turn != 0:
        if player_x == computer_x:
            fight = True
            return True
        else:
            return False
    
def game_over():
    if player_health == 0:
        return True
    
def finish_line():
    if player_x == 80:
        if player_y == 340:
            return True

def player():
    screen.blit(player_icon, (player_x, player_y))


def computer():
    screen.blit(computer_icon, (computer_x, computer_y))
    
def display_message(text, x, y):       
    render_message =  message_font.render(text, True, (WHITE))
    screen.blit(render_message, (x, y))

        

def mini_game():
    games = "12"
    randgame = random.choice(games)
    winner = ""
    if randgame == 1:
        winner = ""
    elif randgame == 2:
        True
        winner = ""
    
    if winner == "Computer":
        lose_health()
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                turn += 1
                player_move = roll_dice(player_dice, player_dice_x, player_dice_y)
                player_die_roll = player_move
                computer_move = roll_dice(computer_dice, computer_dice_x, computer_dice_y)
                computer_die_roll = computer_move
                
      


    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    display_player_health()
    display_message(str(player_die_roll), player_dice_x + 80, player_dice_y)
    display_message(str(computer_die_roll), computer_dice_x + 80, computer_dice_y)
    player()
    computer()
 


    
    while player_move != 0:
        reached_finish = finish_line()
        if reached_finish:
            player_move = 0
        else: 
            if player_x == end_of_board:
                player_y += 200
                player_steps = -200
                player_x += player_steps
            else: 
                player_x += player_steps
                pygame.time.wait(1000)
            player_move -= 1


    while computer_move != 0:
        collision = is_collision()
        if collision:
                computer_move = 0
                if fight:
                    mini_game()
                    fight = False
        else: 
            if computer_x == end_of_board:
                computer_y += 200
                computer_steps = -200
                computer_x += computer_steps
            else:
                computer_x += computer_steps
                computer_move = computer_move - 1
            pygame.time.wait(1000)
        
    if reached_finish:
        display_message(winner)
        player_move = 0
        computer_move = 0
            
    pygame.display.update()
    
                    
        
                
            
                    
    




