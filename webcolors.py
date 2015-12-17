import colorsys


def scale_rgb_tuple(rgb, down=True):
    if not down:
        return tuple([int(c*255) for c in rgb])
    return tuple([round(float(c)/255, 2) for c in rgb])


def hex_to_rgb(hex_str):
    if hex_str.startswith('#'):
        hex_str = hex_str[1:]
    return tuple([int(hex_str[i:i + 2], 16) for i in xrange(0, len(hex_str), 2)])


def hex_to_rgb_float(hex_str):
    return scale_rgb_tuple(hex_to_rgb(hex_str), down=True)


def rgb_to_hex(rgb):
    return ''.join(["%0.2X" % c for c in rgb])


def hsv_to_hex(hsv):
    return rgb_to_hex(scale_rgb_tuple(colorsys.hsv_to_rgb(*hsv), down=False))
