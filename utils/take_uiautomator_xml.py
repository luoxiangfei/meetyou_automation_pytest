import subprocess
import os
from utils.config import Config

other_config = Config('other_config.yaml')
sdcard_path = other_config.get('mobile_screencap_path')
pc_path = other_config.get('pc_screencap_path')

def get_uix_and_pull():
    p = subprocess.Popen('adb shell uiautomator dump %s/app.uix' % sdcard_path, shell=True)
    p.wait()
    p = subprocess.Popen('adb pull %s/app.uix %s/app.uix' % (sdcard_path, pc_path), shell=True)
    p.wait()


def get_screen_and_pull():
    p = subprocess.Popen('adb shell screencap -p %s/app.png' % sdcard_path, shell=True)
    p.wait()
    p = subprocess.Popen('adb pull %s/app.png %s/app.png' % (sdcard_path, pc_path), shell=True)
    p.wait()

def clear_sdcard_screencap_file():
    p = subprocess.Popen('adb shell rm -rfv %s/*' % sdcard_path, shell=True)
    p.wait()

def clear_pc_screencap_file():
    file_list = os.listdir(pc_path)
    if len(file_list):
        for i in os.listdir(pc_path):
            os.remove(os.path.join(pc_path, i))
        print('OK')


if __name__ == '__main__':
    clear_pc_screencap_file()
    get_uix_and_pull()
    get_screen_and_pull()
    clear_sdcard_screencap_file()
