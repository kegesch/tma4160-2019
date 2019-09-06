#pot
def pot(G, g, a):
    binary = bin(a)[2:]
    size = len(binary)
    pots = [g]
    for i in range(1, size):
        pots.append(pots[i-1]**2 % G)

    result = 1
    pots = list(reversed(pots))
    j = 0
    print pots
    for i in binary:
        if int(i) == 1:
            #print(int(i)*pots[j])
            result = (result * int(i)*pots[j])
        j += 1

    return result % G


print(pot(10007, 5, 582))

