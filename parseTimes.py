# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:15:34 2016

@author: Alex Hamme
"""

import dialogWindow as dWin
import parseByDays


def main(lst):
    '''
    intended to be used AFTER list of classes has been ran through parseByDays
    :param lst: list of classes
    :return: list of classes with times converted to 24 hour time
    '''

    classes_list = list(lst)

    classes = {}

    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    for i in range(len(classes_list)):  # list of lists of classes for each day

        classes[day_names[i]] = []
        if classes_list[i] is None:
            continue

        start_times = []
        end_times = []

        for cls in classes_list[i]:
            start_time = 0
            end_time = 0
            tmp = []

            for var, lst, idx in zip([start_time, end_time], [start_times, end_times], [2, 3]):
                try:
                    var = str(cls[idx])
                    assert ':' in var
                    assert ('AM' in var or 'am' in var or 'PM' in var or 'pm' in var)
                except AssertionError:
                    raise ValueError("Start time entered incorrectly: {}".format(cls[idx]))
                else:
                    if var[-3] == ' ':
                        hr, mns = var[:-3].split(':')
                    else:
                        hr, mns = var[:-2].split(':')
                    try:
                        hr = int(hr)
                        mns = int(mns)
                    except:
                        raise ValueError("Time entered incorrectly")

                    if var[-2:] in ['PM', 'pm'] and hr not in [12, '12']:  # don't need to do anything for AM
                        hr += 12

                    tmp.append((hr, mns))  # adds start_time first iteration, adds end_time second iteration

            classes[day_names[i]] += [(tuple(tmp), cls[0], cls[1])]

    return classes
