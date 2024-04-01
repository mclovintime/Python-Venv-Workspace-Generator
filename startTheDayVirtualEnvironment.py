import os
import datetime
import subprocess
import sys

# Define the path to the "work" directory on your desktop
work_dir = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', 'work')

# Check if the "work" directory exists, create it if it doesn't
if not os.path.exists(work_dir):
    os.makedirs(work_dir)

# Get the current month and day
current_month = datetime.datetime.now().strftime('%B')
current_day = datetime.datetime.now().day

# Create the sub-directory with the current month and day
sub_dir = os.path.join(work_dir, f'{current_month.lower()}{current_day}')
if not os.path.exists(sub_dir):
    os.makedirs(sub_dir)
    with open(os.path.join(sub_dir, 'log.txt'), 'w') as log_file:
        log_file.write(f'Folder initialized at {datetime.datetime.now()}\n')

# Create A.py and B.py if they don't exist
file_A = os.path.join(sub_dir, 'A.py')
file_B = os.path.join(sub_dir, 'B.py')
if not os.path.exists(file_A):
    with open(file_A, 'w'):
        pass
if not os.path.exists(file_B):
    with open(file_B, 'w'):
        pass

# Create a virtual environment in the sub-directory
venv_dir = os.path.join(sub_dir, 'venv')
if not os.path.exists(venv_dir):
    subprocess.run([sys.executable, '-m', 'venv', venv_dir])

# Activate the virtual environment
activate_cmd = f'source {venv_dir}/bin/activate'
subprocess.run(activate_cmd, shell=True, executable='/bin/bash')

# Prompt the user to install packages
while True:
    package = input("Enter a package to install (or 'q' to quit): ")
    if package.lower() == 'q':
        break
    install_cmd = f'{venv_dir}/bin/pip install {package}'
    subprocess.run(install_cmd, shell=True, executable='/bin/bash')
    with open(os.path.join(sub_dir, 'log.txt'), 'a') as log_file:
        log_file.write(f'Package {package} installed at {datetime.datetime.now()}\n')