# coding=utf-8
from __future__ import absolute_import, print_function

import os
from suanpan.app.arguments import String
from suanpan.app import app
from suanpan.storage import storage


@app.output(String(key="outputData"))
def SPConvertSync(context):
    args = context.args
    path = os.path.split(str(args.outputData))[0]

    storage.upload(path.replace("/sp_data/", ""), path)

    return "Images Saved..."


if __name__ == "__main__":
    SPConvertSync()

