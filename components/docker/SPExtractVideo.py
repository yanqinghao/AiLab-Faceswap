# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.app.arguments import Folder, String, Int
from suanpan.app import app
from mainscripts import VideoEd
from utils import get_all_files


@app.input(Folder(key="inputData"))
@app.param(String(key="outputExt", default="png", help="jpg png"))
@app.param(Int(key="fps", default=0))
@app.output(Folder(key="outputData"))
def SPExtractVideo(context):
    args = context.args

    inputFile = get_all_files(args.inputData)

    VideoEd.extract_video(inputFile[0], args.outputData, args.outputExt, args.fps)

    return args.outputData


if __name__ == "__main__":
    SPExtractVideo()
