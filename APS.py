looping = 0
Qta = float(input("Quantos litros de combustivel são gastos em media por caminhão?"))
Frota = float(input("Quantos caminhões tem na sua frota?"))

while looping == 0:
    Comb = input("Diga o tipo de combustivel que seu caminhão usa:").upper().strip()

    if Comb in ["GASOLINA", "Gasolina"]:
        CarbUni = Qta * 0.82 * 0.75 * 3.7
        CarbFro = CarbUni * Frota
        looping = + 1

    elif Comb in ["ETANOL", "Etanol"]:
        CarbUni = Qta * 0.18 * 3.7
        CarbFro = CarbUni * Frota
        looping = + 1

    elif Comb in ["DIESEL", "Diesel"]:
        CarbUni = Qta * 0.83 * 3.7
        CarbFro = CarbUni * Frota
        looping = + 1
    else:
        print(Comb + " não é um combustivel valido")

print("A quantidade media de carbono que um caminhão gera é ", CarbUni, " e sua frota gera ", CarbFro)
ArvreAtl = CarbFro // 130
ArvreAma = CarbFro // 222
Credito = CarbFro / 1000
print("É possivel plantar", ArvreAtl, " Arvores da floresta atlantica ou ", ArvreAma, " Arvores da floresta Amazonica,"
" ou então trocar seus caminhões por caminhões eletricos, zerando a quantiade de carbono gerada, gerando um total de ", Credito, " Creditos")

