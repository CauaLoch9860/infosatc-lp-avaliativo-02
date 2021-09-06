Filmes = ["Os homens de preto","Up altas aventuras","Velozes e furiosos"]
Jogos = ["Mine","Lol","Cs","Dota","Poe"]
Livros = ["É agora ou nunca","O mundo é uma bola","A arte da guerra"]
Esporte = ["Futsal","basquete","vôlei","tênis"]

Filmes.append("Eu nunca")
Filmes.insert(0,"Não case se beber")

Jogos.append("Roblox")
Jogos.insert(0,"Black desert")

Livros.append("A menina q roubava livro")
Livros.insert(0,"A cabana")

Esporte.append("Corrida")
Esporte.insert(0,"Rugbi")

lista_nova = Filmes + Jogos + Livros + Esporte 

print(Livros[2])

del Esporte[0]

lista_nova.append("Disciplina")
print(lista_nova)

