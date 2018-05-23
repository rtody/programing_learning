import itertools

def solution(A, B, C, D):
    longest = None

    pts = []
    sort_ABCD = sorted((A, B, C, D))

    # Find out all possible points
    for pt in itertools.permutations((A, B, C, D), 2):
        pts.append(pt)

    for pair_pts in itertools.combinations(pts, 2):
        # Check if we use a number more than one time
        if sort_ABCD != sorted(pair_pts[0] + pair_pts[1]):
            continue

        # Calculate squared distance by selected points
        sqd_dist = (pair_pts[0][0] - pair_pts[1][0]) ** 2 + (pair_pts[0][1] - pair_pts[1][1]) ** 2

        if longest is None or sqd_dist > longest:
            longest = sqd_dist

    print(longest)
    return longest

solution(2, 4, 2, 4)
