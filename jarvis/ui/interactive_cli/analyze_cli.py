"""
JARVIS-MoCap (https://jarvis-mocap.github.io/jarvis-docs)
Copyright (c) 2022 Timo Hueser.
https://github.com/JARVIS-MoCap/JARVIS-HybridNet
Licensed under GNU Lesser General Public License v3.0
"""

import os
import sys
import torch
import cv2
import inquirer as inq
import matplotlib.pyplot as plt

from jarvis.config.project_manager import ProjectManager
from jarvis.utils.utils import CLIColors
import jarvis.analysis.analyze as analyze
import jarvis.analysis.plotting as plotting
import jarvis.utils.clp as clp


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def launch_analyze_menu():
    cls()
    menu_items = ['Analyze Validation Data', 'Plot Error Histogram',
                'Plot Error per Keypoint', 'Plot Error Histogram per Keypoint',
                '<< back']
    menu = inq.list_input(f"{CLIColors.OKGREEN}{CLIColors.BOLD}Training "
                f"Menu{CLIColors.ENDC}", choices = menu_items)

    if menu == '<< back':
        return
    elif menu == "Analyze Validation Data":
        analyze_validation_data()
    elif menu == "Plot Error Histogram":
        plot_error_histogram()
    elif menu == "Plot Error per Keypoint":
        plot_error_per_keypoint()
    elif menu == "Plot Error Histogram per Keypoint":
        plot_error_histogram_per_keypoint()


def analyze_validation_data():
    cls()
    projectManager = ProjectManager()
    projects = projectManager.get_projects()
    project_name = inq.list_input("Select project to load", choices=projects)
    projectManager.load(project_name)
    cfg = projectManager.get_cfg()

    use_latest_center = inq.list_input("Use most recently saved CenterDetect "
                "weights?", choices=["Yes", "No"])

    if use_latest_center == "Yes":
        weights_center = 'latest'
    else:
        weights_center = inq.text("Path to CenterDetect '.pth' weights file",
                    validate = lambda _, x: (os.path.isfile(x)
                    and x.split(".")[-1] == 'pth'))
    use_latest_hybridnet = inq.list_input("Use most recently saved HybridNet "
                "weights?", choices=["Yes", "No"])
    if use_latest_hybridnet == "Yes":
        weights_hybridnet = 'latest'
    else:
        weights_hybridnet = inq.text("Path to HybirdNet '.pth' weights file",
                    validate = lambda _, x: (os.path.isfile(x)
                    and x.split(".")[-1] == 'pth'))
    subset_cams = inq.list_input("Use only a subset of available cameras?",
                choices=["Yes", "No"], default = "No")
    if subset_cams == "Yes":
        dataset_name = cfg.DATASET.DATASET_3D
        if os.path.isabs(dataset_name):
            calib_root_path = os.path.join(dataset_name, 'calib_params')
        else:
            calib_root_path = os.path.join(cfg.PARENT_DIR,
                        cfg.DATASET.DATASET_ROOT_DIR, dataset_name,
                        'calib_params')
        calib_path = os.path.join(calib_root_path,
                    os.listdir(calib_root_path)[0])
        camera_names = os.listdir(calib_path)
        camera_names = [cam.split(".")[0] for cam in camera_names]
        cameras_to_use = inq.checkbox('Select cameras to be used for analysis',
                    choices=camera_names)
    else:
        cameras_to_use = None
    analyze.analyze_validation_data(project_name, weights_center,
                weights_hybridnet, cameras_to_use)

    print ()
    input ("press Enter to continue")
    launch_analyze_menu()


def get_analysis_path():
    project = ProjectManager()
    projects = project.get_projects()
    project_name = inq.list_input(message="Select project to load",
                choices=projects)
    project.load(project_name)
    cfg = project.get_cfg()
    analysis_path = os.path.join(project.parent_dir,
                project.cfg.PROJECTS_ROOT_PATH, project_name,
                'analysis')
    if len(os.listdir(analysis_path)) == 0:
        clp.error("Please run Analysis on this project first! Aborting...")
        return None, None
    analysis_set = inq.list_input("Select Anlysis Set to load",
                choices = sorted(os.listdir(analysis_path))[::-1])
    path = os.path.join(analysis_path, analysis_set)
    return path, project_name


def get_interactive():
    interactive = inq.list_input("Show interactive Matplotlib window?",
                choices =["Yes", "No"], default = "Yes")
    if interactive == "Yes":
        return True
    else:
        return False


def plot_error_histogram():
    cls()
    path,_ = get_analysis_path()
    if path == None:
        print ()
        input ("press Enter to continue")
        launch_analyze_menu()
        return
    add_more_data = True
    additional_data = {}
    while add_more_data:
        add_more = inq.list_input( "Add another '.csv' file containing "
                    "predictions?", choices =["Yes", "No"], default = "No")
        if add_more == "Yes":
            pred_name = inq.text("Path to prediction '.csv' file",
                        validate = lambda _, x: (os.path.isfile(x)
                        and x.split(".")[-1] == 'csv')),
            data_path = inq.text("Name of the Predictions for Legend")
            additional_data[pred_name] = data_path
        else:
            add_more_data = False
    cutoff = -1
    use_cutoff = inq.list_input("Use Error Cutoff? (Values above cutoff will "
                "be grouped in one bin)", choices =["Yes", "No"],
                default = "No")
    if use_cutoff == "Yes":
        cutoff = int(inq.text("Cutoff Value", default = "30",
                    validate = lambda _, x: (x.isdigit() and int(x) > 0)))
    interactive = get_interactive()
    plotting.plot_error_histogram(path, additional_data, cutoff,
                interactive = interactive)
    launch_analyze_menu()


def plot_error_per_keypoint():
    cls()
    path, project_name = get_analysis_path()
    if path == None:
        print ()
        input ("press Enter to continue")
        launch_analyze_menu()
        return
    interactive = get_interactive()
    plotting.plot_error_per_keypoint(path, project_name, interactive)
    launch_analyze_menu()


def plot_error_histogram_per_keypoint():
    cls()
    path, project_name = get_analysis_path()
    if path == None:
        print ()
        input ("press Enter to continue")
        launch_analyze_menu()
        return
    interactive = get_interactive()
    plotting.plot_error_histogram_per_keypoint(path, project_name, cutoff = -1,
                interactive = interactive)
    launch_analyze_menu()
