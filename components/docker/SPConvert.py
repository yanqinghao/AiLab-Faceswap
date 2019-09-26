# coding=utf-8
from __future__ import absolute_import, print_function

import os
from suanpan.app.arguments import Folder, String, Int
from suanpan.app import app
from lib import cli
from utils import get_all_files


@app.input(Folder(key="inputData1"))
@app.input(Folder(key="inputData2"))
@app.input(Folder(key="inputModel"))
@app.param(
    String(
        key="colorAdjustment",
        default="avg-color",
        help="avg-color color-transfer manual-balance match-hist seamless-clone none",
    )
)
@app.param(Int(key="__gpu", default=0))
@app.param(
    String(
        key="maskType",
        default="predicted",
        help="components dfl_full extended facehull predicted none",
    )
)
@app.param(
    String(
        key="scaling",
        default="none",
        help="sharpen none",
    )
)
@app.output(Folder(key="outputData"))
def SPConvert(context):
    args = context.args

    video = get_all_files(args.refVideo)[0] if args.refVideo else args.refVideo

    PARSER = cli.FullHelpArgumentParser()
    CONVERT = cli.ConvertArgs(
        PARSER, "convert", "Convert a source image to a new one with the face swapped"
    )

    ARGUMENTS = PARSER.parse_args(
        [
            "--input-dir",
            args.inputData1,
            "--model-dir",
            args.inputModel,
            "--output-dir",
            args.outputData,
            "--alignments",
            os.path.join(args.inputData2, "alignments.json"),
            "--color-adjustment",
            args.colorAdjustment,
            "--mask-type",
            args.maskType,
            "--scaling",
            args.scaling,
            "--gpus",
            str(args.__gpu),
        ]
    )
    ARGUMENTS.func(ARGUMENTS)

    return args.outputData


if __name__ == "__main__":
    SPConvert()
