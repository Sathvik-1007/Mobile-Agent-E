import subprocess

def send_hello_adb():
    try:
        # This sends "hello" as input text to the connected Android device
        subprocess.run(["adb", "shell", "input", "text", "hello"], check=True)
        print("Sent 'hello' to Android device.")
    except subprocess.CalledProcessError as e:
        print("ADB command failed:", e)
    except FileNotFoundError:
        print(" 'adb' not found. Make sure ADB is installed and in your PATH.")

send_hello_adb()
