# SET을 활용한 문제 해결 코드 
def solution(n, lost, reserve):
    # 1. Set을 만든다
    reserve_only = list(set(reserve) - set(lost))
    lost_only = list(set(lost) - set(reserve))
    reserve_only.sort();
    
    # 2. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려준다.
    for reserve in reserve_only:
        front = reserve - 1
        back = reserve + 1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)

    #3. 최대한 나눠준 뒤에 lost에 남아있는 학생들은 체육복이 없는 학생들이다.
    return n - len(lost_only)

print(solution(5,[2,4],[1,3,5]))

# 배열을 활용한 문제 해결 코드 
def solution(n, lost, reserve):
    # 1. student 배열 생성
    student = [0]*(n+2)

    # 2. reserve / lost 정보 반영
    for r in reserve:
        student[r] += 1
    for l in lost:
        student[l] -= 1

    # 3. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려준다.
    for i in range(1, n+1):
        if student[i] > 0:
            if student[i-1] < 0:
                student[i] -= 1
                student[i-1] += 1
            elif student[i+1] < 0:
                student[i] -= 1
                student[i+1] += 1

    # 4. 체육복을 갖고 있는 학생 수를 계산한다.
    answer = 0
    for i in range(1, n+1):
        if student[i] > -1:
            answer += 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
