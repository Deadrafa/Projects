import pygame
import time

clock = pygame.time.Clock()

pygame.init()
exet = True

screen = pygame.display.set_mode((1024, 1000)) #pygame.FULLSCREEN flags=pygame.NOFRAME
pygame.display.set_caption("RoboDendi")

ikonka = pygame.image.load("image/icon.png")
pygame.display.set_icon(ikonka)
fon = pygame.image.load("image/gamefon.png")
score_user = 0
score = pygame.font.Font('shrift/NotoSansJP-Thin.ttf',20)
score_text = score.render(f'Score:{score_user}', True, 'White')

natpis = pygame.font.Font('shrift/NotoSansJP-Thin.ttf',40)
natpis_text = natpis.render('テトリス', True, 'White')
zvyk = pygame.mixer.Sound("zvyki/exet.mp3")

figura = [
    pygame.image.load("image/prygol.png"),
    pygame.image.load("image/prygol2.png")

]

figura2 = [
    pygame.image.load("image/noga.png"),
    pygame.image.load("image/noga2.png"),
    pygame.image.load("image/noga3.png"),
    pygame.image.load("image/noga4.png")

]

flag = 0
figura_kor = 0
figura_kor2 = 0
figura_animationX = 100
figura_animationY = 100
figura_animation_shagXLEFT = 5
figura_animation_shagXRIGHT = 5
figura_animation_shagYDOWN = 5
figura_animation_shagYUP = 5


figura_animationXNEW = 100
figura_animationYNEW = 100
figura_animation_shagXLEFTNEW = 5
figura_animation_shagXRIGHTNEW = 5
figura_animation_shagYDOWNNEW = 5
figura_animation_shagYUPNEW = 5


while exet:

    screen.blit(fon, (0, 0))
    screen.blit(natpis_text,(1024 / 3 + 60, 0))
    screen.blit(score_text, (1024 / 3 + 110, 1000 - 40))
    screen.blit(figura[figura_kor], (figura_animationX, figura_animationY))
    if flag == 1:
        screen.blit(figura2[figura_kor2], (figura_animationXNEW, figura_animationYNEW))

    keybor = pygame.key.get_pressed()
    if keybor[pygame.K_F11]:
        screen = pygame.display.set_mode((1024, 1000),flags=pygame.NOFRAME)
    elif keybor[pygame.K_LEFT]:
        if figura_animationX == 3:
            pass
        elif figura_animationX >= 3:
            figura_animationX -= figura_animation_shagXLEFT
    elif keybor[pygame.K_RIGHT]:
        if figura_animationX >= 926:
            pass
        elif figura_animationX < 1024:
            figura_animationX += figura_animation_shagXRIGHT
    elif keybor[pygame.K_SPACE]:
        time.sleep(0.1)
        if figura_kor == 0:
            figura_kor += 1
        elif figura_kor == 1:
            figura_kor -= 1

    elif keybor[pygame.K_DOWN]:
        figura_animationY  += figura_animation_shagYDOWN
        if figura_animationY  >=1000 -20:
            figura_animation_shagYDOWN = 0
            figura_animation_shagYUP = 0
            figura_animation_shagXLEFT = 0
            figura_animation_shagXRIGHT = 0
            flag = 1
    elif keybor[pygame.K_UP]:
        figura_animationY -= figura_animation_shagYUP
        if figura_animationY <= 3:
            figura_animation_shagYUP = 0


    elif keybor[pygame.K_LEFT]: #Начало новой фигуры
        if figura_animationXNEW == 3:
            pass
        elif figura_animationXNEW >= 3:
            figura_animationXNEW -= figura_animation_shagXLEFTNEW
    elif keybor[pygame.K_RIGHT]:
        if figura_animationXNEW >= 926:
            pass
        elif figura_animationXNEW < 1024:
            figura_animationXNEW += figura_animation_shagXRIGHTNEW
    elif keybor[pygame.K_SPACE]:
        time.sleep(0.1)
        if figura_kor2 <= 0:
            figura_kor2 += 1
        elif figura_kor2 == 3:
            figura_kor2 -= 1

    elif keybor[pygame.K_DOWN]:
        figura_animationYNEW  += figura_animation_shagYDOWNNEW
        if figura_animationY  >=1000 -20:
            figura_animation_shagYDOWNNEW = 0
            figura_animation_shagYUPNEW = 0
            figura_animation_shagXLEFTNEW = 0
            figura_animation_shagXRIGHTNEW = 0
            flag = 1
    elif keybor[pygame.K_UP]:
        figura_animationYNEW -= figura_animation_shagYUPNEW
        if figura_animationYNEW <= 3:
            figura_animation_shagYUPNEW = 0
    


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exet = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                zvyk.play()
                time.sleep(0.5)
                exet = False
            elif event.key == pygame.K_1:
                score_user += 1
                score_text = score.render(f'Score:{score_user}', True, 'White')


    clock.tick(30)
       
        
