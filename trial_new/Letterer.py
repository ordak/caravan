import enum
import queue
import time
import random
import toolz.itertoolz as itz
import itertools
import json

class AlphaSet:
    def __init__(self, alphabet, sidelobe_size=2):
        self._alphabet = alphabet
        self._sidelobe_size = sidelobe_size
        self._update_window_indices()
        self._iterator = itz.sliding_window(5, itertools.cycle(list(alphabet)))
        self._current = next(self._iterator)

    def _update_window_indices(self):
        self._window_size = 2 * sidelobe_size + 1
        self._window_center_index = sidelobe_size

    def get_center_letter(self):
        return self._current[self._window_center_index]



class Letterer:
    def __init__(self, sidelobe_size=2):
        self._alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 01234567890'
alphaSet = next(alphaIter)
accumulated = "Wiggle"
