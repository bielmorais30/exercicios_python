op = 0
c1 = 0
c2 = 0
c3 = 0
branco = 0

while op != 5:
    op = int(input(f"Opções: \n1 - Candidato 1 \n2 - Candidato 2 \n3 - Candidato 3 \n4 - Branco \n5 - Sair e ver resultados\n"))
    match op:
        case 1:
            c1 = c1+1
        case 2:
            c2 = c2+1
        case 3:
            c3 = c3+1
        case 4:
            branco = branco+1

print(f"Resultados: \n1 - Candidato 1 : Votos {c1} ou {((100/(c1+c2+c3+branco)))*c1}%\n2 - Candidato 2 : Votos {c2} ou {((100/(c1+c2+c3+branco)))*c2}%\n3 - Candidato 3 : Votos {c3} ou {((100/(c1+c2+c3+branco)))*c3}%\n4 - Branco      : Votos {branco} ou {((100/(c1+c2+c3+branco)))*branco}%\n")
