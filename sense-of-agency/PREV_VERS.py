﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 05, 2022, at 12:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard


############################
#                          #
#  Threading for logging!  #
#                          #
############################
import time
import threading
import sys
sys.path.append('../')

###  UNCOMMENT THESE TO LOG BACK TO RTM  ###
from UDP_rec_and_send import start_loop
game_state_dict = {}  # dictionary to update throughout experiment with game state (which we pass to the logger)
logging_thread = threading.Thread(target=start_loop, args=(game_state_dict,))
logging_thread.start()
start_time = time.time()
#^^^^^^^^^^^^^^^^^^^^^^^^^^#



leftOpacity = 1;
rightOpacity = 1;
delaymain = 0;


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'mukesh_IB'  # from the Builder filename that created this script
expInfo = {'Participant': '001', 'Session': '', 'Block': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s/%s_%s' %(expInfo['Participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mukes.DESKTOP-PFSHT1J\\Downloads\\IB_new_task_Feb7\\IB_new_task_Feb7\\IB_task_new_main.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 810], fullscr=False, screen=0,  #size=[1920, 1080], fullscr=True,
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome_main"
welcome_mainClock = core.Clock()
from psychopy import core, event
curPos = -0.5
Instructions_2 = visual.TextStim(win=win, name='Instructions_2',
    text='Welcome to the experiment.\n\nIn this block, you have to report the time interval between your button click and the motion onset of the ball on the screen.\n\nOn each trial you have to choose in which direction you want to move the ball either left or right. \n\nWhen you are ready you can choose left or right option. After a variable delay of button click, you will see the ball moving. The ball may move in your intended direction or may move in opposite direction.\n\nYou have to report the delay between your button click and when the ball started moving by choosing the number between 0ms to 2000ms.\n\nYou also have to report about much control you experienced over the ball, by selecting  a number between “No control” to "Full control”.\n\nYou also have to report if the ball moved in your intended direction or not.\n\nPress SPACEBAR to continue.\n',
    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Inst_key_2 = keyboard.Keyboard()

# Initialize components for Routine "intention_main"
intention_mainClock = core.Clock()
background = visual.ImageStim(
    win=win,
    name='background', 
    image='Field.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Instructions_3 = visual.TextStim(win=win, name='Instructions_3',
    text='Which direction do you wish to move the ball?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
football = visual.ImageStim(
    win=win,
    name='football', units='height', 
    image='football.png', mask=None,
    ori=0.0, pos=(0, -0.19), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
post_left = visual.ImageStim(
    win=win,
    name='post_left', 
    image='post.png', mask=None,
    ori=0.0, pos=(-.73, -0.29), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=leftOpacity,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
post_right = visual.ImageStim(
    win=win,
    name='post_right', 
    image='post.png', mask=None,
    ori=0.0, pos=(.73, -0.29), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=rightOpacity,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
leftGesture = visual.ImageStim(
    win=win,
    name='leftGesture', 
    image='Power_Front.png', mask=None,
    ori=90.0, pos=(-0.25, -0.6), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
rightGesture = visual.ImageStim(
    win=win,
    name='rightGesture', 
    image='OpenHand_Front.png', mask=None,
    ori=90.0, pos=(0.25, -0.6), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
intention_keys = keyboard.Keyboard()
leftBar = visual.Rect(
    win=win, name='leftBar',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
rightBar = visual.Rect(
    win=win, name='rightBar',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
leftCount = -1
rightCount = -1

leftOrder = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21];
leftList = ['L','L','L','L','L','L','L','L','L','L','L','R', 'R','R','R','R','R','R','R','R','R','R'];
leftDelay = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2];
shuffle(leftOrder)

rightOrder = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21];
rightList = ['L','L','L','L','L','L','L','L','L','L','L','R', 'R','R','R','R','R','R','R','R','R','R'];
rightDelay = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2];
shuffle(rightOrder)

lh = [0.02,0.02];
rh = [0.02,0.02];

lpos = [-0.9,0];
rpos = [0.9,0];



# Initialize components for Routine "delay_main"
delay_mainClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
background_2 = visual.ImageStim(
    win=win,
    name='background_2', 
    image='Field.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
post_left_2 = visual.ImageStim(
    win=win,
    name='post_left_2', 
    image='post.png', mask=None,
    ori=0.0, pos=(-.73, -0.29), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=leftOpacity,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
post_right_2 = visual.ImageStim(
    win=win,
    name='post_right_2', 
    image='post.png', mask=None,
    ori=0.0, pos=(.73, -0.29), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=rightOpacity,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
football_2 = visual.ImageStim(
    win=win,
    name='football_2', units='height', 
    image='football.png', mask=None,
    ori=0.0, pos=(0, -0.19), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
leftGesture_2 = visual.ImageStim(
    win=win,
    name='leftGesture_2', 
    image='Power_Front.png', mask=None,
    ori=90.0, pos=(-0.25, -0.6), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
rightGesture_2 = visual.ImageStim(
    win=win,
    name='rightGesture_2', 
    image='OpenHand_Front.png', mask=None,
    ori=90.0, pos=(0.25, -0.6), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
leftBar_2 = visual.Rect(
    win=win, name='leftBar_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
rightBar_2 = visual.Rect(
    win=win, name='rightBar_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
Instructions_5 = visual.TextStim(win=win, name='Instructions_5',
    text='Which direction do you wish to move the ball?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "target_main"
target_mainClock = core.Clock()
background_3 = visual.ImageStim(
    win=win,
    name='background_3', 
    image='Field.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
post_left_3 = visual.ImageStim(
    win=win,
    name='post_left_3', 
    image='post.png', mask=None,
    ori=0.0, pos=(-.73, -0.29), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=leftOpacity,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
post_right_3 = visual.ImageStim(
    win=win,
    name='post_right_3', 
    image='post.png', mask=None,
    ori=0.0, pos=(.73, -0.29), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=rightOpacity,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
football_3 = visual.ImageStim(
    win=win,
    name='football_3', units='height', 
    image='football.png', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
leftGesture_3 = visual.ImageStim(
    win=win,
    name='leftGesture_3', 
    image='Power_Front.png', mask=None,
    ori=90.0, pos=(-0.25, -0.6), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
rightGesture_3 = visual.ImageStim(
    win=win,
    name='rightGesture_3', 
    image='OpenHand_Front.png', mask=None,
    ori=90.0, pos=(0.25, -0.6), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
leftBar_3 = visual.Rect(
    win=win, name='leftBar_3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
rightBar_3 = visual.Rect(
    win=win, name='rightBar_3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
Instructions_6 = visual.TextStim(win=win, name='Instructions_6',
    text='Which direction do you wish to move the ball?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "resp_main"
resp_mainClock = core.Clock()
from psychopy import core, event
timeTicks = range(1,2000)


timing_slider = visual.Slider(win=win, name='timing_slider',
    startValue=None, size=(1.5, 0.2), pos=(0, -0.4), units=None,
    labels=('0ms', '2000ms'), ticks=[0, 2000], granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.07,
    flip=False, depth=-1, readOnly=False)
submit_button = visual.ButtonStim(win, 
    text='Submit', font='Arial',
    pos=(0, -0.7),
    letterHeight=0.09,
    size=(.3,.3), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='submit_button'
)
submit_button.buttonClock = core.Clock()
Timetext = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, -0.8),     letterHeight=0.07,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='Timetext',
     autoLog=True,
)
timing_question = visual.TextStim(win=win, name='timing_question',
    text='What was the delay between the buttonpress and the motion onset?\n',
    font='Arial',
    pos=[0, 0.1], height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()

# Initialize components for Routine "rating_main"
rating_mainClock = core.Clock()
confidenceScale = visual.Slider(win=win, name='confidenceScale',
    startValue=None, size=(1.5, 0.2), pos=(0, -0.4), units=None,
    labels=("No control", "Full Control"), ticks=[1,2,3,4,5,6], granularity=1.0,
    style='slider', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.07,
    flip=False, depth=-1, readOnly=False)
condifence_submit = visual.ButtonStim(win, 
    text='Submit', font='Arial',
    pos=(0, -0.7),
    letterHeight=0.09,
    size=(.3,.3), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='condifence_submit'
)
condifence_submit.buttonClock = core.Clock()
Confidence_question = visual.TextStim(win=win, name='Confidence_question',
    text='How much control did you feel in this trial?\n',
    font='Arial',
    pos=[0, 0.1], height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "intention_check"
intention_checkClock = core.Clock()
intentionCheck = " ";
only_Question = visual.TextStim(win=win, name='only_Question',
    text='Did the ball move as you intended?\n',
    font='Arial',
    pos=[0, 0.1], height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
button_no = visual.ButtonStim(win, 
    text='      No', font='Arial',
    pos=(-.25, -0.6),
    letterHeight=0.1,
    size=[.3,.3], borderWidth=0.0,
    fillColor='darkslategrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_no'
)
button_no.buttonClock = core.Clock()
button_yes = visual.ButtonStim(win, 
    text='    Yes', font='Arial',
    pos=(.25, -0.6),
    letterHeight=0.1,
    size=[.3,.3], borderWidth=0.0,
    fillColor='darkslategrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_yes'
)
button_yes.buttonClock = core.Clock()

# Initialize components for Routine "thanks_2"
thanks_2Clock = core.Clock()
Instructions_7 = visual.TextStim(win=win, name='Instructions_7',
    text='Thanks for participating',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome_main"-------
continueRoutine = True
# update component parameters for each repeat
event.Mouse(visible=False)
Inst_key_2.keys = []
Inst_key_2.rt = []
_Inst_key_2_allKeys = []
# keep track of which components have finished
welcome_mainComponents = [Instructions_2, Inst_key_2]
for thisComponent in welcome_mainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_main"-------
# first step in loop bool
first_loop = True  # update game state in first iteration of while DW
while continueRoutine:

    # STEP 1, update game_state to 0.1 DW
    if first_loop == True:
        game_state_dict["current_state"] = 0.1  # welcome_main
        game_state_dict["time_entered_state"] = time.time() - start_time
        first_loop = False

    # get current time
    t = welcome_mainClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_mainClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions_2* updates
    if Instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_2.frameNStart = frameN  # exact frame index
        Instructions_2.tStart = t  # local t and not account for scr refresh
        Instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_2, 'tStartRefresh')  # time at next scr refresh
        Instructions_2.setAutoDraw(True)
    
    # *Inst_key_2* updates
    waitOnFlip = False
    if Inst_key_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Inst_key_2.frameNStart = frameN  # exact frame index
        Inst_key_2.tStart = t  # local t and not account for scr refresh
        Inst_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Inst_key_2, 'tStartRefresh')  # time at next scr refresh
        Inst_key_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Inst_key_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Inst_key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Inst_key_2.status == STARTED and not waitOnFlip:
        theseKeys = Inst_key_2.getKeys(keyList=['space'], waitRelease=False)
        _Inst_key_2_allKeys.extend(theseKeys)
        if len(_Inst_key_2_allKeys):
            Inst_key_2.keys = _Inst_key_2_allKeys[-1].name  # just the last key pressed
            Inst_key_2.rt = _Inst_key_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_mainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_main"-------
for thisComponent in welcome_mainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions_2.started', Instructions_2.tStartRefresh)
thisExp.addData('Instructions_2.stopped', Instructions_2.tStopRefresh)
# check responses
if Inst_key_2.keys in ['', [], None]:  # No response was made
    Inst_key_2.keys = None
thisExp.addData('Inst_key_2.keys',Inst_key_2.keys)
if Inst_key_2.keys != None:  # we had a response
    thisExp.addData('Inst_key_2.rt', Inst_key_2.rt)
thisExp.addData('Inst_key_2.started', Inst_key_2.tStartRefresh)
thisExp.addData('Inst_key_2.stopped', Inst_key_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome_main" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mainExpLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond_trial.xlsx'),
    seed=None, name='mainExpLoop')
thisExp.addLoop(mainExpLoop)  # add the loop to the experiment
thisMainExpLoop = mainExpLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMainExpLoop.rgb)
if thisMainExpLoop != None:
    for paramName in thisMainExpLoop:
        exec('{} = thisMainExpLoop[paramName]'.format(paramName))

for thisMainExpLoop in mainExpLoop:
    currentLoop = mainExpLoop
    # abbreviate parameter names if possible (e.g. rgb = thisMainExpLoop.rgb)
    if thisMainExpLoop != None:
        for paramName in thisMainExpLoop:
            exec('{} = thisMainExpLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intention_main"-------
    continueRoutine = True
    # update component parameters for each repeat
    intention_keys.keys = []
    intention_keys.rt = []
    _intention_keys_allKeys = []
    leftBar.setPos(lpos)
    leftBar.setSize(lh)
    rightBar.setPos(rpos)
    rightBar.setSize(rh)
    event.Mouse(visible=False,newPos=(0,curPos))
    # keep track of which components have finished
    intention_mainComponents = [background, Instructions_3, football, post_left, post_right, leftGesture, rightGesture, intention_keys, leftBar, rightBar]
    for thisComponent in intention_mainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intention_mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # count main loops
    mainExpLoop_counter = 1

    # -------Run Routine "intention_main"-------
    first_loop = True # update game state in first loop of while

    while continueRoutine:

        # update game_state
        if first_loop == True:
            game_state_dict["current_state"] = mainExpLoop_counter + 0.1  # intention_main
            game_state_dict["time_entered_state"] = time.time() - start_time
            first_loop = False

        # get current time
        t = intention_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intention_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background* updates
        if background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background.frameNStart = frameN  # exact frame index
            background.tStart = t  # local t and not account for scr refresh
            background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background, 'tStartRefresh')  # time at next scr refresh
            background.setAutoDraw(True)
        
        # *Instructions_3* updates
        if Instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_3.frameNStart = frameN  # exact frame index
            Instructions_3.tStart = t  # local t and not account for scr refresh
            Instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_3, 'tStartRefresh')  # time at next scr refresh
            Instructions_3.setAutoDraw(True)
        
        # *football* updates
        if football.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            football.frameNStart = frameN  # exact frame index
            football.tStart = t  # local t and not account for scr refresh
            football.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(football, 'tStartRefresh')  # time at next scr refresh
            football.setAutoDraw(True)
        
        # *post_left* updates
        if post_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            post_left.frameNStart = frameN  # exact frame index
            post_left.tStart = t  # local t and not account for scr refresh
            post_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(post_left, 'tStartRefresh')  # time at next scr refresh
            post_left.setAutoDraw(True)
        
        # *post_right* updates
        if post_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            post_right.frameNStart = frameN  # exact frame index
            post_right.tStart = t  # local t and not account for scr refresh
            post_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(post_right, 'tStartRefresh')  # time at next scr refresh
            post_right.setAutoDraw(True)
        
        # *leftGesture* updates
        if leftGesture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leftGesture.frameNStart = frameN  # exact frame index
            leftGesture.tStart = t  # local t and not account for scr refresh
            leftGesture.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftGesture, 'tStartRefresh')  # time at next scr refresh
            leftGesture.setAutoDraw(True)
        
        # *rightGesture* updates
        if rightGesture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightGesture.frameNStart = frameN  # exact frame index
            rightGesture.tStart = t  # local t and not account for scr refresh
            rightGesture.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightGesture, 'tStartRefresh')  # time at next scr refresh
            rightGesture.setAutoDraw(True)
        
        # *intention_keys* updates
        waitOnFlip = False
        if intention_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intention_keys.frameNStart = frameN  # exact frame index
            intention_keys.tStart = t  # local t and not account for scr refresh
            intention_keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intention_keys, 'tStartRefresh')  # time at next scr refresh
            intention_keys.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(intention_keys.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(intention_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if intention_keys.status == STARTED and not waitOnFlip:
            theseKeys = intention_keys.getKeys(keyList=['left', 'right', 'escape'], waitRelease=False)
            _intention_keys_allKeys.extend(theseKeys)
            if len(_intention_keys_allKeys):
                intention_keys.keys = _intention_keys_allKeys[-1].name  # just the last key pressed
                intention_keys.rt = _intention_keys_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *leftBar* updates
        if leftBar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leftBar.frameNStart = frameN  # exact frame index
            leftBar.tStart = t  # local t and not account for scr refresh
            leftBar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftBar, 'tStartRefresh')  # time at next scr refresh
            leftBar.setAutoDraw(True)
        
        # *rightBar* updates
        if rightBar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightBar.frameNStart = frameN  # exact frame index
            rightBar.tStart = t  # local t and not account for scr refresh
            rightBar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightBar, 'tStartRefresh')  # time at next scr refresh
            rightBar.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intention_mainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intention_main"-------
    for thisComponent in intention_mainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mainExpLoop.addData('background.started', background.tStartRefresh)
    mainExpLoop.addData('background.stopped', background.tStopRefresh)
    mainExpLoop.addData('Instructions_3.started', Instructions_3.tStartRefresh)
    mainExpLoop.addData('Instructions_3.stopped', Instructions_3.tStopRefresh)
    mainExpLoop.addData('football.started', football.tStartRefresh)
    mainExpLoop.addData('football.stopped', football.tStopRefresh)
    mainExpLoop.addData('post_left.started', post_left.tStartRefresh)
    mainExpLoop.addData('post_left.stopped', post_left.tStopRefresh)
    mainExpLoop.addData('post_right.started', post_right.tStartRefresh)
    mainExpLoop.addData('post_right.stopped', post_right.tStopRefresh)
    mainExpLoop.addData('leftGesture.started', leftGesture.tStartRefresh)
    mainExpLoop.addData('leftGesture.stopped', leftGesture.tStopRefresh)
    mainExpLoop.addData('rightGesture.started', rightGesture.tStartRefresh)
    mainExpLoop.addData('rightGesture.stopped', rightGesture.tStopRefresh)
    # check responses
    if intention_keys.keys in ['', [], None]:  # No response was made
        intention_keys.keys = None
    mainExpLoop.addData('intention_keys.keys',intention_keys.keys)
    if intention_keys.keys != None:  # we had a response
        mainExpLoop.addData('intention_keys.rt', intention_keys.rt)
    mainExpLoop.addData('intention_keys.started', intention_keys.tStartRefresh)
    mainExpLoop.addData('intention_keys.stopped', intention_keys.tStopRefresh)
    mainExpLoop.addData('leftBar.started', leftBar.tStartRefresh)
    mainExpLoop.addData('leftBar.stopped', leftBar.tStopRefresh)
    mainExpLoop.addData('rightBar.started', rightBar.tStartRefresh)
    mainExpLoop.addData('rightBar.stopped', rightBar.tStopRefresh)
    if intention_keys.keys == 'left': 
        leftCount += 1;
        cond = leftList[leftOrder[leftCount]]
        delaymain = leftDelay[leftOrder[leftCount]]
    elif intention_keys.keys == 'right':
        rightCount += 1;
        cond = rightList[rightOrder[rightCount]]
        delaymain = rightDelay[rightOrder[rightCount]]
    elif intention_keys.keys == 'escape':
        core.quit()
        
    thisExp.addData('ActualBallDirection', cond)
    thisExp.addData('ActualOnsetDelay', delaymain)
    # the Routine "intention_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "delay_main"-------
    continueRoutine = True
    # update component parameters for each repeat
    leftBar_2.setPos(lpos)
    leftBar_2.setSize(lh)
    rightBar_2.setPos(rpos)
    rightBar_2.setSize(rh)
    # keep track of which components have finished
    delay_mainComponents = [text_2, background_2, post_left_2, post_right_2, football_2, leftGesture_2, rightGesture_2, leftBar_2, rightBar_2, Instructions_5]
    for thisComponent in delay_mainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    delay_mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "delay_main"-------
    first_loop = True
    while continueRoutine:

        # update game_state
        if first_loop == True:
            game_state_dict["current_state"] = mainExpLoop_counter + 0.2  # delay_main
            game_state_dict["time_entered_state"] = time.time() - start_time
            first_loop = False

        # get current time
        t = delay_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=delay_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + delaymain-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *background_2* updates
        if background_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background_2.frameNStart = frameN  # exact frame index
            background_2.tStart = t  # local t and not account for scr refresh
            background_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_2, 'tStartRefresh')  # time at next scr refresh
            background_2.setAutoDraw(True)
        if background_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_2.tStartRefresh + delaymain-frameTolerance:
                # keep track of stop time/frame for later
                background_2.tStop = t  # not accounting for scr refresh
                background_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(background_2, 'tStopRefresh')  # time at next scr refresh
                background_2.setAutoDraw(False)
        
        # *post_left_2* updates
        if post_left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            post_left_2.frameNStart = frameN  # exact frame index
            post_left_2.tStart = t  # local t and not account for scr refresh
            post_left_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(post_left_2, 'tStartRefresh')  # time at next scr refresh
            post_left_2.setAutoDraw(True)
        if post_left_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > post_left_2.tStartRefresh + delaymain-frameTolerance:
                # keep track of stop time/frame for later
                post_left_2.tStop = t  # not accounting for scr refresh
                post_left_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(post_left_2, 'tStopRefresh')  # time at next scr refresh
                post_left_2.setAutoDraw(False)
        
        # *post_right_2* updates
        if post_right_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            post_right_2.frameNStart = frameN  # exact frame index
            post_right_2.tStart = t  # local t and not account for scr refresh
            post_right_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(post_right_2, 'tStartRefresh')  # time at next scr refresh
            post_right_2.setAutoDraw(True)
        if post_right_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > post_right_2.tStartRefresh + delaymain-frameTolerance:
                # keep track of stop time/frame for later
                post_right_2.tStop = t  # not accounting for scr refresh
                post_right_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(post_right_2, 'tStopRefresh')  # time at next scr refresh
                post_right_2.setAutoDraw(False)
        
        # *football_2* updates
        if football_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            football_2.frameNStart = frameN  # exact frame index
            football_2.tStart = t  # local t and not account for scr refresh
            football_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(football_2, 'tStartRefresh')  # time at next scr refresh
            football_2.setAutoDraw(True)
        if football_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > football_2.tStartRefresh + delaymain-frameTolerance:
                # keep track of stop time/frame for later
                football_2.tStop = t  # not accounting for scr refresh
                football_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(football_2, 'tStopRefresh')  # time at next scr refresh
                football_2.setAutoDraw(False)
        
        # *leftGesture_2* updates
        if leftGesture_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leftGesture_2.frameNStart = frameN  # exact frame index
            leftGesture_2.tStart = t  # local t and not account for scr refresh
            leftGesture_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftGesture_2, 'tStartRefresh')  # time at next scr refresh
            leftGesture_2.setAutoDraw(True)
        if leftGesture_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > leftGesture_2.tStartRefresh + delaymain-frameTolerance:
                # keep track of stop time/frame for later
                leftGesture_2.tStop = t  # not accounting for scr refresh
                leftGesture_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(leftGesture_2, 'tStopRefresh')  # time at next scr refresh
                leftGesture_2.setAutoDraw(False)
        
        # *rightGesture_2* updates
        if rightGesture_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightGesture_2.frameNStart = frameN  # exact frame index
            rightGesture_2.tStart = t  # local t and not account for scr refresh
            rightGesture_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightGesture_2, 'tStartRefresh')  # time at next scr refresh
            rightGesture_2.setAutoDraw(True)
        if rightGesture_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rightGesture_2.tStartRefresh + delaymain-frameTolerance:
                # keep track of stop time/frame for later
                rightGesture_2.tStop = t  # not accounting for scr refresh
                rightGesture_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rightGesture_2, 'tStopRefresh')  # time at next scr refresh
                rightGesture_2.setAutoDraw(False)
        
        # *leftBar_2* updates
        if leftBar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leftBar_2.frameNStart = frameN  # exact frame index
            leftBar_2.tStart = t  # local t and not account for scr refresh
            leftBar_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftBar_2, 'tStartRefresh')  # time at next scr refresh
            leftBar_2.setAutoDraw(True)
        if leftBar_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > leftBar_2.tStartRefresh + delaymain-frameTolerance:
                # keep track of stop time/frame for later
                leftBar_2.tStop = t  # not accounting for scr refresh
                leftBar_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(leftBar_2, 'tStopRefresh')  # time at next scr refresh
                leftBar_2.setAutoDraw(False)
        
        # *rightBar_2* updates
        if rightBar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightBar_2.frameNStart = frameN  # exact frame index
            rightBar_2.tStart = t  # local t and not account for scr refresh
            rightBar_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightBar_2, 'tStartRefresh')  # time at next scr refresh
            rightBar_2.setAutoDraw(True)
        if rightBar_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rightBar_2.tStartRefresh + delaymain-frameTolerance:
                # keep track of stop time/frame for later
                rightBar_2.tStop = t  # not accounting for scr refresh
                rightBar_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rightBar_2, 'tStopRefresh')  # time at next scr refresh
                rightBar_2.setAutoDraw(False)
        
        # *Instructions_5* updates
        if Instructions_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_5.frameNStart = frameN  # exact frame index
            Instructions_5.tStart = t  # local t and not account for scr refresh
            Instructions_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_5, 'tStartRefresh')  # time at next scr refresh
            Instructions_5.setAutoDraw(True)
        if Instructions_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Instructions_5.tStartRefresh + delaymain-frameTolerance:
                # keep track of stop time/frame for later
                Instructions_5.tStop = t  # not accounting for scr refresh
                Instructions_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Instructions_5, 'tStopRefresh')  # time at next scr refresh
                Instructions_5.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in delay_mainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "delay_main"-------
    for thisComponent in delay_mainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mainExpLoop.addData('text_2.started', text_2.tStartRefresh)
    mainExpLoop.addData('text_2.stopped', text_2.tStopRefresh)
    mainExpLoop.addData('background_2.started', background_2.tStartRefresh)
    mainExpLoop.addData('background_2.stopped', background_2.tStopRefresh)
    mainExpLoop.addData('post_left_2.started', post_left_2.tStartRefresh)
    mainExpLoop.addData('post_left_2.stopped', post_left_2.tStopRefresh)
    mainExpLoop.addData('post_right_2.started', post_right_2.tStartRefresh)
    mainExpLoop.addData('post_right_2.stopped', post_right_2.tStopRefresh)
    mainExpLoop.addData('football_2.started', football_2.tStartRefresh)
    mainExpLoop.addData('football_2.stopped', football_2.tStopRefresh)
    mainExpLoop.addData('leftGesture_2.started', leftGesture_2.tStartRefresh)
    mainExpLoop.addData('leftGesture_2.stopped', leftGesture_2.tStopRefresh)
    mainExpLoop.addData('rightGesture_2.started', rightGesture_2.tStartRefresh)
    mainExpLoop.addData('rightGesture_2.stopped', rightGesture_2.tStopRefresh)
    mainExpLoop.addData('leftBar_2.started', leftBar_2.tStartRefresh)
    mainExpLoop.addData('leftBar_2.stopped', leftBar_2.tStopRefresh)
    mainExpLoop.addData('rightBar_2.started', rightBar_2.tStartRefresh)
    mainExpLoop.addData('rightBar_2.stopped', rightBar_2.tStopRefresh)
    mainExpLoop.addData('Instructions_5.started', Instructions_5.tStartRefresh)
    mainExpLoop.addData('Instructions_5.stopped', Instructions_5.tStopRefresh)
    # the Routine "delay_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    motionLoop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('cond_' +cond +'_xpos.xlsx'),
        seed=None, name='motionLoop')
    thisExp.addLoop(motionLoop)  # add the loop to the experiment
    thisMotionLoop = motionLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMotionLoop.rgb)
    if thisMotionLoop != None:
        for paramName in thisMotionLoop:
            exec('{} = thisMotionLoop[paramName]'.format(paramName))
    
    for thisMotionLoop in motionLoop:
        currentLoop = motionLoop
        # abbreviate parameter names if possible (e.g. rgb = thisMotionLoop.rgb)
        if thisMotionLoop != None:
            for paramName in thisMotionLoop:
                exec('{} = thisMotionLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "target_main"-------
        continueRoutine = True
        routineTimer.add(0.017000)
        # update component parameters for each repeat
        football_3.setPos(xpos_fb)
        leftBar_3.setPos(lpos)
        leftBar_3.setSize(lh)
        rightBar_3.setPos(rpos)
        rightBar_3.setSize(rh)
        # keep track of which components have finished
        target_mainComponents = [background_3, post_left_3, post_right_3, football_3, leftGesture_3, rightGesture_3, leftBar_3, rightBar_3, Instructions_6]
        for thisComponent in target_mainComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        target_mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "target_main"-------
        first_loop = True

        while continueRoutine and routineTimer.getTime() > 0:

            # update game_state
            if first_loop == True:
                game_state_dict["current_state"] = mainExpLoop_counter + 0.3  # target_main
                game_state_dict["time_entered_state"] = time.time() - start_time
                first_loop = False

            # get current time
            t = target_mainClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=target_mainClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background_3* updates
            if background_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                background_3.frameNStart = frameN  # exact frame index
                background_3.tStart = t  # local t and not account for scr refresh
                background_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(background_3, 'tStartRefresh')  # time at next scr refresh
                background_3.setAutoDraw(True)
            if background_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > background_3.tStartRefresh + 0.017-frameTolerance:
                    # keep track of stop time/frame for later
                    background_3.tStop = t  # not accounting for scr refresh
                    background_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(background_3, 'tStopRefresh')  # time at next scr refresh
                    background_3.setAutoDraw(False)
            
            # *post_left_3* updates
            if post_left_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                post_left_3.frameNStart = frameN  # exact frame index
                post_left_3.tStart = t  # local t and not account for scr refresh
                post_left_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(post_left_3, 'tStartRefresh')  # time at next scr refresh
                post_left_3.setAutoDraw(True)
            if post_left_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > post_left_3.tStartRefresh + 0.017-frameTolerance:
                    # keep track of stop time/frame for later
                    post_left_3.tStop = t  # not accounting for scr refresh
                    post_left_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(post_left_3, 'tStopRefresh')  # time at next scr refresh
                    post_left_3.setAutoDraw(False)
            
            # *post_right_3* updates
            if post_right_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                post_right_3.frameNStart = frameN  # exact frame index
                post_right_3.tStart = t  # local t and not account for scr refresh
                post_right_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(post_right_3, 'tStartRefresh')  # time at next scr refresh
                post_right_3.setAutoDraw(True)
            if post_right_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > post_right_3.tStartRefresh + 0.017-frameTolerance:
                    # keep track of stop time/frame for later
                    post_right_3.tStop = t  # not accounting for scr refresh
                    post_right_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(post_right_3, 'tStopRefresh')  # time at next scr refresh
                    post_right_3.setAutoDraw(False)
            
            # *football_3* updates
            if football_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                football_3.frameNStart = frameN  # exact frame index
                football_3.tStart = t  # local t and not account for scr refresh
                football_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(football_3, 'tStartRefresh')  # time at next scr refresh
                football_3.setAutoDraw(True)
            if football_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > football_3.tStartRefresh + 0.017-frameTolerance:
                    # keep track of stop time/frame for later
                    football_3.tStop = t  # not accounting for scr refresh
                    football_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(football_3, 'tStopRefresh')  # time at next scr refresh
                    football_3.setAutoDraw(False)
            
            # *leftGesture_3* updates
            if leftGesture_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftGesture_3.frameNStart = frameN  # exact frame index
                leftGesture_3.tStart = t  # local t and not account for scr refresh
                leftGesture_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftGesture_3, 'tStartRefresh')  # time at next scr refresh
                leftGesture_3.setAutoDraw(True)
            if leftGesture_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftGesture_3.tStartRefresh + 0.017-frameTolerance:
                    # keep track of stop time/frame for later
                    leftGesture_3.tStop = t  # not accounting for scr refresh
                    leftGesture_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftGesture_3, 'tStopRefresh')  # time at next scr refresh
                    leftGesture_3.setAutoDraw(False)
            
            # *rightGesture_3* updates
            if rightGesture_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightGesture_3.frameNStart = frameN  # exact frame index
                rightGesture_3.tStart = t  # local t and not account for scr refresh
                rightGesture_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightGesture_3, 'tStartRefresh')  # time at next scr refresh
                rightGesture_3.setAutoDraw(True)
            if rightGesture_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightGesture_3.tStartRefresh + 0.017-frameTolerance:
                    # keep track of stop time/frame for later
                    rightGesture_3.tStop = t  # not accounting for scr refresh
                    rightGesture_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightGesture_3, 'tStopRefresh')  # time at next scr refresh
                    rightGesture_3.setAutoDraw(False)
            
            # *leftBar_3* updates
            if leftBar_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftBar_3.frameNStart = frameN  # exact frame index
                leftBar_3.tStart = t  # local t and not account for scr refresh
                leftBar_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftBar_3, 'tStartRefresh')  # time at next scr refresh
                leftBar_3.setAutoDraw(True)
            if leftBar_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftBar_3.tStartRefresh + 0.017-frameTolerance:
                    # keep track of stop time/frame for later
                    leftBar_3.tStop = t  # not accounting for scr refresh
                    leftBar_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftBar_3, 'tStopRefresh')  # time at next scr refresh
                    leftBar_3.setAutoDraw(False)
            
            # *rightBar_3* updates
            if rightBar_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightBar_3.frameNStart = frameN  # exact frame index
                rightBar_3.tStart = t  # local t and not account for scr refresh
                rightBar_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightBar_3, 'tStartRefresh')  # time at next scr refresh
                rightBar_3.setAutoDraw(True)
            if rightBar_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightBar_3.tStartRefresh + 0.017-frameTolerance:
                    # keep track of stop time/frame for later
                    rightBar_3.tStop = t  # not accounting for scr refresh
                    rightBar_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightBar_3, 'tStopRefresh')  # time at next scr refresh
                    rightBar_3.setAutoDraw(False)
            
            # *Instructions_6* updates
            if Instructions_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Instructions_6.frameNStart = frameN  # exact frame index
                Instructions_6.tStart = t  # local t and not account for scr refresh
                Instructions_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Instructions_6, 'tStartRefresh')  # time at next scr refresh
                Instructions_6.setAutoDraw(True)
            if Instructions_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Instructions_6.tStartRefresh + 0.017-frameTolerance:
                    # keep track of stop time/frame for later
                    Instructions_6.tStop = t  # not accounting for scr refresh
                    Instructions_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Instructions_6, 'tStopRefresh')  # time at next scr refresh
                    Instructions_6.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in target_mainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "target_main"-------
        for thisComponent in target_mainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        motionLoop.addData('background_3.started', background_3.tStartRefresh)
        motionLoop.addData('background_3.stopped', background_3.tStopRefresh)
        motionLoop.addData('post_left_3.started', post_left_3.tStartRefresh)
        motionLoop.addData('post_left_3.stopped', post_left_3.tStopRefresh)
        motionLoop.addData('post_right_3.started', post_right_3.tStartRefresh)
        motionLoop.addData('post_right_3.stopped', post_right_3.tStopRefresh)
        motionLoop.addData('football_3.started', football_3.tStartRefresh)
        motionLoop.addData('football_3.stopped', football_3.tStopRefresh)
        motionLoop.addData('leftGesture_3.started', leftGesture_3.tStartRefresh)
        motionLoop.addData('leftGesture_3.stopped', leftGesture_3.tStopRefresh)
        motionLoop.addData('rightGesture_3.started', rightGesture_3.tStartRefresh)
        motionLoop.addData('rightGesture_3.stopped', rightGesture_3.tStopRefresh)
        motionLoop.addData('leftBar_3.started', leftBar_3.tStartRefresh)
        motionLoop.addData('leftBar_3.stopped', leftBar_3.tStopRefresh)
        motionLoop.addData('rightBar_3.started', rightBar_3.tStartRefresh)
        motionLoop.addData('rightBar_3.stopped', rightBar_3.tStopRefresh)
        motionLoop.addData('Instructions_6.started', Instructions_6.tStartRefresh)
        motionLoop.addData('Instructions_6.stopped', Instructions_6.tStopRefresh)
    # completed 1.0 repeats of 'motionLoop'
    
    
    # ------Prepare to start Routine "resp_main"-------
    continueRoutine = True
    # update component parameters for each repeat
    event.Mouse(visible=True,newPos=(0,curPos))
    
    timeValue = 0;
    timing_slider.reset()
    Timetext.reset()
    # keep track of which components have finished
    resp_mainComponents = [timing_slider, submit_button, Timetext, timing_question]
    for thisComponent in resp_mainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    resp_mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "resp_main"-------
    first_loop = True
    while continueRoutine:

        # update game_state
        if first_loop == True:
            game_state_dict["current_state"] = mainExpLoop_counter + 0.4  # resp_main
            game_state_dict["time_entered_state"] = time.time() - start_time
            first_loop = False

        # get current time
        t = resp_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=resp_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if timing_slider.getMarkerPos():
            timeValue = round(timing_slider.getMarkerPos(),0)
            
        
        
        # *timing_slider* updates
        if timing_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timing_slider.frameNStart = frameN  # exact frame index
            timing_slider.tStart = t  # local t and not account for scr refresh
            timing_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timing_slider, 'tStartRefresh')  # time at next scr refresh
            timing_slider.setAutoDraw(True)
        
        # *submit_button* updates
        if submit_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            submit_button.frameNStart = frameN  # exact frame index
            submit_button.tStart = t  # local t and not account for scr refresh
            submit_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(submit_button, 'tStartRefresh')  # time at next scr refresh
            submit_button.setAutoDraw(True)
        if submit_button.status == STARTED:
            # check whether submit_button has been pressed
            if submit_button.isClicked:
                if not submit_button.wasClicked:
                    submit_button.timesOn.append(submit_button.buttonClock.getTime()) # store time of first click
                    submit_button.timesOff.append(submit_button.buttonClock.getTime()) # store time clicked until
                else:
                    submit_button.timesOff[-1] = submit_button.buttonClock.getTime() # update time clicked until
                if not submit_button.wasClicked:
                    continueRoutine = False  # end routine when submit_button is clicked
                    None
                submit_button.wasClicked = True  # if submit_button is still clicked next frame, it is not a new click
            else:
                submit_button.wasClicked = False  # if submit_button is clicked next frame, it is a new click
        else:
            submit_button.wasClicked = False  # if submit_button is clicked next frame, it is a new click
        
        # *Timetext* updates
        if Timetext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Timetext.frameNStart = frameN  # exact frame index
            Timetext.tStart = t  # local t and not account for scr refresh
            Timetext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Timetext, 'tStartRefresh')  # time at next scr refresh
            Timetext.setAutoDraw(True)
        if Timetext.status == STARTED:  # only update if drawing
            Timetext.setText(str(timeValue) +"ms", log=False)
        
        # *timing_question* updates
        if timing_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timing_question.frameNStart = frameN  # exact frame index
            timing_question.tStart = t  # local t and not account for scr refresh
            timing_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timing_question, 'tStartRefresh')  # time at next scr refresh
            timing_question.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resp_mainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "resp_main"-------
    for thisComponent in resp_mainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('SubmittedTimeRating', timeValue)
    mainExpLoop.addData('timing_slider.response', timing_slider.getRating())
    mainExpLoop.addData('timing_slider.rt', timing_slider.getRT())
    mainExpLoop.addData('timing_slider.started', timing_slider.tStartRefresh)
    mainExpLoop.addData('timing_slider.stopped', timing_slider.tStopRefresh)
    mainExpLoop.addData('submit_button.started', submit_button.tStartRefresh)
    mainExpLoop.addData('submit_button.stopped', submit_button.tStopRefresh)
    mainExpLoop.addData('submit_button.numClicks', submit_button.numClicks)
    if submit_button.numClicks:
       mainExpLoop.addData('submit_button.timesOn', submit_button.timesOn)
       mainExpLoop.addData('submit_button.timesOff', submit_button.timesOff)
    else:
       mainExpLoop.addData('submit_button.timesOn', "")
       mainExpLoop.addData('submit_button.timesOff', "")
    mainExpLoop.addData('Timetext.started', Timetext.tStartRefresh)
    mainExpLoop.addData('Timetext.stopped', Timetext.tStopRefresh)
    mainExpLoop.addData('timing_question.started', timing_question.tStartRefresh)
    mainExpLoop.addData('timing_question.stopped', timing_question.tStopRefresh)
    # the Routine "resp_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    feedbackComponents = []
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    first_loop = True
    while continueRoutine:

        # update game_state
        if first_loop == True:
            game_state_dict["current_state"] = mainExpLoop_counter + 0.5  # feedback
            game_state_dict["time_entered_state"] = time.time() - start_time
            first_loop = False

        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rating_main"-------
    continueRoutine = True
    # update component parameters for each repeat
    event.Mouse(visible=True,newPos=(0,curPos))
    confidenceValue = 0;
    confidenceScale.reset()
    # keep track of which components have finished
    rating_mainComponents = [confidenceScale, condifence_submit, Confidence_question]
    for thisComponent in rating_mainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rating_mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rating_main"-------
    first_loop = True
    while continueRoutine:

        # update game_state
        if first_loop == True:
            game_state_dict["current_state"] = mainExpLoop_counter + 0.6  # rating_main
            game_state_dict["time_entered_state"] = time.time() - start_time
            first_loop = False

        # get current time
        t = rating_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rating_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if confidenceScale.getMarkerPos():
            confidenceValue = confidenceScale.getMarkerPos()
            confidenceValue = round(confidenceValue)
        
        # *confidenceScale* updates
        if confidenceScale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confidenceScale.frameNStart = frameN  # exact frame index
            confidenceScale.tStart = t  # local t and not account for scr refresh
            confidenceScale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confidenceScale, 'tStartRefresh')  # time at next scr refresh
            confidenceScale.setAutoDraw(True)
        
        # *condifence_submit* updates
        if condifence_submit.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            condifence_submit.frameNStart = frameN  # exact frame index
            condifence_submit.tStart = t  # local t and not account for scr refresh
            condifence_submit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(condifence_submit, 'tStartRefresh')  # time at next scr refresh
            condifence_submit.setAutoDraw(True)
        if condifence_submit.status == STARTED:
            # check whether condifence_submit has been pressed
            if condifence_submit.isClicked:
                if not condifence_submit.wasClicked:
                    condifence_submit.timesOn.append(condifence_submit.buttonClock.getTime()) # store time of first click
                    condifence_submit.timesOff.append(condifence_submit.buttonClock.getTime()) # store time clicked until
                else:
                    condifence_submit.timesOff[-1] = condifence_submit.buttonClock.getTime() # update time clicked until
                if not condifence_submit.wasClicked:
                    continueRoutine = False  # end routine when condifence_submit is clicked
                    None
                condifence_submit.wasClicked = True  # if condifence_submit is still clicked next frame, it is not a new click
            else:
                condifence_submit.wasClicked = False  # if condifence_submit is clicked next frame, it is a new click
        else:
            condifence_submit.wasClicked = False  # if condifence_submit is clicked next frame, it is a new click
        
        # *Confidence_question* updates
        if Confidence_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Confidence_question.frameNStart = frameN  # exact frame index
            Confidence_question.tStart = t  # local t and not account for scr refresh
            Confidence_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Confidence_question, 'tStartRefresh')  # time at next scr refresh
            Confidence_question.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rating_mainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rating_main"-------
    for thisComponent in rating_mainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mainExpLoop.addData('confidenceScale.response', confidenceScale.getRating())
    mainExpLoop.addData('confidenceScale.rt', confidenceScale.getRT())
    mainExpLoop.addData('confidenceScale.started', confidenceScale.tStartRefresh)
    mainExpLoop.addData('confidenceScale.stopped', confidenceScale.tStopRefresh)
    mainExpLoop.addData('condifence_submit.started', condifence_submit.tStartRefresh)
    mainExpLoop.addData('condifence_submit.stopped', condifence_submit.tStopRefresh)
    mainExpLoop.addData('condifence_submit.numClicks', condifence_submit.numClicks)
    if condifence_submit.numClicks:
       mainExpLoop.addData('condifence_submit.timesOn', condifence_submit.timesOn)
       mainExpLoop.addData('condifence_submit.timesOff', condifence_submit.timesOff)
    else:
       mainExpLoop.addData('condifence_submit.timesOn', "")
       mainExpLoop.addData('condifence_submit.timesOff', "")
    mainExpLoop.addData('Confidence_question.started', Confidence_question.tStartRefresh)
    mainExpLoop.addData('Confidence_question.stopped', Confidence_question.tStopRefresh)
    # the Routine "rating_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "intention_check"-------
    continueRoutine = True
    # update component parameters for each repeat
    event.Mouse(visible=True,newPos=(0,curPos))
    # keep track of which components have finished
    intention_checkComponents = [only_Question, button_no, button_yes]
    for thisComponent in intention_checkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intention_checkClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "intention_check"-------
    first_loop = True
    while continueRoutine:

        # update game_state
        if first_loop == True:
            game_state_dict["current_state"] = mainExpLoop_counter + 0.7  # intention_check
            game_state_dict["time_entered_state"] = time.time() - start_time
            first_loop = False

        # get current time
        t = intention_checkClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intention_checkClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *only_Question* updates
        if only_Question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            only_Question.frameNStart = frameN  # exact frame index
            only_Question.tStart = t  # local t and not account for scr refresh
            only_Question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(only_Question, 'tStartRefresh')  # time at next scr refresh
            only_Question.setAutoDraw(True)
        
        # *button_no* updates
        if button_no.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_no.frameNStart = frameN  # exact frame index
            button_no.tStart = t  # local t and not account for scr refresh
            button_no.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_no, 'tStartRefresh')  # time at next scr refresh
            button_no.setAutoDraw(True)
        if button_no.status == STARTED:
            # check whether button_no has been pressed
            if button_no.isClicked:
                if not button_no.wasClicked:
                    button_no.timesOn.append(button_no.buttonClock.getTime()) # store time of first click
                    button_no.timesOff.append(button_no.buttonClock.getTime()) # store time clicked until
                else:
                    button_no.timesOff[-1] = button_no.buttonClock.getTime() # update time clicked until
                if not button_no.wasClicked:
                    continueRoutine = False  # end routine when button_no is clicked
                    None
                button_no.wasClicked = True  # if button_no is still clicked next frame, it is not a new click
            else:
                button_no.wasClicked = False  # if button_no is clicked next frame, it is a new click
        else:
            button_no.wasClicked = False  # if button_no is clicked next frame, it is a new click
        
        # *button_yes* updates
        if button_yes.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_yes.frameNStart = frameN  # exact frame index
            button_yes.tStart = t  # local t and not account for scr refresh
            button_yes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_yes, 'tStartRefresh')  # time at next scr refresh
            button_yes.setAutoDraw(True)
        if button_yes.status == STARTED:
            # check whether button_yes has been pressed
            if button_yes.isClicked:
                if not button_yes.wasClicked:
                    button_yes.timesOn.append(button_yes.buttonClock.getTime()) # store time of first click
                    button_yes.timesOff.append(button_yes.buttonClock.getTime()) # store time clicked until
                else:
                    button_yes.timesOff[-1] = button_yes.buttonClock.getTime() # update time clicked until
                if not button_yes.wasClicked:
                    continueRoutine = False  # end routine when button_yes is clicked
                    None
                button_yes.wasClicked = True  # if button_yes is still clicked next frame, it is not a new click
            else:
                button_yes.wasClicked = False  # if button_yes is clicked next frame, it is a new click
        else:
            button_yes.wasClicked = False  # if button_yes is clicked next frame, it is a new click
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intention_checkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intention_check"-------
    for thisComponent in intention_checkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if button_no.isClicked:
        intentionCheck = 'No'
    elif button_yes.isClicked:
        intentionCheck = 'Yes'
        
    if intention_keys.keys == 'left': 
        lh[1] += 0.02;
        lpos[1]+=0.02/2;
     
    elif intention_keys.keys == 'right':
        rh[1] += 0.02;
        rpos[1]+=0.02/2;
        
    thisExp.addData('intentionCheck', intentionCheck);
    mainExpLoop.addData('only_Question.started', only_Question.tStartRefresh)
    mainExpLoop.addData('only_Question.stopped', only_Question.tStopRefresh)
    mainExpLoop.addData('button_no.started', button_no.tStartRefresh)
    mainExpLoop.addData('button_no.stopped', button_no.tStopRefresh)
    mainExpLoop.addData('button_no.numClicks', button_no.numClicks)
    if button_no.numClicks:
       mainExpLoop.addData('button_no.timesOn', button_no.timesOn)
       mainExpLoop.addData('button_no.timesOff', button_no.timesOff)
    else:
       mainExpLoop.addData('button_no.timesOn', "")
       mainExpLoop.addData('button_no.timesOff', "")
    mainExpLoop.addData('button_yes.started', button_yes.tStartRefresh)
    mainExpLoop.addData('button_yes.stopped', button_yes.tStopRefresh)
    mainExpLoop.addData('button_yes.numClicks', button_yes.numClicks)
    if button_yes.numClicks:
       mainExpLoop.addData('button_yes.timesOn', button_yes.timesOn)
       mainExpLoop.addData('button_yes.timesOff', button_yes.timesOff)
    else:
       mainExpLoop.addData('button_yes.timesOn', "")
       mainExpLoop.addData('button_yes.timesOff', "")
    # the Routine "intention_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'mainExpLoop'


# ------Prepare to start Routine "thanks_2"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanks_2Components = [Instructions_7]
for thisComponent in thanks_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanks_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks_2"-------
first_loop = True
while continueRoutine and routineTimer.getTime() > 0:

    # update game_state
    if first_loop == True:
        game_state_dict["current_state"] = 0.2  # thanks_2
        game_state_dict["time_entered_state"] = time.time() - start_time
        first_loop = False

    # get current time
    t = thanks_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanks_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions_7* updates
    if Instructions_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_7.frameNStart = frameN  # exact frame index
        Instructions_7.tStart = t  # local t and not account for scr refresh
        Instructions_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_7, 'tStartRefresh')  # time at next scr refresh
        Instructions_7.setAutoDraw(True)
    if Instructions_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Instructions_7.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            Instructions_7.tStop = t  # not accounting for scr refresh
            Instructions_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instructions_7, 'tStopRefresh')  # time at next scr refresh
            Instructions_7.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanks_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks_2"-------
for thisComponent in thanks_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions_7.started', Instructions_7.tStartRefresh)
thisExp.addData('Instructions_7.stopped', Instructions_7.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
