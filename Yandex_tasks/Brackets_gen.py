"""
Генерация лексикографической скобочной последовательности по введенному числу(пар скобочек).
"""
def br(n: int, s='', left=0, right=0):
    if left == n and right == n:
        print(s)
    if left < n:
        br(n, s + '(', left + 1, right)
    if right < left:
        br(n, s + ')', left, right + 1)


br(n=3)
