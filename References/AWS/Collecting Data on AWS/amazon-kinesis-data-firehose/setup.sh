# This should create a Python virtual environment called venv:
python3 -m venv venv

# This should activate the environment so we can install Python packages in it
# Other machines may use different commands. See this link for more details: 
# https://docs.python.org/3/library/venv.html
source venv/bin/activate

# For Powershell:
# venv\Scripts\Activate.ps1

# For cmd.exe:
# venv\Scripts\activate.bat

# Then install the boto3 package
pip install boto3

# And open up the Python interpreter
python3