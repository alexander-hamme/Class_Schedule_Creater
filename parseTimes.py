# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:15:34 2016

@author: Alex Hamme
"""


'''
################ have a list of class start times ordered by soonness.

add empty cells while the time != the next start time.

have a full class block ready to insert at that point.

when you reach the first start time, add that, then delete that start time from the list.


https://docs.python.org/3/tutorial/datastructures.html



reroute stderr error stream to a file


replace all 'class' with 'course' for semantics


make a Course Object class?
with startTime,endTime attributes, for example

'''

import dialogWindow as dWin
import parseByDays

#class Course:

def main(lst, debug = True):    
    
    # intended to be used AFTER list of classes has been ran through parseByDays
    
    classesList = list(lst)
    
    #classes = []
    classes = {}
    
    
    dayNames = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    for i in range(len(classesList)):   # list of lists of classes for each day
      classes[dayNames[i]] = []
      if classesList[i] == None:
          continue
      startTimes = []
      endTimes = []
      for cls in classesList[i]:
          startTime = 0
          endTime = 0
          tmp = []
          #for i in range(2,4):  ( combine into one block )
          for var,lst,idx in zip([startTime,endTime],[startTimes,endTimes],[2,3]): 
              try:
                  var = str(cls[idx])
                  assert ':' in var
                  assert ('AM' in var or 'am' in var or 'PM' in var or 'pm' in var)
              except AssertionError:
                  raise Exception("Start time entered incorrectly")
              except Exception as e: 
                  raise e
              else:   
                  print "var = ",var
                  if var[-3] == ' ':
                     hr,mns = var[:-3].split(':')
                  else:
                     hr,mns = var[:-2].split(':')
                  try:
                     #seconds = sum(int(x) * 60 ** (i+1) for i,x in enumerate([mns,hr]))
                     hr = int(hr)
                     mns = int(mns)
                    
                     # totalMinutes = (hr-1)*60+mns # hasn't gone thru full current hour 
                     # need to also add end Time is the problem - will be a separate item in the list
                  except:
                     raise Exception("Time entered incorrectly")
                
                  if var[-2:] in ['PM','pm'] and hr not in [12,'12']:  # don't need to do anything for AM
                      print "changing",hr,"in",cls[idx],"to",hr+12
                      hr += 12
                      print "new hr: ",hr                 
                 
                  tmp.append((hr,mns)) # adds startTime first iteration, adds EndTime second iteration
              
              print "tmp = ",tmp
              #classes.append((dayNames[i],(tmp,cls[0],cls[1])))
          classes[dayNames[i]] += [(tuple(tmp),cls[0],cls[1])]
    '''tmpLst = []    
    for idx, (d,c) in enumerate(classes):
        if idx < len(classes)-1:
            if d == classes[idx+1][0]:
                #tmpLst.append(next(((d,c) for (d,c) in classes if d == classes[idx+1][0])))
                
            else:
                tmpLst.append((d,c))
          
      print tmpLst
    '''
        
    return classes#startTimes,endTimes
            #print dayNames[i],("\n{0}, {1}, {2}, {3}").format(var,hr,mns,totalMinutes)

#main(parseByDays.main(dWin.main()))           
          
            
            
            
            
def simpleParse(lst):
      classes = []
      classesList = list(lst)
      startTimes = []
      endTimes = []
      for cls in classesList:
        startTime = 0
        endTime = 0
        tmp = []
        #for i in range(2,4):  ( combine into one block )
        for var,lst,idx in zip([startTime,endTime],[startTimes,endTimes],[2,3]): 
            try:
                var = str(cls[idx])
                assert ':' in var
                assert ('AM' in var or 'am' in var or 'PM' in var or 'pm' in var)
            except AssertionError:
                raise Exception("Start time entered incorrectly")
            except Exception as e: 
                raise e
            else:   
                if var[-3] == ' ':
                    hr,mns = var[:-3].split(':')
                else:
                    hr,mns = var[:-2].split(':')
                try:
                    #seconds = sum(int(x) * 60 ** (i+1) for i,x in enumerate([mns,hr]))
                    hr = int(hr)
                    mns = int(mns)
                    
                    totalMinutes = (hr-1)*60+mns # hasn't gone thru full current hour 
                    
                    tmp.append((cls,(hr,mns)))
                    
                except:
                    raise Exception("Time entered incorrectly")
                
                if var[-2:] in ['PM','pm'] and hr not in [12,'12']:  # don't need to do anything for AM
                    hr += 12
                else:
                    pass
        classes.append(tmp)
            
        return classes     
#if __name__ == '__main__':
#    import sys
#    main(sys.argv[1])
    

