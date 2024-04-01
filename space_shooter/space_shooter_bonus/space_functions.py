import pygame

largeur = 800
hauteur = 450


class Vaisseau:
    def __init__(self):
        self.x = (largeur//2)-largeur//16
        self.y = (hauteur//4)*3
        self.longueur = largeur//8
        self.img_tempo = pygame.image.load("./img/vaisseau.png").convert_alpha()
        self.img = pygame.transform.scale(self.img_tempo, (self.longueur,self.longueur))
        self.hitbox = pygame.Rect(self.x,self.y,self.x+self.longueur,self.y+self.longueur)
        self.pv = 50               # pv = points de vie

    def afficher(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def deplacer_hitbox(self):
        self.hitbox = pygame.Rect(self.x,self.y,self.x+self.longueur,self.y+self.longueur)
        return(self.hitbox)


class Monstre:
    def __init__(self,monstre_x,monstre_y,hitbox):
        self.img_tempo = pygame.image.load("./img/monstre.png").convert_alpha()
        self.img = pygame.transform.scale(self.img_tempo, (largeur//20,largeur//20))
        self.x=monstre_x
        self.y=monstre_y
        self.hitbox = hitbox

    def afficher(self, screen):
        screen.blit(self.img, (self.x, self.y))
        #pygame.draw.rect(screen, (255,0,0), [self.x,self.y,largeur//20,largeur//20])

class Bullet_Vaisseau:
    def __init__(self,x):
        self.vitesse = 25
        self.img_tempo = pygame.image.load("./img/bullet_vaisseau.png").convert_alpha()
        self.img = pygame.transform.scale(self.img_tempo, (largeur//32//20*16,largeur//32//20*16))
        self.x = x
        self.y = largeur/2


    def afficher(self, screen):
        screen.blit(self.img, (self.x, self.y))
        #pygame.draw.rect(screen, (0,125,255), [self.x, self.y, largeur//32//20*16,largeur//32//20*16])



class Bullet_Monstre:
    def __init__(self,x,y):
        self.vitesse = 25
        self.img_tempo = pygame.image.load("./img/bullet_monstre.png").convert_alpha()
        self.img = pygame.transform.scale(self.img_tempo, (largeur//32//20*16,largeur//32//20*16))
        self.x = x
        self.y = y


    def afficher(self, screen):
        screen.blit(self.img, (self.x, self.y))
        #pygame.draw.rect(screen, (255,0,0), [self.x, self.y, largeur//32//20*16,largeur//32//20*16])

class Bonus_Vie:
    def __init__(self,x):
        self.vitesse = 15
        self.img_tempo = pygame.image.load("./img/bonus_vie.png").convert_alpha()
        self.img = pygame.transform.scale(self.img_tempo, (largeur//32//20*16,largeur//32//20*16))
        self.x = x
        self.y = (largeur/2)


    def afficher(self, screen):
        screen.blit(self.img, (self.x, self.y))

class Invocation:
    def __init__(self,x,y):
        self.img_tempo = pygame.image.load("./img/Invocation.png").convert_alpha()
        self.img = pygame.transform.scale(self.img_tempo, (largeur//20,largeur//20))
        self.x=x
        self.y=y


    def afficher(self, screen):
        screen.blit(self.img, (self.x, self.y))



class Bullet_Bonus_Invocation:
    def __init__(self,x):
        self.vitesse = 15
        self.img_tempo = pygame.image.load("./img/bonus_invocation.png").convert_alpha()
        self.img = pygame.transform.scale(self.img_tempo, (largeur//32//20*16,largeur//32//20*16))
        self.x = x
        self.y = (largeur/2)

    def afficher(self, screen):
        screen.blit(self.img, (self.x, self.y))


class Boss:
    def __init__(self):
        self.longueur = largeur//4
        self.x = (largeur/2)-self.longueur//1.5
        self.y = 0
        self.longueur = largeur//4
        self.img_tempo = pygame.image.load("./img/mother_boss.png").convert_alpha()
        self.img = pygame.transform.scale(self.img_tempo, (self.longueur,self.longueur))
        self.hitbox = pygame.Rect(self.x,self.y,self.x+self.longueur,self.y+self.longueur)
        self.pv = 1000               # pv = points de vie

    def afficher(self, screen):
        screen.blit(self.img, (self.x, self.y))

class Vaisseau_Boss:
    def __init__(self):
        self.x = (largeur/2)-largeur//16
        self.y = (hauteur/40)*35
        self.longueur = largeur//16
        self.img_tempo = pygame.image.load("./img/vaisseau.png").convert_alpha()
        self.img = pygame.transform.scale(self.img_tempo, (self.longueur,self.longueur))
        self.hitbox = pygame.Rect(self.x,self.y,self.x+self.longueur,self.y+self.longueur)
        self.pv = 50               # pv = points de vie

    def afficher(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def deplacer_hitbox(self):
        self.hitbox = pygame.Rect(self.x,self.y,self.x+self.longueur,self.y+self.longueur)
        return(self.hitbox)