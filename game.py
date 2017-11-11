import pygame
 

pygame.init()
screen = pygame.display.set_mode((700,400))

finished =False # 0 < 10->True 10<10->False
x = 0
y = 50

#array = [0,1.2,4.5,"Hello"]
#print(array)

#print (pygame.K_SPACE)
while finished == False:#While our game is not finished
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

	pressedKeys = pygame.key.get_pressed()
	             #[....,UP,DOWN,LEFT,SPACE,...]
	if pressedKeys [pygame.K_SPACE] == 1:
		y += 1
	rectOne = pygame.Rect(x,y,30,30)#x,y,width,height

	color = (0,0,255) #R,G,B
	black = (0,0,0)
	screen.fill(black)
	pygame.draw.rect(screen, color,rectOne)
	pygame.display.flip()




