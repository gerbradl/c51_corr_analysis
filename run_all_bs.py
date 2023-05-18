import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

input_dir = 'tests/input_file/updated'
cmd_template = "fit_corr tests/input_file/updated/{}.py --fit --bs --Nbs 5000 --bs_seed {} --bs_results bs_results/scale_setting_3.h5 --bs_path {}"

def run_command(ensemble_name):
    cmd = cmd_template.format(ensemble_name, ensemble_name,ensemble_name)
    print(f"Running: {cmd}")
    process = subprocess.Popen(cmd, shell=True)
    process.communicate()

tasks = []
executor = ProcessPoolExecutor(max_workers=5)

for dirpath, dirnames, filenames in os.walk(input_dir):
    for filename in filenames:
        if filename.endswith('.py'):
            ensemble_name = os.path.splitext(filename)[0]
            tasks.append(executor.submit(run_command, ensemble_name))

for task in tasks:
    task.result()
