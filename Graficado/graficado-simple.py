'''
Como en la clase anterior inicializamos el env adentro de esta carpeta,
ahora nos aparece el env en la carpeta.
Sin embargo, no necesitamos poner en marcha el amb virtual hasta que vayamos a 
ejecutar el programa.
'''
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    '''
    Para un grafico de linea necesitaremos un array de x y un array de y, los dos del mismo tamano.
    Cada grafico tiene sus propios requerimentos.
    '''
    output_file('graficado-simple.html')
    # el archivo donde se dibujara.
    fig = figure()
    # donde ejecutaremos los graficos.
    
    total_values = int(input('Cuantos valores queres graficar? '))
    x_values = list(range(total_values))
    # genero una lista con los valores de x.
    
    y_values = []
    for x in x_values:
        value = int(input(f'Valor y para {x}: '))
        y_values.append(value)
        # Por cada valor de x, el user define el valor de y.
        
    fig.line(x_values, y_values, line_width = 2)
    # crea una linea de ancho 2, con los valores de x y de y dados.
    show(fig)
    # la muestra.
    