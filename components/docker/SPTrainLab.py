# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.app.arguments import Folder, String, Bool, Int
from suanpan.app import app
from mainscripts import Trainer


@app.input(Folder(key="trainingDataSrcDir"))
@app.input(Folder(key="trainingDataDstDir"))
@app.input(Folder(key="pretrainingDataDir"))
@app.param(
    String(
        key="modelName",
        default="SAE",
        help="AVATAR, DF, H64, H128, LIAEF128, SAE, DEV_FANSEG",
    )
)
@app.param(Int(key="forceGpuIdx", default=-1))
@app.param(Bool(key="cpuOnly", default=False))
@app.output(Folder(key="modelDir"))
def SPTrainLab(context):
    args = context.args
    training_args = {
        "training_data_src_dir": args.trainingDataSrcDir,
        "training_data_dst_dir": args.trainingDataDstDir,
        "pretraining_data_dir": args.pretrainingDataDir,
        "model_path": args.modelDir,
        "model_name": args.modelName,
        "no_preview": True,
        "debug": False,
        "execute_programs": [],
    }
    device_args = {"cpu_only": args.cpuOnly, "force_gpu_idx": args.forceGpuIdx}

    Trainer.main(training_args, device_args)

    return args.modelDir


if __name__ == "__main__":
    SPTrainLab()
