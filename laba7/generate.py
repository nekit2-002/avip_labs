from os import path
from math import ceil
from helpers import np, cut_white, calculate_profile
from PIL import Image, ImageFont, ImageDraw
from fontTools.ttLib import TTFont
from binarization import simple_bin


font_path = path.join('fonts', 'NotoSansOsmanya-Regular.ttf')
font_size = 52
osmanya = [
    '𐒀', '𐒁', '𐒂', '𐒃', '𐒄', '𐒅', '𐒆', '𐒇',
    '𐒈', '𐒉', '𐒊', '𐒋', '𐒌', '𐒍', '𐒎', '𐒏',
    '𐒐', '𐒑', '𐒒', '𐒓', '𐒔', '𐒕', '𐒖', '𐒗',
    '𐒘', '𐒙', '𐒚', '𐒛', '𐒜', '𐒝'
]


def filename(n):
    # return f"alphabet/direct/letter_{str(n + 1).zfill(2)}.png"
    return f"../laba6/results/symbols/letter_{n}.png"


class FontDrawer:
    def __init__(self):
        self.font = TTFont(font_path)
        self.img_font = ImageFont.truetype(font_path, font_size)
        self.cmap = self.font['cmap']
        self.t = self.cmap.getcmap(3, 1).cmap
        self.s = self.font.getGlyphSet()
        self.units_per_em = self.font['head'].unitsPerEm

    def render_text(self, text):
        img = Image.new(mode="RGB",
                        size=(ceil(self.get_text_width(text, font_size)),
                              font_size),
                        color="white")

        draw = ImageDraw.Draw(img)
        draw.text((0, -5), text, (0, 0, 0), font=self.img_font)

        return img

    def render_binarized(self, text, level=100):
        img = self.render_text(text)
        return 255 - simple_bin(np.array(img), level)

    def get_char_width(self, c, point_size):
        assert len(c) == 1

        if ord(c) in self.t and self.t[ord(c)] in self.s:
            pts = self.s[self.t[ord(c)]].width

        else:
            pts = self.s['.notdef'].width

        return pts * float(point_size) / self.units_per_em

    def get_text_width(self, text, point_size):
        total = 100

        for c in text:
            total += self.get_char_width(c, point_size)

        return total


def save_arr_as_img(arr, file_name):
    binarized_letter = Image.fromarray(255 - arr, 'L')
    binarized_letter = binarized_letter.convert('1')
    binarized_letter.save(file_name)


if __name__ == '__main__':
    font_drawer = FontDrawer()
    # letters that can merge
    for i, letter in enumerate(osmanya):
        binarized_arr = font_drawer.render_binarized(letter)
        # Delete white around letter
        for axis in (0, 1):
            letter_profile = calculate_profile(binarized_arr, axis)
            binarized_arr, _ = cut_white(binarized_arr, letter_profile, axis)

        save_arr_as_img(binarized_arr, filename(i))
