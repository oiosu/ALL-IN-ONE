import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\Algorithm_J\8월\0824_codingtest\쇠막대기.txt", "r", encoding="utf-8")



# s = input()
# stack = []
# cnt = 0

# for i in range(len(s)):
#     if s[i] == '(':
#         stack.append(s[i])
#     else:
#         if s[i-1] == '(':
#             stack.pop()
#             cnt += len(stack)
#         else:
#             stack.pop()
#             cnt += 1
# print(cnt)


s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(':   # i가 0 이라면!? 주의  
            cnt += len(stack)
        else:         
            cnt += 1
print(cnt)