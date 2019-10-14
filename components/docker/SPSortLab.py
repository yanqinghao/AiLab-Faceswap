# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.app.arguments import Folder, String
from suanpan.app import app
from mainscripts import Sorter


@app.input(Folder(key="inputData"))
@app.param(
    String(
        key="sortByMethod",
        default="blur",
        help='("blur", "face", "face-dissim", "face-yaw", "face-pitch", "hist", "hist-dissim", "brightness", "hue", "black", "origname", "oneface", "final", "final-no-blur", "test")',
    )
)
@app.output(Folder(key="outputData"))
def SPSortLab(context):
    args = context.args

    Sorter.main(input_path=args.inputData, sort_by_method=args.sortByMethod)

    return args.inputData


if __name__ == "__main__":
    SPSortLab()
