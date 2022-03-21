#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Thu Mar 17 16:51:39 2022
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Interval_training'  # from the Builder filename that created this script
expInfo = {'Participant': '', 'Session': '', 'Block': ''}
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
    originPath='/Users/derekwacks/Documents/research-sessions/Games/PythonGames/sense-of-agency/IB_task_new_training_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
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
    text='Welcome\n\nIn this block, you will learn to report the time interval between your button click and the onset of the beep.\n\nOn each trial  you have to click the "Down Arrow key " which will trigger an auditory beep.\n\nFirst 5 trials will be example of 0ms delay followed by 5 trials of 1000ms delay. Then you will get to the main training trails with delay varing betweem 0ms to 1000ms.\n\nYou have to report the delay between your button click and the onset  of the beep by choosing the number between 0ms to 1000ms. After your judgement you will receive the feedback of the actual delay. You can use this feedback to improvise your judgement.\n\n\nPress SPACEBAR to continue.\n',
    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Inst_key_2 = keyboard.Keyboard()

# Initialize components for Routine "shortBegin"
shortBeginClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Short example begins ...',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "intention_main"
intention_mainClock = core.Clock()
from psychopy import core, event
Instructions_3 = visual.TextStim(win=win, name='Instructions_3',
    text='Click the Down Arrow button to listen to a beep?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
intention_keys = keyboard.Keyboard()




# Initialize components for Routine "delay_main"
delay_mainClock = core.Clock()
Instructions_5 = visual.TextStim(win=win, name='Instructions_5',
    text='Click the Down Arrow button to listen to a beep?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "target_main"
target_mainClock = core.Clock()
Instructions_6 = visual.TextStim(win=win, name='Instructions_6',
    text='Click the Down Arrow button to listen to a beep?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Beep = sound.Sound('beep-02.wav', secs=.1, stereo=True, hamming=True,
    name='Beep')
Beep.setVolume(1.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_txt = visual.TextStim(win=win, name='feedback_txt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "longBegin"
longBeginClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Long example begins ...',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "intention_main"
intention_mainClock = core.Clock()
from psychopy import core, event
Instructions_3 = visual.TextStim(win=win, name='Instructions_3',
    text='Click the Down Arrow button to listen to a beep?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
intention_keys = keyboard.Keyboard()




# Initialize components for Routine "delay_main"
delay_mainClock = core.Clock()
Instructions_5 = visual.TextStim(win=win, name='Instructions_5',
    text='Click the Down Arrow button to listen to a beep?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "target_main"
target_mainClock = core.Clock()
Instructions_6 = visual.TextStim(win=win, name='Instructions_6',
    text='Click the Down Arrow button to listen to a beep?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Beep = sound.Sound('beep-02.wav', secs=.1, stereo=True, hamming=True,
    name='Beep')
Beep.setVolume(1.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_txt = visual.TextStim(win=win, name='feedback_txt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MainBegin"
MainBeginClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Main training Begins ...',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "intention_main"
intention_mainClock = core.Clock()
from psychopy import core, event
Instructions_3 = visual.TextStim(win=win, name='Instructions_3',
    text='Click the Down Arrow button to listen to a beep?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
intention_keys = keyboard.Keyboard()




# Initialize components for Routine "delay_main"
delay_mainClock = core.Clock()
Instructions_5 = visual.TextStim(win=win, name='Instructions_5',
    text='Click the Down Arrow button to listen to a beep?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "target_main"
target_mainClock = core.Clock()
Instructions_6 = visual.TextStim(win=win, name='Instructions_6',
    text='Click the Down Arrow button to listen to a beep?',
    font='Arial',
    pos=[0, 0.8], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Beep = sound.Sound('beep-02.wav', secs=.1, stereo=True, hamming=True,
    name='Beep')
Beep.setVolume(1.0)

# Initialize components for Routine "resp_main"
resp_mainClock = core.Clock()
from psychopy import core, event
timeTicks = range(1,2000)


timing_slider = visual.Slider(win=win, name='timing_slider',
    startValue=None, size=(1.5, 0.2), pos=(0, -0.4), units=None,
    labels=('0ms', '1000ms'), ticks=[0, 1000], granularity=1.0,
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
feedback_txt = visual.TextStim(win=win, name='feedback_txt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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
while continueRoutine:
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

# ------Prepare to start Routine "shortBegin"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
shortBeginComponents = [text_3]
for thisComponent in shortBeginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
shortBeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "shortBegin"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = shortBeginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=shortBeginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in shortBeginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "shortBegin"-------
for thisComponent in shortBeginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# set up handler to look after randomisation of conditions etc
shortExample = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond_short.xlsx'),
    seed=None, name='shortExample')
thisExp.addLoop(shortExample)  # add the loop to the experiment
thisShortExample = shortExample.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisShortExample.rgb)
if thisShortExample != None:
    for paramName in thisShortExample:
        exec('{} = thisShortExample[paramName]'.format(paramName))

for thisShortExample in shortExample:
    currentLoop = shortExample
    # abbreviate parameter names if possible (e.g. rgb = thisShortExample.rgb)
    if thisShortExample != None:
        for paramName in thisShortExample:
            exec('{} = thisShortExample[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intention_main"-------
    continueRoutine = True
    # update component parameters for each repeat
    event.Mouse(visible=False,newPos=(0,curPos))
    intention_keys.keys = []
    intention_keys.rt = []
    _intention_keys_allKeys = []
    # keep track of which components have finished
    intention_mainComponents = [Instructions_3, intention_keys]
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
    
    # -------Run Routine "intention_main"-------
    while continueRoutine:
        # get current time
        t = intention_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intention_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_3* updates
        if Instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_3.frameNStart = frameN  # exact frame index
            Instructions_3.tStart = t  # local t and not account for scr refresh
            Instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_3, 'tStartRefresh')  # time at next scr refresh
            Instructions_3.setAutoDraw(True)
        
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
            theseKeys = intention_keys.getKeys(keyList=['escape', 'down'], waitRelease=False)
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
    shortExample.addData('Instructions_3.started', Instructions_3.tStartRefresh)
    shortExample.addData('Instructions_3.stopped', Instructions_3.tStopRefresh)
    # check responses
    if intention_keys.keys in ['', [], None]:  # No response was made
        intention_keys.keys = None
    shortExample.addData('intention_keys.keys',intention_keys.keys)
    if intention_keys.keys != None:  # we had a response
        shortExample.addData('intention_keys.rt', intention_keys.rt)
    shortExample.addData('intention_keys.started', intention_keys.tStartRefresh)
    shortExample.addData('intention_keys.stopped', intention_keys.tStopRefresh)
    if intention_keys.keys == 'escape':
        core.quit()
    
    cond = 'down'
    thisExp.addData('ActualBallDirection', cond)
    # the Routine "intention_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "delay_main"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    delay_mainComponents = [Instructions_5]
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
    while continueRoutine:
        # get current time
        t = delay_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=delay_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
    shortExample.addData('Instructions_5.started', Instructions_5.tStartRefresh)
    shortExample.addData('Instructions_5.stopped', Instructions_5.tStopRefresh)
    # the Routine "delay_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "target_main"-------
    continueRoutine = True
    routineTimer.add(0.100000)
    # update component parameters for each repeat
    Beep.setSound('beep-02.wav', secs=.1, hamming=True)
    Beep.setVolume(1.0, log=False)
    # keep track of which components have finished
    target_mainComponents = [Instructions_6, Beep]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = target_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=target_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
            if tThisFlipGlobal > Instructions_6.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                Instructions_6.tStop = t  # not accounting for scr refresh
                Instructions_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Instructions_6, 'tStopRefresh')  # time at next scr refresh
                Instructions_6.setAutoDraw(False)
        # start/stop Beep
        if Beep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Beep.frameNStart = frameN  # exact frame index
            Beep.tStart = t  # local t and not account for scr refresh
            Beep.tStartRefresh = tThisFlipGlobal  # on global time
            Beep.play(when=win)  # sync with win flip
        if Beep.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Beep.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                Beep.tStop = t  # not accounting for scr refresh
                Beep.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Beep, 'tStopRefresh')  # time at next scr refresh
                Beep.stop()
        
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
    shortExample.addData('Instructions_6.started', Instructions_6.tStartRefresh)
    shortExample.addData('Instructions_6.stopped', Instructions_6.tStopRefresh)
    Beep.stop()  # ensure sound has stopped at end of routine
    shortExample.addData('Beep.started', Beep.tStartRefresh)
    shortExample.addData('Beep.stopped', Beep.tStopRefresh)
    
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
    while continueRoutine and routineTimer.getTime() > 0:
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
    shortExample.addData('feedback_txt.started', feedback_txt.tStartRefresh)
    shortExample.addData('feedback_txt.stopped', feedback_txt.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'shortExample'


# ------Prepare to start Routine "longBegin"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
longBeginComponents = [text_4]
for thisComponent in longBeginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
longBeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "longBegin"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = longBeginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=longBeginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in longBeginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "longBegin"-------
for thisComponent in longBeginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)

# set up handler to look after randomisation of conditions etc
LongExample = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond_long.xlsx'),
    seed=None, name='LongExample')
thisExp.addLoop(LongExample)  # add the loop to the experiment
thisLongExample = LongExample.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLongExample.rgb)
if thisLongExample != None:
    for paramName in thisLongExample:
        exec('{} = thisLongExample[paramName]'.format(paramName))

for thisLongExample in LongExample:
    currentLoop = LongExample
    # abbreviate parameter names if possible (e.g. rgb = thisLongExample.rgb)
    if thisLongExample != None:
        for paramName in thisLongExample:
            exec('{} = thisLongExample[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intention_main"-------
    continueRoutine = True
    # update component parameters for each repeat
    event.Mouse(visible=False,newPos=(0,curPos))
    intention_keys.keys = []
    intention_keys.rt = []
    _intention_keys_allKeys = []
    # keep track of which components have finished
    intention_mainComponents = [Instructions_3, intention_keys]
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
    
    # -------Run Routine "intention_main"-------
    while continueRoutine:
        # get current time
        t = intention_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intention_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_3* updates
        if Instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_3.frameNStart = frameN  # exact frame index
            Instructions_3.tStart = t  # local t and not account for scr refresh
            Instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_3, 'tStartRefresh')  # time at next scr refresh
            Instructions_3.setAutoDraw(True)
        
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
            theseKeys = intention_keys.getKeys(keyList=['escape', 'down'], waitRelease=False)
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
    LongExample.addData('Instructions_3.started', Instructions_3.tStartRefresh)
    LongExample.addData('Instructions_3.stopped', Instructions_3.tStopRefresh)
    # check responses
    if intention_keys.keys in ['', [], None]:  # No response was made
        intention_keys.keys = None
    LongExample.addData('intention_keys.keys',intention_keys.keys)
    if intention_keys.keys != None:  # we had a response
        LongExample.addData('intention_keys.rt', intention_keys.rt)
    LongExample.addData('intention_keys.started', intention_keys.tStartRefresh)
    LongExample.addData('intention_keys.stopped', intention_keys.tStopRefresh)
    if intention_keys.keys == 'escape':
        core.quit()
    
    cond = 'down'
    thisExp.addData('ActualBallDirection', cond)
    # the Routine "intention_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "delay_main"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    delay_mainComponents = [Instructions_5]
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
    while continueRoutine:
        # get current time
        t = delay_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=delay_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
    LongExample.addData('Instructions_5.started', Instructions_5.tStartRefresh)
    LongExample.addData('Instructions_5.stopped', Instructions_5.tStopRefresh)
    # the Routine "delay_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "target_main"-------
    continueRoutine = True
    routineTimer.add(0.100000)
    # update component parameters for each repeat
    Beep.setSound('beep-02.wav', secs=.1, hamming=True)
    Beep.setVolume(1.0, log=False)
    # keep track of which components have finished
    target_mainComponents = [Instructions_6, Beep]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = target_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=target_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
            if tThisFlipGlobal > Instructions_6.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                Instructions_6.tStop = t  # not accounting for scr refresh
                Instructions_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Instructions_6, 'tStopRefresh')  # time at next scr refresh
                Instructions_6.setAutoDraw(False)
        # start/stop Beep
        if Beep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Beep.frameNStart = frameN  # exact frame index
            Beep.tStart = t  # local t and not account for scr refresh
            Beep.tStartRefresh = tThisFlipGlobal  # on global time
            Beep.play(when=win)  # sync with win flip
        if Beep.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Beep.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                Beep.tStop = t  # not accounting for scr refresh
                Beep.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Beep, 'tStopRefresh')  # time at next scr refresh
                Beep.stop()
        
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
    LongExample.addData('Instructions_6.started', Instructions_6.tStartRefresh)
    LongExample.addData('Instructions_6.stopped', Instructions_6.tStopRefresh)
    Beep.stop()  # ensure sound has stopped at end of routine
    LongExample.addData('Beep.started', Beep.tStartRefresh)
    LongExample.addData('Beep.stopped', Beep.tStopRefresh)
    
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
    while continueRoutine and routineTimer.getTime() > 0:
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
    LongExample.addData('feedback_txt.started', feedback_txt.tStartRefresh)
    LongExample.addData('feedback_txt.stopped', feedback_txt.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'LongExample'


# ------Prepare to start Routine "MainBegin"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
MainBeginComponents = [text_2]
for thisComponent in MainBeginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
MainBeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "MainBegin"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = MainBeginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=MainBeginClock)
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
        if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MainBeginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MainBegin"-------
for thisComponent in MainBeginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
mainExpLoop = data.TrialHandler(nReps=3, method='random', 
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
    intention_mainComponents = [Instructions_3, intention_keys]
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
    
    # -------Run Routine "intention_main"-------
    while continueRoutine:
        # get current time
        t = intention_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intention_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_3* updates
        if Instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_3.frameNStart = frameN  # exact frame index
            Instructions_3.tStart = t  # local t and not account for scr refresh
            Instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_3, 'tStartRefresh')  # time at next scr refresh
            Instructions_3.setAutoDraw(True)
        
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
            theseKeys = intention_keys.getKeys(keyList=['escape', 'down'], waitRelease=False)
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
    mainExpLoop.addData('Instructions_3.started', Instructions_3.tStartRefresh)
    mainExpLoop.addData('Instructions_3.stopped', Instructions_3.tStopRefresh)
    # check responses
    if intention_keys.keys in ['', [], None]:  # No response was made
        intention_keys.keys = None
    mainExpLoop.addData('intention_keys.keys',intention_keys.keys)
    if intention_keys.keys != None:  # we had a response
        mainExpLoop.addData('intention_keys.rt', intention_keys.rt)
    mainExpLoop.addData('intention_keys.started', intention_keys.tStartRefresh)
    mainExpLoop.addData('intention_keys.stopped', intention_keys.tStopRefresh)
    if intention_keys.keys == 'escape':
        core.quit()
    
    cond = 'down'
    thisExp.addData('ActualBallDirection', cond)
    # the Routine "intention_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "delay_main"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    delay_mainComponents = [Instructions_5]
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
    while continueRoutine:
        # get current time
        t = delay_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=delay_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
    mainExpLoop.addData('Instructions_5.started', Instructions_5.tStartRefresh)
    mainExpLoop.addData('Instructions_5.stopped', Instructions_5.tStopRefresh)
    # the Routine "delay_main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "target_main"-------
    continueRoutine = True
    routineTimer.add(0.100000)
    # update component parameters for each repeat
    Beep.setSound('beep-02.wav', secs=.1, hamming=True)
    Beep.setVolume(1.0, log=False)
    # keep track of which components have finished
    target_mainComponents = [Instructions_6, Beep]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = target_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=target_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
            if tThisFlipGlobal > Instructions_6.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                Instructions_6.tStop = t  # not accounting for scr refresh
                Instructions_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Instructions_6, 'tStopRefresh')  # time at next scr refresh
                Instructions_6.setAutoDraw(False)
        # start/stop Beep
        if Beep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Beep.frameNStart = frameN  # exact frame index
            Beep.tStart = t  # local t and not account for scr refresh
            Beep.tStartRefresh = tThisFlipGlobal  # on global time
            Beep.play(when=win)  # sync with win flip
        if Beep.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Beep.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                Beep.tStop = t  # not accounting for scr refresh
                Beep.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Beep, 'tStopRefresh')  # time at next scr refresh
                Beep.stop()
        
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
    mainExpLoop.addData('Instructions_6.started', Instructions_6.tStartRefresh)
    mainExpLoop.addData('Instructions_6.stopped', Instructions_6.tStopRefresh)
    Beep.stop()  # ensure sound has stopped at end of routine
    mainExpLoop.addData('Beep.started', Beep.tStartRefresh)
    mainExpLoop.addData('Beep.stopped', Beep.tStopRefresh)
    
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
    while continueRoutine:
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
    while continueRoutine and routineTimer.getTime() > 0:
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
    thisExp.nextEntry()
    
# completed 3 repeats of 'mainExpLoop'


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
while continueRoutine and routineTimer.getTime() > 0:
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
