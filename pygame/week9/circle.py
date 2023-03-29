import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False

x = 50
y = 50
width = 500
height = 500

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y > 20: y -= 20
        if pressed[pygame.K_DOWN] and y < height: y += 20
        if pressed[pygame.K_LEFT] and x > 20: x-=20
        if pressed[pygame.K_RIGHT] and x < width : x += 20
        
        screen.fill((0, 0, 0))
        
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

        
        pygame.display.flip()
        clock.tick(60)