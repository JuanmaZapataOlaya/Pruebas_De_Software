
def es_par(n):
    if n%2 == 0:
        return True
    
    else:
        return False

def es_multiplo(n,m):
    if n == 0:
        return False
    
    if m == 0:
        return False

    if n%m == 0:
        return True
    else:
        return False
    
