import string
import sys
import time
sys.path.append("..")
from kea.main import *

class Test(Kea):
    

    @precondition(
        lambda self: d(text="Download").exists() and d(text="Stream").exists() and d(resourceId="de.danoeh.antennapod:id/visit_website_item").exists()
    )
    @rule()
    def change_setting_should_not_influence_Download_function(self):
        d(text="Download").click()
        
        assert d(text="Delete").exists() or d(text="Cancel").exists()



t = Test()

setting = Setting(
    apk_path="./apk/antennapod/1.8.0.apk",
    device_serial="emulator-5554",
    output_dir="output/antennapod/3786/random_100/1",
    policy_name="random",

    main_path="main_path/antennapod/3786.json"
)
run_android_check_as_test(t,setting)

