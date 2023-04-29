import pygame

pygame.init()


win=pygame.display.set_mode((500, 500))

pygame.display.set_caption("Scrolling Text")

Font=pygame.font.SysFont('timesnewroman',  30)

white=(255, 255, 255)
yellow=(255, 255, 0)
green=(0, 255, 255)
orange=(255, 100, 0)
done=False

letter1=Font.render("H", False, orange, yellow)
letter2=Font.render("E", False, orange, green)
letter3=Font.render("M", False, orange, yellow)
letter4=Font.render("A", False, orange, green)
letter5=Font.render("N", False, orange, yellow)
letter6=Font.render("T", False, orange, green)
letter7=Font.render("H", False, orange, yellow)

i=0
c=1

while not done:
    if(i>=820):
        i=0
        c+=1
        pygame.time.wait(500)

    win.fill(white)

    if(c%6==0):
        win.blit(letter1, (662-i, -162+i))
        win.blit(letter2, (639-i, -139+i))
        win.blit(letter3, (608-i, -108+i))
        win.blit(letter4, (579-i, -79+i))
        win.blit(letter5, (552-i, -52+i))
        win.blit(letter6, (529-i, -29+i))
        win.blit(letter7, (500 -i, 0 + i))

        i+=80

    if(c%6==5):
        win.blit(letter1, (-162+i, -162+i)) 
        win.blit(letter2, (-135+i, -135+i))
        win.blit(letter3, (-110+i, -110+i))
        win.blit(letter4, (-79+i, -79+i))
        win.blit(letter5, (-52+i, -52+i))
        win.blit(letter6, (-27+i, -27+i))
        win.blit(letter7, (0+i, 0+i))

        i+=80

    if(c%6==4):
        win.blit(letter1, (480, -180+i))
        win.blit(letter2, (480, -150+i))
        win.blit(letter3, (480, -120+i))
        win.blit(letter4, (480, -90+i))
        win.blit(letter5, (480, -60+i))
        win.blit(letter6, (480, -30+i))
        win.blit(letter7, (480, 0+i))

        i +=80

    if(c%6==3):
        win.blit(letter1, (0, -180+i))
        win.blit(letter2, (0, -150+i))
        win.blit(letter3, (0, -120+i))
        win.blit(letter4, (0, -90+i))
        win.blit(letter5, (0, -60+i))
        win.blit(letter6, (0, -30+i))
        win.blit(letter7, (0, 0+i))

        i+=80

    if(c%6==2):
        win.blit(letter1, (-124+i, 470))
        win.blit(letter2, (-102+i, 470))
        win.blit(letter3, (-82+i, 470))
        win.blit(letter4, (-58+i, 470))
        win.blit(letter5, (-40+i, 470))
        win.blit(letter6, (-19+i, 470))
        win.blit(letter7, (0+i, 470))

        i+=80
     
    if(c%6==1):
        win.blit(letter1, (-124+i, 0))
        win.blit(letter2, (-102+i, 0))
        win.blit(letter3, (-82+i, 0))
        win.blit(letter4, (-58+i, 0))
        win.blit(letter5, (-40+i, 0))
        win.blit(letter6, (-19+i, 0))
        win.blit(letter7, (0+i, 0))

        i +=80

    pygame.display.update()

    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            done=True

    pygame.time.wait(500)
pygame.quit()