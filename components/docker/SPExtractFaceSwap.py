# coding=utf-8
from __future__ import absolute_import, print_function

import os
from suanpan.app.arguments import Folder, String, Int, Float
from suanpan.app import app
from lib import cli


@app.input(Folder(key="inputData"))
@app.param(String(key="detector", default="cv2-dnn", help="cv2-dnn mtcnn s3fd"))
@app.param(String(key="aligner", default="cv2-dnn", help="cv2-dnn fan"))
@app.param(String(key="normalization", default="none", help="none clahe hist mean"))
@app.param(Int(key="minSize", default=0, help="(0, 1080)"))
@app.param(Float(key="blurThreshold", default=0.0, help="(0.0, 100.0)"))
@app.output(Folder(key="outputData1"))
@app.output(Folder(key="outputData2"))
def SPExtractFace(context):
    args = context.args

    PARSER = cli.FullHelpArgumentParser()
    EXTRACT = cli.ExtractArgs(PARSER, "extract", "Extract the faces from pictures")

    ARGUMENTS = PARSER.parse_args(
        [
            "--input-dir",
            args.inputData,
            "--output-dir",
            args.outputData1,
            "--alignments",
            os.path.join(args.outputData2, "alignments.json"),
            "--detector",
            args.detector,
            "--aligner",
            args.aligner,
            "--normalization",
            args.normalization,
            "--min-size",
            str(args.minSize),
            "--blur-threshold",
            str(args.blurThreshold),
        ]
    )
    ARGUMENTS.func(ARGUMENTS)

    return args.outputData1, args.outputData2


if __name__ == "__main__":
    SPExtractFace()
