# Python

print('Welcome to TRUWHPYQUIZ')
answer=input("Quiz de 3 perguntas, i´m you ready ? : (yes/no)")
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: Qual é a sua linguagem de programação preferida?')
    if answer.lower()=='python':
        score += 1
        print('a minha tbm ;)')
    else:
        print('Próxima questão :(')
 
 
    answer=input('Question 2: Você segue a TREWHPY no instagram ? ')
    if answer.lower()=='Sim':
        score += 1
        print('boa!')
    else:
        print('não perca tempo!')
 
    answer=input('Question 3: Qual é o presidente da rússia, cite apenas o primeiro nome..?')
    if answer.lower()=="vladimir":
        score += 1
        print('correto')
    else:
        print('erro system32:(')
 
print('Obrigado por testar nosso desenvolvimento, em breve terá novas ideias...',score,"Questões corretas!")
mark=(score/total_questions)*100
print('Pontuação:',mark)
print('Thanks, Trewhpy!')
