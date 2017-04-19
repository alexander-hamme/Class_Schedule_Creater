# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:03:47 2016

@author: Alex Hamme
"""
from collections import deque
import scheduleCellsDataStructure as schedCells
import tkMessageBox, tkSimpleDialog
import Tkinter as tk
import dialogWindow
import time
import sys
import os

# Avoid overwriting file with same name
pathNumb = 0
while os.path.exists('schedule'+str(pathNumb)+'.html'):
    pathNumb += 1

widthNumb = 95
    
with open('schedule'+str(pathNumb)+'.html', 'w') as f: 
    
    #f = open('schedule'+str(pathNumb)+'.html','w')
    f.write('''<!DOCTYPE html>
                <html>
                <head>
                <title>ScheduleCreater</title>
                <meta charset="UTF-8" content="width=device-width, initial-scale=1.0">
                '''#<link rel="stylesheet" href="styleFile.css">
                '''
                <style>
                
                
                   body { 

                        font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
                        background-image: url('images/concrete_wall.png');
                        background-repeat: repeat;
                        background-color: gray;
                    }
                    
                    table {
                    
                        width: 10%;        
                        float: left;
                        
                        <!--table-layout: fixed;-->
                        
                        overflow:auto;<!--hidden?-->
                        border: solid 1px silver;
                        border-collapse:collapse;
                        background-image: url('images/blizzard.png');
                        background-repeat: repeat;
                        background-color: ghostwhite;
                    }
                    
                    th
                    {
                        margin: 0;
                        padding: 5px 10px;
                        text-align: center;
                        border-collapse: collapse;
                        border: 1px solid black;
                    }
                    
                    tr {
                    padding:0px;
                    border: 1px solid silver;-->
                    }
                    
                    td
                    {
                      
                      text-align: center;
                      margin: 0; 
                      padding: 0px 0px;
                      border-collapse: collapse;
                      border: 1px solid silver;
                    }
                    .borders {
                       border: 1px solid silver;
                       border-collapse:collapse;
                    }
                    
                    .noborders td {
                       border:0;
                    }
                    
                    .timeCell {
                       padding: 0px 0px;
                       border: 1px solid black;
                       margin: 0;
                       height:60px; 
                       
                    }
                    
                    .freeCell {
                    }
                    
                    th.timeHeading {
                        margin:0;
                        padding: 5px 10px;
                        text-align: center;
                        border-collapse: collapse;
                        border: 1px solid black;
                        background-color:white;
                    }
                    
                </style>
                </head>
                <body>''')
    

    f.write('''
            <table style = "width:7%; border-collapse:collapse"><tr><th id = "timeHeading">Time</th></tr>
    
            <tbody>
                    <tr>
                    <td class = "timeCell">8:00am</td></tr>   
            </tbody>
            <tbody>
                    <tr>
                    <td class = "timeCell">9:00am</td></tr>   
            </tbody>
            <tbody>
                    <tr>
                    <td class = "timeCell">10:00am</td></tr>   
            </tbody>
            <tbody>
                    <tr>
                    <td class = "timeCell">11:00am</td></tr>   
            </tbody>
            <tbody>
                    <tr>
                    <td class = "timeCell">12:00pm</td></tr>   
            </tbody>
            <tbody>
                    <tr>
                    <td class = "timeCell">1:00pm</td></tr>   
            </tbody>
            <tbody>
                    <tr>
                    <td class = "timeCell">2:00pm</td></tr>   
            </tbody>
            <tbody>
                    <tr>
                    <td class = "timeCell">3:00pm</td></tr>   
            </tbody>
            <tbody>
                    <tr>
                    <td class = "timeCell">4:00pm</td></tr>   
            </tbody>
            <tbody>
                    <tr>
                    <td class = "timeCell">5:00pm</td></tr>   
            </tbody>
            <tbody>
                    <tr>
                    <td class = "timeCell">6:00pm</td></tr>   
            </tbody>
            
            
            </table>''')
    
    
    
    
    """<table style = "width:10%; border-collapse:collapse"><tr><th id = "timeHeading">Time</th></tr>
            <tr style = "height:60px; border: 1px solid black">
                <td class = "timeCell">8:00 am</td></tr>
            <tr style = "height:60px; border: 1px solid black">
                <td style = "border: 1px solid black">9:00 am</td></tr>
            <tr style = "height:60px; border: 1px solid black">
                <td style = "border: 1px solid black">10:00 am</td></tr>        
            <tr style = "height:60px; border: 1px solid black">
                <td style = "border: 1px solid black">11:00 am</td></tr> 
            <tr style = "height:60px; border: 1px solid black">
                <td style = "border: 1px solid black">12:00 pm</td></tr>    
            <tr style = "height:60px; border: 1px solid black">
                <td style = "border: 1px solid black">1:00 pm</td></tr>
            <tr style = "height:60px; border: 1px solid black">
                <td style = "border: 1px solid black">2:00 pm</td></tr>    
            <tr style = "height:60px; border: 1px solid black">
                <td style = "border: 1px solid black">3:00 pm</td></tr>   
            <tr style = "height:60px; border: 1px solid black">
                <td style = "border: 1px solid black">4:00 pm</td></tr>    
            <tr style = "height:60px; border: 1px solid black">
                <td style = "border: 1px solid black">5:00 pm</td></tr>   
            <tr style = "height:60px; border: 1px solid black">
                <td style = "border: 1px solid black">6:00 pm</td></tr>    
            
            </table>
            
            """
    
    
    """
    for i in range(len(classes)):
        f.write("<th>")
        f.write("<td><tl>Course: "+classes[i][0]+"</tl></td>")
        f.write("<td>Room Number: "+classes[i][1]+"</td>")
        f.write("<td>Time: "+classes[i][2]+"</td>")
        f.write("<td>Days: "+classes[i][3]+"</td>")
        f.write("</th>")
    """
    html,timeElapsed = schedCells.main()
    #print html
    #f.write("<table>")
    f.write(str(html))
    #f.write("</table>")
    f.write('''</body>
                </html>''')
print "Elapsed time: {}s".format(timeElapsed)
#f.close()