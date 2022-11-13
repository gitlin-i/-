import sys
input = sys.stdin.readline

pokemon_book = []
pokemon_book_dict = {}
n,m = map(int,input().split())

for i in range(n):
    pokemon = input().rstrip()
    pokemon_book.append(pokemon)
    pokemon_book_dict[pokemon] = i +1

for _ in range(m):
    problem = input().rstrip()
    
    if problem.isnumeric():

        answer = pokemon_book[int(problem) -1]
    else:

        answer = pokemon_book_dict[problem]
    

    print(answer)



"""
boj_problem=1620
"""