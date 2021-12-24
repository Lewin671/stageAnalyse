import signal
import subprocess
import time


def cmd(command):
    subp = subprocess.Popen(command, shell=True, stdout=None, stderr=None, encoding="utf-8")
    return subp


def run_with_recording(func, file_name):
    task = cmd('scrcpy --no-display --max-size 1024 --max-fps 120 --render-expired-frames --record ' + file_name)
    time.sleep(2)
    func()
    task.send_signal(signal.SIGINT)
    task.wait(3)
