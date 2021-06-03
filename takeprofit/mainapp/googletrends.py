import pandas as pd                        
from pytrends.request import TrendReq
from datetime import date

def llamar_api_gt (timeframe, ticker):
    pytrend = TrendReq()
    kw_list = [ticker]
    pytrend.build_payload(kw_list, cat=0, timeframe=timeframe)
    data = pytrend.interest_over_time()
    print(data)
    return data

def obtener_media_semanas (df):
    medias = []
    i = 0
    descuadre = 1
    for x in range(len(df)):
        descuadre += 1
        i += df.iloc[x,0]
        if descuadre%7 == 0 and x != 0:
            medias.append(i/7)
            i = 0

    print("Medias semanales:\n",medias)
    return medias

def get_trend (ticker):
    timeframe = 'today 3-m'  # Informacion de los ultimos tres meses 
    data = llamar_api_gt(timeframe,ticker)
    medias = obtener_media_semanas(data)
    diff = []
    for i in range(1,len(medias)):
        diff.append ( ( medias[i] - medias[i-1] ) * medias[i-1] )
    print("Diferencias ponderadas:\n",diff)

    rango = 0
    for d in diff:
        rango += abs(d)
    print("El rango total es:\n",rango)

    rango_actual = 0
    simbolo_actual = 0
    rango_positivo = 0
    for d in diff [-1:len(diff)-5:-1]:
        rango_positivo += d
        rango_actual += abs(d)
    print("El rango actual es:\n",rango_actual)
    print("El rango positivo es:\n",rango_positivo)
    ratio = rango_actual/rango  # Cuanto aporta los ultimos cambios en volumen respecto al total
    print("Ratio de trends:\n", ratio)
    if(rango_positivo>0):
        return ratio
    else:
        return ratio * -1

    

#print("El dato seleccionado es: ",data.iloc[0,0])
#otrodata = data.loc['2021-03-01':'2021-03-02',:]
#print(otrodata)

"""todayaux = date.today()
today = todayaux.strftime("%Y-%m-%d")
print("Today's date:", today)
timeframe2 = '2020-12-01 2021-05-06'
timeframe3 = '2021-04-01 2021-05-01'
timeframe4 = '2021-03-01 2021-04-01'"""