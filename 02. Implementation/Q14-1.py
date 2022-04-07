# def perm(arr, n) :
#     result = []
#     if n > len(arr) :
#         return arr
#     if n == 1 :
#         for i in arr :
#             result.append([i])
#     elif n > 1 :
#         for i in range(len(arr)) :
#             ans = [i for i in arr]
#             ans.remove(arr[i])
#             for p in perm(ans, n-1) :
#                 result.append([arr[i]]+p)
#     return result
from itertools import permutations

def solution(n, weak, dist) :
    # 원형을 일자로 만들기 위해 2배
    length = len(weak)
    for i in range(length) :
        weak.append(weak[i]+n)
    # 친구 최솟갑 구해야 하므로 초기값 설정
    answer = len(dist) + 1

    for start in range(length) :
        # 친구를 나열하는 모든 경우의 수 확인
        # for friends in list(perm(dist, len(dist))) :
        for friends in list(permutations(dist, len(dist))) :
            # 투입 친구 수
            count = 1
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count-1]
            # 시작점 부터 모든 취약 위치 확인
            for index in range(start, start + length) :
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index] :
                    # 친구 추가
                    count += 1
                    # 더 투입 불가하면 종료
                    if count > len(dist) :
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)

    if answer > len(dist) :
        return -1
    return answer




