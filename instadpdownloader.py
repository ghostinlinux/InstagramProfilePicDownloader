import os
import instaloader


def instadpdownloader(*args):
    for user in args:
        instance = instaloader.Instaloader()
        os.chdir(os.path.join(os.path.expanduser("~"), device_location))
        instance.download_profile(user, profile_pic_only=True)


device_location = input("Enter device location : ")
username = input("Enter username >> ").split(",")
instadpdownloader(*username)
