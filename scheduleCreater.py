# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:03:47 2016
@author: Alex Hamme
"""
from collections import deque
import tkMessageBox, tkSimpleDialog
import Tkinter as tk
import dialogWindow
import scheduleCells
import time
import sys
import os

# Avoid overwriting file with same name
pathNumb = 0
while os.path.exists('schedule'+str(pathNumb)+'.html'):
    pathNumb += 1

widthNumb = 95
    
with open('schedule'+str(pathNumb)+'.html', 'w') as f: 
    
    f.write('''<!DOCTYPE html>
                <html>
                <head>
                <title>ScheduleCreater</title>
                <meta charset="UTF-8" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" type="text/css" href="stylefile.css">
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

    html, time_elapsed = scheduleCells.CellScheduler.main()

    f.write(str(html))
    f.write('''</body>
                </html>''')
print "Elapsed time: {}s".format(time_elapsed)
