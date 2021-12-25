from stagesepx.cutter import VideoCutter
from stagesepx.video import VideoObject

import config
from hooks import HOOKS


def cutting_video(file_name: str, threshold: float = config.THRESHOLD):
    video = VideoObject(file_name)
    video.load_frames()

    # cutting video
    cutter = VideoCutter()

    for hook in HOOKS:
        cutter.add_hook(hook)

    # calculate the ssim and psnr of every blocks of every frames
    res = cutter.cut(video, block=config.BLOCK_NUMBER)

    # classify sections by the its stability
    stable, unstable = res.get_range(threshold=threshold, offset=config.OFFSET)
    return stable, unstable, res
