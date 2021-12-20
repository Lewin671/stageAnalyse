import config
from cutter import cutting_video

file_name = config.TRAINING_VIDEO_PATH
stable, unstable, res = cutting_video(file_name)

# 把分好类的稳定阶段的图片存本地
res.pick_and_save(stable, 100, to_dir=config.TRAINING_SET_PATH, meaningful_name=True)
