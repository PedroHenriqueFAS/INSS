def desconto_inss(salario_bruto):
    faixas = [1100.00, 2203.48, 3305.22, 6433.57]
    aliquotas = [0.075, 0.09, 0.12, 0.14, 0.15]
    
    teto = 751.99
    inss = 0
    faixa = 0
    for i in range(len(faixas)):
        if salario_bruto <= faixas[i]:
            if i > 0:
                salario_bruto = salario_bruto - faixas[i-1]
            inss += salario_bruto * aliquotas[i]
            break
        else:
            if i > 0:
                faixa = faixas[i] - faixas[i-1]
            else:
                faixa += faixas[i]
            inss += faixa *aliquotas[i]
    if inss > teto:
        inss = teto
    print(inss)
    return inss

desconto_inss(1500)