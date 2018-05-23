def solution(T):
    # write your code in Python 3.6
    counts = dict()
    ans = list()

    def dfs(city_Q, level):
        for city_P in range(len(T)):
            # print(city_P, city_Q)
            if T[city_P] == city_Q and city_P != city_Q:
                if level not in counts:
                    counts[level] = 1
                else:
                    counts[level] += 1
                dfs(city_P, level+1)

    for city_P in range(len(T)):
        if city_P == T[city_P]:
            # print(city_P)
            cap_city = city_P

    dfs(cap_city, 1)
    for k, v in counts.items():
        ans.append(v)
    for i in range(len(T) - len(ans)):
        ans.append(0)
    print(ans)
    return ans

"""
T[0] = 9, T[1] = 1, T[2] = 4
T[3] = 9, T[4] = 0, T[5] = 4
T[6] = 8, T[7] = 9, T[8] = 0
T[1] = 1
"""


solution([9,1,4,9,0,4,8,9,0,1])
