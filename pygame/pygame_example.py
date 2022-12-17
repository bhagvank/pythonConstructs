import pygame  as pyg
import sys  
   
class Sprite(pyg.sprite.Sprite):  
    def __init__(self, pos):  
        pyg.sprite.Sprite.__init__(self)  
        self.image = pyg.Surface([20, 20])  
        self.image.fill((255, 0, 255))  
        self.rect = self.image.get_rect()  
        self.rect.center = pos  
def main():  
    pyg.init()  
    clock = pyg.time.Clock()  
    fps = 50  
    bg = [255, 255, 255]  
    size =[300, 300]  
    window = pyg.display.set_mode(size)  
    gamePlayer = Sprite([40, 50])  
    gamePlayer.move = [pyg.K_LEFT, pyg.K_RIGHT, pyg.K_UP, pyg.K_DOWN]  
    gamePlayer.vx = 5  
    gamePlayer.vy = 5  
  
    wall = Sprite([100, 60])  
  
    wall_group = pyg.sprite.Group()  
    wall_group.add(wall)  
  
    gamePlayer_group = pyg.sprite.Group()  
    gamePlayer_group.add(gamePlayer)  
  
    while True:  
        for event in pyg.event.get():  
            if event.type == pyg.QUIT:  
                return False  
        key = pyg.key.get_pressed()  
        for i in range(2):  
            if key[gamePlayer.move[i]]:  
                gamePlayer.rect.x += gamePlayer.vx * [-1, 1][i]  
  
        for i in range(2):  
            if key[gamePlayer.move[2:4][i]]:  
                gamePlayer.rect.y += gamePlayer.vy * [-1, 1][i]  
        window.fill(bg)  
 
        collision = pyg.sprite.spritecollide(gamePlayer, wall_group, True)  
        if collision:    
            gamePlayer.image.fill((0, 0, 0))  
        gamePlayer_group.draw(window)  
        wall_group.draw(window)  
        pyg.display.update()  
        clock.tick(fps)  
    pyg.quit()  
    sys.exit  
if __name__ == '__main__': 
    main()