from util.capture_audio import record_to_file
from run_pathfinder import find_keywords
    
if __name__ == '__main__':
    print("Witamy w systemie banku xyz. Możesz tutaj odblokować swoje konto internetowe, sprawdzić historię transakcji lub zastrzec kartę kredytową\n")
    
    wave_filename = "waves/answer.wav"

    'first answer recording'
    #print("recording...\n")
    #record_to_file(wave_filename)
    
    # Define phrases you want to spot
    phrases = ['historię', 'transakcji', 'transakcje', 'odblokować', 'zastrzec', 'zablokować', 'kartę']
    spotted = find_keywords(phrases, "waves/example_answer.wav")
