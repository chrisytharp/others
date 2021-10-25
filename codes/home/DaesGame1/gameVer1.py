import pygame, math, random
from pygame.locals import *
# 2 - Initialize the game
pygame.init()
width, height = 1800, 1500
color = [255,20,78]
screen=pygame.display.set_mode((width, height))
#pi screen support [(1920, 1080), (1600, 900), (1280, 800), (1280, 720), (1152, 864), (1024, 768), (832, 624), (800, 600), (720, 480), (720, 400), (640, 480)]
#screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
keys = [False, False, False, False]
playerpos=[500,500]
acc=[0,0]
arrows=[]
badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194



# 3 - Load images
player = pygame.image.load("dae/dae.png")
dad = pygame.image.load("dad/dad.png")
sissy = pygame.image.load("sissy/sissy.png")
bubba = pygame.image.load("bubba/bubba.png")
arrow = pygame.image.load("mom/mom.png")
badguyimg1 = pygame.image.load("doughnut.png")
badguyimg=badguyimg1


#castle = pygame.image.load("resources/images/castle.png")
# 4 - keep looping through
while 1:
    badtimer-=1

    # 5 - clear the screen before drawing it again
    screen.fill(color)
    # 6 - draw the screen elements
    screen.blit(dad,(0,30))
    screen.blit(bubba,(0,300))
    screen.blit(sissy,(0,500))
#    screen.blit(player, (playerpos))
    # 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)
        # 6.2 - Draw arrows
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        
        if bullet[1]<-1000 or bullet[1]>1000 or bullet[2]<-500 or bullet[2]>1000:
            arrows.pop(index)
        index+=1
        
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
    # 6.3 - Draw badgers
    if badtimer==0:
        badguys.append([1500, random.randint(50,430)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=7
        # 6.3.1 - Attack castle
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        #6.3.2 - Check for collisions
        index1=0
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):
                acc[0]+=1
                badguys.pop(index)
                arrows.pop(index1)
            index1+=1

        # 6.3.3 - Next bad guy
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)


    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_DOWN:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False
        
#        if event.type==pygame.QUIT:
#            # if it is quit the game
#            pygame.quit() 
#            exit(0)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit(0)

        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])

            # 9 - Move player
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
