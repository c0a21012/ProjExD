import pygame as pg
import sys

def main():
    clock  = pg.time.Clock()

    #練習１
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))
    screen_rect = screen_sfc.get_rect()

    #練習2
    pg.image.load("fig/pg_bg.jpg")
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rect = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rect)

    #練習3
    kkimg_sfc = pg.image.load("fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rect = kkimg_sfc.get_rect()
    kkimg_rect.center = 900, 400

    
    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()