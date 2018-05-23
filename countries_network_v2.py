class cityNode:
    def __init__(self, city):
        self.city = city
        self.conn = []

def solution(T):
    # Find out the distance to each city from capital
    def cityDist(city, level):
        for c in city.conn:
            if level not in counts:
                counts[level] = 1
            else:
                counts[level] += 1
            cityDist(c, level+1)

    # Traverse cities based on T and create a tree of city nodes
    def cityTree(root):
        while (city_lst):
            for c in city_lst:
                # T[city_P] == city_Q ?
                if T[c] == root.city:
                    root.conn.append(cityNode(c))
                    rmv_lst.append(c)

            # Remove cities we've passed through from city list
            while (rmv_lst):
                city_lst.remove(rmv_lst.pop(0))

            # Keep traversing if any connected cities
            if root.conn:
                for r in root.conn:
                    cityTree(r)
            return

    counts = dict()
    ans = list()

    # Find out capital city
    for city_P in range(len(T)):
        if city_P == T[city_P]:
            capital = city_P

    # A list of city_P, ex.[0, 1, ..., M-1] if there are M cities
    city_lst = list(range(len(T)))
    city_lst.remove(capital)

    # Used for temporarily storing cities we're going to delete from city list
    rmv_lst = list()

    root = cityNode(capital)

    cityTree(root)
    cityDist(root, 1)

    for k, v in sorted(counts.items()):
        ans.append(v)

    for i in range(len(T) - len(ans)):
        ans.append(0)

    print(ans)
    return ans

"""
T[0] = 9, T[1] = 1, T[2] = 4
T[3] = 9, T[4] = 0, T[5] = 4
T[6] = 8, T[7] = 9, T[8] = 0
T[9] = 1
"""

solution([9,1,4,9,0,4,8,9,0,1])
