# -*- coding: utf-8 -*-
"""
Random_art.py

@author: amonmillner, adapted from pruvolo work
"""

# you do not have to use these particular modules, but they may help
from random import randint
from PIL import Image
from math import *

def build_random_function(min_depth, max_depth):
    """ This function takes in two inputs: min_depth and max_depth. The input min_depth specifies the minimum amount of nesting for the function that you generate.  The input max_depth specifies the maximum amount of nesting of the function that you generate.
    """

    if (min_depth <= 1 and randint(0,1)) or (max_depth == 1):
        if randint(0,1):
            return ["x"]
        return ["y"]
    
    z = randint(0,2)
    if z == 0:  
        return ["prod",build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
    elif z == 1:
        return ["cos_pi",build_random_function(min_depth-1,max_depth-1)]
    else: 
        return ["sin_pi",build_random_function(min_depth-1,max_depth-1)]


def evaluate_random_function(f, x, y):
    """ This function takes three inputs. 
        The first input is the random function generated using the function build_random_function; the second input is the value of x to evaluate the function at; and the third input is the value of y to evaluate the function at. 
        The output of this function is the value of the input function evaluated at the input (x,y) pair.
    """

    if f[0] == "prod":
        return evaluate_random_function(f[1],x,y) * evaluate_random_function(f[2],x,y)
    elif f[0] == "sin_pi":
        return sin(evaluate_random_function(f[1],x,y) * pi)
    elif f[0] == "cos_pi":
        return cos(evaluate_random_function(f[1],x,y) * pi)
    elif f[0] == "x":
        return x
    else:
        return y


def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    """
    
    return ((float(val-input_interval_start) * (output_interval_end-output_interval_start)) / (input_interval_end-input_interval_start)) + output_interval_start

    
# v = build_random_function(2,10)
# print v
# print evaluate_random_function(v, -1, 1)

a = randint(2,10)
b = randint(2,10)
c = randint(2,10)
red = build_random_function(a, a + 5)
green = build_random_function(b, b + 5)
blue = build_random_function(c, c + 5)
im = Image.new("RGB",(350,350))

pixel = im.load()
for x in xrange(350):
    x2 = remap_interval(x,0,350,-1,1)
    for y in xrange(350):
        y2 = remap_interval(y,0,350,-1,1)
        r = evaluate_random_function(red,x2,y2)
        g = evaluate_random_function(green,x2,y2)
        b = evaluate_random_function(blue,x2,y2)
        r2 = remap_interval(r,-1,1,0,255)
        g2 = remap_interval(g,-1,1,0,255)
        b2 = remap_interval(b,-1,1,0,255)
        pixel[x,y] = (int(r2),int(g2),int(b2))

im.show()
im.save("example2.png")