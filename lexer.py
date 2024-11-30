import sys

# GLOBAL VARIABLES AND LISTS
premenna = ''
cislo = ''
ident = False
number = False
length_chr = 0

IDENT = 0
NUMBER = 1
LPARAN = 2
RPARAN = 3
ASSIGNOP = 4
PLUSOP = 5
MINUSOP = 6
MULTOP = 7
DIVIDEOP = 8
SEMICOL = 9
RETURN = 10

output = []
id_output = []
int_output = []
#############################

# Write identity to output.. so we focus on chars a..z 
def identity_write():
    global premenna, ident, length_chr
    if premenna == "return":
        output.append(RETURN)
    else:
        output.append(IDENT)
        id_output.append(premenna)
    premenna = ''
    ident = False
    length_chr = 0

# Write integer numbers to ouput.. we focus on chars 0..9
def number_write():
    global cislo, length_chr, number
    output.append(NUMBER)
    int_output.append(cislo)
    cislo = ''
    number = False
    length_chr = 0

##########################################################

# functions for checking if char is a-z (identity) or 0-9 (number)
def is_ident(chr):
    return (97 <= ord(chr) <= 122)
def is_number(chr):
    return (48 <= ord(chr) <= 57)

###########################################################

def lexer(input):
    line = 1
    column = 0
    global length_chr, premenna, cislo, ident, number
    
    for char in input:
        if char == ' ' or char == '\n' or char == '\t':
            if(ident):
                identity_write()
            if(number):
                number_write()
            if(char == '\n'):
                line += 1
                column = 0
        elif char == '=':
            if(ident):
                identity_write()
            if(number):
                number_write()
            output.append(ASSIGNOP)
        elif char == '(':
            if(ident):
                identity_write()
            if(number):
                number_write()    
            output.append(LPARAN)
        elif char == ')':
            if(ident):
                identity_write()
            if(number):
                number_write()    
            output.append(RPARAN)
        elif char == '+':
            if(ident):
                identity_write()
            if(number):
                number_write()      
            output.append(PLUSOP)
        elif char == '-':
            if(ident):
                identity_write()
            if(number):
                number_write()      
            output.append(MINUSOP)
        elif char == '*':
            if(ident):
                identity_write()
            if(number):
                number_write()    
            output.append(MULTOP)
        elif char == '/':
            if(ident):
                identity_write()
            if(number):
                number_write()   
            output.append(DIVIDEOP)
        elif char == ";":
            if(ident):
                identity_write()
            if(number):
                number_write()    
            output.append(SEMICOL)
        elif is_ident(char):
            ident = True
            length_chr += 1
            premenna += char
            if(length_chr > 10):
                sys.stderr.write(f"ERROR - INVALID IDENTITY on line {line}, column {column}.")
                sys.exit(1)    
        elif is_number(char):
            number = True
            length_chr += 1
            cislo += char
            if(length_chr > 5):
                sys.stderr.write(f"ERROR - INVALID NUMBER on line {line}, column {column}.")
                sys.exit(1)
        else:
            sys.stderr.write(f"ERROR - INVALID CHARACTER on line {line}, column {column}.")
            sys.exit(1)      
        column += 1
        

# Format output so it looks like we want it to look...
def vystup(output):
    int_idx = 0
    id_idx = 0
    
    for token in output:
        match token:
            case 0:
                print(f"IDENT({IDENT}, '{id_output[id_idx]}')")
                id_idx += 1
            case 1:
                print(f"NUMBER({NUMBER}, '{int_output[int_idx]}')")
                int_idx += 1
            case 2:
                print(f"LPARAN({LPARAN})")
            case 3:
                print(f"RPARAN({RPARAN})")
            case 4:
                print(f"ASSIGNOP({ASSIGNOP})")
            case 5:
                print(f"PLUSOP({PLUSOP})")
            case 6:
                print(f"MINUSOP({MINUSOP})")
            case 7:
                print(f"MULTOP({MULTOP})")
            case 8:
                print(f"DIVIDEOP({DIVIDEOP})")
            case 9:
                print(f"SEMICOL({SEMICOL})")
            case 10:
                print(f"RETURN({RETURN})")
        
        
#########################################################

# Main function of the program.. cool stuff happens here
if __name__ == "__main__":
    filename = sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    
    #print(characters)
    lexer(characters)
    #print(output)
    #print(id_output)  
    #print(int_output)  
    
    vystup(output)


