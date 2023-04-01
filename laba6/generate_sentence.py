from PIL import Image
from PIL.ImageOps import invert
from gen import FontDrawer
from helpers import calculate_profile, cut_black

SENTENCE = "𐒁𐒋𐒔𐒄𐒆𐒊 𐒇𐒘𐒝𐒏𐒆𐒎𐒓 𐒂𐒈𐒒𐒋𐒔𐒜𐒌 𐒍𐒗 𐒖𐒕𐒑𐒛𐒚"

if __name__ == '__main__':
    util = FontDrawer()
    result = util.render_binarized(SENTENCE, 170)

    initial = Image.fromarray(result,'L')
    initial.save(f"results/initial_sentence_white.bmp")
    initial = invert(initial)
    initial.save(f"results/initial_sentence_black.bmp")

    for axis in (0, 1):
        text_profile = calculate_profile(result, axis)
        result, _ = cut_black(result, text_profile, axis)

    string = Image.fromarray(result,'L')
    string.save(f"results/sentence_white.bmp")

    string = invert(string)
    string.save(f"results/sentence_black.bmp")