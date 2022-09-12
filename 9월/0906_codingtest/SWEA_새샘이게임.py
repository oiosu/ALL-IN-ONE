# 입력 
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 7개의 서로 다른 정수가 공백으로 구분되어 주어진다. 
# 각 정수는 1이상 100이하이다.

# 출력 
# 각 테스트 케이스마다 첫 번째 줄에는 
# ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 답을 출력한다.

def my_sum(idx,res,cnt): # 위치, 합, 몇 번 더했는지
    
    # 탈출조건, 3번 더했으면
    if cnt == 3:
        
        # num_save 안에 중복된 숫자 없으면
        if res not in num_save:
            num_save.append(res)
        return
 
    for w in range(idx,7):
        my_sum(w+1,res+numbers[w],cnt+1)
    return
 
T = int(input())
 
for tc in range(1,1+T):
    
    # 7개의 숫자
    numbers = list(map(int,input().split()))
 
    # 저장소
    num_save = []
 
    # 하나씩 보내기
    # 6번째 숫자에서 시작하면 3번 더할 수 없음
    for q in range(5):
        my_sum(q+1,numbers[q],1)
 
    num_save.sort(reverse=True)
 
    print('#{} {}'.format(tc,num_save[4]))