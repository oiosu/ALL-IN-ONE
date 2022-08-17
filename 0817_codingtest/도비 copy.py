import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\Algorithm_J\8월\0817_codingtest\도비.txt", "r", encoding="utf-8")


while True:
    n = int(input())
    if n == 0: 
        break
    words = []

    for _ in range(n):
        word = input()
        # print(word)
        # Cat
        # fat
        # bAt
        # call
        # ball
        # All
        # Hall
        words.append((word.lower(), word))

    words.sort()
    print(words.sort())
    #print(words[0][1])
    print(words[0])


# print(words)
# [('cat', 'Cat')]
# [('cat', 'Cat'), ('fat', 'fat')]
# [('cat', 'Cat'), ('fat', 'fat'), ('bat', 'bAt')]
# [('call', 'call')]
# [('call', 'call'), ('ball', 'ball')]
# [('call', 'call'), ('ball', 'ball'), ('all', 'All')]
# [('call', 'call'), ('ball', 'ball'), ('all', 'All'), ('hall', 'Hall')]


#print(word.lower())
# cat
# fat
# bat
# call
# ball
# all
# hall