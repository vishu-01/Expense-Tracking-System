# whenever we need some setup in python like changing system path, configuration we can do this in a file named conftest.py


import os
import sys 


# Our file is not refering the parent file directory. To solve this we will join our current directory with the parent directory


project_root = os.path.join(os.path.dirname(__file__), '..')         # Here we are joining the directories.' .. ' is here parent directory
print("**PROJECT ROOT: ", project_root)
sys.path.insert(0, project_root)
print(sys.path)

