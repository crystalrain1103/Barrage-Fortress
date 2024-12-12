from pygame.locals import  *

##Music config
CYCLE = -1
MUSIC_VOLUME = 0.5

##Color config
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
GREEN = (0, 128, 0)

##Screen config
LEFT_BORDER_FOR_STAFF = 0
RIGHT_BORDER_FOR_STAFF = 1090
UP_BORDER_FOR_STAFF = 0
DOWN_BORDER_FOR_STAFF = 600
LEFT_BORDER_FOR_BOSS_STAGE1 = 0
RIGHT_BORDER_FOR_BOSS_STAGE1 = 1100
UP_BORDER_FOR_BOSS_STAGE1 = 50
DOWN_BORDER_FOR_BOSS_STAGE1 = 550
LEFT_BORDER_FOR_BOSS_STAGE2 = 0
RIGHT_BORDER_FOR_BOSS_STAGE2 = 1200
UP_BORDER_FOR_BOSS_STAGE2 = 0
DOWN_BORDER_FOR_BOSS_STAGE2 = 660
LEFT_BORDER = -50
RIGHT_BORDER = 1330
UP_BORDER = -50
DOWN_BORDER = 770
LEFT_TOP = (1000, 50)
GRID = 80
SCREEN_SIZE = (1280, 720)
TITLE = ('咪咪咪离离原上咪😺咪咪咪一岁一咪咪🐱咪咪咪野火哈基米🐈春风~春风~吹又咪',
         '这个王师傅也是有意思，一有人上厕所就要跳出来发表一下意见😅',
         '爽！😎这才叫音乐！😋👍🏻爽！😎这才叫音乐！😋👍🏻爽！😎这才叫音乐！',
         '肚子巨型，牙齿宇宙，技术探底，颜值腐蚀，舞台剧暴怒，对局交易，手在下面快枪，快枪完微缩',
         '这个古夫也是有意思，明知道主播喜欢上厕所还在这嘘嘘嘘',
         '那今天就到这里哈🤓👉我去吃饭了哈🤓👆大家晚安🤓👈大家明天见🤓👇',
         '《合了一套神棍大哥德😃》《终于排到神棍老师了🤩》《咦？他怎么是术士？🤔》《叮！😡》',
         '时间流，揭示了齿轮变速的潜力！⚙️👋😡 扫清了邪恶的评论👐',
         '这个geyuan6怎么刷弹幕这么快，不会看直播也用变速齿轮吧😓'
         )

ORIGIN = (0, 0)

ICON_PATH = '../pic/Icon/icon.jpg'
GAME_BACKGROUND_PATH = '../pic/Background/background.png'

##Menu config
MENU_BACKGROUND_PATH = '../pic/Menu/menu.jpg'
MAIN_MENU_TITLE = '（伪）狂弹要塞 ver.alpha'
MAIN_TITLE_LOC = (400, 200)
DIFFICULTY_PIC_PATH = '../pic/Menu/difficulty.jpg'
DIFFICULTY_TITLE_LOC = (450, 200)
DIFFICULTY_PIC_RECT = (700, 150, 100, 100)
DIFFICULTY_PIC_SIZE = (100, 100)

SETTINGS_BUTTON_ID = 0
START_BUTTON_ID = 1
QUIT_BUTTON_ID = 2
PRESENT_BUTTON_ID = 3
FUTURE_BUTTON_ID = 4
BEYOND_BUTTON_ID = 5
DIFFICULTY_BACK_BUTTON_ID = 6
SETTINGS_TEMP_DIALOG_ID = 7

##Font config
FONT_SIZE = 40
PAUSE_FONT_SIZE = 100
TIME_MAIN_COLOR_FONT_LOC = (10, 20)
TIME_SHADOW_COLOR_FONT_LOC = (13, 23)
POINTS_MAIN_COLOR_FONT_LOC = (300, 20)
POINTS_SHADOW_COLOR_FONT_LOC = (303, 23)
PAUSE_MAIN_COLOR_FONT_LOC = (500, 250)
PAUSE_SHADOW_COLOR_FONT_LOC = (503, 253)

##Object config
CONVICTION_BULLET_ID = 0
CONVICTION_ID = 1
CONVICTION_POS = (0, 200)
BUFF_ID = 2
HEAL_ID = 3
PLANE_LEVEL1_ID = 4
BOSS_STAGE1_ID = 5
BOSS_STAGE2_ID = 6
NORMAL_BULLET_ID = 7
SPECIAL_BULLET_ID = 8
PLANE_ICE_ID = 9

SPAWN_BOSS_TIME = 60
BUFF_BONUS = 2
DEBUFF_EFFECT = 3
HITBOX = 10
##Game config
KEY_DELAY = 10
KEY_INTERVAL = 2
DETECT_TIME = 1
MOVE = (K_a, K_w, K_s, K_d)
PAUSE = (K_ESCAPE, )

COLD_PATH = '../pic/Condition/cold.png'
COLD_SIZE = (50, 50)
LOSE_AUDIO_PATH = '../music/lose_audio.mp3'
LOSE_ANIME_PATH = '../pic/LoseAnime/losePic.png'
WIN_AUDIO_PATH = '../music/win_audio.mp3'
WIN_ANIME_PATH = '../pic/WinAnime/%d.png'