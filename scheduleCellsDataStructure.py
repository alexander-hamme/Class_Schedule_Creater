# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:50:11 2016

@author: Alex Hamme
"""

''' 

convert HH:MM times to seconds?


--> 
t = "11:10"
seconds = sum(int(x) * 60 ** (i+1) for i,x in enumerate(reversed(t.split(":"))))
^ needs to be in 24 hour format already


or tuples with hour as key; (hour, val)?
--> so each hour has its own tuple

'''

''' for html table, group cells into hour blocks? *** if they are all the same.

otherwise, divide up until you reach the smallest time unit that will allow you to display the class time.

E.g. hour --> 2   30 minute blocks --> 4   15 minute blocks --> 6   10 minute blocks --> 12   5 minute blocks



jsfiddle.net
'''

import dialogWindow as dWin
import parseByDays, parseTimes
from collections import deque
import operator, random, time

beginningTime = (8,0)  #8:00 AM
endingTime = (18,60)    #up until 7:00 PM

''' make it by 5 minute intervals, if less, round down or up?'''


''' don't do it by hours, except for the very left column!!!'''

class cellBlock:
    def __init__(self):
      self.rowSpan = 1
      self.html = ""

def main():
    #%%
    
    fullFreeHourCell = '''<tbody class = "border">'''+ 4*'''<tr class = "noborders"> <td>&nbsp</td></tr>'''
    
            
    def maintainHHMM(timeTuple):
        tmp = tuple(timeTuple)
        if tmp[1] >= 60 or tmp[1]%15 != 0:
            if tmp[1] >= 60:
                tmp = tuple((tmp[0]+1,tmp[1]%60))
            if tmp[1]%15 != 0:
                tmp = (tmp[0],(tmp[1]+5)-(tmp[1]+5)%15) # round down to nearest 15 unless within 5
                
        return tmp
    
    def incrementTime(timeTuple):
        #return maintainHHMM((timeTuple[0],timeTuple[1]+15))
        return ((timeTuple[0],timeTuple[1]+15))
    # DON'T use unless you can check that you are at the beginning of an hour slot
    
    """ make it by 15 min slots. if it's at 3:10, for example, just position it at 15.""" 
    
    tableHTML = ""
    
    #with open("tableHTML.txt",'r+') as tableHTML:
    
    all_classes = parseTimes.main(parseByDays.main(dWin.main()))
    
    timeZero = time.time()
    
    #classColors = ["#6AA783","#E0D1FF","#A8CD1B","#D9853B","#A2AB58","#CCEBF5","#BDA04F","#F0E0B2", 
    #               "#8EBCDE", "#FFCC66", "#9DBDBC","BCBD22", "9467BD","E377C2","17BECF"]   

    classColors = ["#C0DCEB", "#B2E48A", "#FBA4A3","#FDBF6F","#CAB2D6", "#FFFF99", "#FFE1E6", "#33A090", "#A99B47", "#4755A9", "#9A3D6D", "#6A3D9A"]

    '''          https://www.pinterest.com/kwaje/color-palette/
                 pinterest --> color palettes'''
                  
    cellPxSize = 15
    tableWidth = 95
    for day in ['Monday','Tuesday','Wednesday','Thursday','Friday']:
        
        tableHTML += '''<table><tr><th>'''+day+'''</th></tr>'''
        
        tableWidth -= 14
        classes = all_classes.get(day)
        print classes
        if classes == None or len(classes) == 0:
            
            ''' write blank cells'''
            fullDayCellHeight = (endingTime[0]*100 + endingTime[1]) - (beginningTime[0]*100 + beginningTime[1])
            if 7 <= fullDayCellHeight%15 <= 14: 
                fullDayCellHeight = (fullDayCellHeight+8)//15
            else:
                fullDayCellHeight = fullDayCellHeight//15
                
            timePos = beginningTime
            tableHTML+="<tbody>"
            while timePos <= endingTime:
                timePos = incrementTime(timePos)
                if timePos[1] == 60: 
                    tableHTML+= '''<tr><td style = "border:1px solid black; height:60px;">&nbsp</td></tr>'''
                timePos = maintainHHMM(timePos)
            tableHTML += "</tbody></table>"
            continue
        
        startTimes = []
        endTimes = []
        for cls in classes:
            startTimes.append(cls[0][0])    # adds in order of the classes
            endTimes.append(cls[0][1])
            
        print "startimes: ",startTimes,'\n',"endTimes: ",endTimes
        
        # Sort startTimes, while maintaining correct matching of each sTime - eTime pair
        sortedTogether = zip(*sorted(zip(list(startTimes), list(endTimes)), reverse=False))
        
        # make queue out of the sorted times
        startTimes = deque(sortedTogether[0])
        endTimes = deque(sortedTogether[1])
        
        print "new sTimes: ",startTimes, '\nnew eTimes: ', endTimes
        
        timePos = beginningTime
        
        
        classIdx = 0
        while True:#timePos <= endingTime: # while True instead. add a break statement. (?)
        #for hr in range (beginningTime[0], endingTime[0]+1):  # number of hours included in the schedule
            
        
        
            "TODO: change the text size of the cell if it is a very short duration. Cell padding too?"
        
            timePos = maintainHHMM(timePos) 
            
            if timePos >= endingTime:
                "Breaking now"
                break
        
            ''' instead of adding a bunch of free cells, 
            
            add one free cell block for every hour (or up until the start of a class)
            
            instead of:
            have a running cell height number and increment by (10)px each time
            until timePos reaches the start time of the next class, then write the cell.'''
            
            if len(startTimes) > 0 and len(endTimes) > 0:
                sTime = startTimes[0]#  peek           startTimes.popleft()
                eTime = endTimes[0]#                   endTimes.popleft()
                
                
                #startTimes MUST BE IN ORDER
                
                # assert: startTimes in order
                
            else:
                # No more classes for this day
                sTime = (0,0)
                eTime = (0,0)
                

            """ moving height attribute from <tr style> to <td style> may be critical"""
            
            if (timePos[0] != sTime[0]):
                # if there is no class within 15 minutes of timePos
                print "\nFirst if-block reached. timePos =",timePos
                
                count = 0
                while timePos[1] < 60 and timePos < endingTime:
                    #if timePos >= endingTime:
                    #    break
                    timePos = incrementTime(timePos)
                    count+=1
                tableHTML+= '''<tbody><tr>
                <td style = "border:1px solid black; height: {}px;">&nbsp</td></tr></tbody>'''.format(cellPxSize*count)
            
                timePos = maintainHHMM(timePos)
                
                print "timePos is now", timePos
                print "wrote free block"
  
            elif (timePos[0] == sTime[0] and abs(timePos[1] - sTime[1]) > 7 ):  # there is a class within current hour slot
               
            
            
                """this (was)? the part that was not working right.
                
                NOW it's the actual class block - for short classes / correct class duration
                
                """
            
            
                print "\nSecond if-block reached. timePos is {} and start time is {}".format(timePos,sTime)
                
                count = 0
                tmp = maintainHHMM(sTime)
                while timePos[1] < tmp[1]:  #<-- <= ???
                    timePos = incrementTime(timePos)
                    count+=1
                    if count == 4:
                        break

                print "timePos now at class start:",timePos,"~=",sTime,"?"
                #"border:1px solid black; 
                tableHTML+= '''<tbody><tr>
                <td style = "border:1px solid black; height: {}px;">&nbsp</td></tr></tbody>'''.format(cellPxSize*count)
                
                print "Count = {}, Free cell block should have a height of {} pixels".format(count, cellPxSize*count)
                
                timePos = maintainHHMM(timePos)
                 
                print "wrote free cells up to class"
                
            elif (timePos[0] == sTime[0] and abs(timePos[1] - sTime[1]) <= 7):   

                # if in current hour slot and minutes within nearest half of current pos  

                print "Reached class"# tableHTML += fullFreeHourCell  -- too risky
                
                
                '''needs to be accurate for shorter classes. Off by one 15 minute block right now?'''
                
                
                """
                count = 0 # Instead of <= because the class goes THROUGH the time, but we need timePos to stay at ending time(?)
                tmp = maintainHHMM(eTime)
                while timePos < tmp:    #need to compare both here, because hour values will probably change.
                                         
                    print "timePos is {} and <= {}?".format(timePos,tmp)    
                    timePos = maintainHHMM(incrementTime(timePos))
                    
                    count+=1
                    if timePos > endingTime:
                        raise Exception("Passed Ending Time")
                """
                
                # Instead of <= because the class goes THROUGH the time, but we need timePos to stay at ending time(?)
                tmp = maintainHHMM(eTime)
                while timePos < tmp:    #need to compare both here, because hour values will probably change.          
                    print "timePos is {} and <= {}?".format(timePos,tmp)    
                    timePos = maintainHHMM(incrementTime(timePos))
                    if timePos > endingTime:
                        raise Exception("Passed Final Ending Time")
                        
                classDur = (eTime[0]*60 + eTime[1]) - (sTime[0]*60 + sTime[1])
                count = (classDur+7)//15
            
                print "timePos reached class end:",timePos,"~=",eTime,"?","\ncount =",count

                """
                classDur = (eTime[0]*100 + eTime[1]) - (sTime[0]*100 + sTime[1])
                #classDur = tuple ((classDur//60, classDur%60))
                        #while timePos < classes[idx][1]: # less than, because otherwise it will continue into next cell
                #classEnd = tuple(map(lambda x, y: x + y, timePos, classDur))
                
                if 7 <= classDur%15 <= 14:      # divide the classDur by # of 15 minute blocks, **rounded up**
                    cellNumbs = (classDur+8)//15
                else:
                    cellNumbs = classDur//15
                """    
                    
                #cellNumbs = int(count)
                    
                    
                color = random.choice(classColors)
                print "Color = '{}'".format(color)
                
                try:
                    classColors.remove(color) # shuffle...
                except:
                    print "color not removed"
                    
                cls = classes[classIdx]
                
                ''' or get from parseByDays???  (e.g. by calling it again?)'''
                print cls
                
                cellHeight = count*cellPxSize 
                
                fontSize = 16 # (default size)
                lineHeight = 15
                
                for numb1,numb2 in zip([100,200,300],[50,40,30]):
                    if cellHeight > numb1:
                        lineHeight += 15
                #   for numb in [50,40,30]:
                    if cellHeight < numb2:
                        fontSize -= 3                    
                print "cellHeight: {}, lineHeight: {}, fontSize: {}".format(cellHeight,lineHeight,fontSize)
                tableHTML += '''<tbody>
                <tr>
                <td style = "border:1px solid black; height:{}px; background-color: {}; line-height:{}px; font-size:{}px">
                {} <!--<br></br>--> Room {} <!--<br></br>-->
                {}:{}-{}:{}
                </td></tr></tbody>'''.format(cellHeight, str(color), lineHeight, fontSize, str(cls[1]), str(cls[2]), str(cls[0][0][0]), str(cls[0][0][1]), str(cls[0][1][0]), str(cls[0][1][1]))
            
                
                # removing the space between {} and px after height: was critical
                
                #while timePos < eTime:#classEnd:
                    
                #    '''<td style="height:100px">   <-- change height according to class length? '''
                    
                #    tableHTML += '''<tr style = "border:2px solid black; background-color:''' + color +'''"> 
                #                    <td>Class '''+str(sTime)+'-' +str(eTime)+'''</td>
                #                </tr>'''
                    
                   # timePos = maintainHHMM(incrementTime(timePos))
                #timePos = eTime
               
                
                
                '''
                \/ this isn't accurate because classDur doesn't follow 60 minute stuff
                classDur = tuple ((classDur//60, classDur%60))
                timePos = tuple(map(lambda x, y: x + y, timePos, classDur)) # move timePos to end of written class
                '''

                print "timePos = end of class", timePos, "=", eTime, timePos == eTime
                
                try:
                    startTimes.popleft()    
                    endTimes.popleft()
                except:
                    try:
                        startTimes.remove(sTime)
                        endTimes.remove(eTime)
                    except Exception as e:
                        raise e    # need to stop the program because schedule won't write properly
                else:
                    print "Popped class: ",cls
                    
                classIdx += 1
                
            else:
                # Unnecessary, but just in case to prevent infinite looping
                timePos = incrementTime(timePos)
        
        print "Ending timePos =",timePos                        

        for i in range(len(startTimes)):    # semantically, the number of classes for the current day 
            pass
         
        tableHTML +="</table>"

    return tableHTML, "{:.10f}".format(time.time()-timeZero)
        

