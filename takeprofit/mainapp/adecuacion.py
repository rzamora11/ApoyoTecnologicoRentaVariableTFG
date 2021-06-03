from mainapp.models import *

# Colores #
color_ph = 	'#F0F8FF'
verde = '#568203'
amarillo = '#FFD700'
rojo = '#B22222'

# Valores frontera #
frontera_ROA = 10
frontera_TRENDS = 0.2


def get_colores (empresa, medianas):

    if (empresa.ticker == 'PLCH'):  # Si no se ha introducido ninguna empresa, se apagan los indicadores
        colores = [color_ph,color_ph,color_ph,color_ph,color_ph,color_ph]
        return colores

    ### Color para el PER ###
    ''' Partimos de la base de la mediana del PER entre todos los activos. Se compara el PER del activo frente a la mediana. 
        Si está por encima, rojo. Si está por debajo, verde. Si se aproxima hasta un 10%, amarillo. '''
    if(empresa.PER > (medianas['PER']*1.1)): color_PER = rojo
    elif(empresa.PER < (medianas['PER']*0.9)): color_PER = verde
    else: color_PER = amarillo

    #########################
    ### Color para el ROA ###
    ''' Partimos de la base del estudio que indica un 5 para empresas tradicionales. 
        Hay que tener en cuenta el componente tecnológico, y por tanto escogemos 10%. Si se aproxima hasta un 10%, amarillo.'''
    if(empresa.ROA < (frontera_ROA*0.9)): color_ROA = rojo
    elif(empresa.ROA > (frontera_ROA*1.1)): color_ROA = verde
    else: color_ROA = amarillo

    #########################
    ### Color para el Debt to Equity ###
    ''' Partimos de la base de la insostenibilidad de una deuda alta, pero el extremo conservador de no disponer de cierta deuda.
         Deuda superior a 2, rojo. Inferior a 0,4 amarillo. Entre 0,4 y 2, verde.'''
    if(empresa.DEBT >= 2): color_DEBT = rojo
    elif(empresa.DEBT <= 0.5): color_DEBT = amarillo
    else: color_DEBT = verde    

    #########################
    ### Color para el INSIDERS ###
    ''' Partimos de la base de la mediana del PER entre todos los activos. Se compara el PER del activo frente a la mediana. 
        Si está por encima, rojo. Si está por debajo, verde. Si se aproxima hasta un 10%, amarillo. '''
    if(empresa.INSIDERS > (medianas['INSIDERS']*1.1)): color_INSIDERS = verde
    elif(empresa.INSIDERS < (medianas['INSIDERS']*0.9)): color_INSIDERS = rojo
    else: color_INSIDERS = amarillo

    #########################
    ### Color para el TRENDS ###
    ''' El calculo consiste en evaluar el movimiento en las ultimas cuatro semanas respecto a los tres meses. 
        Si el volumen reciente es positivo, y además representa un cambio sustancial respecto a los tres meses, verde.
        Por ello, si el ratio se encuentra más allá de 0,3, se considera positivo. Entre 0,1 y 0,3 está estático. Menor, el volumen ha reducido.
        El ratio puede variar entre -1 y 1. '''
    if(empresa.TRENDS>(frontera_TRENDS*1.5)): color_TRENDS = verde
    if(empresa.TRENDS<(frontera_TRENDS*0.5)): color_TRENDS = rojo 
    else: color_TRENDS = amarillo

    #########################
    ### Color para el ESG ###
    ''' Partimos de la base del marco de evaluación ESG Benchmarking de MSCI. 
    Si entra en el rango de A, verde. Si entra en el rango de B, amarillo. Si entra en el rango de C, rojo. '''
    if(empresa.ESG == 'AAA' or empresa.ESG == 'AA' or empresa.ESG== 'A'): color_ESG = verde
    elif(empresa.ESG == 'BBB' or empresa.ESG == 'BB' or empresa.ESG== 'B'): color_ESG = amarillo
    else: color_ESG = rojo    
   
    
    colores = [color_PER,color_ROA,color_DEBT,color_INSIDERS,color_TRENDS,color_ESG]
    return colores

