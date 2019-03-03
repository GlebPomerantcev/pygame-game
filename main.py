import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("HEH")

finished = False
x = 50
y = 425
width = 40
height = 60
speed = 5
isJump = False
jumpCount = 10

while not finished:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[pygame.K_LEFT] and x > 5:
        x -= speed

    if pressedKeys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed

    if not isJump:
        if pressedKeys[pygame.K_UP] and y > 5:
            y -= speed

        if pressedKeys[pygame.K_DOWN] and y < 500 - height - 15:
            y += speed

        if pressedKeys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount>= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    rect = pygame.Rect(x,y,width,height)

    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,0,255),rect)
    pygame.display.update()

pygame.quit()