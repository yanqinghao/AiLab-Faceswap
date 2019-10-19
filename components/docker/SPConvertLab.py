# coding=utf-8
from __future__ import absolute_import, print_function

import os
from suanpan.app.arguments import Folder, String, Int, Bool
from suanpan.app import app



@app.input(Folder(key="inputData"))
@app.input(Folder(key="alignedDir"))
@app.input(Folder(key="modelDir"))
@app.param(Bool(key="__edit", default=False))
@app.param(
    String(
        key="modelName",
        default="SAE",
        help="AVATAR, DF, H64, H128, LIAEF128, SAE, DEV_FANSEG",
    )
)
@app.param(Int(key="forceGpuIdx", default=-1))
@app.param(Bool(key="cpuOnly", default=False))
@app.output(Folder(key="outputData"))
def SPConvertLab(context):
    args = context.args

    convert_args = {
        "input_dir": args.inputData,
        "output_dir": args.outputData,
        "aligned_dir": args.alignedDir,
        "model_dir": args.modelDir,
        "model_name": args.modelName,
    }
    device_args = {
        "cpu_only": args.cpuOnly,
        "force_gpu_idx": args.forceGpuIdx,
    }
    if not args.__edit:
        os.environ["SP_FaceLab_Edit"] = "False"
    from mainscripts import Converter
    Converter.main(convert_args, device_args)

    return args.outputData


if __name__ == "__main__":
    SPConvertLab()
