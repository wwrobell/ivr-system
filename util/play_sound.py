import winsound

def play_audio(audio_name):
    path = 'waves/' + audio_name
    winsound.PlaySound(path, winsound.SND_FILENAME)
    winsound.PlaySound('waves/sys_ping', winsound.SND_FILENAME)
