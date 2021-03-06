import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 16
TITLE = "Blake and Shiler's Game"
BGCOLOR = BLACK

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 100
PLAYER_IMG_1 = 'female_front.png'
PLAYER_IMG_2 = 'female_front_l.png'
PLAYER_IMG_3 = 'female_front_r.png'
PLAYER_IMG_4 = 'female_back.png'
PLAYER_IMG_5 = 'female_back_l.png'
PLAYER_IMG_6 = 'female_back_r.png'
PLAYER_IMG_7 = 'female_right.png'
PLAYER_IMG_8 = 'female_right_l.png'
PLAYER_IMG_9 = 'female_right_r.png'
PLAYER_IMG_10 = 'female_left.png'
PLAYER_IMG_11 = 'female_left_l.png'
PLAYER_IMG_12 = 'female_left_r.png'

PLAYER_HIT_RECT = pg.Rect(0, 0, 24, 36)


# Map List
map_dict = {'home_interior':'home_interior.tmx','home_exterior':'home_exterior.tmx',
            'cross_roads':'cross_roads.tmx','town_square':'town_square.tmx',
            'town_shop':'town_shop.tmx','town_house_1':'town_house_1.tmx',
            'town_house_2':'town_house_2.tmx','town_mayor_house':'town_mayor_house.tmx',
            'wild_field_1':'wild_field_1.tmx','wild_field_2':'wild_field_2.tmx',
            'dungeon_1_floor_1':'dungeon_1_floor_1.tmx'}


background = ['Tile Layer 1','Tile Layer 2','Tile Layer 3']

forground = ['Tile Layer 4','Tile Layer 5','Tile Layer 6']
forground_1 = 'Tile Layer 4'




start_map = map_dict['home_interior']
back = map_dict['home_interior']
front = map_dict['home_interior']


play_map = start_map
play_map_background = back
play_map_forground = front



####   States

state_dict = {}








# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2