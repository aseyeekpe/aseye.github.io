# import pygame
# import sys
# import os

# # Initoilizing things
# pygame.init()
# pygame.font.init()

# # Draw window
# window_width = 600
# window_height = 600
# window = pygame.display.set_mode((window_width, window_height))
# pygame.display.set_caption("My Pong Game")
# window.fill((255, 255, 255))

# # Draw paddle
# paddle_width = 100
# paddle_height = 25

# # Draw ball
# ball_x = window_width // 2
# ball_y = window_height // 2
# ball_speed_x = 0.5
# ball_speed_y = 0.5
# ball = pygame.draw.circle(window,(0,0,0),(ball_x,ball_y),10)

# # Starting Score
# score = 0
# score_box = pygame.draw.rect(window, (0,0,0), (520, 50, 60, 40), 3)

# running = True
# while running:
#     font = pygame.font.Font(None, 20)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:  
#             running = False
#         mouse_x,mouse_y = pygame.mouse.get_pos()

#     # Clear the screen
#     window.fill((255, 255, 255))

#     ball_x += ball_speed_x
#     ball_y += ball_speed_y

#     # Bounce off left/right walls
#     if (ball_x - 10) <= 0 or (ball_x + 10) >= window_width:
#         ball_speed_x *= -1

#     # Bounce off top wall
#     if (ball_y - 10) <= 0:
#         ball_speed_y *= -1

#     # Add point to score and start from new position
#     if ball_y >=window_height:
#         score += 1
#         ball_y = window_width // 2

#     # Write score text on window
#     score_box = pygame.draw.rect(window, (0,0,0), (520, 50, 70, 40), 3)
#     score_text = font.render(f'Score: {score}', True, (0, 25, 0))
#     window.blit(score_text, (530, 60))
    
#     # Bounce off the paddle
#     if (ball_y+10)==(window_height-paddle_height):    
#         if ball_x>=mouse_x and ball_x<=mouse_x+(paddle_width/2):#If the ball is on the left of the paddle
#             ball_speed_x *=-1
#             ball_speed_y *=-1.05
#         if ball_x<=mouse_x and ball_x>=mouse_x-(paddle_width/2): #If the ball is on the right of the paddle
#             ball_speed_x*=-1
#             ball_speed_y *=-1.05
        
    

#     ball = pygame.draw.circle(window,(0,0,0),(ball_x,ball_y),10)

#     # Keep the paddle where the mouse is
#     paddle = pygame.draw.rect(window, (0,0,0),pygame.Rect(mouse_x-(paddle_width/2),window_height-paddle_height,paddle_width,paddle_height))

#     # Update the display
#     pygame.display.flip()



import pygame
import sys

# initialize pygame and fonts
pygame.init()
pygame.font.init()

# window setup
window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("My Pong Game")

# paddle dimensions
paddle_width = 100
paddle_height = 25

# ball setup
ball_x = window_width // 2
ball_y = window_height // 2
ball_speed_x = 4
ball_speed_y = 4
ball_radius = 10

# starting score
score = 0

# font for score
font = pygame.font.Font(None, 30)

# clock to control FPS
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)  # limit to 60 FPS for smooth movement

    # handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

    # get mouse position for paddle
    mouse_x, mouse_y = pygame.mouse.get_pos()

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # bounce off left/right walls
    if (ball_x - ball_radius) <= 0 or (ball_x + ball_radius) >= window_width:
        ball_speed_x *= -1
    # bounce off top
    if (ball_y - ball_radius) <= 0:
        ball_speed_y *= -1

    # if ball goes past bottom of paddle, add to score and reset
    if ball_y >= window_height:
        score += 1
        ball_x = window_width // 2
        ball_y = window_height // 2
        ball_speed_y *= -1

    # create rectangles for collision detection
    paddle_rect = pygame.Rect(mouse_x - paddle_width//2, window_height - paddle_height, paddle_width, paddle_height)
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius*2, ball_radius*2)

    # bounce ball off paddle
    if ball_rect.colliderect(paddle_rect) and ball_speed_y > 0:
        ball_speed_y *= -1
        # change speed depending on where it hits on the paddle
        offset = (ball_x - mouse_x) / (paddle_width / 2)
        ball_speed_x += offset * 2

    # clear screen
    window.fill((255, 255, 255))

    # draw ball
    pygame.draw.circle(window, (0, 0, 0), (int(ball_x), int(ball_y)), ball_radius)

    # draw paddle
    pygame.draw.rect(window, (0, 0, 0), paddle_rect)

    # draw score box and text
    pygame.draw.rect(window, (0, 0, 0), (372, 50, 195, 40), 3)
    score_text = font.render(f'Computer Score: {score}', True, (0, 25, 0))
    window.blit(score_text, (375, 60))

    # update screen
    pygame.display.flip()

pygame.quit()
sys.exit()
