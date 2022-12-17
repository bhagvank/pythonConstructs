import pygame as pyg 

pyg.init()  

window = pyg.display.set_mode([500, 500])

loop = True
while loop:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            loop = False

    window.fill((255, 255, 255))

    pyg.draw.circle(window, (255, 0, 0), (250, 250), 75)


    pyg.display.flip()


pyg.quit() 
