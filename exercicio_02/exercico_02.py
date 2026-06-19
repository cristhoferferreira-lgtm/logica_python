def desenha_linha (limte, preenchimento, largura) :
    print (limite + (preenchimento * (largura - 2)) + limite)

desenha_linha ('+', '-', 20)
for l in range(1, 5) : 
    desenha_linha('|', '', 20)
desenha_linha('+', '-', 20)
