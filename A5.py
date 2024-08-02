"""
Aim: Using colour code to draw a pixel 
art pattern and the value contains the colour.
Author: Yiyang Yuan
yyua260
"""
from tkinter import *

def get_lines_from_file(filename):
    output = open(filename, "r")
    content = output.read()
    return content.split("\n")
    output.close()
    
def create_pattern_list(lines):
    lista = []
    listb = []
    for i in lines:
        for x in i:
            lista.append(x)
        listb.append(lista)
        lista = []
    return listb

def create_colour_dictionary(colours_list):
    dict1 = {}
    for i in colours_list:
        position = i.find(":")
        dict1[i[0]] = i[position + 1:]
    return dict1

def draw_pattern(a_canvas, colour_dictionary, pattern_list, size, start_x, start_y):
    number_of_rows = len(pattern_list)	
    number_of_columns = len(pattern_list[0])
    for i in range(number_of_rows):
        start_x = 100
        line = pattern_list[i]
        for x in range(number_of_columns):
            a_canvas.create_rectangle(start_x, start_y, start_x + size, start_y + size, fill = colour_dictionary[line[x]])
            start_x = start_x + size 
        start_y = start_y + size



#-------------------------------------------
#-------------------------------------------
# main() function
#-------------------------------------------
def main():
    size = 50
    start_x = size * 2
    start_y = size * 2
    name = input("Enter a name: ")
    palette_content = get_lines_from_file(name+"_palette.txt")
    colour_dictionary = create_colour_dictionary(palette_content)   
    pattern_content = get_lines_from_file(name+".txt")
    pattern_list = create_pattern_list(pattern_content)
    
    number_of_rows = len(pattern_list)	
    number_of_columns = len(pattern_list[0])
    canvas_width = size * number_of_columns +size * 4
    canvas_height = number_of_rows * size + size * 4
    window = Tk() 
    window.title("A5 by yyua260") 
    geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
    window.geometry(geometry_string)
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand = True)  
    draw_pattern(a_canvas, colour_dictionary, pattern_list, size, start_x, start_y)
    window.mainloop()


main()
