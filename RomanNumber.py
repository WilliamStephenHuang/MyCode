def intToRoman(num: int) -> str:
    numberlist = []
    while num >= 10:
        numberlist.append(num % 10)
        num //= 10
    else:
        numberlist.append(num)
    length = len(numberlist)
    T = ['', 'M', 'MM', 'MMM']
    H = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    t = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    ans = I[numberlist[0]]
    if length > 1:
        ans = t[numberlist[1]] + ans
    if length > 2:
        ans = H[numberlist[2]] + ans
    if length > 3:
        ans = T[numberlist[3]] + ans

    return ans


while True:
    a = input()
    print(intToRoman(int(a)))

# 数字转罗马字
# numberBase = [1, 10, 100, 1000]
# numberFive = [5, 50, 500]
# I V X L C D M
# 1: I 10: X 100: C
# 2: II 20: XX 200: CC
# 3: III 30: XXX 300: CCC
# 4: IV 40: XL 400: CD
# 5: V 50: L 500: D
# 6: VI 60: LX 600: DC
# 7: VII 70: LXX 700: DCC
# 8: VIII 80: LXXX 800: DCCC
# 9: IX 90: XC 900: CM
