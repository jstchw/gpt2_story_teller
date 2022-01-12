import unittest
import os
from PIL import Image


class UnitTestBack(unittest.TestCase):
    memeDIR = 'www/img/memes'

    # If the image doesn't contain a number - the test doesn't pass
    def test_image_name(self):
        for root, dirs, files in os.walk(self.memeDIR):
            for name in files:
                name_spellcheck = name[:-5]
                self.assertEqual(name_spellcheck, 'meme', name_spellcheck)
                name_digitcheck = name[4:-4]
                self.assertTrue(name_digitcheck.isdigit(), name_digitcheck)

    # Check if the image is corrupted
    def test_image_integrity(self):
        assertion = True
        for filename in os.listdir(self.memeDIR):
            if filename.endswith('.jpg'):
                try:
                    img = Image.open(self.memeDIR + '/' + filename)
                    img.verify()
                except (IOError, SyntaxError) as e:
                    assertion = False

                self.assertTrue(assertion)

    def test_dir_availability(self):
        imgDIR = 'www/img'
        styleDIR = 'www/style'

        self.assertTrue(os.path.isdir(imgDIR))
        self.assertTrue(os.path.isdir(styleDIR))


if __name__ == '__main__':
    unittest.main()
