import pygame
import space_functions
import time
import greetings_ne_pas_regarder
import random

LARGEUR = space_functions.largeur
HAUTEUR = space_functions.hauteur

vitesse_a_appliquer=0
cooldown_tir = 0
cooldown_tir_monstre = 0
pygame.init()
clock = pygame.time.Clock()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Space Shooter")

background_space_tempo = pygame.image.load("./img/espace.jpg").convert_alpha()
image_perdu_tempo = pygame.image.load("./img/perdu.jpg").convert_alpha()
image_gagne_tempo = pygame.image.load("./img/gagne.jpg").convert_alpha()

vert = (0,255,0)
rouge = (255,0,0)
background_space=pygame.transform.scale(background_space_tempo, (LARGEUR ,HAUTEUR))
image_gagne=pygame.transform.scale(image_gagne_tempo, (LARGEUR ,HAUTEUR))
image_perdu=pygame.transform.scale(image_perdu_tempo, (LARGEUR ,HAUTEUR))


nombre_de_monstre=0
vitesse_deplacement_boss = 10
################################################################################
############################### Fonction General ###############################
################################################################################

def appliquer_vitesse(vitesse):
    mon_vaisseau.x+=vitesse
    if mon_vaisseau.x<0:
        mon_vaisseau.x= 0
    elif mon_vaisseau.x>LARGEUR-mon_vaisseau.longueur:
        mon_vaisseau.x=LARGEUR-mon_vaisseau.longueur
    space_functions.Vaisseau.deplacer_hitbox(mon_vaisseau)


def tirer_vaisseau_boss():
    balles_vaisseau.append(space_functions.Bullet_Vaisseau(mon_vaisseau.x+mon_vaisseau.longueur//20))
    balles_vaisseau.append(space_functions.Bullet_Vaisseau(mon_vaisseau.x+mon_vaisseau.longueur-mon_vaisseau.longueur//3))





################################################################################
############################## Fonctions Niv Boss ##############################
################################################################################

liste_monstres= []
balles_vaisseau=[]
balles_monstres=[]

mon_boss = space_functions.Boss()

def dessiner_tout_lvl_boss():
    """dessins du niv du boss"""
    fenetre.blit(background_space, (0, 0))

    for balle_tiree_vaisseau in balles_vaisseau:
        space_functions.Bullet_Vaisseau.afficher(balle_tiree_vaisseau,fenetre)
    for petit_monstre in liste_monstres:
        space_functions.Monstre.afficher(petit_monstre,fenetre)
    for balle_tiree_monstres in balles_monstres:
        space_functions.Bullet_Monstre.afficher(balle_tiree_monstres,fenetre)
    mon_vaisseau.afficher(fenetre)
    mon_boss.afficher(fenetre)
    pygame.draw.rect(fenetre, vert, [0, HAUTEUR-10, LARGEUR//5*(mon_vaisseau.pv//10), 10])
    pygame.draw.rect(fenetre, rouge, [0,0,LARGEUR//100*(mon_boss.pv//10),10])


def collisions_vaisseau_monstres():
    """
    quand les balles du vaisseau touchent un monstres
    """
    monstre = 0
    for petit_monstre in liste_monstres:
        balle = 0
        for balle_tiree in balles_vaisseau:
            if petit_monstre.hitbox.collidepoint(balle_tiree.x,balle_tiree.y):
                liste_monstres.pop(monstre)
                balles_vaisseau.pop(balle)
            elif balle_tiree.y < -20:
                balles_vaisseau.pop(balle)
            if balle_tiree.y > HAUTEUR + 10:
                balles_vaisseau.pop(balle)
            balle+=1
        monstre+=1

def collisions_boss_vaisseau():
    """
    quand la balles du boss touchent le boss vaisseau
    """
    balle = 0
    for balle_tiree in balles_vaisseau:
        if mon_vaisseau.x <= balle_tiree.x <= mon_vaisseau.x+mon_vaisseau.longueur and mon_vaisseau.y<= balle_tiree.y <= mon_vaisseau.y+mon_vaisseau.longueur:
            mon_vaisseau.pv-=10
            balles_monstres.pop(balle)
        balle+=1

def collisions_monstres_vaisseau():
    """
    quand la balles d'un monstres touchent le vaisseau
    """
    balle = 0
    for balle_tiree in balles_monstres:
        if mon_vaisseau.x <= balle_tiree.x <= mon_vaisseau.x+mon_vaisseau.longueur and mon_vaisseau.y<= balle_tiree.y <= mon_vaisseau.y+mon_vaisseau.longueur:
            mon_vaisseau.pv-=10
            balles_monstres.pop(balle)
        if balle_tiree.y< -200:
            balles_monstres.pop(balle)
        balle+=1

def collisions_vaisseau_boss():
    """
    quand la balles du vaisseau touchent le boss
    """
    balle = 0
    for balle_tiree in balles_vaisseau:
        if mon_boss.x <= balle_tiree.x <= mon_boss.x+mon_boss.longueur and mon_boss.y<= balle_tiree.y <= mon_boss.y+mon_boss.longueur:
            mon_boss.pv-=10
            balles_vaisseau.pop(balle)
        balle+=1

def deplacement_boss(vitesse):
    if mon_boss.x<0 or mon_boss.x+mon_boss.longueur> LARGEUR:
        vitesse = -abs(vitesse)
    mon_boss.x += vitesse




################################################################################
################################### starting ###################################
################################################################################
mon_vaisseau = space_functions.Vaisseau_Boss()
niveau_boss = True
fin = False
perdu = False
gagne = False

################################################################################
################################### niv boss ###################################
################################################################################

while niveau_boss:
    dessiner_tout_lvl_boss()
    deplacement_boss(vitesse_deplacement_boss)

    appliquer_vitesse(vitesse_a_appliquer)

    if cooldown_tir == 15:
        tirer_vaisseau_boss()
        cooldown_tir = 0
    collisions_vaisseau_monstres()
    collisions_vaisseau_boss()

    for balle in balles_vaisseau:
        balle.y-=7
    cooldown_tir += 1



    if mon_vaisseau.pv <= 0:
        niveau_boss = False
        fin = True
        perdu = True


    elif mon_boss.pv <= 0:
        niveau_boss = False
        fin = True
        gagne = True


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            niveau_boss = False
            fin = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT or event.key == pygame.K_a and mon_vaisseau.x>0:
                    vitesse_a_appliquer = -15
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d and mon_vaisseau.x<LARGEUR-mon_vaisseau.longueur:
                    vitesse_a_appliquer = 15



        if event.type == pygame.KEYUP:
            vitesse_a_appliquer = 0



    clock.tick(75)
    pygame.display.flip()

################################################################################
################################## niveau fin ##################################
################################################################################

while fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = False
    keys = pygame.key.get_pressed()
    if perdu:
        fenetre.blit(image_perdu, (0,0))


    if gagne:
        fenetre.blit(image_gagne, (0,0))


    if keys[pygame.K_RETURN]:
        fin = False




    clock.tick(50)
    pygame.display.flip()

################################################################################

pygame.quit()