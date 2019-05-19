def balls_collide(pos1, pos2):
    if pos1[2] < 0 or pos2[2] < 0:
        raise ValueError('Negative radius! Try again')
    else:
        return (pos2[2] + pos1[2]) ** 2 >= ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)
