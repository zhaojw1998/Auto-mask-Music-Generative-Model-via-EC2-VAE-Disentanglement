import pretty_midi as pyd
import os 

raw_midi_root = 'C:/Users/lenovo/Desktop/Computer Music Research/Deep-Music-Analogy-Demos/nottingham_midi'
dual_track_midi_root = 'C:/Users/lenovo/Desktop/Computer Music Research/Deep-Music-Analogy-Demos/nottingham_midi_dual-track'
if not os.path.exists(dual_track_midi_root):
    os.mkdir(dual_track_midi_root)
for mid in os.listdir(raw_midi_root):
    midi = os.path.join(raw_midi_root, mid)
    midi_data = pyd.PrettyMIDI(midi)
    if len(midi_data.instruments) == 1:
        midi_data.write(os.path.join(dual_track_midi_root, mid))
        continue
    melody = midi_data.instruments[0]
    chord_1 = midi_data.instruments[1]
    chord_2 = midi_data.instruments[2]
    new_chords = pyd.Instrument(program = pyd.instrument_name_to_program('Acoustic Grand Piano'))
    last_start = chord_1.notes[0].start
    for note in chord_1.notes:
        if note.start == last_start:
            continue
        for chord_note in chord_2.notes:
            if chord_note.start >= last_start and chord_note.end <= note.start:
                new_note = pyd.Note(velocity = 100, pitch = chord_note.pitch, start = last_start, end = note.start)
                new_chords.notes.append(new_note)
        last_start = note.start
    for chord_note in chord_2.notes:
        if chord_note.start >= last_start:
            new_note = pyd.Note(velocity = 100, pitch = chord_note.pitch, start = last_start, end = melody.notes[-1].end)
            new_chords.notes.append(new_note)
    gen_midi = pyd.PrettyMIDI()
    gen_midi.instruments.append(melody)
    gen_midi.instruments.append(new_chords)
    gen_midi.write(os.path.join(dual_track_midi_root, mid))
