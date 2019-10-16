# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.app.arguments import Folder
from suanpan.app import app


@app.output(Folder(key="modelDir"))
def SPTrainSync(context):
    args = context.args

    return args.modelDir


if __name__ == "__main__":
    SPTrainSync()
