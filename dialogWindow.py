# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:45:20 2016

@author: Alex Hamme
"""

import Tkinter as tK
import random


class DialogWindow:
    def __init__(self, parent, numbclasses=5):
        self.answer1, self.answer2 = None, None  # so cancel will work
        self.days = None
        self.e_course = None
        self.e_rm_numb = None
        self.e_time = None
        self.e_class_days = None
        self.classes = []
        self.numb_classes = numbclasses
        self.top = tK.Toplevel(parent)

        self.e_courses = []
        self.e_rm_numbs = []
        self.e_start_times = []
        self.e_end_times = []
        self.e_days = []

        self.row_offset = 2

        self.setup(parent, numbclasses)

    def make_entry(self, parent, rw, col, insert_text, width=None, **options):
        entry = tK.Entry(parent, **options)

        if width:
            entry.config(width=width)

        entry.grid(row=rw, column=col, padx=5)
        entry.insert(0, insert_text)
        return entry

    def setup(self, parent, numb_classes):
        top = self.top
        top.title("Add Courses")
        top.geometry("800x400")
        top.bind('<Return>', self.func)  # makes it possible to press enter button

        # Start out with 5 courses
        tK.Label(top, text="Course name").grid(columnspan=2, row=2, column=0, sticky='W', padx=5)
        tK.Label(top, text="Room number").grid(columnspan=2, row=2, column=1, sticky='W', padx=5)
        tK.Label(top, text="Start time").grid(columnspan=2, row=2, column=2, sticky='W', padx=5)
        tK.Label(top, text="End time").grid(columnspan=2, row=2, column=3, sticky='W', padx=5)
        tK.Label(top, text="Days").grid(columnspan=2, row=2, column=4, sticky='W', padx=10)
        # TODO: add |+| plus button to add a course

        row_numb = 4

        for i in range(self.numb_classes):
            # Generate random values for each text field
            rand_course = "Course" + str(random.randint(101, 334))
            rand_room = str(random.randint(100, 230))
            rand_start_hr = random.randint(8, 11)
            rand_end_hr = random.choice([random.randint(1, 5), 12])

            rand_start_time = str(str(rand_start_hr) + ':' + str(random.choice(["00", "10", "15", "30", "45"])) + ' AM')
            rand_end_time = str(str(rand_end_hr) + ':' + str(random.choice(["00", "10", "15", "30", "45"])) + ' PM')
            rand_days = ''.join(random.sample(["M/", "T/", "W/", "Th/", "F/"], random.randint(1, 5)))

            self.e_courses.append(self.make_entry(top, row_numb, 0, insert_text=rand_course, width=None))
            self.e_rm_numbs.append(self.make_entry(top, row_numb, 1, insert_text=rand_room, width=None))
            self.e_start_times.append(self.make_entry(top, row_numb, 2, insert_text=rand_start_time, width=None))
            self.e_end_times.append(self.make_entry(top, row_numb, 3, insert_text=rand_end_time, width=None))
            self.e_days.append(self.make_entry(top, row_numb, 4, rand_days, width=None))

            row_numb += self.row_offset

        plus = tK.Button(top, text="plus", width=15, padx=5)
        plus.grid(row=row_numb, column=5)

        b = tK.Button(top, text="Enter", command=self.ok, width=15, padx=5)
        b.grid(row=4 + row_numb, column=2)

        c = tK.Button(top, text="Cancel", command=self.cancel, width=7, padx=5)
        c.grid(row=4 + row_numb, column=3)

    def cancel(self):
        self.top.destroy()

    def func(self, event):
        self.ok()

    def ok(self):
        # Get values for each text box
        for c, r, tS, tE, d in zip(self.e_courses, self.e_rm_numbs, self.e_start_times, self.e_end_times, self.e_days):
            self.classes.append((c.get(), r.get(), tS.get(), tE.get(), d.get()))

        self.top.destroy()
        return self.classes

def main():
    root = tK.Tk()
    root.withdraw()
    d = DialogWindow(root)
    root.wait_window(d.top)
    return d.classes
