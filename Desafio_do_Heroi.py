
# Dados do Heroi

nome_heroi = "Jabuti"
xp_heroi = 7590
nivel = ""

# Estrutura de processamento dos niveis

if xp_heroi < 1000:
    nivel = "Ferro"

elif xp_heroi <=2000:
    nivel = "Bronze"

elif xp_heroi <= 5000:
    nivel = "Prata"

elif xp_heroi <= 7000:
    nivel = "Ouro"

elif xp_heroi <= 8000:
    nivel = "Platina"

elif xp_heroi <= 9000:
    nivel = "Ascendente"

elif xp_heroi <= 10000:
    nivel = "Imortal"

else:
    nivel = "Radiante"



# Saida final

print("O heroi de nome " + nome_heroi + " esta no nivel de " + nivel)
