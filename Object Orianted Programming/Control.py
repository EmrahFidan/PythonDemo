import random
import time

class DynamicArray:
    def __init__(self):
        self._data = [None]
        self._size = 0

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return self._size

    def append(self, value):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._data[self._size] = value
        self._size += 1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty list")
        value = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return value

class TVController:
    def __init__(self, tv_status="Off", tv_volume=0, channel_list=DynamicArray(), current_channel="Trt"):
        self.tv_status = tv_status
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.current_channel = current_channel

    def turn_on_tv(self):
        if self.tv_status == "On":
            print("TV is already on.")
        else:
            print("Turning on the TV...")
            self.tv_status = "On"

    def turn_off_tv(self):
        if self.tv_status == "Off":
            print("TV is already off.")
        else:
            print("Turning off the TV...")
            self.tv_status = "Off"

    def adjust_volume(self):
        while True:
            user_input = input("Decrease Volume: '<'\nIncrease Volume: '>'\nExit: '0'\n'")

            if user_input == "<":
                if self.tv_volume > 0:
                    self.tv_volume -= 1
                    print("Volume:", self.tv_volume)
            elif user_input == ">":
                if self.tv_volume < 31:
                    self.tv_volume += 1
                    print("Volume:", self.tv_volume)
            elif user_input.lower() == "0":
                print("Volume settings updated:", self.tv_volume)
                break
            else:
                print("Invalid Input. Please try again.")
        
    def add_channel(self, channel_names):
        # Adds new channels to the channel list.
        names = channel_names.split(",")
        for channel_name in names:
            channel_name = channel_name.strip()  # Kenar boşlukları temizle
            if channel_name:
                print("Adding channel:", channel_name)
                time.sleep(1)
                self.channel_list.append(channel_name)
                print("Channel added:", channel_name)

    def switch_to_random_channel(self):
        random_channel = random.choice(self.channel_list)
        self.current_channel = random_channel
        print("Current Channel:", self.current_channel)

    def get_channel_count(self):
        return len(self.channel_list)

    def __str__(self):
        return "TV Status: {}\nTV Volume: {}\nChannel List: {}\nCurrent Channel: {}\n".format(
            self.tv_status, self.tv_volume, self.channel_list[:], self.current_channel
        )

def main():
    tv_controller = TVController()

    print(
        """
    TV Application

    1. Turn On TV
    2. Turn Off TV
    3. Adjust Volume
    4. Add Channel
    5. Get Channel Count
    6. Switch to Random Channel
    7. TV Information

    Press 'q' to quit.
    """
    )

    while True:
        action = input("Select an action:")

        if action.lower() == "q":
            print("Exiting the program...")
            break

        action_map = {
            "1": tv_controller.turn_on_tv,
            "2": tv_controller.turn_off_tv,
            "3": tv_controller.adjust_volume,
            "4": lambda: tv_controller.add_channel(
                input("Enter channel names separated by commas:")
            ),
            "5": lambda: print("Channel Count:", tv_controller.get_channel_count()),
            "6": tv_controller.switch_to_random_channel,
            "7": lambda: print(tv_controller),
        }

        selected_action = action_map.get(action)
        if selected_action:
            selected_action()
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
