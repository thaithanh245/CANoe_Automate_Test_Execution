from Source.Config.Config_Handler import ConfigHandler
from Source.CANoe_Lib.CANoe_App import CanoeApp
import os
import sys
import time
import traceback

try:

    current_dir = os.getcwd()

    config_handler = ConfigHandler(current_dir=current_dir)
    canoe_config_direct_directory = config_handler.get_canoe_config_direct_directory()

    canoe = CanoeApp(canoe_direct_directory=canoe_config_direct_directory)
    print("num of test environemt:")
    print(canoe.test_environments.num_test_environment)
    print("list of test environemts:")
    list_environment = canoe.test_environments.get_list_of_test_environments()
    print(list_environment)
    # list_environment[0].enable()
    canoe.measurement.start()
    time.sleep(5)
    canoe.measurement.stop()
    #canoe.close()

    #input("Press Enter to continue ......")
    sys.exit()

except Exception as error:
    traceback.print_exc()
    input("Press Enter to continue ......")
    sys.exit(error)
