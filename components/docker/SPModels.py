# coding=utf-8
from __future__ import absolute_import, print_function

import os
from suanpan.app import app
from suanpan.docker.arguments import Folder, String
from suanpan.storage import StorageProxy


@app.param(String(key="storageType", default="oss"))
@app.param(
    String(key="folder", default="man_face_25k", help="girl_face_50k  man_face_25k")
)
@app.output(Folder(key="modelDir"))
def SPModels(context):
    args = context.args

    storage = StorageProxy(None, None)
    storage.setBackend(type=args.storageType)

    storage.download(os.path.join("common/model/facelab", args.folder), args.modelDir)

    return args.modelDir


if __name__ == "__main__":
    SPModels()  # pylint: disable=no-value-for-parameter
