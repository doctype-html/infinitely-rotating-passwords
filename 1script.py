import getpass
import subprocess
import time

def change_password(new_password):
    """change password"""
    username = getpass.getuser()  # get user
    try:
        subprocess.run(
            ['sudo', 'chpasswd'],
            input=f'{username}:{new_password}'.encode(),
            check=True
        )
        print(f"yay password changed!")
    except subprocess.CalledProcessError as e:
        print(f"an unexpected error occured {e}")

passwords = [
    "V4aiU1zh!Fr",
    "eech5UdLQL!",
    "rEI05Y9cKC!",
    "t9iu!8geKTi",
    "uOLctmvn!jc"
]

def rotate_passwords():
    """rotates thru predetermined set of passwords periodically"""
    while True:
        for password in passwords:
            change_password(password)
            time.sleep(30)
if __name__ == "__main__":
    try: 
        rotate_passwords()

# NOTES that i think you already know but...
 # 1) run this script with sudo "sudo python3 script1.py" so the code actually works
 # 2) sudo chpasswd to change password
 # 3) after that it should rotate thru pre-determined list 
 # 4) i may attempt to make it randomly generate passwords every 30 secs which is simple but currently have 0 time so.
