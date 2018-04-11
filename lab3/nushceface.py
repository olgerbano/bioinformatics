secv = 'AAATTTCTCTGGTAGA'
def number2(secv):
    a = [y for y in filter(lambda x: x =='A' or x == 'T', secv)]
    n = len(a)
    return ( n, len(secv)-n)

print(str(number2(secv)));
