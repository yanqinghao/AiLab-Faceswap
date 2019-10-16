# coding=utf-8
from __future__ import absolute_import, print_function

import os
from suanpan.app.arguments import String
from suanpan.app import app
from suanpan.storage import storage


@app.output(String(key="modelDir"))
def SPTrainSync(context):
    args = context.args
    path = os.path.split(str(args.modelDir))[0]

    storage.upload(path.replace("/sp_data/", ""), path)

    return "Model Saved..."


if __name__ == "__main__":
    SPTrainSync()
