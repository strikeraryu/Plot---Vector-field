import pygame
import os
import math
pygame.init()

# CONSTANTS

# Lenght of window
len = 800
# Magnification factor (1 unit = mag)
mag = 40
# Thickness of vector
thk = 15
# Range factor of vector lenght(i.e the possible number of lenght of vector is vec_rng)
vec_rng = 20
# Pi value
pi = 3.14159265359

bg_col = (255, 255, 255)
ln_col = (0, 0, 0)

#colour variation
col_var = False

# vector image
vector = pygame.image.load(os.path.join('images', 'vector.png'))
# vector image with colour variation
c_vector = [pygame.image.load(os.path.join('images', 'col_vector (1).png')), pygame.image.load(os.path.join('images', 'col_vector (2).png')), pygame.image.load(os.path.join('images', 'col_vector (3).png')), pygame.image.load(os.path.join('images', 'col_vector (4).png')), pygame.image.load(os.path.join('images', 'col_vector (5).png')), pygame.image.load(os.path.join('images', 'col_vector (6).png')), pygame.image.load(os.path.join('images', 'col_vector (7).png')), pygame.image.load(os.path.join('images', 'col_vector (8).png')), pygame.image.load(os.path.join('images', 'col_vector (9).png')), pygame.image.load(os.path.join('images', 'col_vector (10).png')), pygame.image.load(os.path.join('images', 'col_vector (11).png'))]
win = pygame.display.set_mode((len, len))
pygame.display.set_caption("PLOT - Vector Field")

# To calculate distance


def dist(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

# To calculate the value of a vector


def modu(x, y):
    return (x**2+y**2)**0.5

# To draw the vector on [x,y] coordinate with slope tan(ang) and value related to fact


def draw_vect(x, y, ang, fact):
    # To convert the coordinates
    x = x*mag+(len)/2
    y = (-y*mag)+len/2
    # Transformation of vector lenght
    fact = round(vec_rng - fact)
    wth = mag-1*fact
    if col_var:
        tmp_vector = c_vector[int(fact/2)]
    else:
        tmp_vector = vector
    tmp_vector = pygame.transform.scale(tmp_vector, (wth, thk))
    # To rotate the vector such that slope is tan(ang)
    ang = math.degrees(ang)
    tmp_vector = pygame.transform.rotate(tmp_vector, ang)
    # The new coordintes of the tip of vector
    rect = tmp_vector.get_rect(center=[x, y])
    win.blit(tmp_vector, rect)

# To plot the graph  of vector field eq_x i + eq_y j


def plot_graph(eq_x, eq_y, min, max):
    x = (-len/2)/mag
    while x <= (len/2)/mag:
        y = (-len/2)/mag
        while y <= (len/2)/mag:
            try:
                tmp_x = eval(eq_x)
                tmp_y = eval(eq_y)
            except ZeroDivisionError:
                y += 1
                continue
            ang = math.atan2(tmp_y, tmp_x)
            # To calculate lenght factor
            rng = (min+max)/vec_rng
            fact = (modu(tmp_x, tmp_y)-min)/rng
            # Wrong vector at [0, 0]
            if x != 0 or y != 0:
                draw_vect(x, y, ang, fact)
            pygame.display.update()
            y += 1
        x += 1

# To calculate min and max vale of eq_x i + eq_y j


def min_max(eq_x, eq_y):
    x = (-len/2)/mag
    min = 1000000000
    max = 0
    while x <= (len/2)/mag:
        y = (-len/2)/mag
        while y <= (len/2)/mag:
            try:
                tmp_x = eval(eq_x)
                tmp_y = eval(eq_y)
            except ZeroDivisionError:
                y += 1
                continue
            if min > modu(tmp_x, tmp_y):
                min = modu(tmp_x, tmp_y)
            if max < modu(tmp_x, tmp_y):
                max = modu(tmp_x, tmp_y)
            y += 1
        x += 1
    return min, max


# To draw the graph
def draw_graph():
    pygame.draw.rect(win, bg_col, (0, 0, len, len))
    pygame.draw.line(win, ln_col, (0, len/2), (len, len/2), 3)
    pygame.draw.line(win, ln_col, (len/2, 0), (len/2, len), 3)
    for i in range(0, len+1, mag):
        pygame.draw.line(win, ln_col, (i, 0), (i, len), 1)
        pygame.draw.line(win, ln_col, (0, i), (len, i), 1)
    pygame.display.update()


# dipole equation
di_pole = '((x-5)/(((x-5)**2+y**2)**1.5))-((x+5)/(((x+5)**2+y**2)**1.5))i+(y/(((x-5)**2+y**2)**1.5))-(y/(((x+5)**2+y**2)**1.5))j'
# qudrupole equation
quad_pole = '((x-5)/(((x-5)**2+(y-5)**2)**1.5))-((x-5)/(((x-5)**2+(y+5)**2)**1.5))+((x+5)/(((x+5)**2+(y+5)**2)**1.5))-((x+5)/(((x+5)**2+(y-5)**2)**1.5))i+((y-5)/(((x-5)**2+(y-5)**2)**1.5))+((y+5)/(((x+5)**2+(y+5)**2)**1.5))-((y+5)/(((x-5)**2+(y+5)**2)**1.5))-((y-5)/(((x+5)**2+(y-5)**2)**1.5))j'

# Enter you equation here
equation = di_pole


# To slice the equation
equation = equation[:-1]
eq_x, eq_y = equation.split('i')
min, max = min_max(eq_x, eq_y)
draw_graph()
plot_graph(eq_x, eq_y, min, max)
# To quit the program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()