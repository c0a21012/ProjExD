import pygame as pg
import sys
import random

def main():
    clock  = pg.time.Clock()
    #練習１：スクリーンと背景
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))
    screen_rect = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rect = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rect)

    #練習3：こうかとん
    kkimg_sfc = pg.image.load("fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rect = kkimg_sfc.get_rect()
    kkimg_rect.center = 900, 400

    #練習5：爆弾
    bombimg_sfc = pg.Surface((20, 20)) #Surface
    pg.draw.circle(bombimg_sfc, (255, 0, 0), (10, 10), 10)
    bombimg_rect = bombimg_sfc.get_rect()
    bombimg_rect.centerx = random.randint(0, screen_rect.width)
    bombimg_rect.centery = random.randint(0, screen_rect.height)
    
    

    vx, vy = 1, 1 #練習6
    
    
    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rect)
        

        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        #練習4
        key_lst = pg.key.get_pressed()
        if key_lst [pg.K_UP] == True:#y座標を-1
            kkimg_rect.centery -= 1
        if key_lst [pg.K_DOWN] == True:#y座標を+1
            kkimg_rect.centery += 1
        if key_lst [pg.K_LEFT] == True:#x座標を-1
            kkimg_rect.centerx -= 1
        if key_lst [pg.K_RIGHT] == True:#x座標を+1
            kkimg_rect.centerx += 1
        if bound(kkimg_rect, screen_rect) != (1, 1):
            if key_lst [pg.K_UP] == True:
                kkimg_rect.centery += 1
            if key_lst [pg.K_DOWN] == True:
                kkimg_rect.centery -= 1
            if key_lst [pg.K_LEFT] == True:
                kkimg_rect.centerx += 1
            if key_lst [pg.K_RIGHT] == True:
                kkimg_rect.centerx -= 1
            
        screen_sfc.blit(kkimg_sfc, kkimg_rect)
        
        bombimg_rect.move_ip(vx, vy)
        
        screen_sfc.blit(bombimg_sfc, bombimg_rect)
        
        yoko, tate = bound(bombimg_rect, screen_rect)
        vx *= yoko
        vy *= tate
    
        if kkimg_rect.colliderect(bombimg_rect):
            return

        pg.display.update()
        clock.tick(1000)

def bound(rect, screen_rect):
    '''
    [1] rect: こうかとん　or 爆弾のRect
    [2] screen_rect: スクリーンのRect
    '''
    yoko, tate = 1, 1
    if rect.left < screen_rect.left or screen_rect.right < rect.right: #領域外
        yoko = -1
    if rect.top < screen_rect.top or screen_rect.bottom < rect.bottom: #領域外
        tate = -1
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()