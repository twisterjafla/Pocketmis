

from multiprocessing import Process
import os
import pygame



def artemis(isFirst:bool):
    pygame.init()
        


    displayWidth = 400
    displayHeight = 500

    gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))

    pygame.display.set_caption('Pocketmis')
    



    

    directory = os.path.dirname(os.path.realpath(__file__))
    artemis = pygame.image.load(os.path.join(directory, 'Artemis.png'))






    shouldContinue=True
    while shouldContinue:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shouldContinue = False


          

        gameDisplay.fill(color=(230, 54, 58))
        gameDisplay.blit(artemis, ((displayWidth-300)/2, (displayHeight-200)/2))
        if isFirst:
            font = pygame.font.SysFont('Comic Sans MS', 100)
            gameDisplay.blit(font.render("Hiii", False, (255,255,255)), (100,30))
        else:
            font = pygame.font.SysFont('Comic Sans MS', 60)
            gameDisplay.blit(font.render("Its fine I have QR", False, (255,255,255)), (30,65))
        

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()

artemis(True)


while True:
    artemis(False)
