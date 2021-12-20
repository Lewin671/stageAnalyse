from stagesepx.classifier.keras import KerasClassifier

import config

classifier = KerasClassifier(
    epochs=config.EPOCH_NUMBER
)
classifier.train(config.TRAINING_SET_PATH)
classifier.save_model(config.MODEL_PATH, overwrite=True)
