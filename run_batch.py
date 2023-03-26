import sys
import os 


def main():
    project_path = os.path.normpath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))
    path = project_path + '/c51_corr_analysis_gb/tests/input_file/'
    # path = os.path.realpath('/c51_corr_analysis_gb/tests/input_file/')
    for root, dirs, files in os.walk(path):
        for file in files:
            os.system ('fit_corr.py {}'.format(root + '/' + file))

if __name__ == "__main__":
    main()
