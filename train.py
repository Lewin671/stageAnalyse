from stagesepx.classifier.keras import KerasClassifier

import config
import hooks

if __name__ == '__main__':
    classifier = KerasClassifier(
        epochs=config.EPOCH_NUMBER,
        target_size=config. TARGET_SIZE
    )
    for hook in hooks.HOOKS:
        classifier.add_hook(hook)
    classifier.train(config.TRAINING_SET_PATH)
    classifier.save_model(config.MODEL_PATH, overwrite=True)
