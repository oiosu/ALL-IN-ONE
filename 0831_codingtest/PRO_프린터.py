def solution(priorities, location):

    L = [i for i in range(len(priorities))]  # 인덱스 저장하는 리스트

    i = 0
    while priorities != sorted(priorities, reverse=True):
        if priorities[i] < max(priorities[i+1:]):
            # 인덱스 저장한 리스트와 원래 리스트 둘 다 
            # 맨 앞값을 빼서 리스트 뒤로 더해준다
            priorities.append(priorities.pop(i))
            L.append(L.pop(i))
        else:
            i += 1    # 만약 맨 앞이 가장 크다면 한칸 넘어간다
    return L.index(location)+1