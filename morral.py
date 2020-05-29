

def morral(tamanoMorral, pesos, valores, n):
    '''
    Cada posicion i de 'pesos' corresponde a la posicion i de 'valores'.
    '''
    if (( n == 0 ) or ( tamanoMorral == 0 )):
        return 0
    
    if pesos [ n - 1 ] > tamanoMorral:
        # el peso del elem actual es mayor a lo que soporta el morral.
        return morral( tamanoMorral, pesos, valores, n - 1 )
    
    return max( valores [ n - 1 ] + morral( tamanoMorral - pesos [ n - 1 ], pesos, valores, n - 1 ), 
                morral( tamanoMorral, pesos, valores, n - 1 ))
    # obtengo el maximo valor de: agregar el elem actual, o no agregarlo.
        

if __name__ == '__main__':
    
    valores = [60, 100, 120, 150, 190, 250, 260, 350, 400, 425, 475, 500]
    pesos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    tamanoMorral = 235
    n = len(valores)
    
    valorMaximo = morral(tamanoMorral, pesos, valores, n)
    print(valorMaximo)