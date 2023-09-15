
import os

def clscon():
    os.system("cls" if os.name == "nt" else "clear")

def quiz():
    print("Bem vindo ao Quiz Python\n")
    
    answer_user = input("Iniciar? (S/N) ")
    
    if answer_user != "S" and answer_user != "s":
        return
    
    score = 0
    
    clscon()
    
    print("\nComeçando...\n")
    
    print("1. Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (a) Rockstar \n (b) Ubisoft \n (c) Activision \n (d) EA \n")
    q1 = input("Resposta: ")
    
    if q1 != "a" and q1 != "A":
        print("\nIncorreta!\n")
    else:
        print("\nCorreta!\n")
        score += 1
    
    print("2. Qual é o planeta mais próximo do Sol? \n (a) Vênus \n (b) Marte \n (c) Júpiter \n (d) Mercúrio \n")
    q2 = input("Resposta: ")
    
    if q2 != "d" and q2 != "D":
        print("\nIncorreta!\n")
    else:
        print("\nCorreta!\n")
        score += 1
    
    print("3. Qual é o maior mamífero terrestre? \n (a) Elefante africano \n (b) Girafa \n (c) Hipopótamo \n (d) Rinoceronte \n")
    q3 = input("Resposta: ")
    
    if q3 != "a" and q3 != "A":
        print("\nIncorreta!\n")
    else:
        print("\nCorreta!\n")
        score += 1
    
    print("4. Qual é a capital da França? \n (a) Berlim \n (b) Madri \n (c) Londres \n (d) Paris \n")
    q4 = input("Resposta: ")
    
    if q4 != "d" and q4 != "D":
        print("\nIncorreta!\n")
    else:
        print("\nCorreta!\n")
        score += 1
    
    print("5. Qual é o maior órgão do corpo humano? \n (a) Estômago \n (b) Cérebro \n (c) Pele \n (d) Coração \n")
    q5 = input("Resposta: ")
    
    if q5 != "c" and q5 != "C":
        print("\nIncorreta!\n")
    else:
        print("\nCorreta!\n")
        score += 1
    
    print("\nQuiz Finalizado!")
    answer_user = input("\nVer Resultado? (S/N) ")
    
    clscon()
    
    if answer_user != "S" and answer_user != "s":
        return
    else:
        print("\nQuiz Finalizado!")
        print("\nSua Pontuação é: ",score)

while True:
    quiz()
    answer_user = input("\nJogar Novamente? (S/N) ")
    if answer_user != "S" and answer_user != "s":
        break

    clscon()



