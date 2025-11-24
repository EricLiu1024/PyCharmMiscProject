class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a
        m, n = len(a), len(b)
        a = [float('-inf')] + a + [float('inf')]
        b = [float('-inf')] + b + [float('inf')]
        i, j = 0, (m + n + 1) // 2
        while True:
            if a[i] <= b[j + 1] and a[i + 1] > b[j]:
                max1 = max(a[i], b[j])
                min2 = min(a[i + 1], b[j + 1])
                return max1 if (m + n) % 2 else (max1 + min2) / 2
            i += 1
            j -= 1


