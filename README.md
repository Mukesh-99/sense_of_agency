# sense-of-agency


Code for implementing a BrainGate research session exploring a sense of agency with BrainGate's iBCI system (intended to be launched on the user's computer, and interacted with using BG Home). 

 <br />

### Key Directories

- General python files (regarding receiving and parsing UDP packets containing decoded neural signals) applicable to all python-based research sessions are in the root directory. 
- sense-of-agency/ directory contains all SoA files
 
 <br />

### Key Files

- `sense-of-agency/timing_training.py`: practice psychopy experiment, giving the participant exposure to estimating time delays. 
- `sense-of-agency/main_wo_survey_qs.py`: main psychopy experiment file. 

 <br />
 

### While developing...

- please do not develop with `.psyexp` files, as these need to be converted back to `.py` files to be integrated with BrainGate system code. 

 <br />
 
 
 
### Launching the experiment

**During a session:**

- run research-sessions/Scripts/Start_Sense_of_Agency_PRACTICE.bat
- run research-sessions/Scripts/Start_Sense_of_Agency_MAIN.bat

 
**Testing:**

- `timing_training.py` and `main_wo_survey_qs.py` may be run from the command line (example: `python file_name.py`) as long as `python` maps to a version with psychopy installed as a requirement. 

 <br />

### Reintegrating with the BrainGate code base...

- When adding files back to research-sessions/ BrainGate repo, all of this code is contained within the "PythonGames/" directory
- research-sessions/Scripts/ should contain a bat file to start each applicable python script! (`research-sessions/Scripts/Start_Sense_of_Agency_MAIN.bat`)



Author: Derek Wacks <br />
Updated: 3.21.2022

