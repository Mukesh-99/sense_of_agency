#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon Feb  7 12:59:16 2022
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
sys.path.append('../../')
from UDP_rec_and_send import start_loop

game_state_dict = {}  # dictionary to update throughout experiment with game state (which we pass to the logger)
logging_thread = threading.Thread(target=start_loop, args=(game_state_dict))
logging_thread.start()

start_time = time.time()
#^^^^^^^^^^^^^^^^^^^^^^^^^^#


leftOpacity = 1;
rightOpacity = 1;

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
    originPath='/Users/mmakwana/Downloads/IB_task/IB_new_task/IB_task_new_practice.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
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
from psychopy import core, event
Instructions_3 = visual.TextStim(win=win, name='Instructions_3',
    text='Which direction do you wish to move the ball?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
football = visual.ImageStim(
    win=win,
    name='football', units='height', 
    image='football.png', mask=None,
    ori=0.0, pos=(0, -0.19), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
post_left = visual.ImageStim(
    win=win,
    name='post_left', 
    image='post.png', mask=None,
    ori=0.0, pos=(-.73, -0.29), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=leftOpacity,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
post_right = visual.ImageStim(
    win=win,
    name='post_right', 
    image='post.png', mask=None,
    ori=0.0, pos=(.73, -0.29), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=rightOpacity,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
leftGesture = visual.ImageStim(
    win=win,
    name='leftGesture', 
    image='Power_Front.png', mask=None,
    ori=90.0, pos=(-0.25, -0.6), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
rightGesture = visual.ImageStim(
    win=win,
    name='rightGesture', 
    image='OpenHand_Front.png', mask=None,
    ori=90.0, pos=(0.25, -0.6), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
intention_keys = keyboard.Keyboard()
leftCount = -1
rightCount = -1

leftList = ['L','L','L','L','L','R','R','R','R','R'];
shuffle(leftList)

rightList = ['L','L','L','L','L','R','R','R','R','R'];
shuffle(rightList)




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

# Initialize components for Routine "resp_main"
resp_mainClock = core.Clock()
from psychopy import core, event
timeTicks = range(1,2000)


key_resp = keyboard.Keyboard()
confidence_slider = visual.Slider(win=win, name='confidence_slider',
    startValue=None, size=(1.5, 0.2), pos=(0, -0.4), units=None,
    labels=None, ticks=timeTicks, granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-2, readOnly=False)
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
     pos=(0, -0.8),     letterHeight=0.05,
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

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_txt = visual.TextStim(win=win, name='feedback_txt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "rating_main"
rating_mainClock = core.Clock()
key_resp_3 = keyboard.Keyboard()
main_shape_check = visual.RatingScale(win=win, name='main_shape_check', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=6, labels=['No Control', ' Full Control'], scale='How much control did you feel in this trial?')

# Initialize components for Routine "intention_check"
intention_checkClock = core.Clock()
only_Question = visual.TextStim(win=win, name='only_Question',
    text='Did the ball move as you intended?\n',
    font='Arial',
    pos=[0, 0.1], height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
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
first_loop = True  # update game state in first iteration of while
while continueRoutine:

    # STEP 1, update game_state to 0.1
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
    trialList=data.importConditions('cond_LR_prac.xlsx'),
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
    event.Mouse(visible=False,newPos=(0,curPos))
    intention_keys.keys = []
    intention_keys.rt = []
    _intention_keys_allKeys = []
    # keep track of which components have finished
    intention_mainComponents = [background, Instructions_3, football, post_left, post_right, leftGesture, rightGesture, intention_keys]
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
    if intention_keys.keys == 'left': 
        leftCount += 1;
        cond = leftList[leftCount]
    elif intention_keys.keys == 'right':
        rightCount += 1;
        cond = rightList[rightCount]
    elif intention_keys.keys == 'escape':
        core.quit()
    # the Routine "intention_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "delay_main"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    delay_mainComponents = [text_2, background_2, post_left_2, post_right_2, football_2]
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
        # keep track of which components have finished
        target_mainComponents = [background_3, post_left_3, post_right_3, football_3]
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
    # completed 1.0 repeats of 'motionLoop'
    
    
    # ------Prepare to start Routine "resp_main"-------
    continueRoutine = True
    # update component parameters for each repeat
    event.Mouse(visible=True,newPos=(0,curPos))
    
    timeValue = 0;
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    confidence_slider.reset()
    Timetext.reset()
    # keep track of which components have finished
    resp_mainComponents = [key_resp, confidence_slider, submit_button, Timetext]
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

    first_loop = True
    # -------Run Routine "resp_main"-------
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
        timeValue = confidence_slider.getMarkerPos()
        timeValue = round(timeValue)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *confidence_slider* updates
        if confidence_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confidence_slider.frameNStart = frameN  # exact frame index
            confidence_slider.tStart = t  # local t and not account for scr refresh
            confidence_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confidence_slider, 'tStartRefresh')  # time at next scr refresh
            confidence_slider.setAutoDraw(True)
        
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
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    mainExpLoop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        mainExpLoop.addData('key_resp.rt', key_resp.rt)
    mainExpLoop.addData('key_resp.started', key_resp.tStartRefresh)
    mainExpLoop.addData('key_resp.stopped', key_resp.tStopRefresh)
    mainExpLoop.addData('confidence_slider.response', confidence_slider.getRating())
    mainExpLoop.addData('confidence_slider.rt', confidence_slider.getRT())
    mainExpLoop.addData('confidence_slider.started', confidence_slider.tStartRefresh)
    mainExpLoop.addData('confidence_slider.stopped', confidence_slider.tStopRefresh)
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
    # the Routine "resp_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(0.600000)
    # update component parameters for each repeat
    feedback_txt.setText(delayms)
    # keep track of which components have finished
    feedbackComponents = [feedback_txt]
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        
        # *feedback_txt* updates
        if feedback_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_txt.frameNStart = frameN  # exact frame index
            feedback_txt.tStart = t  # local t and not account for scr refresh
            feedback_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_txt, 'tStartRefresh')  # time at next scr refresh
            feedback_txt.setAutoDraw(True)
        if feedback_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_txt.tStartRefresh + .6-frameTolerance:
                # keep track of stop time/frame for later
                feedback_txt.tStop = t  # not accounting for scr refresh
                feedback_txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_txt, 'tStopRefresh')  # time at next scr refresh
                feedback_txt.setAutoDraw(False)
        
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
    mainExpLoop.addData('feedback_txt.started', feedback_txt.tStartRefresh)
    mainExpLoop.addData('feedback_txt.stopped', feedback_txt.tStopRefresh)
    
    # ------Prepare to start Routine "rating_main"-------
    continueRoutine = True
    # update component parameters for each repeat
    event.Mouse(visible=True,newPos=(0,curPos))
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    main_shape_check.reset()
    # keep track of which components have finished
    rating_mainComponents = [key_resp_3, main_shape_check]
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

    first_loop = True
    # -------Run Routine "rating_main"-------
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
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *main_shape_check* updates
        if main_shape_check.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_shape_check.frameNStart = frameN  # exact frame index
            main_shape_check.tStart = t  # local t and not account for scr refresh
            main_shape_check.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_shape_check, 'tStartRefresh')  # time at next scr refresh
            main_shape_check.setAutoDraw(True)
        continueRoutine &= main_shape_check.noResponse  # a response ends the trial
        
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
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    mainExpLoop.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        mainExpLoop.addData('key_resp_3.rt', key_resp_3.rt)
    mainExpLoop.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    mainExpLoop.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # store data for mainExpLoop (TrialHandler)
    mainExpLoop.addData('main_shape_check.response', main_shape_check.getRating())
    mainExpLoop.addData('main_shape_check.rt', main_shape_check.getRT())
    mainExpLoop.addData('main_shape_check.started', main_shape_check.tStart)
    mainExpLoop.addData('main_shape_check.stopped', main_shape_check.tStop)
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

    first_loop = True
    # -------Run Routine "intention_check"-------
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
    thisExp.addData('only_Question.started', only_Question.tStartRefresh)
    thisExp.addData('only_Question.stopped', only_Question.tStopRefresh)
    thisExp.addData('button_no.started', button_no.tStartRefresh)
    thisExp.addData('button_no.stopped', button_no.tStopRefresh)
    thisExp.addData('button_no.numClicks', button_no.numClicks)
    if button_no.numClicks:
       thisExp.addData('button_no.timesOn', button_no.timesOn)
       thisExp.addData('button_no.timesOff', button_no.timesOff)
    else:
       thisExp.addData('button_no.timesOn', "")
       thisExp.addData('button_no.timesOff', "")
    thisExp.addData('button_yes.started', button_yes.tStartRefresh)
    thisExp.addData('button_yes.stopped', button_yes.tStopRefresh)
    thisExp.addData('button_yes.numClicks', button_yes.numClicks)
    if button_yes.numClicks:
       thisExp.addData('button_yes.timesOn', button_yes.timesOn)
       thisExp.addData('button_yes.timesOff', button_yes.timesOff)
    else:
       thisExp.addData('button_yes.timesOn', "")
       thisExp.addData('button_yes.timesOff', "")
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
