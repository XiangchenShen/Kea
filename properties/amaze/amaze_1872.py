import string
import sys
import time
sys.path.append("..")
from kea.main import *

class Test(Kea):
    
    @initialize()
    def set_up(self):
        if d(text="ALLOW").exists():
            d(text="ALLOW").click()
            
        elif d(text="Allow").exists():
            d(text="Allow").click()
            
            
    @precondition(lambda self: 
                  d(resourceId="com.amaze.filemanager:id/search").exists() and not 
                  d(text="Internal Storage").exists() and not 
                  d(resourceId="com.amaze.filemanager:id/cpy").exists() and 
                  d(resourceId="com.amaze.filemanager:id/firstline").exists()
    )
    @rule()
    def search_folder_should_be_opened(self):
        
        folder_count = d(resourceId="com.amaze.filemanager:id/firstline").count
        print("folder count: "+str(folder_count))
        folder = None
        for i in range(folder_count):
            folder_index = random.randint(0, folder_count-1)
            print("folder index: "+str(folder_index))
            folder_ui = d(resourceId="com.amaze.filemanager:id/firstline")[folder_index]
            folder_ui_name = folder_ui.get_text()          
            if "." in folder_ui_name:
                continue
            folder = folder_ui
            folder_name = folder_ui_name
            break
        if folder is None:
            print("no folder found")
            return
        print("folder name: "+str(folder_name))
        folder.click()
        
        assert not d(text="Open As").exists(), "open folder failed with folder name: "+str(folder_name)




t = Test()

setting = Setting(
    apk_path="./apk/amaze/amaze-3.4.3.apk",
    device_serial="emulator-5554",
    output_dir="output/amaze/1872/mutate/1",
    policy_name="random",

    main_path="main_path/amaze/1872.json"
)
run_android_check_as_test(t,setting)

