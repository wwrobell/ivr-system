from util.capture_audio import record_to_file
from util.ivr_tree import classify
from util.pin_check import check_pin
from run_pathfinder import find_keywords
from run_sarmata import recognize_numbers
import winsound

def play_audio(audio_name):
    path = 'waves/' + audio_name
    winsound.PlaySound(path, winsound.SND_FILENAME)
    winsound.PlaySound('waves/sys_ping', winsound.SND_FILENAME)

def rec_pin():
    play_audio('sys_pin')
    print("answer recording...\n")
    record_to_file(answer_filename)
    client_pin = recognize_numbers(answer_filename)
    print("client pin = ", client_pin)
    return client_pin

if __name__ == '__main__':
    
    answer_filename = "waves/answer.wav"
    node = 1
    count = 0
    
    while (count < 4):
        if node == 1:   
            count = count + 1
            if count == 4:
                play_audio('sys_error')
                node = 3
                break

            if count == 1:
                play_audio('sys_intro')
            else:
                play_audio('sys_again')
            
            'first node answer recording'
            print("answer recording...\n")
            record_to_file(answer_filename)
        
            # Define phrases you want to spot
            phrases = ['historię', 'transakcji', 'transakcje', 'odblokować', 'zastrzec', 'zablokować', 'kartę', 'hasło']
            spotted = find_keywords(phrases, answer_filename)

            node = classify(spotted)
            

        if node == 2:
            count = 0
            while (count < 4):
                count = count + 1
                
                if count == 4:
                    play_audio('sys_error')
                    node = 3
                    break
                
                play_audio('sys_client')
                'second node answer recording (client number)'
                print("answer recording...\n")
                record_to_file(answer_filename)
                client_id = recognize_numbers(answer_filename)
                if client_id is None:
                    print("No numbers detected\n")
                else:
                    print("client id = ", client_id)
                    client_pin = rec_pin()
                    node = 3
                    break

        if node == 3:
            print('the end\n')
            break


