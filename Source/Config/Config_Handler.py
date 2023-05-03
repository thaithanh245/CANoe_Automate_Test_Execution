import json
import os
import shutil

class ConfigHandler:
    def __init__(self, current_dir:str):
        self.tools_config = {}
        self.test_run_config = {}
        self.cwd = current_dir
        self.load_config()

    def load_config(self):
        with open(f"{self.cwd}\\Config\\Tools_Config.json", "r") as config_file:
            self.tools_config = json.load(config_file)
        for key in self.tools_config["tool_directories"].keys():
            self.tools_config["tool_directories"][key] = self.cwd + self.tools_config["tool_directories"][key]

        with open(f"{self.cwd}\\Config\\Test_Run_Config.json", "r") as config_file:
            self.test_run_config = json.load(config_file)

    def clean_up_and_reset_output(self):
        output_folder_dir = self.tools_config["tool_directories"]["output_folder"]
        database_folder_dir = self.tools_config["tool_directories"]["database_folder"]
        # delete and create new output folder
        if os.path.isdir(output_folder_dir) == True:
            shutil.rmtree(output_folder_dir)
        os.mkdir(output_folder_dir)
        # if Database folder got deleted, create new Database folder
        if os.path.isdir(database_folder_dir) != True:
            os.mkdir(database_folder_dir)
    
    def get_canoe_config_direct_directory(self):
        return  self.test_run_config["CANoe_config_directory"]["CANoe_config_direct_directory"]