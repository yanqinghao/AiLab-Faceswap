# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.app.arguments import Folder, String, Float, Int
from suanpan.app import app
from tools import cli
from lib.cli import FullHelpArgumentParser


@app.input(Folder(key="inputData"))
@app.param(
    String(
        key="sortBy",
        default="face",
        help="blur, face, face-cnn, face-cnn-dissim, face-yaw, hist, hist-dissim",
    )
)
@app.param(
    Float(
        key="refThreshold",
        default=-1.0,
        help="(-1.0, 10.0) Defaults: face-cnn 7.2, hist 0.3",
    )
)
@app.param(String(key="finalProcess", default="rename", help="folders, rename"))
@app.param(String(key="groupBy", default="hist", help="blur, face-cnn, face-yaw, hist"))
@app.param(Int(key="bins", default=5, help="(1, 100)"))
@app.output(Folder(key="outputData"))
def SPSort(context):
    args = context.args

    PARSER = FullHelpArgumentParser()
    SORT = cli.SortArgs(
        PARSER, "sort", "This command lets you sort images using various methods."
    )

    ARGUMENTS = PARSER.parse_args(
        [
            "--input",
            args.inputData,
            "--output",
            args.outputData,
            "--sort-by",
            args.sortBy,
            "--ref_threshold",
            str(args.refThreshold),
            "--final-process",
            args.finalProcess,
            "--group-by",
            args.groupBy,
            "--bins",
            str(args.bins),
        ]
    )
    ARGUMENTS.func(ARGUMENTS)

    return args.outputData


if __name__ == "__main__":
    SPSort()
