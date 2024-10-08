import string
import sys
import time
sys.path.append("..")
from kea.main import *

class Test(Kea):
    

    @initialize()
    def set_up(self):
        d(text="Get Started").click()
        
    # 7695
    @precondition(
        lambda self: d(text="Manage note types").exists() and d(resourceId="com.ichi2.anki:id/note_name").exists()
    )
    @rule()
    def rename_note_type_shouldnot_display(self):
        d(resourceId="com.ichi2.anki:id/note_name").click()
        
        d(text="Front").click()
        
        d(text="Rename field").click()
        
        assert not d(text="Rename note type").exists(), "Rename note type found"




t = Test()

setting = Setting(
    apk_path="./apk/ankidroid/2.18alpha6.apk",
    device_serial="emulator-5554",
    output_dir="output/ankidroid/7695/mutate_new/1",
    policy_name="random",

    main_path="main_path/ankidroid/7695_new.json"
)
run_android_check_as_test(t,setting)

