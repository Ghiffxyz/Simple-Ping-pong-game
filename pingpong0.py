print("Hello, World!")

import pygame
pygame.init()

#scene
tinggi_scene = 500
lebar_scene = 500
#warna_black = 18, 15, 31
backgroundtexture = "wallhaven-p91dym_2560x1440.png"
gambar_pemain = "wallhaven-p91dym_2560x1440.png"
game_RUN = True
game_END = False
#musicfx = ""





#scene2
scene = pygame.display.set_mode((lebar_scene, tinggi_scene))
#scene.fill(warna_black)
background = pygame.transform.scale(pygame.image.load(backgroundtexture), (lebar_scene, tinggi_scene))

#pygame.mixer.init()
#pygame.mixer.music.load(musicfx)
#pygame.mixer.music.set_volume(1)
#pygame.mixer.music.play()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, gambar, x, y, lebar, tinggi, kecepatan):
        self.lebar = lebar
        self.tinggi = tinggi
        self.kecepatan = kecepatan
        self.image = pygame.transform.scale(pygame.image.load(gambar), 
            (self.lebar, self.tinggi))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def tampil(self):
        scene.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def gerak_kiri(self):
        tombol = pygame.key.get_pressed()
        if tombol[pygame.K_w] and self.rect.y>0:
            self.rect.y -= self.kecepatan
        if tombol[pygame.K_s] and self.rect.y<tinggi_scene-self.tinggi:
            self.rect.y += self.kecepatan

    def gerak_kanan(self):
        tombol = pygame.key.get_pressed()
        if tombol[pygame.K_UP]and self.rect.y>0:
            self.rect.y -= self.kecepatan
        if tombol[pygame.K_DOWN] and self.rect.y<tinggi_scene-self.tinggi:
            self.rect.y += self.kecepatan

PLAYER1 = Player(gambar_pemain, 20, 20, 50, 50, 5)
PLAYER2 = Player(gambar_pemain, 400, 400, 50, 50, 5)


FPS = pygame.time.Clock()
while game_RUN:

    #event handler untuk quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_RUN = False

    if game_END == False:
        
        scene.blit(background, (0,0))
        PLAYER1.tampil()
        PLAYER2.tampil()

        PLAYER1.gerak_kiri()
        PLAYER2.gerak_kanan()
    
    FPS.tick(60)
    pygame.display.update()