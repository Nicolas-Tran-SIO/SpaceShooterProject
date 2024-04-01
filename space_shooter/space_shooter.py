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
background_space=pygame.transform.scale(background_space_tempo, (LARGEUR ,HAUTEUR))
image_gagne=pygame.transform.scale(image_gagne_tempo, (LARGEUR ,HAUTEUR))
image_perdu=pygame.transform.scale(image_perdu_tempo, (LARGEUR ,HAUTEUR))


mon_vaisseau = space_functions.Vaisseau()

nombre_de_monstre=0

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


def tirer_vaisseau():
    balles_vaisseau.append(space_functions.Bullet_Vaisseau(mon_vaisseau.x+(LARGEUR//8)//4.7-9))
    balles_vaisseau.append(space_functions.Bullet_Vaisseau(mon_vaisseau.x+(LARGEUR//8)//4.7+LARGEUR//20+9))



################################################################################
########################### Fonctions Niveaux 1 et 2 ###########################
################################################################################


liste_monstres= []
balles_vaisseau=[]
balles_monstres=[]

def dessiner_tout():
    """dessins du niv 1"""
    fenetre.blit(background_space, (0, 0))
    #pygame.draw.rect(fenetre, (0,0,0), [0,0,LARGEUR,HAUTEUR])

    for balle_tiree_vaisseau in balles_vaisseau:
        space_functions.Bullet_Vaisseau.afficher(balle_tiree_vaisseau,fenetre)
    for petit_monstre in liste_monstres:
        space_functions.Monstre.afficher(petit_monstre,fenetre)
    for balle_tiree_monstres in balles_monstres:
        space_functions.Bullet_Monstre.afficher(balle_tiree_monstres,fenetre)
    space_functions.Vaisseau.afficher(mon_vaisseau,fenetre)
    pygame.draw.rect(fenetre, vert, [0, HAUTEUR-10, LARGEUR//5*(mon_vaisseau.pv//10), 10])


def tirer_monstre(monstre):
    balles_monstres.append(space_functions.Bullet_Monstre(monstre.x+LARGEUR//60,monstre.y+LARGEUR//27))



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
            if balle_tiree.y > HAUTEUR + 10:
                balles_vaisseau.pop(balle)
            balle+=1
        monstre+=1


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


def apparition_monstres(monstres):
    for i in range(4):
        for j in range(17):
            rect_monstre = pygame.Rect(j*LARGEUR//17,i*LARGEUR//17,LARGEUR//20,LARGEUR//20)
            liste_monstres.append(space_functions.Monstre(j*LARGEUR//17,i*LARGEUR//17,rect_monstre))
            monstres+=1
    return(monstres)

################################################################################
################################### starting ###################################
################################################################################

niveau_1 = True
if niveau_1:
    apparition_monstres(nombre_de_monstre)
niveau_2 = False
fin = False
perdu = False
gagne = False

################################################################################
################################### niveau 1 ###################################
################################################################################
pygame.display.set_caption("Space Shooter Niveau 1")
while niveau_1:
    dessiner_tout()
    appliquer_vitesse(vitesse_a_appliquer)

    if cooldown_tir == 15:
        tirer_vaisseau()
        cooldown_tir = 0

    for balle in balles_vaisseau:
        balle.y-=7
    cooldown_tir += 1


    for petit_monstre in liste_monstres:
        if random.randint(0,2000) == 10:

            tirer_monstre(petit_monstre)

    for balle_du_monstre in balles_monstres:
        balle_du_monstre.y+=7


    cooldown_tir_monstre += 1

    collisions_vaisseau_monstres()
    collisions_monstres_vaisseau()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            niveau_1=False
            niveau_2 = False
            niveau_boss = False
            fin = False


    if mon_vaisseau.pv <= 0:
        niveau_1=False
        niveau_2 = False
        niveau_boss = False
        fin = True
        perdu = True

    elif len(liste_monstres) <= 0:
        niveau_1= False
        niveau_2 = True



    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a and mon_vaisseau.x>0:
                vitesse_a_appliquer = -15
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d and mon_vaisseau.x<LARGEUR-mon_vaisseau.longueur:
                vitesse_a_appliquer =15

    if event.type == pygame.KEYUP:
        vitesse_a_appliquer = 0


    clock.tick(50)
    pygame.display.flip()

################################################################################
################################### niveau 2 ###################################
################################################################################

if niveau_2:
    apparition_monstres(nombre_de_monstre)
    if mon_vaisseau.pv <= 40:
        mon_vaisseau.pv += 10
pygame.display.set_caption("Space Shooter Niveau 2")
while niveau_2:
    dessiner_tout()
    appliquer_vitesse(vitesse_a_appliquer)

    if cooldown_tir == 15:
        tirer_vaisseau()
        cooldown_tir = 0

    for balle in balles_vaisseau:
        balle.y-=7
    cooldown_tir += 1


    for petit_monstre in liste_monstres:
        if random.randint(0,15*len(liste_monstres)) == 10:

            tirer_monstre(petit_monstre)

    for balle_du_monstre in balles_monstres:
        balle_du_monstre.y+=7


    cooldown_tir_monstre += 1

    collisions_vaisseau_monstres()
    collisions_monstres_vaisseau()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            niveau_1=False
            niveau_2 = False

            fin = False


    if mon_vaisseau.pv <= 0:
        niveau_1=False
        niveau_2 = False
        fin = True
        perdu = True

    elif len(liste_monstres) <= 0:
        niveau_2 = False
        fin = True
        gagne = True


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a and mon_vaisseau.x>0:
                vitesse_a_appliquer = -15
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d and mon_vaisseau.x<LARGEUR-mon_vaisseau.longueur:
                vitesse_a_appliquer =15

    if event.type == pygame.KEYUP:
        vitesse_a_appliquer = 0


    clock.tick(75)
    pygame.display.flip()

################################################################################
############################# Niveau 3 #########################################
################################################################################
if niveau_3:
    apparition_monstres(nombre_de_monstre)
    if mon_vaisseau.pv <= 40:
        mon_vaisseau.pv += 10

while niveau_2:
    dessiner_tout()
    appliquer_vitesse(vitesse_a_appliquer)
    if cooldown_tir == 15:
        tirer_vaisseau()
        cooldown_tir = 0

    for balle in balles_vaisseau:
        balle.y-=7
    cooldown_tir += 1


    for petit_monstre in liste_monstres:
        if random.randint(0,2000) == 10:

            tirer_monstre(petit_monstre)

    for balle_du_monstre in balles_monstres:
        balle_du_monstre.y+=7


    cooldown_tir_monstre += 1

    collisions_vaisseau_monstres()
    collisions_monstres_vaisseau()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            niveau_1=False
            niveau_2 = False
            niveau_boss = False
            fin = False


    if mon_vaisseau.pv <= 0:
        niveau_1=False
        niveau_2 = False
        niveau_boss = False
        fin = True
        perdu = True

    elif len(liste_monstres) <= 0:
        niveau_1= False
        niveau_2 = True



    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a and mon_vaisseau.x>0:
                vitesse_a_appliquer = -15
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d and mon_vaisseau.x<LARGEUR-mon_vaisseau.longueur:
                vitesse_a_appliquer =15

    if event.type == pygame.KEYUP:
        vitesse_a_appliquer = 0


    clock.tick(50)
    pygame.display.flip()

################################################################################
############################# affichage fin du jeu #############################
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