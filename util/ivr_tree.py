
def max_score_idx(spotted):
    acc_expected = ['odblokować', 'hasło']
    hist_expected = ['historię', 'transakcji', 'transakcje']
    card_expected = ['zastrzec', 'zablokować', 'kartę']

    acc_score = 0
    hist_score = 0
    card_score = 0

    if spotted:
        for x in spotted:
            keyword = x.get('phrase')
            score = x.get('score')
            
            if keyword in acc_expected:
                #0 konto
                acc_score += score
                
            elif keyword in hist_expected:
                #1 historia
                hist_score += score
                
            elif keyword in card_expected:
                #2 karta
                card_score += score
                
        scores = [acc_score, hist_score, card_score]
        max_value = max(scores)
        max_index = scores.index(max_value)
        if max_value > 0:
            return max_index
        else:
            return -1
    else:
        return -1

def classify(spotted):
    num = max_score_idx(spotted)
    print('\nakcja: ')
    
    if num == 0:
        # konto
        print("odblokowanie konta\n")
        return 2
    elif num == 1:
        # historia
        print("historia transakcji\n")
        return 2
    elif num == 2:
        # karta
        print("zastrzeganie karty\n")
        return 2
    elif num == -1:
        # niepewne rozw
        print("rozpoznanie niepewne\n")
        return 1
    else:
        #wrong input message
        print("wrong input message\n")
        return 1



