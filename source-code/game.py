import pygame
import random
import time
import timer
import data_difficulty
import image
import conviction
import heal
import buff
import planelevel1
import planeice
import boss_stage1
import boss_stage2
from const import *

def getGameTime():
    return time.time() - timer.getPauseTime()

def doFight(a, b):
    a.hp -= b.dmg
    b.hp -= a.dmg
    if a.hp < 0:
        a.hp = 0
    if b.hp < 0:
        b.hp = 0

class Game(object):
    def __init__(self, screen, difficulty):
        self.screen = screen
        self.difficulty = difficulty
        self.background = image.Image(GAME_BACKGROUND_PATH, 0,
                                      False, False, None, False, None,
                                      False, None, 0,
                                      False, None, 0,
                                      ORIGIN, SCREEN_SIZE, 0)
        self.staff_conviction = conviction.Conviction(CONVICTION_ID, CONVICTION_POS)
        self.boss_stage1 = boss_stage1.BossStage1(BOSS_STAGE1_ID, LEFT_TOP)
        self.boss_stage2 = boss_stage2.BossStage2(BOSS_STAGE2_ID, LEFT_TOP)
        self.staffs = [self.staff_conviction]
        self.enemies = []
        self.specials = []
        self.friendly_bullets = []
        self.enemy_bullets = []
        self.special_summons = []
        self.timeCnt = ('00', '00')
        self.killCnt = 0
        self.timeFont = pygame.font.Font(None, FONT_SIZE)
        self.killFont = pygame.font.Font(None, FONT_SIZE)
        self.planeiceGenerateTime = 0
        self.planelevel1GenerateTime = 0
        self.buffGenerateTime = 0
        self.healGenerateTime = 0
        self.doBossSpawn = False
        self.win = False
        self.lose = False
        self.getDifficultyConst()
        pygame.mixer.music.set_volume(MUSIC_VOLUME)
        pygame.mixer.music.load(self.musicPath)
        pygame.mixer.music.play(CYCLE)


    def getData(self):
        return data_difficulty.data[self.difficulty]

    def getDifficultyConst(self):
        self.healBonus = self.getData()['HEAL_BONUS']
        self.buffTime = self.getData()['BUFF_TIME']
        self.debuffRange = self.getData()['DEBUFF_RANGE']
        self.spawnBuffCD = self.getData()['SPAWN_BUFF_CD']
        self.spawnHealCD = self.getData()['SPAWN_HEAL_CD']
        self.spawnPlaneLevel1CD = self.getData()['SPAWN_PLANE_LEVEL1_CD']
        self.spawnPlaneIceCD = self.getData()['SPAWN_PLANE_ICE_CD']
        self.musicPath = self.getData()['MUSIC_PATH']

    def renderFont(self):
        self.timeCnt = timer.fTime()
        textImage = self.timeFont.render("Time : " + str(self.timeCnt[0]) + ":" + str(self.timeCnt[1]), True, BLACK)
        self.screen.blit(textImage, TIME_SHADOW_COLOR_FONT_LOC)
        textImage = self.timeFont.render("Time : " + self.timeCnt[0] + ":" + self.timeCnt[1], True, WHITE)
        self.screen.blit(textImage, TIME_MAIN_COLOR_FONT_LOC)

        textImage = self.timeFont.render("Points : " + str(self.killCnt), True, BLACK)
        self.screen.blit(textImage, POINTS_SHADOW_COLOR_FONT_LOC)
        textImage = self.timeFont.render("Points : " + str(self.killCnt), True, WHITE)
        self.screen.blit(textImage, POINTS_MAIN_COLOR_FONT_LOC)

    def draw(self):
        self.background.draw(self.screen)
        for staff in self.staffs:
            staff.draw(self.screen)
            staff.drawHPBar(self.screen, GREEN, RED)
        for enemy in self.enemies:
            enemy.draw(self.screen)
            enemy.drawHPBar(self.screen, GREEN, RED)
        for special in self.specials:
            special.draw(self.screen)
        for bullet in self.friendly_bullets:
            bullet.draw(self.screen)
        for bullet in self.enemy_bullets:
            bullet.draw(self.screen)
        self.renderFont()

    def update(self):
        self.background.update()

        for staff in self.staffs:
            staff.update()
            if staff.hasSummon():
                bullet = staff.doSummon()
                if bullet is not None:
                    for i in range(len(bullet)):
                        self.friendly_bullets.append(bullet[i])

        for special in self.specials:
            special.update()
            if special.hasSummon():
                summon = special.doSummon()
                if summon is not None:
                    for i in range(len(summon)):
                        self.special_summons.append(summon[i])

        for enemy in self.enemies:
            enemy.update()
            if enemy.hasSummon():
                bullet = enemy.doSummon()
                if bullet is not None:
                    for i in range(len(bullet)):
                        self.enemy_bullets.append(bullet[i])

        for bullet in self.friendly_bullets:
            bullet.update()
        for bullet in self.enemy_bullets:
            bullet.update()
        for summon in self.special_summons:
            summon.update()

        self.checkSpawn()
        self.checkOutMap()
        self.checkBuff()
        self.checkDebuff()
        self.checkFight()
        self.checkRevive()
        self.checkDie()

    def checkSpawn(self):
        if getGameTime()  - self.planeiceGenerateTime > self.spawnPlaneIceCD:
            self.planeiceGenerateTime = getGameTime()
            self.addPlane_Ice(1, random.randint(0, 6))

        if getGameTime()  - self.planelevel1GenerateTime > self.spawnPlaneLevel1CD:
            self.planelevel1GenerateTime = getGameTime()
            self.addPlane_level1(1, random.randint(0, 6))

        if getGameTime() - self.buffGenerateTime > self.spawnBuffCD:
            self.buffGenerateTime = getGameTime()
            self.addBuff(1, random.randint(0, 6))

        if getGameTime() - self.healGenerateTime > self.spawnHealCD:
            self.healGenerateTime = getGameTime()
            self.addHeal(1, random.randint(0, 6))

        if timer.getTotalTime() > SPAWN_BOSS_TIME and not self.doBossSpawn:
            self.enemies.append(self.boss_stage1)
            self.doBossSpawn = True

    def checkOutMap(self):
        for bullet in self.friendly_bullets:
            if not(LEFT_BORDER < bullet.getRect().x < RIGHT_BORDER and UP_BORDER < bullet.getRect().y < DOWN_BORDER):
                self.friendly_bullets.remove(bullet)
                break
        for bullet in self.enemy_bullets:
            if not(LEFT_BORDER < bullet.getRect().x < RIGHT_BORDER and UP_BORDER < bullet.getRect().y < DOWN_BORDER):
                self.enemy_bullets.remove(bullet)
                break
        for summon in self.special_summons:
            if not(LEFT_BORDER < summon.getRect().x < RIGHT_BORDER and UP_BORDER < summon.getRect().y < DOWN_BORDER):
                self.friendly_bullets.remove(summon)
                break
        for special in self.specials:
            if not(LEFT_BORDER < special.getRect().x < RIGHT_BORDER and UP_BORDER < special.getRect().y < DOWN_BORDER):
                self.specials.remove(special)
                break
        for enemy in self.enemies:
            if not(LEFT_BORDER < enemy.getRect().x < RIGHT_BORDER and UP_BORDER < enemy.getRect().y < DOWN_BORDER):
                if enemy not in (self.boss_stage1, self.boss_stage2):
                    self.enemies.remove(enemy)
                    break

    def checkBuff(self):
        for staff in self.staffs:
            if getGameTime() - staff.getBuffTime >= self.buffTime:
                staff.removeBuffed()

            for special in self.specials:
                if staff.isCollide(special):
                    if special.hasBuff:
                        self.specials.remove(special)
                        staff.preBuffed(getGameTime())
                    if special.hasHeal:
                        self.specials.remove(special)
                        staff.hp += self.healBonus
                        if staff.hp > staff.getHP():
                            staff.hp = staff.getHP()


    def checkDebuff(self):
        for enemy in self.enemies:
            for staff in self.staffs:
                if enemy.hasDebuff:
                    if -self.debuffRange < enemy.pos[0] - staff.pos[0] < self.debuffRange and\
                    -self.debuffRange < enemy.pos[1] - staff.pos[1] < self.debuffRange:
                        coldPic = pygame.image.load(COLD_PATH)
                        coldPic = pygame.transform.scale(coldPic, COLD_SIZE)
                        rect = staff.getRect()
                        self.screen.blit(coldPic, (rect.x + 30, rect.y - 30, rect.width, rect.height))
                        pygame.display.update()
                        staff.preDebuffed()
                    else:
                        staff.removeDebuffed()

    def checkFight(self):
        for bullet in self.friendly_bullets:
            for enemy in self.enemies:
                if bullet.isCollide(enemy):
                    doFight(bullet, enemy)
                    if enemy.hp <= 0:
                        if enemy.hasRevive:
                            enemy.revive = True
                        else:
                            enemy.die = True
                    if bullet in self.friendly_bullets:
                        self.friendly_bullets.remove(bullet)

        for bullet in self.enemy_bullets:
            for staff in self.staffs:
                if bullet.checkHit(staff):
                    doFight(bullet, staff)
                    if staff.hp <= 0:
                        if staff is self.staff_conviction:
                            self.lose = True
                        else:
                            self.staffs.remove(staff)
                    if bullet in self.enemy_bullets:
                        self.enemy_bullets.remove(bullet)

        for bullet1 in self.friendly_bullets:
            for bullet2 in self.enemy_bullets:
                if (bullet1.tearShield or bullet2.tearShield) and bullet1.isCollide(bullet2):
                    if bullet1 in self.friendly_bullets:
                        self.friendly_bullets.remove(bullet1)
                    if bullet2 in self.enemy_bullets:
                        self.enemy_bullets.remove(bullet2)

    def checkRevive(self):
        for enemy in self.enemies:
            if not enemy.doRevive:
                enemy.pathIndex = 0
                enemy.doRevive = True
            if enemy in self.enemies and enemy.revive and enemy.pathIndex == enemy.revivePathIndexCount - 1:
                if enemy is self.boss_stage1:
                    self.enemies.remove(enemy)
                    self.boss_stage2 = boss_stage2.BossStage2(BOSS_STAGE2_ID, enemy.pos)
                    self.enemies.append(self.boss_stage2)

    def checkDie(self):
        for enemy in self.enemies:
            if not enemy.doDie:
                enemy.pathIndex = 0
                enemy.doDie = True
            if enemy in self.enemies and enemy.die and enemy.pathIndex == enemy.diePathIndexCount - 1:
                self.enemies.remove(enemy)
                self.killCnt += 1
                if enemy is self.boss_stage2:
                    self.win = True

    def keyPressedHandler(self, key):
         if key in MOVE:
            self.staff_conviction.doMove(key)

    def showPause(self):
        pauseFont = pygame.font.Font(None, PAUSE_FONT_SIZE)
        textImage = pauseFont.render('PAUSE', True, BLACK)
        self.screen.blit(textImage, PAUSE_SHADOW_COLOR_FONT_LOC)
        textImage = pauseFont.render('PAUSE', True, WHITE)
        self.screen.blit(textImage, PAUSE_MAIN_COLOR_FONT_LOC)

    def addPlane_Ice(self, x, y):
        pos = LEFT_TOP[0] + x * GRID, LEFT_TOP[1] + y * GRID
        Plane_Ice = planeice.PlaneIce(PLANE_ICE_ID, pos)
        self.enemies.append(Plane_Ice)

    def addPlane_level1(self, x, y):
        pos = LEFT_TOP[0] + x * GRID, LEFT_TOP[1] + y * GRID
        Plane_level1 = planelevel1.PlaneLevel1(PLANE_LEVEL1_ID, pos)
        self.enemies.append(Plane_level1)

    def addBuff(self, x, y):
        pos = LEFT_TOP[0] + x * GRID, LEFT_TOP[1] + y * GRID
        Buff = buff.Buff(BUFF_ID, pos)
        self.specials.append(Buff)

    def addHeal(self, x, y):
        pos = LEFT_TOP[0] + x * GRID, LEFT_TOP[1] + y * GRID
        Heal = heal.Heal(HEAL_ID, pos)
        self.specials.append(Heal)

    def selectDifficulty(self, difficulty):
        self.difficulty = difficulty

    def gameEnd(self):
        if self.win:
            self.winEvent()
            return True
        elif self.lose:
            self.loseEvent()
            return True
        else:
            return False

    def winEvent(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        winAnime = image.Image(WIN_ANIME_PATH, 0,
                               False, False, None, False, None,
                               False, None, 0,
                               False, None, 0,
                               ORIGIN, SCREEN_SIZE, 41)
        pygame.mixer.music.load(WIN_AUDIO_PATH)
        pygame.mixer.music.play(1)
        pygame.time.wait(250)
        while True:
            if winAnime.pathIndex < winAnime.pathIndexCount - 1:
                winAnime.pathIndex += 1
                winAnime.updateImage()
                self.background.draw(self.screen)
                winAnime.draw(self.screen)
                pygame.display.update()
            else:
                if not pygame.mixer.music.get_busy():
                    break

        pygame.mixer.music.unload()

    def loseEvent(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        loseAnime = image.Image(LOSE_ANIME_PATH, 0,
                               False, False, None, False, None,
                               False, None, 0,
                               False, None, 0,
                               ORIGIN, SCREEN_SIZE, 0)
        pygame.mixer.music.load(LOSE_AUDIO_PATH)
        pygame.mixer.music.play(1)
        loseAnime.draw(self.screen)
        pygame.display.update()
        pygame.time.wait(2500)
        while True:
            if not pygame.mixer.music.get_busy():
                break

        pygame.mixer.music.unload()
