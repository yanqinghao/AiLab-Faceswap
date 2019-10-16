# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.app.arguments import String
from suanpan.app import app
from suanpan.storage import storage


@app.output(String(key="outputData"))
def SPConvertSync(context):
    args = context.args
    storage.upload(args.modelDir, "/sp_data/" + args.outputData)

    return "/sp_data/" + args.outputData


if __name__ == "__main__":
    SPConvertSync()
