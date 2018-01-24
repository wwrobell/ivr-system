#!/usr/bin/env python
# -*- coding: utf-8 -*-

from techmo_sarmata_pyclient.utils.wave_loader import load_wave
from techmo_sarmata_pyclient.service.sarmata_settings import SarmataSettings
from techmo_sarmata_pyclient.service.sarmata_recognize import SarmataRecognizer
from techmo_sarmata_pyclient.service.asr_service_pb2 import ResponseStatus
from address_provider import AddressProvider
import os


def print_results(responses):
    if responses is None:
        print("Empty results - None object")
        return

    for response in responses:
        if response is None:
            print("Empty results - skipping response")
            continue

        print("Received response with status: {}".format(ResponseStatus.Name(response.status)))

        if response.error:
            print("[ERROR]: {}".format(response.error))

        for n, res in enumerate(response.results):
            transcript = " ".join([word.transcript for word in res.words])
            print("[{}.] {} /{}/ ({})".format(n, transcript, res.semantic_interpretation, res.confidence))


def glue_numbers(responses):
    numbers = []
    if responses is None:
        print("Empty results - None object")
        return
    try:
        res = responses[1].results[0]
        for word in res.words:
             numbers.append(word.transcript)

        return numbers
    except IndexError:
        return

def recognize_numbers(wave_file):
    ap = AddressProvider()
    grammar_file = "grammars/cyfry.abnf"
    address = ap.get("sarmata")

    audio = load_wave(wave_file)

    settings = SarmataSettings()
    session_id = os.path.basename(wave_file)
    settings.set_session_id(session_id)
    settings.load_grammar(grammar_file)

    recognizer = SarmataRecognizer(address)
    results = recognizer.recognize(audio, settings)
    #print_results(results)
    pass_words = glue_numbers(results)
    
    return pass_words
