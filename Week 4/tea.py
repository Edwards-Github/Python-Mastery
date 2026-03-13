from utils import execution_timer
import time

@execution_timer
def brew_tea(tea_type, steep_time):
	print(f"Brewing {tea_type} tea...")
	time.sleep(steep_time)
	print("Tea is ready!")

@execution_timer
def make_matcha():
	print("Making matcha...")
	time.sleep(1)
	print("Tea is ready!")

brew_tea("green", 1)
brew_tea(tea_type="black", steep_time=3)
make_matcha()