import pygame

pygame.init()
screen_width, screen_height = 1600, 500
screen = pygame.display.set_mode((screen_width, screen_height))
WHITE = (0, 0, 0)

def draw_horizontal_lines():
    pygame.draw.line(screen, WHITE, (50, 0), (50, 1600), 5 )
    pygame.draw.line(screen, WHITE, (450, 0), (450, 1600), 5 )

while True:
    draw_horizontal_lines()








#class Draft_Board():
    # characterX = 0
    # characterY = 0
    # characterPosition = "| A |"
    
    # board = [["|   |" for a in range(12)] for b in range(1)]
    # board[characterY][characterX] = characterPosition
    
    # while True:
    #     for i in board:
    #         print("----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ")
    #         print(" ".join(i))
    #         print("----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ")
            
    #     direction = input("input:")
    #     if direction == "W":
    #         board[characterX][characterY] = "|   |"
    #         characterX -= 1
    #         board[characterX][characterY] = "| A |"
    #     elif direction == "S":
    #         board[characterX][characterY] = "|   |"
    #         characterX += 1
    #         board[characterX][characterY] = "| A |"
    #     elif direction == "A":
    #         board[characterX][characterY] = "|   |"
    #         characterY -= 1
    #         board[characterX][characterY] = "| A |"
    #     elif direction == "D":
    #         board[characterX][characterY] = "|   |"
    #         characterY += 1
    #         board[characterX][characterY] = "| A |"
        