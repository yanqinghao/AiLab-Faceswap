# coding=utf-8
from __future__ import absolute_import, print_function

import os
from suanpan.app.arguments import Folder, String, Bool, Int
from suanpan.app import app



@app.input(Folder(key="trainingDataSrcDir"))
@app.input(Folder(key="trainingDataDstDir"))
@app.input(Folder(key="pretrainingDataDir"))
@app.param(Bool(key="__edit", default=False))
@app.param(
    String(
        key="modelName",
        default="SAE",
        help="AVATAR, DF, H64, H128, LIAEF128, SAE, DEV_FANSEG",
    )
)
@app.param(Int(key="iterations", default=1000))
@app.param(Int(key="batchSize", default=4))
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
    if not args.__edit:
        os.environ["SP_FaceLab_Edit"] = "False"
        os.environ["SP_FaceLab_Iterations"] = str(args.iterations)
        os.environ["SP_FaceLab_Batch_Size"] = str(args.batchSize)
    from mainscripts import Trainer
    Trainer.main(training_args, device_args)

    return args.modelDir


if __name__ == "__main__":
    SPTrainLab()
