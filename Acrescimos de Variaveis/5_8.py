# -*- coding: utf-8 -*-
"""5.8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jU8JnvhSshcEqnvH-BniPA4Lad5-kjgP

##Importando o Pandas e lendo o arquivo csv
"""

import pandas as pd

dataf = pd.read_csv('df_OVNI_limpo.csv')
del dataf['Unnamed: 0'] #Eliminando a coluna desnecessária

"""##Criando uma coluna para DATA e uma coluna para HORA"""

dataf['Sight_Date'] = pd.to_datetime(dataf['Date / Time']).dt.strftime(date_format='%m-%d-%y') #Criando a coluna Sight_Date no fromato mês/dia/ano
dataf['Sight_Time'] = pd.to_datetime(dataf['Date / Time']).dt.strftime(date_format='%H:%M')    #Criando a coluna Sight_Time no formato hora:minuto

dataf = dataf.drop(['Date / Time'], axis = 1)                                                  #Deletando a coluna Date / Time

"""##Criando uma coluna para os dias da semana"""

dataf['Sight_Weekday'] = pd.to_datetime(dataf['Sight_Date']).dt.weekday_name    #Criando a coluna Sight_Weekday para mostrar o dia da semana

"""##Criando as colunas DIA e MÊS"""

dataf['Sight_Day'] = pd.to_datetime(dataf['Sight_Date']).dt.strftime(date_format='%d')    #Criando a coluna Sight_Day para mostrar o dia do mês que ocorreu o relato
dataf['Sight_Month'] = pd.to_datetime(dataf['Sight_Date']).dt.strftime(date_format='%m')  #Criando a coluna Sight_Month para mostrar o mês do relato

"""##Criando um arquivo csv"""

dataf.to_csv('df_OVNI_preparado.csv', index = False)