def solution(scoville, K):
    answer = 0
    while (1):
        if scoville[0] < K:
            scoville[0] = scoville[0] + (scoville.pop(1) * 2)
            answer += 1
            scoville.sort()

        if scoville[0] >= K:
            return answer


print(solution([1, 2, 3, 9, 10, 12], 7))