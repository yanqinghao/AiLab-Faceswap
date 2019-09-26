# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.app.arguments import Folder, String, Int
from suanpan.app import app
from mainscripts import VideoEd
from utils import get_all_files


@app.input(Folder(key="inputData"))
@app.param(String(key="fromTime", default="00:00:00.000"))
@app.param(String(key="toTime", default="00:00:01.000"))
@app.param(Int(key="audioTrackId", default=0))
@app.param(Int(key="bitrate", default=25))
@app.output(Folder(key="outputData"))
def SPCutVideo(context):
    args = context.args

    fileList = get_all_files(args.inputData)

    VideoEd.cut_video(
        fileList[0],
        args.outputData,
        args.fromTime,
        args.toTime,
        args.audioTrackId,
        args.bitrate,
    )

    return args.outputData


if __name__ == "__main__":
    SPCutVideo()
