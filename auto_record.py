import time

import uiautomator2

import logger
import utils

DEVICE_ID = "e8f9445d"
PACKAGE_NAME = "com.taobao.taobao"
video_fp = "./demo.mp4"


def click(device):
    logger.log("click now")
    device(text="天猫新品").click()
    time.sleep(3)


def record_task(file_name):
    device = uiautomator2.connect(DEVICE_ID)
    logger.log("Device Info", device.info)
    device.app_start(PACKAGE_NAME, wait=True, stop=True)

    # wait app to be front
    device.app_wait(PACKAGE_NAME, front=True)
    logger.log("App come to the front")

    # wait 3s to make it stable
    device.app_wait(PACKAGE_NAME, timeout=3)
    logger.log("ready to click button")

    # record clicking
    raw_file_name = "./video/raw_" + file_name
    file_name = "./video/" + file_name
    utils.run_with_recording(lambda: click(device), raw_file_name)
    utils.cmd('ffmpeg -r 60 -i ' + raw_file_name + " " + file_name).wait()


if __name__ == '__main__':
    cnt = 0
    for i in range(10):
        file_name = "file" + str(i) + ".mp4"
        record_task(file_name)
