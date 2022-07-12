from pickle import NONE
from zipfile import ZIP_MAX_COMMENT
import pygame as pg
import sys
import random


def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : 
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: 
        tate = -1 # 領域外
    return yoko, tate


class Screen:
    def __init__(self, title, wh, img):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)        # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.bgi_sfc = pg.image.load(img)         # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()    # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, img: str, zoom: float, xy):
        self.sfc = pg.image.load(img)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
        

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1      
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)




class Bomb:
    def __init__(self, color, zoom, vxy, scr):
        self.sfc = pg.Surface((2*zoom, 2*zoom)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (zoom, zoom), zoom)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def update(self, scr):
        self.rct.move_ip(self.vx, self.vy)
        
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate

        self.blit(scr)

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)
        # 練習5
        
class BirdBomb:
    def __init__(self, color, zoom, xy):
        self.sfc = pg.Surface((2*zoom, 2*zoom)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (zoom, zoom), zoom)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.center = xy
        #self.rct.centerx += 2

    def update(self, scr):
        # key_states = pg.key.get_pressed()
        # if key_states[pg.K_SPACE]:
        #     self.rct.centerx += 2
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_w]: 
            self.rct.centery -= 1      
        if key_states[pg.K_s]: 
            self.rct.centery += 1
        if key_states[pg.K_a]: 
            self.rct.centerx -= 1
        if key_states[pg.K_d]: 
            self.rct.centerx += 1
        
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_w]: 
                self.rct.centery += 1
            if key_states[pg.K_s]: 
                self.rct.centery -= 1
            if key_states[pg.K_a]: 
                self.rct.centerx += 1
            if key_states[pg.K_d]: 
                self.rct.centerx -= 1
        self.blit(scr)

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)


class Enemy:
    def __init__(self, img: str, zoom: float, xy, vxy, scr):
        self.sfc = pg.image.load(img)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def update(self, scr):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)
    

def main():
    clock = pg.time.Clock()
    scr = Screen("戦え！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    ene = Enemy("fig/リガルオン.png", 0.1, (200, 200), (+2, +2), scr)
    bird_bomb = BirdBomb((0, 0, 255), 20, (900, 400))
    while True:
        scr.blit()
        
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            #  if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                
                # while (0 <bird_bomb.rct.centerx < 1600 
                #         and 0 < bird_bomb.rct.centery < 900):
                #         i = 0
                #         bird_bomb = BirdBomb((0, 0, 255), 20+i, (900, 400))
        kkt.update(scr)
        bkd.update(scr)
        ene.update(scr)
        bird_bomb.update(scr)
                
        if kkt.rct.colliderect(bkd.rct) or kkt.rct.colliderect(ene.rct):
            return

        if ene.rct.colliderect(bird_bomb.rct):
            return 

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()