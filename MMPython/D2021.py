import pandas as pd 
import xlsxwriter
import datetime
import json

gado_list = []  #Lista que será responsável pela lista de gados

###FUNCTIONS###
def RegistrarGado():
    print('\nSimulação registro de gado no sistema\n') #aqui vamos simular a entrada de um gado, respondendo algumas perguntas que serão adicionadas no objeto gado

    name = input('Informe o código do gado:')
    atividade = int(input('Informe o grau de atividade do gado (Escala 1 a 5):'))
    date = str(datetime.datetime.now())
    temperature = int(input('Informe a temperatura do animal:'))
    antena = input('Informe código da Antena receptora:')

    gado_json = {
        'CÓDIGO ANIMAL' : name,
        'ATIVIDADE' : atividade, 
        'TEMPERATURA': temperature,
        'ANTENA': antena, 
        'REGISTRY_DATE': date
    }

    gado_json = json.dumps(gado_json)
    gado_json = json.loads(gado_json)
    gado_list.append(gado_json)
def ExtrairExcel():
    #Cria um Dataframe com os dados registrados dos gados
    df = pd.DataFrame(gado_list)

    # Cria um montador de Excel e nomeia nosso arquivo
    writer = pd.ExcelWriter('GADO_EXCEL'+ str(datetime.datetime.now())+'.xlsx', engine='xlsxwriter')

    # Converte o dataframe em um arquivo excel
    df.to_excel(writer, sheet_name='Relatório')

    # Salva o arquivo
    writer.save()

###########INICIA CODIGO###############

print ('--------------CODE BEGIN--------------')
print ('Menu principal\n')

while True:
    print ('A = Registrar Gado')
    print ('B = Visualizar Dataframe')
    print ('C = Extrair Excel')
    print ('D = Desligar Sistema')
    x = input("Selecione uma função\n").upper()

    if x == 'A':
        print('---REGISTRAR GADO---')
        RegistrarGado()
        print ('GADO REGISTRADO\n\n')
    elif x == 'B':
        df = pd.DataFrame(gado_list)
        print (df)
    elif x == 'C':
        print("---EXTRAIR EXCEL---\n")
        ExtrairExcel()
        gado_list = []
        print ('EXCEL EXTRAÍDO COM SUCESSO')
    elif x == 'D':
        print ('---DESLIGAR SISTEMA---')
        print ('\nEMITINDO RELATÓRIO FINAL DE DESLIGAMENTO')
        ExtrairExcel()
        print ('EXCEL EXTRAÍDO COM SUCESSO')
        exit()
    else:
        print ('---OPÇÃO ERRADA, TENTE NOVAMENTE---')
