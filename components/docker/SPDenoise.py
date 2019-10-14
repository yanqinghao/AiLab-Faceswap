# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.app.arguments import Folder, String, Int
from suanpan.app import app
from mainscripts import VideoEd


@app.input(Folder(key="inputData"))
@app.param(String(key="ext", default="png"))
@app.param(Int(key="factor", default=5))
@app.output(Folder(key="outputData"))
def SPDenoise(context):
    args = context.args

    VideoEd.denoise_image_sequence(
        args.inputData, args.outputData, ext=args.ext, factor=args.factor
    )

    return args.outputData


if __name__ == "__main__":
    SPDenoise()
