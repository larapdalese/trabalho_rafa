import aplicativo as app

tipo_de_entrada = input("Determine o tipo de entrada:\n(1) Console\n(2) Arquivo Texto\n")

if tipo_de_entrada == "1":
    data = input("Insira as datas separadas por um hífen (-)")
    data = data.split("-")
    data_inicio = data[0]
    data_fim = data[1]
    print(app.numero_de_dias_entre_datas(data_fim, data_inicio))
elif tipo_de_entrada == "2":
    pass
else:
    print("O número oferecido não é uma opção.")
