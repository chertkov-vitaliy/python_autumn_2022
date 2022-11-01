#!/bin/python
# use:   $./mkdir.py [dt_lesson]

from sys import argv
from datetime import date
import re
import os

FOLDER_HOMEWORK  = "homework"
FOLDER_CLASSWORK = "classwork"
FOLDER_MANUAL    = "manual"


def nice_day():
    today = date.today()
    dt_arg = argv[1] if len(argv) != 1 else None
    dt = "{0:%d}.{0:%m}.{0:%Y}".format(today)
    dt = dt_arg or dt
    return dt


def current_lesson():
    lst_dir = os.listdir(path='.')
    max_element = []
    for dir_ in lst_dir:
        m = re.search(r"_(?:\d+)_", dir_)
        if m:
            max_element.append(int(m.group(0).replace("_", "")))
    last_lesson = max(max_element)
    return last_lesson + 1


def get_name_folder():
    curr_lesson = current_lesson()
    dt = nice_day()
    folder = f"lesson_{curr_lesson}_{dt}"
    return folder


def mkdir():
    folder = get_name_folder()
    try:
        os.mkdir(folder)
        os.mkdir(f"{folder}/{FOLDER_HOMEWORK}")
        os.mkdir(f"{folder}/{FOLDER_CLASSWORK}")
        os.mkdir(f"{folder}/{FOLDER_MANUAL}")

    except Exception as e:
        print("Ошибка создания папки!", e)



mkdir()