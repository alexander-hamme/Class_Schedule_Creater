# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:45:20 2016

@author: Alex Hamme
"""

import Tkinter as tk
import tkMessageBox
import random

''' fancy stuff:
    https://www.tutorialspoint.com/python/tk_listbox.htm
    
https://www.tutorialspoint.com/python/tk_menu.htm
- main menu buttons and such
    
'''


'''

use wxPython or PyQT5   ?

'''



class dialogWindow:

    def __init__(self, parent, numbClasses = 5):
        
        self.answer1,self.answer2 = None,None #so cancel will work
        self.days = None
        
        self.eCourse = None
        self.eRmNumb = None
        self.eTime = None
        self.eClassDays = None
        self.classes = []
        
        self.numbClasses = numbClasses
        
        top = self.top = tk.Toplevel(parent)
        top.title("Add Courses")
        top.geometry("800x400")
        top.bind('<Return>', self.func)        #makes it possible to press enter button       
        
        ''' start out with 5(?) courses, add |+| plus button to add a course'''

        tk.Label(top, text = "Course name").grid(columnspan = 2, row = 2, column = 0, sticky = 'W',padx=5) #pack(side = 'left')
        tk.Label(top, text = "Room number").grid(columnspan = 2, row = 2, column = 1, sticky = 'W',padx=5)      
        tk.Label(top, text = "Start time").grid(columnspan = 2, row = 2, column = 2, sticky = 'W',padx=5)
        tk.Label(top, text = "End time").grid(columnspan = 2, row = 2, column = 3, sticky = 'W',padx=5)
        tk.Label(top, text = "Days").grid(columnspan = 2, row = 2, column = 4, sticky = 'W', padx = 10)
        
        numbClasses = 2
        rowNumb = 4
        
        #entryLabels = []
        
        def makeEntry(parent, rw, col, insertText, width=None, **options):
            entry = tk.Entry(parent, **options)
            # what other options?
            if width:
                entry.config(width=width)

            entry.grid(row = rw, column = col, padx = 5)
            entry.insert(0,insertText)
            return entry   
            
        
        #self.days = []    
        #def select(v):
        #    self.days.append(v.get())
            #more stuff?
            # or else get rid of this
        
        self.eCourses = []
        self.eRmNumbs = []
        self.eStartTimes = []
        self.eEndTimes = []
        self.eDays = []
        
        self.rowOffset = 2
        for i in range(self.numbClasses):
            #classV.__str__ = ''
            #classDays = []
            randCourse = "Course" + str(random.randint(101,334))
            randRoom = str(random.randint(100,230))
            randStartHr = random.randint(8,11)
            randEndHr = random.choice([random.randint(1,5),12])
            #randStartTime = random.choice([(str(randStartHr)+':'+random.choice(["00","10","15","30","45"])+' AM'),
            #                               (str(randEndHr)+':'+random.choice(["00","10","15","30","45"])+' PM')])
            randStartTime = str(str(randStartHr)+':'+str(random.choice(["00","10","15","30","45"]))+' AM')
            randEndTime = str(str(randEndHr)+':'+str(random.choice(["00","10","15","30","45"]))+' PM')
            randDays = ''.join(random.sample(["M/","T/","W/","Th/","F/"],random.randint(1,5)))
            self.eCourses.append(makeEntry(top, rowNumb, 0, insertText = randCourse, width = None))
            self.eRmNumbs.append(makeEntry(top, rowNumb, 1,insertText = randRoom, width = None))
            self.eStartTimes.append(makeEntry(top, rowNumb, 2, insertText = randStartTime, width = None))
            self.eEndTimes.append(makeEntry(top,rowNumb,3,insertText = randEndTime,width = None))
            
            
            #self.eDays.append(makeEntry(top,rowNumb,4,"M/Tu/W/Th/F",width = None))
            self.eDays.append(makeEntry(top,rowNumb,4,randDays,width = None))

            rowNumb += self.rowOffset
        
        plus = tk.Button(top, text = "plus", width = 15, padx = 5)
        plus.grid(row = rowNumb, column = 5)
        
        b = tk.Button(top, text = "Enter", command = self.ok, width = 15, padx = 5)
        b.grid(row = 4+rowNumb, column = 2)
        
        c = tk.Button(top, text = "Cancel", command = self.cancel, width = 7, padx = 5)
        c.grid(row = 4+rowNumb, column = 3)
        
        '''return tuple or dict for each class '''

        #top.mainloop()
    def cancel(self):
        self.top.destroy() #close window when done
    
    def func(self, event):
        self.ok()

    def ok(self):#storeClassInfo(self):
        #self.class1 = self.e.get()
        #self.answer1 = self.e.get()
        #self.answer2 = self.e2.get()
        '''
        self.eClassDays = [self.classDaysVar1.get(),self.classDaysVar2.get(),self.classDaysVar3.get(),self.classDaysVar4.get(),self.classDaysVar5.get()]
        
                           
        self.classDaysVar1 = ''.join(self.class1Days) 
        print self.classDaysVar1
                           
        print 'length is',len(self.eClassDays)
        print self.eClassDays
        '''
        
        """
        tmp = []
        classDays = []
        tmp.append(self.eClassDays[0][0])
        rowNumb = 4
        rowNumbs = []#set(self.eClassDays)  # lambda for x in self.eClassDays[0]...
        idx = 0
        
        for pair in self.eClassDays:
            rowNumbs.append(pair[0])
            if pair[0] == rowNumb:
                tmp.append(pair[1])
            else:
                self.eClassDays.append(tmp)
                rowNumb += self.rowOffset
                tmp = []
            '''
            # by rowNumb!!!
            while self.eClassDays[i][0] == self.eClassDays[i-1][0]:#pairs[idx] == pairs[idx-1]:
                tmp.append(self.eClassDays[i][1])
            
            if self.eClassDays[i][0] != self.eClassDays[i-1][0]:
                classDays.append(tmp)
            '''
        rowNumbs = set(rowNumbs)
        print rowNumbs
        """
        
        #for c,r, in zip(self.eCourses,self.eRmNumbs):
        #    print c.get(),r.get()
        for c,r,tS,tE,d in zip(self.eCourses,self.eRmNumbs,self.eStartTimes,self.eEndTimes,self.eDays):
            self.classes.append((c.get(),r.get(),tS.get(),tE.get(),d.get()))
            
        for i in range(len(self.classes)):
            pass
            #print self.classes[i]
        #for d in (self.eClassDays):
        #    print d#print self.classes[0]#days
        # \/ must be last    
        self.top.destroy()
        return self.classes
  

def main():
    root = tk.Tk()
    root.withdraw()
    d = dialogWindow(root)
    root.wait_window(d.top)
    return d.classes
    root.destroy()
    
#if __name__ == '__main__':
#    main()
    
'''
root = tk.Tk()

#root.mainloop()
root.withdraw()
d = dialogWindow(root)
#root.mainloop()
root.wait_window(d.top)
root.destroy()

'''
"""            
self.classDaysVar1 = tk.StringVar(value = "")
self.classDaysVar2 = tk.StringVar(value = "")
self.classDaysVar3 = tk.StringVar(value = "")
self.classDaysVar4 = tk.StringVar(value = "")
self.classDaysVar5 = tk.StringVar(value = "")
#if push add button again:
    # add more
    
# don't need stringvariables too?
self.class1Days = []
self.class2Days = []
self.class3Days = []
self.class4Days = []
self.class5Days = []
#for i,classV in zip( range(numbClasses), [self.classDaysVar1, ...]):
classDays = [self.class1Days,self.class2Days,self.class3Days,self.class4Days,self.class5Days]
classVs = [self.classDaysVar1,self.classDaysVar2,self.classDaysVar3,self.classDaysVar4,self.classDaysVar5]
#for classV,dayList in zip([self.classDaysVar1,self.classDaysVar2,self.classDaysVar3,self.classDaysVar4,self.classDaysVar5],
#                          [self.class1Days,self.class2Days,self.class3Days,self.class4Days,self.class5Days]):   
for i in range(len(classDays)):               

menubutton = tk.Menubutton(top, text="Select", indicatoron=True, borderwidth=1, relief="raised")
menu = tk.Menu(menubutton, tearoff = 1 )
menubutton.configure(menu=menu)
menubutton.grid(columnspan = 1, row = rowNumb, column = 3, padx = 10, pady = 1)

# within loop^



menu.add_checkbutton(label = "Mon", variable = classVs[i], onvalue = 1, offvalue = 0, command = lambda: classDays[i].append('M'))#.set(str(classV.get())+'M'))#select(monVar))
menu.add_checkbutton(label = "Tue", variable = classVs[i], onvalue = 1, offvalue = 0, command = lambda: classDays[i].append('T'))#classV.set(classV.get()+'T'))
menu.add_checkbutton(label = "Wed", variable = classVs[i], onvalue = 1, offvalue = 0, command = lambda: classDays[i].append('W'))#classV.set(classV.get()+'W'))
menu.add_checkbutton(label = "Thu", variable = classVs[i], onvalue = 1, offvalue = 0, command = lambda: classDays[i].append('H'))#classV.set(classV.get()+'H'))
menu.add_checkbutton(label = "Fri", variable = classVs[i], onvalue = 1, offvalue = 0, command = lambda: classDays[i].append('F'))#classV.set(classV.get()+'F'))
'''
menu.add_checkbutton(label = "Mon", variable = classV, onvalue = 1, offvalue = 0, command = lambda: dayList.append('M'))#.set(str(classV.get())+'M'))#select(monVar))
menu.add_checkbutton(label = "Tue", variable = classV, onvalue = 1, offvalue = 0, command = lambda: dayList.append('T'))#classV.set(classV.get()+'T'))
menu.add_checkbutton(label = "Wed", variable = classV, onvalue = 1, offvalue = 0, command = lambda: dayList.append('W'))#classV.set(classV.get()+'W'))
menu.add_checkbutton(label = "Thu", variable = classV, onvalue = 1, offvalue = 0, command = lambda: dayList.append('H'))#classV.set(classV.get()+'H'))
menu.add_checkbutton(label = "Fri", variable = classV, onvalue = 1, offvalue = 0, command = lambda: dayList.append('F'))#classV.set(classV.get()+'F'))
'''


''' add button to add time / week slot /option'''       
'''
monVar = tk.StringVar(value = "Mon"); tueVar = tk.StringVar(value = "Tue"); 
wedVar = tk.StringVar(value = "Wed"); thuVar = tk.StringVar(value = "Thu"); 
friVar = tk.StringVar(value = "Fri")#; add Sat and Sunday as optional (for rehearsals, etc)

#for day, dVar in zip( ["Mon","Tue","Wed","Thu","Fri"], [monVar,tueVar,wedVar,thuVar,friVar]):
#      menu.add_checkbutton(label = day, variable = dVar, onvalue = 1, offvalue = 0, command = lambda: classDays.append(str(dVar.get())))#select(monVar))

menu.add_checkbutton(label = "Mon", variable = monVar, onvalue = 1, offvalue = 0, command = lambda: self.eClassDays.append((rowNumb,monVar.get())))#select(monVar))
menu.add_checkbutton(label = "Tue", variable = tueVar, onvalue = 1, offvalue = 0, command = lambda: self.eClassDays.append((rowNumb,tueVar.get())))
menu.add_checkbutton(label = "Wed", variable = wedVar, onvalue = 1, offvalue = 0, command = lambda: self.eClassDays.append((rowNumb,wedVar.get())))
menu.add_checkbutton(label = "Thu", variable = thuVar, onvalue = 1, offvalue = 0, command = lambda: self.eClassDays.append((rowNumb,thuVar.get())))
menu.add_checkbutton(label = "Fri", variable = friVar, onvalue = 1, offvalue = 0, command = lambda: self.eClassDays.append((rowNumb,friVar.get()))) 


####### use rowNumb as ~unique key for each class.  or just use i'''

'''
def addBin(boolean):
    if boolean:
        classDayVar.set(classDayVar.get() + '1')
### Way to record data for multiple classes:
    
encode string var as "10100..." etc

so command = addClass() or whatever
and it adds "" + "1"
'''

#self.classes.append((self.eCourses[0].get(),self.eRmNumb.get(),self.eTime.get(),self.eClassDays))

# this is only going to store the inserted values because it is appending when it sets up
# the labels
"""