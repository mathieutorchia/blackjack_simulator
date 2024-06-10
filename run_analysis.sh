#!/bin/bash
# Activate the Anaconda environment
source /Users/yourusername/opt/anaconda3/bin/activate base

# Print the Python executable and openpyxl version for verification
echo "Using Python executable:"
which python
echo "openpyxl version:"
python -c "import openpyxl; print(openpyxl.__version__)"

# Run the Python script
/Users/mathieutorchia/opt/anaconda3/bin/python "/Applications/Everything/Personal Projects/GIT/FirstRepo/analysis.py"
