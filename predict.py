from stagesepx.classifier.keras import KerasClassifier
from stagesepx.reporter import Reporter

import config
from cutter import cutting_video

if __name__ == '__main__':
    file_name = config.PREDICTED_VIDEO_PATH
    stable, unstable, _ = cutting_video(file_name)

    classifier = KerasClassifier()
    classifier.load_model(config.MODEL_PATH)

    classify_result = classifier.classify(file_name, stable, keep_data=True)
    result_dict = classify_result.to_dict()

    # 写html报告
    r = Reporter()
    r.draw(classify_result, './result.html')

    last_stage_frame = None
    last_stage = None

    for i in range(len(stable) + 1):
        if last_stage_frame is None:
            last_stage = str(i)
            last_stage_frame = classify_result.last(last_stage)
        else:
            current_stage = str(i)
            current_stage_frame = classify_result.first(current_stage)

            if current_stage_frame is None:
                continue

            print("from stage ", last_stage, " to ", current_stage, " costs " + str(
                current_stage_frame.timestamp - last_stage_frame.timestamp), "s")

            last_stage_frame = current_stage_frame
            last_stage = current_stage
