from math import ceil
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from gen import FontDrawer
from helpers import calculate_profile, cut_black

SENTENCE = "𐒁𐒋𐒔𐒄𐒆𐒊 𐒇𐒘𐒝𐒏𐒆𐒎𐒓 𐒂𐒈𐒒𐒋𐒔𐒜𐒌 𐒍𐒗 𐒖𐒕𐒑𐒛𐒚"

if __name__ == '__main__':
    util = FontDrawer()
    result = util.render_binarized(SENTENCE, 170)

    for axis in (0, 1):
        text_profile = calculate_profile(result, axis)
        result, _ = cut_black(result, text_profile, axis)


    Image.fromarray(result,'L').save(f"results/sentence.bmp")