from stagesepx.classifier.keras import KerasClassifier
from stagesepx.reporter import Reporter

import config
from cutter import cutting_video

file_name = config.PREDICTED_VIDEO_PATH
stable, unstable, _ = cutting_video(file_name)

classifier = KerasClassifier()
classifier.load_model(config.MODEL_PATH)

classify_result = classifier.classify(file_name, stable, keep_data=True)
result_dict = classify_result.to_dict()

# 写html报告
r = Reporter()
r.draw(classify_result, './result.html')
