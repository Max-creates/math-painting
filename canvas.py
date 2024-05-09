import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.color = color

        self.data = np.zeros((self.w, self.h, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)
