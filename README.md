# thoughtspot_tml_modification
This repository has the Script to update the Thoughtspot TML answers and liveboards.

Process:
1. Create an environment with the required packages
   python -m venv ts_search
   pip install -r requirements.txt

2. ts_search_query.py -> Test file to understand iterations of TML.
3. ts_search_fix.py -> Actual file to modify TML answers and liveboards.


NOTE: This will modify every liveboard and answer. If you want certain things to be modified, add a list of files or list of paths.
