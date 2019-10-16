# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.app.arguments import Folder
from suanpan.app import app


@app.output(Folder(key="outputData"))
def SPConvertSync(context):
    args = context.args

    return args.outputData


if __name__ == "__main__":
    SPConvertSync()
