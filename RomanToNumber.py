def function(string, list, base)->int:
    if string in list:
        return list.index(string) * base
    else:
        return 0


def romanToInt(s: str) -> int:
    T = ['', 'M', 'MM', 'MMM']
    H = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    t = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    length = len(s)
    start = 0
    ans = 0
    base = 1000
    for list in (T, H, t, I):
        last = 0
        flag = 0
        for end in range(start, length):
            # 保存计算结果
            temp = function(s[start: end + 1], list, base)
            if temp != 0 and end != length - 1:
                last = temp
                flag = 1
                continue
            elif flag == 1 and temp == 0 and end == length - 1:
                ans += last
                base = 1000
                for list in (T, H, t, I):
                    temp = function(s[end: end + 1], list, base)
                    if temp != 0:
                        ans += temp
                        print(temp)
                    else:
                        base //= 10
            elif end == length - 1:
                ans += temp
            else:
                ans += last
                start = end
            base //= 10
            break

    return ans


romanToInt('MCMXCIV')


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