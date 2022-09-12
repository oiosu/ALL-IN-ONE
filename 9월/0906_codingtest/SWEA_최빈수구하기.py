# 입력 
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.

# 출력 
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다. 


from collections import Counter
 
T = int(input())
for _ in range(1,T+1):
    n = int(input())
    
    li = list(map(int, input().split()))
    most_num = Counter(li).most_common()[0][0]
    print("#"+str(n),str(most_num))