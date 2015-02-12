# A LIST OF THE INTERVAL NAMES INDEXED BY SEMITONE
interval_names = ["Unison", "Minor second", "Major second", "Minor third", "Major third",
                  "Perfect fourth", "Diminished fifth", "Perfect fifth", "Augmented fifth",
                  "Major sixth", "Minor seventh", "Major seventh", "Octave", "Minor ninth",
                  "Major ninth" "Minor tenth" "Major tenth" "Perfect eleventh", "Diminished twelfth",
                  "Perfect twelfth", "Minor thirteenth", "Major thirteenth", "Minor fourteenth", "Major fourteenth"]

# A LIST OF THE NOTE NAMES
note_names = [["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"],
              ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]]

note_index = {"A": 0, "A#": 1, "B": 2, "C": 3, "C#": 4, "D": 5, "D#": 6, "E": 7, "F": 8, "F#": 9, 
                   "G": 10, "G#": 11, "Bb": 13, "Db": 16, "Eb": 18, "Gb": 21, "Ab": 23}


# CHORD INFORMATION

chords = [];

class ChordType:
    intervals = []
    name = ""
    short_name = ""
    position = 0;
    
    def __init__(self, intervals, name, short_name, position):
        self.intervals = intervals
        self.name = name
        self.short_name = short_name
        self.position = position
    
chords.append(ChordType([0, 4, 7], "Major", "", 0))
chords.append(ChordType([0, 3, 8], "Major", "", 1))
chords.append(ChordType([0, 5, 9], "Major", "", 2))
chords.append(ChordType([0, 3, 7], "Minor", "m", 0))
chords.append(ChordType([0, 3, 6], "Augmented", "aug", 0))
chords.append(ChordType([0, 4, 7], "Diminished", "dim", 0))
chords.append(ChordType([0, 4, 7, 9], "Major6th", "Maj6", 0))
chords.append(ChordType([0, 4, 7, 10], "Seventh", "7", 0))
chords.append(ChordType([0, 4, 7, 11], "Major 7th", "Maj7", 0))
chords.append(ChordType([0, 3, 7, 10], "Minor 7th", "m7", 0))
chords.append(ChordType([0, 4, 7, 11, 15], "Major9th", "Maj9", 0))
chords.append(ChordType([0, 4, 5, 7], "Suspended Fourth", "add4", 0))
    
# SCALE INFORMATION

# TWO OCTAVES OF INTERVALS FOR THE MAJOR SCALE
major_intervals = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23]

SHARP = 1
NATURAL = 0
FLAT = -1

# THESE ARE THE OFFSETS INTO THE note_names ARRAY. IF FLATS ARE TO BE USED
# THEN START AT 12 and ADD THE NOTE
SHARPS = 0
NATURALS = 0
FLATS = 1

scales = {};

class ScaleType:
    intervals = []
    name = ""
    notation = []
    
    def __init__(self, name, notation, intervals):
        self.name = name
        # THE OFFSETS RELATIVE TO THE BASELINE OF major_intervals
        self.intervals = intervals
        # INFORMATION USED FOR NAMING THE KEY AND THE NOTES WITHIN IT, FIRST INDEX IS 'A'. 
        self.notation = notation

scales['major'] = ScaleType("Major", [SHARPS, FLATS, SHARPS, NATURALS, FLATS, SHARPS, FLATS, SHARPS, FLATS, SHARPS, SHARPS, FLATS],
                        [NATURAL, NATURAL, NATURAL, NATURAL, NATURAL, NATURAL, NATURAL, NATURAL, NATURAL, NATURAL, NATURAL, NATURAL, NATURAL, NATURAL])

scales['minor'] = ScaleType("Minor", [NATURALS, FLATS, SHARPS, FLATS, SHARPS, FLATS, SHARPS, SHARPS, FLATS, SHARPS, FLATS, SHARPS],
                        [NATURAL, NATURAL, FLAT, NATURAL, NATURAL, FLAT, FLAT, NATURAL, NATURAL, FLAT, NATURAL, NATURAL, FLAT, FLAT])

class Scale:
    root_note = 0
    scale_type = 0
    notes = []
    
    def __init__(self, root_note, scale_type):
        self.root_note = note_index[root_note]
        self.scale_type = scales[scale_type]
        
        for x in range(0,7):
            self.notes.append(self.root_note + scale_type.intervals[x] + major_intervals[x])
        
    def print_notes(self):
        for note in self.notes:
            print note_names[self.scale_type.notation[note % 12]][note % 12]
