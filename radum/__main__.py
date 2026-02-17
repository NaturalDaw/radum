import pygame
from pygame.locals import *
from sys import exit
import math
import random

pygame.init()


window = pygame.display.set_mode((1200,800))
pygame.display.set_caption('radum')


T =      [ pygame.image.load('./image/tutorial/t0.png'),
           pygame.image.load('./image/tutorial/t1.png'),
           pygame.image.load('./image/tutorial/t2.png'),
           pygame.image.load('./image/tutorial/t3.png'),
           pygame.image.load('./image/tutorial/t4.png'),
           pygame.image.load('./image/tutorial/t5.png'),
           pygame.image.load('./image/tutorial/t6.png'),
           pygame.image.load('./image/tutorial/t7.png'),
           pygame.image.load('./image/tutorial/t8.png'),
           pygame.image.load('./image/tutorial/t9.png'),
           pygame.image.load('./image/tutorial/t10.png'),
           pygame.image.load('./image/tutorial/t11.png'),
           pygame.image.load('./image/tutorial/t12.png'),
           pygame.image.load('./image/tutorial/t13.png'),
           pygame.image.load('./image/tutorial/t14.png'),
           pygame.image.load('./image/tutorial/t15.png'),
           pygame.image.load('./image/tutorial/t16.png'),
           pygame.image.load('./image/tutorial/t17.png'),
           pygame.image.load('./image/tutorial/t18.png'),
           pygame.image.load('./image/tutorial/t19.png'),
           pygame.image.load('./image/tutorial/t20.png'),
           pygame.image.load('./image/tutorial/t21.png'),
           pygame.image.load('./image/tutorial/t22.png'),
           pygame.image.load('./image/tutorial/t23.png'),
           pygame.image.load('./image/tutorial/t24.png'),
           pygame.image.load('./image/tutorial/t25.png'),
           pygame.image.load('./image/tutorial/t26.png'),
           pygame.image.load('./image/tutorial/t27.png'),
           pygame.image.load('./image/tutorial/t28.png'),
           pygame.image.load('./image/tutorial/t29.png') ]
Nums =  [[ pygame.image.load('./image/r0.png'),
           pygame.image.load('./image/r1.png'),
           pygame.image.load('./image/r2.png'),
           pygame.image.load('./image/r3.png'),
           pygame.image.load('./image/r4.png'),
           pygame.image.load('./image/r5.png'),
           pygame.image.load('./image/r6.png'),
           pygame.image.load('./image/r7.png'),
           pygame.image.load('./image/r8.png'),
           pygame.image.load('./image/r9.png') ],
         [ pygame.image.load('./image/b0.png'),
           pygame.image.load('./image/b1.png'),
           pygame.image.load('./image/b2.png'),
           pygame.image.load('./image/b3.png'),
           pygame.image.load('./image/b4.png'),
           pygame.image.load('./image/b5.png'),
           pygame.image.load('./image/b6.png'),
           pygame.image.load('./image/b7.png'),
           pygame.image.load('./image/b8.png'),
           pygame.image.load('./image/b9.png') ]]
rr =       pygame.image.load('./image/rr.png')
bb =       pygame.image.load('./image/bb.png')
GF =     [ pygame.image.load('./image/G1F.png'),
           pygame.image.load('./image/G2F.png'),
           pygame.image.load('./image/G3F.png'),
           pygame.image.load('./image/G4F.png'),
           pygame.image.load('./image/G5F.png') ]
GS =     [ pygame.image.load('./image/G1S.png'),
           pygame.image.load('./image/G2S.png'),
           pygame.image.load('./image/G3S.png'),
           pygame.image.load('./image/G4S.png'),
           pygame.image.load('./image/G5S.png') ]
Final    = pygame.image.load('./image/FINAL.png')
LINEbX   = pygame.image.load('./image/BlueLineX.gif')
LINEbY   = pygame.image.load('./image/BlueLineY.gif')
LINErX   = pygame.image.load('./image/RedLineX.gif' )
LINErY   = pygame.image.load('./image/RedLineY.gif' )
Bground  = pygame.image.load('./image/background.png')
interface= pygame.image.load('./image/interface.png')
interfacy= pygame.image.load('./image/interfacy.png')
cleaner  = pygame.image.load('./image/cleaner.png')
tick     = pygame.image.load('./image/tick.png')
Priorimg = pygame.image.load('./image/priority.png')
upgrade  = pygame.image.load('./image/upgrade.png')
pause    = pygame.image.load('./image/pause.png')
flagR    = pygame.image.load('./image/flagR.png')
flagB    = pygame.image.load('./image/flagB.png')
redwins  = pygame.image.load('./image/redwins.png')
bluewins = pygame.image.load('./image/bluewins.png')
draw     = pygame.image.load('./image/draw.png')

Oper  = [[],[]]
Pt = [0, 0]
VPt= [0, 0]
Record = []

Crush = 0

Game  = 1
Round = 6



class number:
    def __init__(self, num=8):
        self.figure = math.floor(math.log(num,10)) if num > 0 else 0
        self.all  = []
        for i in range(10):
            self.doll = [True for j in range(7)]
            if i == 0:
                self.doll[1] = False
            if i == 1:
                self.doll[0] = self.doll[1] = self.doll[2] = self.doll[3] = self.doll[5] = False
            if i == 2:
                self.doll[3] = self.doll[6] = False
            if i == 3:
                self.doll[3] = self.doll[5] = False
            if i == 4:
                self.doll[0] = self.doll[2] = self.doll[5] = False
            if i == 5:
                self.doll[4] = self.doll[5] = False
            if i == 6:
                self.doll[4] = False
            if i == 7:
                self.doll[1] = self.doll[2] = self.doll[3] = self.doll[5] = False
            if i == 9:
                self.doll[5] = False
            self.all.append(self.doll)
        self.num = num
    def output(self, image1, image2, image_size,  x,y):
        for i in range(self.figure+1):
            if self.all[self.num//(10**i)%10][0]:
                window.blit(image1 , (x+0.75*image_size*(self.figure-2*i), y))
            if self.all[self.num//(10**i)%10][1]:
                window.blit(image1 , (x+0.75*image_size*(self.figure-2*i), y+image_size))
            if self.all[self.num//(10**i)%10][2]:
                window.blit(image1 , (x+0.75*image_size*(self.figure-2*i), y+image_size*2))
            if self.all[self.num//(10**i)%10][3]:
                window.blit(image2 , (x+0.75*image_size*(self.figure-2*i), y))
            if self.all[self.num//(10**i)%10][4]:
                window.blit(image2 , (x+image_size+0.75*image_size*(self.figure-2*i) , y))
            if self.all[self.num//(10**i)%10][5]:
                window.blit(image2 , (x+0.75*image_size*(self.figure-2*i) , y+image_size))
            if self.all[self.num//(10**i)%10][6]:
                window.blit(image2 , (x+image_size+0.75*image_size*(self.figure-2*i) , y+image_size))

class sentry:
    def __init__(self):
        self.color = 0 # 0 - empty; 1 - red; 2 - blue.
        self.level = -1
    def upgrade(self):
        if self.level < 9:
            self.level += 1
    def score(self, fact=True):
        (Pt if fact else VPt)[self.color-1] += 2**self.level
        self.level = 0

Board = [[sentry() for i in range(5)] for j in range(5)]

def delay(t):
    for h in range(t):
        hh = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                hh = True
            if event.type == QUIT:
                pygame.quit()
                exit()
        if hh:
            break
        pygame.time.delay(1)

def entrance():
    global Game, Round
    window.blit(interface, (0,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == K_v:
                    vs(True)
                if event.key == K_s:
                    vs(False)
                if event.key == K_t:
                    tutorial()
                if event.key == K_1:
                    Round = 11
                if event.key == K_2:
                    Round = 12
                if event.key == K_3:
                    Round = 3
                if event.key == K_4:
                    Round = 4
                if event.key == K_5:
                    Round = 5
                if event.key == K_6:
                    Round = 6
                if event.key == K_7:
                    Round = 7
                if event.key == K_8:
                    Round = 8
                if event.key == K_9:
                    Round = 9
                if event.key == K_0:
                    Round = 10
                if event.key == K_y:
                    Game = 1
                if event.key == K_u:
                    Game = 2
                if event.key == K_i:
                    Game = 3
                if event.key == K_o:
                    Game = 4
                if event.key == K_p:
                    Game = 5
            if event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if y in range(225,415):
                    vs(True)
                if y in range(415,600):
                    vs(False)
                if y in range(600,800):
                    tutorial()

def tutorial():
    for t in range(30):
        Nextpage = False
        window.blit(T[t], (0,0))
        pygame.display.update()
        if t == 0:
            delay(300)
            continue
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN and t < 6:
                    Nextpage = True
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        if t == 29:
                            from os import system
                            system('shutdown /s /t 5')
                            window.blit(flagB,(0,0))
                            pygame.display.update()
                        else:
                            pygame.quit()
                            exit()
                    if event.key == K_r:
                        entrance()
                    if event.key == K_n:
                        Nextpage = True
            if Nextpage:
                break
    window.blit(interface, (0,0))
    pygame.display.update()

def vs(oppo): # True - human; False - cpu.
    global Pt, VPt, Oper, Board, Crush, Record
    Diff = -1
    if not oppo:
        window.blit(interfacy,(0,0))
        pygame.display.update()
        while Diff == -1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if y in range(0,270):
                        Diff = 0
                    if y in range(270,530):
                        Diff = 1
                    if y in range(530,800):
                        Diff = 2
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.key == K_e:
                        Diff = 0
                    if event.key == K_m:
                        Diff = 1
                    if event.key == K_h:
                        Diff = 2
    for g in range(Game*2):
        Priority = g%2 # 0 - Red; 1 - Blue.
        if Priority:
            window.blit(GS[g//2], (0,0))
        else:
            window.blit(GF[g//2], (0,0))
        if g == Game*2-1:
            window.blit(Final,  (0,600))
        pygame.display.update()
        delay(2000)
        for r in range(Round+1):
            while True:
                window.blit(Bground, (0, 0))
                for i in range(g):
                    number(Record[i][0]).output(LINEbX if i%2 else LINErX, LINEbY if i%2 else LINErY, 30, 275+100*i ,  40)
                    number(Record[i][1]).output(LINErX if i%2 else LINEbX, LINErY if i%2 else LINEbY, 30, 275+100*i , 125)
                for i in range(5):
                    for j in range(5):
                        if Board[i][j].color:
                            window.blit(Nums[Board[i][j].color-1][Board[i][j].level], (150+100*i,250+100*j))
                if len(Oper[0]) == 2:
                    if Board[Oper[0][0]][Oper[0][1]].color:
                        Oper[0] = []
                    window.blit(tick, (800,425))
                if len(Oper[1]) == 2:
                    if Board[Oper[1][0]][Oper[1][1]].color:
                        Oper[1] = []
                    window.blit(tick, (1000,425))
                if len(Oper[0]) == 2 and len(Oper[1]) == 2:
                    if Oper[0] == Oper[1]:
                        if Crush:
                            Oper[2-Crush] = []
                        else:
                            if Priority:
                                window.blit(flagB, (0,0))
                                pygame.display.update()
                                delay(500)
                                Oper[0]  = []
                                Crush    = 2
                                Priority = 0
                            else:
                                window.blit(flagR, (0,0))
                                pygame.display.update()
                                delay(500)
                                Oper[1]  = []
                                Crush    = 1
                                Priority = 1
                    else:
                        Crush = 0
                        Board[Oper[0][0]][Oper[0][1]].color = 1
                        Board[Oper[1][0]][Oper[1][1]].color = 2
                        window.blit(rr, (150+100*Oper[0][0],250+100*Oper[0][1]))
                        window.blit(bb, (150+100*Oper[1][0],250+100*Oper[1][1]))
                        pygame.display.update()
                        delay(500)
                        for i in range(5):
                            for j in range(5):
                                if Board[i][j].color:
                                    trigger = (Board[i][j].color * 2 - 3) * ((i-Oper[0][0])**2 + (j-Oper[0][1])**2 - (i-Oper[1][0])**2 - (j-Oper[1][1])**2)
                                    if trigger > 0:
                                        Board[i][j].upgrade()
                                        window.blit(Nums[Board[i][j].color-1][Board[i][j].level], (150+100*i,250+100*j))
                                        window.blit(upgrade, (150+100*i+65,250+100*j+5))
                                    if trigger < 0:
                                        Board[i][j].score()
                                        window.blit(cleaner, (700, 340))
                                        number(Pt[0]).output(LINErX, LINErY, 30, 800 , 345)
                                        number(Pt[1]).output(LINEbX, LINEbY, 30, 1000, 345)
                                        window.blit(rr if Board[i][j].color == 1 else bb, (150+100*i,250+100*j))
                                    if i == Oper[0][0] and j == Oper[0][1]:
                                        window.blit(rr, (150+100*i,250+100*j))
                                    if i == Oper[1][0] and j == Oper[1][1]:
                                        window.blit(bb, (150+100*i,250+100*j))
                                    pygame.display.update()
                                    delay(500)
                        delay(500)
                        break
                number(Pt[0]).output(LINErX, LINErY, 30, 800 , 345)
                number(Pt[1]).output(LINEbX, LINEbY, 30, 1000, 345)
                if Crush == 1:
                    window.blit(rr, (150+100*Oper[0][0],250+100*Oper[0][1]))
                if Crush == 2:
                    window.blit(bb, (150+100*Oper[1][0],250+100*Oper[1][1]))
                if Priority:
                    window.blit(Priorimg, (1000,500))
                else:
                    window.blit(Priorimg, (800 ,500))
                if r == Round:
                    break
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYUP:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            exit()
                        if Crush != 1:
                            if event.key == K_1:
                                if len(Oper[0]) < 2:
                                    Oper[0].append(0)
                            if event.key == K_2:
                                if len(Oper[0]) < 2:
                                    Oper[0].append(1)
                            if event.key == K_3:
                                if len(Oper[0]) < 2:
                                    Oper[0].append(2)
                            if event.key == K_4:
                                if len(Oper[0]) < 2:
                                    Oper[0].append(3)
                            if event.key == K_5:
                                if len(Oper[0]) < 2:
                                    Oper[0].append(4)
                            if event.key == K_BACKQUOTE:
                                Oper[0] = []
                        if Crush != 2 and oppo:
                            if event.key == K_n:
                                if len(Oper[1]) < 2:
                                    Oper[1].append(0)
                            if event.key == K_m:
                                if len(Oper[1]) < 2:
                                    Oper[1].append(1)
                            if event.key == K_COMMA:
                                if len(Oper[1]) < 2:
                                    Oper[1].append(2)
                            if event.key == K_PERIOD:
                                if len(Oper[1]) < 2:
                                    Oper[1].append(3)
                            if event.key == K_SLASH:
                                if len(Oper[1]) < 2:
                                    Oper[1].append(4)
                            if event.key == K_QUOTE:
                                Oper[1] = []
                        if event.key == K_r:
                            Oper  = [[],[]]
                            Pt = [0, 0]
                            Record = []
                            Crush = 0
                            Board = [[sentry() for i in range(5)] for j in range(5)]
                            entrance()
                v = [[4, 8, 4, 8, 4],
                     [8, 3, 2, 3, 8],
                     [4, 2, 1, 2, 4],
                     [8, 3, 2, 3, 8],
                     [4, 8, 4, 8, 4]]
                if not oppo and len(Oper[1]) < 2:
                    if Diff == 0:
                        Oper[1].append(random.randint(0,4))
                    if Diff == 1:
                        if Crush == 1:
                            evamax = -10000
                            Board[Oper[0][0]][Oper[0][1]].color = 1
                            VBoard = [[sentry() for i in range(5)] for j in range(5)]
                            VPt = [0, 0]
                            for x in range(5):
                                for y in range(5):
                                    if not Board[x][y].color:
                                        for m in range(5):
                                            for n in range(5):
                                                VBoard[m][n].level = Board[m][n].level
                                                VBoard[m][n].color = Board[m][n].color # Shallow copy is really excessive.
                                        VPt = [0, 0]
                                        VBoard[x][y].color = 2
                                        for i in range(5):
                                            for j in range(5):
                                                if VBoard[i][j].color:
                                                    trigger = (VBoard[i][j].color * 2 - 3) * ((i-Oper[0][0])**2 + (j-Oper[0][1])**2 - (i-x)**2 - (j-y)**2)
                                                    if trigger > 0:
                                                        VBoard[i][j].upgrade()
                                                    if trigger < 0:
                                                        VBoard[i][j].score(False)
                                        eva = (VPt[1] - VPt[0]) * 16
                                        for i in range(5):
                                            if r == Round - 1:
                                                break
                                            for j in range(5):
                                                if VBoard[i][j].color:
                                                    if VBoard[i][j].level == 8:
                                                        eva += (VBoard[i][j].color * 2 - 3) * v[i][j] * 704
                                                    elif VBoard[i][j].level == 9:
                                                        eva += (VBoard[i][j].color * 2 - 3) * v[i][j] * 1056
                                                    else:
                                                        eva += (VBoard[i][j].color * 2 - 3) * v[i][j] * 3 * 2 ** VBoard[i][j].level
                                        if eva > evamax:
                                            evamax = eva
                                            Oper[1] = [x, y]
                            Board[Oper[0][0]][Oper[0][1]].color = 0
                        else:
                            if r == Round - 1:
                                hl  = 0
                                hls = []
                                avai= []
                                for i in range(5):
                                    for j in range(5):
                                        if Board[i][j].level > hl:
                                            hls = [[i,j,0,[]]]
                                            hl  = Board[i][j].level
                                        elif Board[i][j].level == hl:
                                            hls.append([i,j,0,[]])
                                        if Board[i][j].level < 0:
                                            avai.append([i,j,0])
                                for i in hls:
                                    for j in avai:
                                        dsq = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
                                        if dsq > i[2]:
                                            i[3] = [j]
                                            i[2] = dsq
                                        elif dsq == i[2]:
                                            i[3].append(j)
                                for i in hls:
                                    for j in i[3]:
                                        j[2] += 1 # Using shallow copy.
                                mul = 0
                                op = []
                                for i in avai:
                                    if i[2] > mul:
                                        mul = i[2]
                                        op = [i[0:2]]
                                    elif i[2] == mul:
                                        op.append(i[0:2])
                                Oper[1] = random.choice(op)
                            else:
                                p = [[4, 8, 4, 8, 4],
                                     [8, 3, 2, 3, 8],
                                     [4, 2, 1, 2, 4],
                                     [8, 3, 2, 3, 8],
                                     [4, 8, 4, 8, 4]] # 'p = v' has been forbidden by shallow copy.
                                for i in range(5):
                                    for j in range(5):
                                        if Board[i][j].color:
                                            for x in range(5):
                                                for y in range(5):
                                                    if x == i and y == j:
                                                        continue
                                                    p[x][y] += 4 * 2 ** Board[i][j].color / ((i-x)**2 + (j-y)**2)
                                
                                for i in range(5):
                                    for j in range(5):
                                        if Board[i][j].color:
                                            p[i][j] = 0
                                for x in range(5):
                                    for y in range(5):
                                        if y:
                                            p[x][y] = math.ceil(3600 * p[x][y]) + p[x][y-1]
                                        else:
                                            if x:
                                                p[x][y] = math.ceil(3600 * p[x][y]) + p[x-1][4]
                                            else:
                                                p[x][y] = math.ceil(3600 * p[x][y])
                                q = random.randint(1,p[4][4])
                                for x in range(5):
                                    for y in range(5):
                                        if p[x][y] > q:
                                            Oper[1] = [x, y]
                                            break
                                    else:
                                        continue
                                    break
                    if Diff == 2:
                        if len(Oper[0]) == 2:
                            if Board[Oper[0][0]][Oper[0][1]].color:
                                Oper[0] = []
                                continue
                            if random.randint(0,3) or Priority:
                                evamax = -10000
                                Board[Oper[0][0]][Oper[0][1]].color = 1
                                VBoard = [[sentry() for i in range(5)] for j in range(5)]
                                VPt = [0, 0]
                                for x in range(5):
                                    for y in range(5):
                                        if not Board[x][y].color:
                                            for m in range(5):
                                                for n in range(5):
                                                    VBoard[m][n].level = Board[m][n].level
                                                    VBoard[m][n].color = Board[m][n].color
                                            VPt = [0, 0]
                                            VBoard[x][y].color = 2
                                            for i in range(5):
                                                for j in range(5):
                                                    if VBoard[i][j].color:
                                                        trigger = (VBoard[i][j].color * 2 - 3) * ((i-Oper[0][0])**2 + (j-Oper[0][1])**2 - (i-x)**2 - (j-y)**2)
                                                        if trigger > 0:
                                                            VBoard[i][j].upgrade()
                                                        if trigger < 0:
                                                            VBoard[i][j].score(False)
                                            eva = (VPt[1] - VPt[0]) * 16
                                            for i in range(5):
                                                if r == Round - 1:
                                                    break
                                                for j in range(5):
                                                    if VBoard[i][j].color:
                                                        if VBoard[i][j].level == 8:
                                                            eva += (VBoard[i][j].color * 2 - 3) * v[i][j] * 704
                                                        elif VBoard[i][j].level == 9:
                                                            eva += (VBoard[i][j].color * 2 - 3) * v[i][j] * 1056
                                                        else:
                                                            eva += (VBoard[i][j].color * 2 - 3) * v[i][j] * 3 * 2 ** VBoard[i][j].level
                                            if eva > evamax:
                                                evamax = eva
                                                Oper[1] = [x, y]
                                if Priority:
                                    Board[Oper[0][0]][Oper[0][1]].color = 2
                                    VBoard = [[sentry() for i in range(5)] for j in range(5)]
                                    VPt = [0, 0]
                                    evamin = 10000
                                    for x in range(5):
                                        for y in range(5):
                                            if not Board[x][y].color:
                                                for m in range(5):
                                                    for n in range(5):
                                                        VBoard[m][n].level = Board[m][n].level
                                                        VBoard[m][n].color = Board[m][n].color
                                                VPt = [0, 0]
                                                VBoard[x][y].color = 1
                                                for i in range(5):
                                                    for j in range(5):
                                                        if VBoard[i][j].color:
                                                            trigger = (VBoard[i][j].color * 2 - 3) * ((i-Oper[0][0])**2 + (j-Oper[0][1])**2 - (i-x)**2 - (j-y)**2)
                                                            if trigger < 0:
                                                                VBoard[i][j].upgrade()
                                                            if trigger > 0:
                                                                VBoard[i][j].score(False)
                                                eva = (VPt[1] - VPt[0]) * 16
                                                for i in range(5):
                                                    if r == Round - 1:
                                                        break
                                                    for j in range(5):
                                                        if VBoard[i][j].color:
                                                            if VBoard[i][j].level == 8:
                                                                eva += (VBoard[i][j].color * 2 - 3) * v[i][j] * 704
                                                            elif VBoard[i][j].level == 9:
                                                                eva += (VBoard[i][j].color * 2 - 3) * v[i][j] * 1056
                                                            else:
                                                                eva += (VBoard[i][j].color * 2 - 3) * v[i][j] * 3 * 2 ** VBoard[i][j].level
                                                if eva < evamin:
                                                    evamin = eva
                                    if evamin > evamax:
                                        Oper[1] = Oper[0]
                                Board[Oper[0][0]][Oper[0][1]].color = 0
                            else:
                                Oper[1] = Oper[0]
                pygame.display.update()
                pygame.event.pump()
        Board = [[sentry() for i in range(5)] for j in range(5)]
        Oper  = [[],[]]
        window.blit(pause, (725,555))
        Record.append(Pt)
        Pt = [0, 0]
        number(Record[g][0]).output(LINEbX if g%2 else LINErX, LINEbY if g%2 else LINErY, 30, 275+100*g ,  40)
        number(Record[g][1]).output(LINErX if g%2 else LINEbX, LINErY if g%2 else LINEbY, 30, 275+100*g , 125)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()
                    elif event.key == K_r:
                        Oper  = [[],[]]
                        Pt = [0, 0]
                        Record = []
                        Crush = 0
                        Board = [[sentry() for i in range(5)] for j in range(5)]
                        entrance()
                    else:
                        break
            else:
                pygame.time.delay(1)
                continue
            break
    red  = 0
    blue = 0
    for g in range(Game*2):
        red  += Record[g][0]
        blue += Record[g][1]
    if red > blue:
        window.blit(redwins , (0,0))
    elif red < blue:
        window.blit(bluewins, (0,0))
    else:
        window.blit(draw, (0,0))
    number(red ).output(LINErX, LINErY, 30, 280, 175)
    number(blue).output(LINEbX, LINEbY, 30, 880, 175)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == K_r:
                    Record = []
                    entrance()
                if event.key == K_p:
                    Record = []
                    vs(oppo)

if __name__ == '__main__':
    entrance()
