import string
import sys
import time
sys.path.append("..")
from kea.main import *

class Test(Kea):
    

    @initialize()
    def set_up(self):
        pass

    @precondition(
        lambda self: d(resourceId="com.ichi2.anki:id/dropdown_deck_name").exists() and not d(resourceId="com.ichi2.anki:id/navdrawer_items_container").exists()
    )
    @rule()
    def add_card_in_one_deck_should_work(self):
        deck_name = d(resourceId="com.ichi2.anki:id/dropdown_deck_name").get_text()
        card_count = int(d(resourceId="com.ichi2.anki:id/dropdown_deck_counts").get_text().split(" ")[0])
        print("deck_name: " + str(deck_name))
        print("card_count: " + str(card_count))
        # add a card
        d(resourceId="com.ichi2.anki:id/action_add_note_from_card_browser").click()
        
        d(resourceId="com.ichi2.anki:id/note_deck_spinner").click()
        
        d(text=deck_name).click()
        
        front = st.text(alphabet=string.printable,min_size=1, max_size=6).example()
        print("front: " + str(front))
        d(resourceId="com.ichi2.anki:id/id_note_editText").set_text(front)
        
        d(resourceId="com.ichi2.anki:id/action_save").click()
        
        d(description="Navigate up").click()
        
        # check if the card is added
        new_card_count = int(d(resourceId="com.ichi2.anki:id/dropdown_deck_counts").get_text().split(" ")[0])
        print("new_card_count: " + str(new_card_count))
        assert new_card_count == card_count + 1, "card count should increase by 1"
        





t = Test()

setting = Setting(
    apk_path="./apk/ankidroid/2.11alpha7.apk",
    device_serial="emulator-5554",
    output_dir="output/ankidroid/6288/random_100/1",
    policy_name="random",
    
    number_of_events_that_restart_app = 100
)
run_android_check_as_test(t,setting)

