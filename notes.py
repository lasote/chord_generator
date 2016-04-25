all_notes = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
scale_pattern_reg = (2, 2, 2, 1, 2, 2, 2, 1)


def next_note_in_scale(scale_pattern, scale_note, step, previous_note):
    if not previous_note:
        next_note = scale_note
    else:
        prev_index = all_notes.index(previous_note)
        increase = scale_pattern_reg[step]
        next_note = all_notes[(prev_index + increase) % len(all_notes)]
    return next_note


def generate_scale_notes(note):
    notes = [note]
    previous = note
    for step in range(1, 7):
        the_next = next_note_in_scale(scale_pattern_reg, note, step, previous)
        notes.append(the_next)
        previous = the_next

    return notes


def generate_grade_chord_in_scale(scale_note, grade):
    notes = generate_scale_notes(scale_note)
    chord_notes = []

    first_index = (grade - 1) % len(notes)
    third_index = (grade + 1) % len(notes)
    fifth_index = (grade + 3) % len(notes)

    chord_notes.append(notes[first_index])
    chord_notes.append(notes[third_index])
    chord_notes.append(notes[fifth_index])
    return chord_notes


def chord_name(chord):
    first_index = all_notes.index(chord[0])
    third_index = all_notes.index(chord[1])
    fifth_index = all_notes.index(chord[2])
    distance_1 = (third_index - first_index) % len(all_notes)
    distance_2 = (fifth_index - third_index) % len(all_notes)
    chords = {(4, 3): "", (3, 4): "m", (3, 3): "dim", (4, 4): "aug"}
    return chord[0] + chords[(distance_1, distance_2)]

if __name__ == "__main__":
    for note in all_notes:
        print "%s scale notes: %s" % (note, generate_scale_notes(note))
        chords = []
        for grade in xrange(1, 8):
            chords.append(chord_name(generate_grade_chord_in_scale(note, grade)))
        print "%s scale chords: %s\n" % (note, chords)
