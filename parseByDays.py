# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:26:50 2016

@author: Alex Hamme
"""

def main(lst):
    classes = list(lst)
    
    Mon = []; Tue = []; Wed = []; Thu = []; Fri = []; Sat = []; Sun = []
    
    for cls in classes:
        days = cls[4]
        
        for lst, dy in zip([Mon,Tue,Wed,Thu,Fri], ['M','Tu','W','Th','F']):
            if dy in days:
                lst.append(cls)
    return (Mon,Tue,Wed,Thu,Fri)
    
#if __name__ == '__main__':
#    import sys
#    main(sys.argv[1])
    