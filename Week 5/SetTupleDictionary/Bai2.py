n = int(input())
my_set = set(map(int, input().split()))

if len(my_set) == n:
    tong = int(input())

    max_subset = set()
    max_length = 0

    for i in my_set:
        subset = set()
        subset_sum = 0

        for j in my_set:
            subset.add(j)
            subset_sum += j

            if subset_sum > tong or len(subset) > len(max_subset):
                break

            if len(subset) > len(max_subset):
                max_subset = subset.copy()

    print(max_subset)
