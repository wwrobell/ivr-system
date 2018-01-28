from run_pathfinder import find_keywords
from run_sarmata import recognize_numbers
from util.capture_audio import record_to_file
from util.play_sound import play_audio

def main_menu():
    state = 'init'
    answer_path = "waves/answer.wav"
    error_threshold = 2
    n = 0
    while n < error_threshold + 1:
        if state == 'init':
            play_audio('sys_intro')
        if state == 'restart':
            n += 1
            if n > error_threshold:
                end_menu('failed')
                break
            else:
                play_audio('sys_again')

        record_to_file(answer_path)
        phrases = ['historię', 'transakcji', 'transakcje', 'odblokować', 'zastrzec', 'zablokować', 'kartę', 'hasło']
        spotted = find_keywords(phrases, answer_path)
        path = max_score_idx(spotted)

        if path == 0:
            account_menu()
            break
        elif path == 1:
            history_menu()
            break
        elif path == 2:
            card_menu()
            break
        else:
            print("Rozpoznanie niepewne \n")
            state = 'restart'
        
def account_menu():
    print("ścieżka: Odblokowanie konta \n")
    authorize_client()
    
def history_menu():
    print("ścieżka: Historia transakcji \n")
    authorize_client()

def card_menu():
    print("ścieżka: Zastrzeganie karty \n")
    authorize_client()

def end_menu(result):
    if result == 'failed':
        print('failed \n')
        play_audio('sys_error')
    if result == 'success':
        print('success \n')
    
    print("END \n")

def authorize_client():
    answer_path = "waves/answer.wav"
    error_threshold = 3
    n = 0
    play_audio('sys_client')
    record_to_file(answer_path)
    client_id = recognize_numbers(answer_path)
    if client_id:
        print("client_id = ", client_id)
        while n < error_threshold + 1:
            if n < error_threshold:
                n += 1
                client_pin = get_pin()
                pin_ok = check_pin(client_pin)
                if pin_ok:
                    end_menu('success')
                    break
            else:
                end_menu('failed')
                break
                
    else:
        print("No numbers detected \n")
        end_menu('failed')

def get_pin():
    answer_path = "waves/answer.wav"
    play_audio('sys_pin')
    record_to_file(answer_path)
    client_pin = recognize_numbers(answer_path)
    print("client pin = ", client_pin)
    return client_pin

def check_pin(client_pin):
    example_pin = ['jeden', 'dwa', 'trzy', 'cztery']
    if client_pin == example_pin:
        print("prawidłowy PIN\n")
        return 1
    else:
        print("błędny PIN \n")
        play_audio('sys_pin_wrong')
        return
    
    
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

def ivr_start():
    main_menu()

if __name__ == '__main__':
    main_menu()
    #authorize_client()
