def spr(str):
    if len(str) == 1 or len(str) == 2:
        return str
    return str[0] + '(' + spr(str[1:-1]) + ')' + str[-1] 
    
print(spr('tete'))