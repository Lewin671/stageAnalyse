from stagesepx.hook import IgnoreHook

HOOKS = [
    # height,width
    IgnoreHook(size=(0.05, 1), overwrite=True),

    # used for local verification
    # FrameSaveHook(target_dir=config.TRANSFORMED_TRAINING_SET_PATH)
]
