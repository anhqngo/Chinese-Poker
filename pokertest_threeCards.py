rank_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def poker(hands):
    handList1 = [rank_value[i[0]] for i in hands[0].split()]
    handList2 = [rank_value[i[0]] for i in hands[1].split()]

    countDict1 = dict((rank,handList1.count(rank)) for rank in set(handList1))
    countDict2 = dict((rank,handList2.count(rank)) for rank in set(handList2))

    if len(set(handList1)) < len(set(handList2)):
        return 0
    elif len(set(handList1)) > len(set(handList2)):
        return 1
    else:
        if len(set(handList1)) == 1:
            if handList1[0] > handList2[0]:
                return 0
            else:
                return 1
        elif len(set(handList1)) == 2:
            (M1, m1) = (max(countDict1, key=countDict1.get), min(countDict1, key=countDict1.get))
            (M2, m2) = (max(countDict2, key=countDict2.get), min(countDict2, key=countDict2.get))
            if M1 > M2:
                return 0
            elif M1 < M2:
                return 1
            else:
                if m1 > m2:
                    return 0
                elif m1 < m2:
                    return 1
                else:
                    return None
        else:
            for _i in range(3):
                if sorted(handList1)[_i] > sorted(handList2)[_i]:
                    return 0
                elif sorted(handList1)[_i] < sorted(handList2)[_i]:
                    return 1
            return None