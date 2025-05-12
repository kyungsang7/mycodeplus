def merge(left, right):
    global ans

    left_idx, right_idx = 0, 0
    res = []

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            res.append(left[left_idx])
            left_idx += 1

        else:
            res.append(right[right_idx])
            right_idx += 1
            ans += len(left) - left_idx

    res += left[left_idx:]
    res += right[right_idx:]

    return res

def merge_sort(A):
    if len(A) == 1:
        return A
    
    idx = len(A) // 2
    left = merge_sort(A[:idx])
    right = merge_sort(A[idx:])

    return merge(left, right)


N = int(input())
A = list(map(int,input().split()))
ans = 0

merge_sort(A)
print(ans)