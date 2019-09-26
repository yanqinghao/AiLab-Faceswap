# coding=utf-8
from __future__ import absolute_import, print_function

import os
from suanpan.app.arguments import Folder, String, Int, Bool
from suanpan.app import app
from mainscripts import VideoEd
from utils import get_all_files


@app.input(Folder(key="inputData"))
@app.input(Folder(key="referenceFolder"))
@app.param(String(key="fileName", default="media.mp4"))
@app.param(String(key="ext", default="png", help="jpg png"))
@app.param(Int(key="fps", default=25))
@app.param(Int(key="bitrate", default=16))
@app.param(Bool(key="lossless", default=False))
@app.output(Folder(key="outputData"))
def SPVideoFromSequence(context):
    args = context.args
    if args.referenceFolder:
        referenceFile = get_all_files(args.referenceFolder)

    VideoEd.video_from_sequence(
        args.inputData,
        os.path.join(args.outputData, args.fileName),
        referenceFile[0],
        args.ext,
        args.fps,
        args.bitrate,
        args.lossless,
    )

    return args.outputData


if __name__ == "__main__":
    SPVideoFromSequence()
