import pygame
 


def checkCollision(x,y,treasureX,treasureY):
	global screen, textWin
	collisionState = False

	if y >= treasureY and y <= treasureY + 40:
		if x >= treasureX and x <= treasureX + 35:
			y = 350
			collisionState = True		
		
		elif x + 35 >= treasureX and x +  35 <= treasureX + 35:
			y = 350	
			collisionState = True


	elif y + 40 >= treasureY and y + 40 <= treasureY + 40:
		if x >= treasureX and x <= treasureX + 35:		
			y = 350	
			collisionState = True

		elif x + 35 >= treasureX and x + 35 <= treasureX + 35:		
			y = 350	
			collisionState = True
	
	return collisionState, y

			

pygame.init()
screen = pygame.display.set_mode((700,400))

finished =False # 0 < 10->True 10<10->False
x = 350 -25/2 
y = 350

#array = [0,1.2,4.5,"Hello"]
#print(array)

#print (pygame.K_SPACE)
playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage, (35,40))
playerImage = playerImage.convert_alpha()
backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage, (700,400))
screen.blit(backgroundImage, (0,0))


treasureImage = pygame.image.load("treasure.png")
treasureImage = pygame.transform.scale(treasureImage, (35,40))
treasureImage = treasureImage.convert_alpha()


treasureX = 350 -35/2
treasureY = 50 



screen.blit(treasureImage, (treasureX, treasureY))

#Text Win
font = pygame.font.SysFont("arial", 30)
level = 1



frame = pygame.time.Clock()

collisionTreasure = False


while finished == False:#While our game is not finished
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

	pressedKeys = pygame.key.get_pressed()
	             #[....,UP,DOWN,LEFT,SPACE,...]
	if pressedKeys [pygame.K_SPACE] == 1:
		y -= 1
	#rectOne = pygame.Rect(x,y,30,30)#x,y,width,height

	color = (0,0,255) #R,G,B
	white = (255,255,255)
	screen.blit(backgroundImage, (0,0))
	screen.blit(treasureImage, (treasureX, treasureY))
	screen.blit(playerImage, (x,y))
	#pygame.draw.rect(screen, color,rectOne)
	collisionTreasure,y = checkCollision(x,y,treasureX,treasureY)

	if collisionTreasure == True:
		level += 1
		textWin = font.render("Great Job, the next level "+ str(level) , True, (0,0,0))
		screen.blit(textWin, (350 - textWin.get_width()/2, 200 - textWin.get_height()/2))
		pygame.display.flip()
		frame.tick(1)




	pygame.display.flip()
	frame.tick(30)
	




