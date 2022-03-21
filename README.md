# sense-of-agency


Sessions testing a sense of agency with BrainGate's iBCI system, intended to be launched on the user's computer, and interacted with using BG Home.


### Key Directories

- General python files (regarding receiving and parsing UDP packets containing decoded neural signals) applicable to all python-based research sessions are in the root directory. 
- sense-of-agency/ directory contains all SoA files


### Key Files

- sense-of-agency/timing_training.py: practice psychopy experiment, giving the participant exposure to estimating time delays. 
- sense-of-agency/main_wo_survey_qs.py: main psychopy experiment file. 


### Launching the experiment

**During a session:**

- run research-sessions/Scripts/Start_Sense_of_Agency_PRACTICE.bat
- run research-sessions/Scripts/Start_Sense_of_Agency_MAIN.bat


**Testing:**

- `timing_training.py` and `main_wo_survey_qs.py` may be run from the command line as with `python file_name.py` as long as `python` maps to a version with psychopy installed as a requirement. 


### Notes

- When adding files back to research-sessions/ BrainGate repo, all of this code is contained within the "PythonGames/" directory



Author: Derek Wacks
Updated: 3.21.2022

