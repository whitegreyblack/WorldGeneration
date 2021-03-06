# COLOR FUNCTIONS
class Color:
    def __init__(self, r=None, g=None, b=None):
        self.color = (r, g, b)
    
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, rgb):
        r, g, b = rgb
        self.__color = combine_hex(
                        to_hex(r or 0), 
                        to_hex(g or 0), 
                        to_hex(b or 0))

def combine_hex(r, g, b):
    return '#' + r + g + b

def pad(value):
    if len(value) < 2:
        return "0" + value
    return value

def to_hex(value):
    return pad(hex(int(value)).split('x')[1])

def clamp(value):
    return max(0, min(value, 1))

def lerp(x, y, t):
    return int(round(x + t * (y-x)))

def norm(x, mini, maxa):
    return (x-mini)/(maxa-mini)

def plot(x, mini, maxa, tot):
    return norm(x, mini, maxa) * tot

def hval(x):
    return int(round(x*255))

def hcolor(x):
    if hval(.8) <= x < hval(1):
        return HEIGHT_SNOW
    elif hval(.6) <= x < hval(.8):
        return HEIGHT_ROCK
    elif hval(.4) <= x < hval(.6):
        return HEIGHT_FOREST
    elif hval(.3) <= x < hval(.4):
        return HEIGHT_GRASS
    elif hval(.2) <= x < hval(.3):
        return HEIGHT_SAND
    elif hval(.1) <= x < hval(.2):
        return HEIGHT_SHALLOW
    else:
        return HEIGHT_DEEP

RED = (250, 0, 0)
BLUE = (0,0,250)
BLACK = (0,0,0)
WHITE = (250,250,250)
LGRAY = (200,200,200)
MGRAY = (150,150,150)
DGRAY = (100,100,100)
HGRAY = (50,50,50)
GREEN = (0, 200, 0)
LGREEN = (100, 250, 100)
DGREEN = (10, 100, 10)
YELLOW = (200, 200, 50)
DYELLOW = (150, 150, 25)

# HEIGHT COLORING
HEIGHT_DEEP = (0, 0, 128)
HEIGHT_ROCK = (128, 128, 128)
HEIGHT_SAND = (240, 240, 64)
HEIGHT_SNOW = (255, 255, 255)
HEIGHT_GRASS = (50, 220, 20)
HEIGHT_FOREST = (16, 160, 0)
HEIGHT_SHALLOW = (25, 25, 150)


# BIOME COLORING
BIOME_ICE = (255, 255, 255)
BIOME_BOREAL = (95, 115, 62)
BIOME_DESERT = (238, 218, 130)
BIOME_TUNDRA = (96, 131, 112)
BIOME_SAVANNA = (177, 209, 110)
BIOME_TROPICS = (66, 123, 25)
BIOME_SEASONAL = (73, 100, 35)
BIOME_WOODLAND = (139, 175, 90)
BIOME_GRASSLAND = (164,225, 99)
BIOME_TEMPERATE = (29, 73, 40)

# HEAT MAP COLORING
HEAT_COLDEST = (0, 255, 255)
HEAT_COLDER = (170, 255, 255)
HEAT_COLD = (0, 229, 133)
HEAT_WARM = (255, 255, 100)
HEAT_WARMER = (255, 100, 0)
HEAT_WARMEST = (241, 12, 0)

# MOISTURE MAP COLORING
MOISTURE_DRYEST = (255, 139, 17)
MOISTURE_DRYER = (245, 245, 23)
MOISTURE_DRY = (80, 255, 0)
MOISTURE_WET = (85, 255, 255)
MOISTURE_WETTER = (20, 70, 255)
MOISTURE_WETTEST = (0,0, 100)

# MOISTURE x HEAT MAPPING
BIOMES = {
    0: { 0: BIOME_ICE, 1: BIOME_TUNDRA, 2: BIOME_GRASSLAND, 3: BIOME_DESERT, 4: BIOME_DESERT, 5: BIOME_DESERT },
    1: { 0: BIOME_ICE, 1: BIOME_TUNDRA, 2: BIOME_GRASSLAND, 3: BIOME_DESERT, 4: BIOME_DESERT, 5: BIOME_DESERT },
    2: { 0: BIOME_ICE, 1: BIOME_TUNDRA, 2: BIOME_WOODLAND, 3: BIOME_WOODLAND, 4: BIOME_SAVANNA, 5: BIOME_SAVANNA },
    3: { 0: BIOME_ICE, 1: BIOME_TUNDRA, 2: BIOME_BOREAL, 3: BIOME_WOODLAND, 4: BIOME_SAVANNA, 5: BIOME_SAVANNA },
    4: { 0: BIOME_ICE, 1: BIOME_TUNDRA, 2: BIOME_BOREAL, 3: BIOME_SEASONAL, 4: BIOME_TROPICS, 5: BIOME_TROPICS },
    5: { 0: BIOME_ICE, 1: BIOME_TUNDRA, 2: BIOME_BOREAL, 3: BIOME_TEMPERATE, 4: BIOME_TROPICS, 5: BIOME_TROPICS },
}

colors = [
    (0,0,0),
    (1,0,103),
    (213,255,0),
    (255,0,86),
    (158,0,142),
    (14,76,161),
    (255,229,2),
    (0,95,57),
    (0,255,0),
    (149,0,58),
    (255,147,126),
    (164,36,0),
    (0,21,68),
    (145,208,203),
    (98,14,0),
    (107,104,130),
    (0,0,255),
    (0,125,181),
    (106,130,108),
    (0,174,126),
    (194,140,159),
    (190,153,112),
    (0,143,156),
    (95,173,78),
    (255,0,0),
    (255,0,246),
    (255,2,157),
    (104,61,59),
    (255,116,163),
    (150,138,232),
    (152,255,82),
    (167,87,64),
    (1,255,254),
    (255,238,232),
    (254,137,0),
    (189,198,255),
    (1,208,255),
    (187,136,0),
    (117,68,177),
    (165,255,210),
    (255,166,254),
    (119,77,0),
    (122,71,130),
    (38,52,0),
    (0,71,84),
    (67,0,44),
    (181,0,255),
    (255,177,103),
    (255,219,102),
    (144,251,146),
    (126,45,210),
    (189,211,147),
    (229,111,254),
    (222,255,116),
    (0,255,120),
    (0,155,255),
    (0,100,1),
    (0,118,255),
    (133,169,0),
    (0,185,23),
    (120,130,49),
    (0,255,198),
    (255,110,65),
    (232,94,190),
]
