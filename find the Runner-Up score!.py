if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    unique_scores = sorted(set(arr), reverse=True)

    if len(unique_scores) >= 2:
        runner_up_score = unique_scores[1]
    else:
        runner_up_score = unique_scores[0]

    print(runner_up_score)
