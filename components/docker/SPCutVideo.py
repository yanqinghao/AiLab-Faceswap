# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.app.arguments import Folder, String, File, Int
from suanpan.log import logger
from suanpan.app import app
from mainscripts import VideoEd


@app.input(File(key="inputData"))
@app.param(String(key="fromTime", default="00:00:00.000"))
@app.param(String(key="toTime", default="00:00:01.000"))
@app.param(Int(key="audioTrackId", default=0))
@app.param(Int(key="bitrate", default=25))
@app.output(Folder(key="outputData"))
def SPCutVideo(context):
    args = context.args

    VideoEd.cut_video(
        args.inputData, args.fromTime, args.toTime, args.audioTrackId, args.bitrate
    )
    
    return args.inputData


if __name__ == "__main__":
    SPCutVideo()
