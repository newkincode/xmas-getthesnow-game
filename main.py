import pygame #모듈 불러오기
import random
from tkinter import messagebox as msgbox

pygame.init() #파이게임 초기화

#변수
color = (130, 202, 255) #튜플 변수(컬러값 변수)
play = True #게임 실행
to_x = 0
period=30

clock = pygame.time.Clock()
#화면크기
screen_width = 500
screen_height = 500
#이미지 불러오기
background = pygame.image.load("img/background.png") #배경이미지 불러오기
playerImg = pygame.image.load("img/player1.png") #플래이어 불러오기
stoneImg = pygame.image.load("img/stone.png") #돌 불러오기
#이미지 위치 불러오기
#플래이어
player_size = playerImg.get_rect().size #플래이어 크기 불러오기
player_x = player_size[0] #플래이어 가로크기
player_y = player_size[1] #플래이어 세로크기
#돌
stone_size = stoneImg.get_rect().size #돌 크기 불러오기
stone_x = stone_size[0] #돌 가로크기
stone_y = stone_size[1] #돌 세로크기
#플래이어 가운대로 이동
player_x_pos = (screen_width/2) - (player_x/2)
player_y_pos = screen_height - player_y
#좌표
stone_x_pos = 10 #돌 x좌표
stone_y_pos = 10 #돌 y좌표
#음악

main_bgm=pygame.mixer.Sound("bgm/main_bgm.mp3")
main_bgm.play(-1)

screen = pygame.display.set_mode((screen_width, screen_height)) #스크린 변수만들기, 창크기 조절
pygame.display.set_caption("돌피하기") #창 이름 정하기
screen.fill(color) #창색 정하기

#클래스
class Stone:
    def __init__(self, xPos, yPos, speed):
        self.x = xPos
        self.y = yPos
        self.speed = speed
        #print("copy stone", self.x)

    def draw(self, img):
        screen.blit(img, (self.x, self.y))

    def move(self):
        self.y += self.speed  #돌 떨어지기
    def re_spawn(self):
        self.x = random.randint(10,490)

    def off_scren(self):
        return self.y >= 500

    #def __del__(self):
        #print("del stone", self.x)

    def check_collision(self, players, stone):
        # rect 변수
        self.player_rect = playerImg.get_rect()
        self.player_rect.left = players.playerXPos
        self.player_rect.top = players.playerYPos

        self.stone_rect = stoneImg.get_rect()
        self.stone_rect.left = self.x
        self.stone_rect.top = self.y

        # 충돌하면 게임오버
        if self.player_rect.colliderect(self.stone_rect):
            return True

class player:
    def __init__(self, playerXPos, playerYPos):
        self.playerXPos = playerXPos
        self.playerYPos = playerYPos
        self.life = 0
        self.setFont = pygame.font.SysFont("font.ttf",30)
        self.textColor = (0,0,0)
        self.speed = 5

    def move(self, dir):
        if dir == "left":
            self.playerXPos += self.speed
        elif dir == "right":
            self.playerXPos -= self.speed

        if self.playerXPos < 0:
            self.playerXPos += 5
        elif self.playerXPos > screen_width-32:
            self.playerXPos -= 5

    def draw(self, img):
        screen.blit(img, (self.playerXPos, self.playerYPos))

class life:
    def __init__(self):
        self.setFont = pygame.font.Font("font.ttf",30)

    def setText(self, life_num):
        text = self.setFont.render(str(life_num), True, (0,0,0))
        screen.blit(text, (50,50))

stones = []

#object1 = Stone(stone_x_pos, stone_y_pos, 1)
#stones.append(object1)
players = player(player_x_pos, 430)
lifes = life()
count = 0
buff=False
buffcount=0
isbuff=0
fps = 100
while play:
    clock.tick(fps)
    # 키 이벤트
    for event in pygame.event.get():  # 키입력 감지
        # 나가기
        if event.type == pygame.QUIT:  # 나가기 버튼 눌럿을때
            play = False  # 와일문 나가기
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dir = "left"
            elif event.key == pygame.K_LEFT:
                dir = "right"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                dir = ""
            elif event.key == pygame.K_LEFT:
                dir = ""

    count += 1
    if count > period:
        object1 = Stone(random.randint(10, 490), stone_y_pos, random.randint(1, 10))
        stones.append(object1)
        count = 0

    if isbuff==50:
        print(buff)
        buff=True
        isbuff=0
    if buff==True:
        print(period)
        if buffcount == 100:
            period=30
            buff=False
            buffcount=0
        else:
            buffcount+=1
            period=10

    print(isbuff)

    screen.blit(background, (0, 0))  # 배경 적용하기
    players.draw(playerImg)
    # 움직이기
    players.move(dir)
    # 생명 표시
    lifes.setText(players.life)

    i = 0
    while i < len(stones):
        stones[i].draw(stoneImg)
        stones[i].move()


        if stones[i].off_scren():
            del stones[i]
            i -= 1
        elif stones[i].check_collision(players,stones[i]):

            players.life += 1
            isbuff+=1
            del stones[i]
            i -= 1
        i += 1

    pygame.display.update()  # 파이게임 업데이트
pygame.quit() #파이게임 나가기
# TODO : 50게 마다 빙수 변수 1추가 빙수 하나마다 1초마다 1달러 추가