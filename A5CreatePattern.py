"""
Aim: Using colour code to art pattern.
Author: Yiyang Yuan
yyua260
"""

def create_basic_pattern(background_colour, size):
    lista = []
    string = ""
    for x in range(size):
        string = background_colour * size
        lista.append(string)
    return lista

def update_pattern(pattern, codes_list):
    for i in codes_list:
        code = i
        colour = code[0]
        row = code[1]
        column = code[2]
        string = pattern[int(row)]
        str1 = string[:int(column)]
        str2 = string[int(column) + 1:]
        new = str1 + colour + str2
        pattern[int(row)] = new
    return pattern

def write_pattern_to_file(pattern):
    output = open("yyua260.txt", "w")
    length = len(pattern)
    for i in range(length):
        output.write(pattern[i] + "\n")
    output.close()

#-------------------------------------------
#-------------------------------------------
# main() function
#-------------------------------------------
    
def main():
    codes_list = ['b41', 'b42', 'b45', 'b46', 'b53', 'b54']
    background_colour = 'y'
    pattern = create_basic_pattern(background_colour, 8)
    update_pattern(pattern, codes_list)
    write_pattern_to_file(pattern)

main()
    
