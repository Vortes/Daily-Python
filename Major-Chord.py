notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
interval = [0, 2, 4, 5, 7, 9, 11, 0]

def octave(key, notes, interval):
    new_scale = []
    marker = notes.index(key)

    if key == notes[0]:
        for i in range(len(interval)):
            new_scale.append(notes[interval[i]])

        return new_scale

    elif key == notes[-1]:
        temp = notes.copy()
        temp.insert(0,notes[-1])

        for i in range(len(interval)):
            new_scale.append(temp[interval[i]])
        
        return new_scale

    else:
        left_hand_side = notes[0:marker]
        left_hand_side.append(key)
        right_hand_side = notes[marker+1:-1]
        right_hand_side.append(notes[-1])
        right_hand_side.insert(0,key)
        temp_scale = right_hand_side + left_hand_side
        
        for i in range(len(interval)):
            new_scale.append(temp_scale[interval[i]])

        return new_scale


print(octave("C#", notes, interval))




