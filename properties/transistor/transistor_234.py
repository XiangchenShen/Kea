import string
import sys
import time
sys.path.append("..")
from kea.main import *

class Test(Kea):
    
    @initialize()
    def set_up(self):
        d(text="Add a new station").click()
        
        d(className="android.widget.EditText").set_text("http://st01.dlf.de/dlf/01/128/mp3/stream.mp3")
        
        d(text="ADD").click()
        

    @precondition(
        lambda self: d(resourceId="org.y20k.transistor:id/player_sheet_station_options_button").exists()
    )
    @rule()
    def cancel_delete_should_not_change_name(self):
        station_name = d(resourceId="org.y20k.transistor:id/player_station_name").get_text()
        print("station_name: " + station_name)
        d(resourceId="org.y20k.transistor:id/player_sheet_station_options_button").click()
        
        d(text="Delete").click()
        
        d(text="CANCEL").click()
             
        assert d(text=station_name).exists(), "NAME changes after cancel delete"





t = Test()

setting = Setting(
    apk_path="./apk/transistor/3.2.2.apk",
    device_serial="emulator-5554",
    output_dir="output/transistor/234/random_100/1",
    policy_name="random",

    main_path="main_path/transistor/234.json"
)
run_android_check_as_test(t,setting)

