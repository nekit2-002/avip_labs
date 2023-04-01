from math import ceil
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from gen import FontDrawer

SENTENCE = "𐒁𐒋𐒔𐒄𐒆𐒊 𐒇𐒘𐒝𐒏𐒆𐒎𐒓 𐒂𐒈𐒒𐒋𐒔𐒜𐒌 𐒍𐒗 𐒖𐒕𐒑𐒛𐒚"

if __name__ == '__main__':
    util = FontDrawer()
    result = util.render_binarized(SENTENCE)

    Image.fromarray(result,'L').save(f"results/sentence.bmp")