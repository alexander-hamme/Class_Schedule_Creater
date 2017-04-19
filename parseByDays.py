# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:26:50 2016

@author: Alex Hamme
"""


def main(lst):
    '''
    Method to split classes up by day of the week. Returns tuple of five lists, one for each day
    :param lst: list of classes
    :return: tuple
    '''

    classes = list(lst)
    
    mon, tue, wed, thu, fri = [], [], [], [], []
    
    for cls in classes:
        days = cls[4]
        
        for lst, dy in zip([mon, tue, wed, thu, fri], ['M', 'Tu', 'W', 'Th', 'F']):
            if dy in days:
                lst.append(cls)

    return mon, tue, wed, thu, fri
