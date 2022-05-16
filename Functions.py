import math


def fill_array(source):
    dist = []
    for i in range(len(source)):
        source[i] = source[i].replace(',', '.').replace('−', '-')
        if "E" in source[i]:
            tokens = source[i].split("E")
            exp = int(tokens[1].replace('-', ''))
            dist.append(float(tokens[0]) * (10 ** -exp))
        else:
            dist.append(float(source[i]))
    return dist


def calculate_angle_deg(source):
    v = []
    for x in source:
        v.append(math.degrees(math.asin(x)))
    return v