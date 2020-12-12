import random, pygame, time

pygame.init()

def display_die():
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    nums = "123456"
    
    random_num = random.choice(nums)
    die_face_to_display = pygame.image.load("./images/dice/die_" +str(random_num) + ".png")
    screen.blit(die_face_to_display, (100, 100))
    pygame.time.wait(2000)
    
i = 0
while i < 7:
    display_die()
    i += 1

    

    
    
    
    

