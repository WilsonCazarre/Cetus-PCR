import pickle
from tkinter import simpledialog

import constants as std

experiments = []


class Experiment:
    def __init__(self):
        self.name = ''
        self.denaturation_c = ''
        self.denaturation_t = ''
        self.annealing_c = ''
        self.annealing_t = ''
        self.extension_c = ''
        self.extension_t = ''
        self.number_cycles = ''
        self.final_temp = ''

    def __str__(self):
        return self.name


class StringDialog(simpledialog._QueryString):
    # Créditos ao TeamSpen210 do Reddit
    def body(self, master):
        super().body(master)
        self.iconbitmap(std.icon)


def ask_string(title, prompt, **kargs):
    d = StringDialog(title, prompt, **kargs)
    return d.result


def open_pickle(path):
    try:
        with open(path, 'rb') as infile:
            newlist = pickle.load(infile)
            return newlist
    except FileNotFoundError:
        return []


def dump_pickle(path, obj):
    with open(path, 'wb') as outfile:
        pickle.dump(obj, outfile)


def validate_entry(new_text):
    if new_text == '':
        return True
    try:
        int(new_text)
        if len(new_text) <= 3:
            return True
        else:
            return False
    except ValueError:
        return False

