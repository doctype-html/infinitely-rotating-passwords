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
            time.sleep(1800)
if __name__ == "__main__":
    try: 
        rotate_passwords()
