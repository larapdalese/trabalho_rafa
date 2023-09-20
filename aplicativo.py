#"A dupla deve elaborar um aplicativo que calcula o número de dias entre duas datas. O usuário pode fornecer duas formas distintas: 
#- Através do console, utilizando o formato "18 de agosto de 2023 - 18 de setembro de 2023"
from datetime import datetime
import doctest

def numero_de_dias_entre_datas(data1, data2):
    """
    

    Parameters
    ----------
    data1 : str
    data2 : str

    Returns
    -------
    diferenca : int

    >>> numero_de_dias_entre_datas("23 de dezembro de 2020", "25 de dezembro de 2020")
    2
    >>> numero_de_dias_entre_datas("4 de janeiro de 2021", "4 de janeiro de 2022")
    365
    """
     
    meses = {
        'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6,
        'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12
    }
    #ivide a string em dia, mês e ano
    partes_data1 = data1.split(' de ')
    partes_data2 = data2.split(' de ')

    #Extrai dia, mês e ano para a primeira data
    dia1, mes1, ano1 = int(partes_data1[0]), meses[partes_data1[1]], int(partes_data1[2])
    #Extrai dia, mês e ano para o segundo dia
    dia2, mes2, ano2 = int(partes_data2[0]), meses[partes_data2[1]], int(partes_data2[2])

    data_inicio = datetime(ano1, mes1, dia1)
    data_fim = datetime(ano2, mes2, dia2)
    
    diferenca = abs((data_fim - data_inicio).days)
    return diferenca
