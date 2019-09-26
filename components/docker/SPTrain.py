# coding=utf-8
from __future__ import absolute_import, print_function

import os
from suanpan.app.arguments import Folder, Int, String, Bool
from suanpan.app import app
from lib import cli


@app.input(Folder(key="inputData1"))
@app.input(Folder(key="alignments1"))
@app.input(Folder(key="inputData2"))
@app.input(Folder(key="alignments2"))
@app.param(Int(key="batchSize", default=4, help="64 (2, 256)"))
@app.param(
    String(
        key="trainer",
        default="original",
        help="original dfaker dfl-h128 dfl-sae iae lightweight realface unbalanced villain",
    )
)
@app.param(Int(key="iterations", default=10000, help="1000000 (0, 5000000)"))
@app.param(Int(key="__gpu", default=0))
@app.param(Bool(key="allowGrowth", default=False))
@app.param(Bool(key="warpToLandmarks", default=False))
@app.param(Bool(key="noFlip", default=False))
@app.param(Bool(key="noAugmentColor", default=False))
@app.output(Folder(key="outputModel"))
def SPTrain(context):
    args = context.args

    PARSER = cli.FullHelpArgumentParser()
    TRAIN = cli.TrainArgs(
        PARSER, "train", "This command trains the model for the two faces A and B"
    )

    argsTransfer = [
        "--input-A",
        args.inputData1,
        "--alignments-A",
        os.path.join(args.alignments1, "alignments.json"),
        "--input-B",
        args.inputData2,
        "--alignments-B",
        os.path.join(args.alignments2, "alignments.json"),
        "--model-dir",
        args.outputModel,
        "--batch-size",
        str(args.batchSize),
        "--trainer",
        args.trainer,
        "--iterations",
        str(args.iterations),
        "--gpus",
        str(args.__gpu),
    ]
    argsNoValue = [
        ("--allow-growth", str(args.allowGrowth)),
        ("--warp-to-landmarks", str(args.warpToLandmarks)),
        ("--no-flip", str(args.noFlip)),
        ("--no-augment-color", str(args.noAugmentColor)),
    ]
    for name, value in argsNoValue:
        if value:
            argsTransfer.append(name)

    ARGUMENTS = PARSER.parse_args(argsTransfer)
    ARGUMENTS.func(ARGUMENTS)

    return args.outputData


if __name__ == "__main__":
    SPTrain()
