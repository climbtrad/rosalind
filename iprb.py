def mendel(k, m, n):
    k += 0.0
    m += 0.0
    n += 0.0
    pop = k + m + n

    # Probability of selecting homozygous dominant first
    dom = k/pop

    # Probability of selecting heterozygous first
    het1dom2 = (m/pop)*(k/(pop-1))
    bothhet = (m/pop)*((m-1)/(pop-1))*0.75
    het1rec2 = (m/pop)*(n/(pop-1))*0.5

    het = het1dom2 + bothhet + het1rec2

    # Probability of selecting homozygous recessive first
    rec1dom2 = (n/pop)*(k/(pop-1))
    rec1het2 = (n/pop)*(m/(pop-1))*0.5

    rec = rec1dom2 + rec1het2

    # Sum of probabilities
    result = dom + het + rec

    return result


if __name__ == '__main__':
    print(mendel(20, 25, 30))