import time

import uiautomator2

import config
import logger
import utils


def click(device):
    logger.log("click now")
    device(text="天猫新品").click()
    time.sleep(8)


def record_task(output_file_path: str):
    device = uiautomator2.connect(config.DEVICE_ID)
    logger.log("Device Info", device.info)
    device.app_start(config.PACKAGE_NAME, wait=True, stop=True)

    # wait app to be front
    device(text="天猫新品").wait(timeout=30)
    logger.log("App come to the front")
    logger.log("ready to click button")

    # record clicking
    raw_file_name = "./video/raw_" + output_file_path
    output_file_path = "./video/" + output_file_path
    utils.run_with_recording(lambda: click(device), raw_file_name)
    utils.cmd('ffmpeg -y -i ' + raw_file_name + " " + output_file_path).wait()


if __name__ == '__main__':
    cnt = 0
    for i in range(10):
        file_name = "file" + str(i) + ".mp4"
        record_task(file_name)
