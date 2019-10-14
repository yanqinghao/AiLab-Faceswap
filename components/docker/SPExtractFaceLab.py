# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.app.arguments import Folder, String, Bool
from suanpan.app import app
from mainscripts import Extractor


@app.input(Folder(key="inputData"))
@app.param(
    String(
        key="faceType",
        default="full_face",
        help="['half_face', 'full_face', 'head', 'full_face_no_align', 'mark_only']",
    )
)
@app.param(String(key="detector", default="s3fd", help="['dlib','mt','s3fd']"))
@app.param(Bool(key="multiGpu", default=False))
@app.param(Bool(key="cpuOnly", default=False))
@app.output(Folder(key="outputData"))
def SPExtractFaceLab(context):
    args = context.args

    Extractor.main(
        args.inputData,
        args.outputData,
        debug_dir=None,
        detector=args.detector,
        manual_fix=False,
        manual_output_debug_fix=False,
        manual_window_size=1368,
        image_size=256,
        face_type=args.faceType,
        device_args={"cpu_only": args.cpuOnly, "multi_gpu": args.multiGpu},
    )

    return args.outputData


if __name__ == "__main__":
    SPExtractFaceLab()
