# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.app.arguments import String
from suanpan.app import app
from suanpan.storage import storage


@app.output(String(key="modelDir"))
def SPTrainSync(context):
    args = context.args
    storage.upload(args.modelDir, "/sp_data/" + args.modelDir)

    return "/sp_data/" + args.modelDir


if __name__ == "__main__":
    SPTrainSync()
