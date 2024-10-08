import string
import sys
import time
sys.path.append("..")
from kea.main import *

class Test(Kea):
    

    @initialize()
    def set_up(self):
        d(description="Add").click()
        
        d(className="android.widget.EditText").set_text("http://st01.dlf.de/dlf/01/128/mp3/stream.mp3")
        
        d(text="ADD").click()
        
        d(description="Add").click()
        
        d(className="android.widget.EditText").set_text("http://stream.live.vc.bbcmedia.co.uk/bbc_world_service")
        
        d(text="ADD").click()
        
        d(description="Add").click()
        
        d(className="android.widget.EditText").set_text("http://www.101smoothjazz.com/101-smoothjazz.m3u")
        
        d(text="ADD").click()

    @precondition(
        lambda self: d(resourceId="org.y20k.transistor:id/list_item_more_button").exists() and d(resourceId="org.y20k.transistor:id/list_item_playback_indicator").exists()
    )
    @rule()
    def rename_station_not_change_station_state(self):
        playing_station_name = d(resourceId="org.y20k.transistor:id/list_item_playback_indicator").sibling(resourceId="org.y20k.transistor:id/list_item_textview").get_text()
        print("playing_station_name: " + playing_station_name)
        d(resourceId="org.y20k.transistor:id/list_item_playback_indicator").sibling(resourceId="org.y20k.transistor:id/list_item_more_button").click()
        
        d(text="Rename").click()
        
        original_name = d(resourceId="org.y20k.transistor:id/dialog_rename_station_input").get_text()
        print("original_name: " + original_name)
        new_name = st.text(alphabet=string.ascii_lowercase,min_size=1, max_size=6).example()
        print("new_name: " + new_name)
        d(resourceId="org.y20k.transistor:id/dialog_rename_station_input").set_text(new_name)
        
        d(text="RENAME").click()
        
        assert d(text=new_name).exists(), "NEW NAME DOES NOT EXIST"
        assert not d(text=original_name).exists(), "OLD NAME STILL EXISTS"
        assert d(resourceId="org.y20k.transistor:id/list_item_playback_indicator").sibling(resourceId="org.y20k.transistor:id/list_item_textview").get_text() == new_name, "station state changed"



t = Test()

setting = Setting(
    apk_path="./apk/transistor/1.2.1.apk",
    device_serial="emulator-5554",
    output_dir="output/transistor/44/mutate/1",
    policy_name="random",

    main_path="main_path/transistor/44.json"
)
run_android_check_as_test(t,setting)

