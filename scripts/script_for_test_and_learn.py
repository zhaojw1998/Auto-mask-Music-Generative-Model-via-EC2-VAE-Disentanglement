import pretty_midi as pyd
import music21 as m21
import os 

track_statistics={}

midi = 'results/presentation sample/Nottingham - 3.mid'
midi_data = pyd.PrettyMIDI(midi)
print(midi_data.instruments[1].notes)