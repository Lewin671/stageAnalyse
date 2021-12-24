import os

from stagesepx.reporter import Reporter

import config
import hooks
from classifier import Classifier
from cutter import cutting_video


def report_path(file_name: str) -> str:
    head, child = os.path.split(file_name)
    _, parent = os.path.split(head)
    return os.path.normpath(os.path.join("./report", parent + "_" + child + "_" + "report.html"))


if __name__ == '__main__':
    classifier = Classifier(target_size=config.TARGET_SIZE)
    classifier.load_model(config.MODEL_PATH)
    for hook in hooks.HOOKS:
        classifier.add_hook(hook)

    report_dir_path = "./report"
    if not os.path.isdir(report_dir_path):
        os.mkdir(report_dir_path)

    for file_name in config.PREDICTED_VIDEO_PATH_LIST:
        stable, unstable, _ = cutting_video(file_name)

        classify_result = classifier.classify(file_name, stable, keep_data=False)
        result_dict = classify_result.to_dict()

        # 写html报告
        r = Reporter()
        r.draw(classify_result, report_path(file_name))

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

        startTime = classify_result.last('0').timestamp
        endTime = classify_result.first(sorted(result_dict.keys())[-1]).timestamp
        print("total costs " + str(endTime - startTime) + "s")
