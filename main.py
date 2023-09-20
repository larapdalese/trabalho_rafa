import aplicativo as app
import doctest

if __name__ == "__main__":
    doctest.testmod(app)

tipo_de_entrada = input("Determine o tipo de entrada:\n(1) Console\n(2) Arquivo Texto\n")

if tipo_de_entrada == "1":
    data = input("Insira as datas separadas por um hífen (-):")
    data = data.split("-")
    data_inicio = data[0]
    data_fim = data[1]
    print(app.numero_de_dias_entre_datas(data_fim, data_inicio))
elif tipo_de_entrada == "2":
    nome_do_arquivo = input("Insira nome do arquivo:\n")
    arquivo = open(nome_do_arquivo)
    data = arquivo.readlines()[0].replace("\n", "")
    data = data.split("-")
    data_inicio = data[0]
    data_fim = data[1]
    print(app.numero_de_dias_entre_datas(data_fim, data_inicio))
else:
    print("O número oferecido não é uma opção.")
