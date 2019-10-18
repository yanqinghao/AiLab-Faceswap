# coding=utf-8
from __future__ import absolute_import, print_function

import os
from suanpan.app import app
from suanpan.docker.arguments import Folder, String
from suanpan.storage import StorageProxy


@app.param(String(key="storageType", default="oss"))
@app.param(String(key="folder", default="man_1", help="girl_0  man_0 girl_1 man_1"))
@app.output(Folder(key="outputData"))
def SPMaterial(context):
    args = context.args

    storage = StorageProxy(None, None)
    storage.setBackend(type=args.storageType)

    storage.download(
        os.path.join("common/data/facelab_material", args.folder, "data.mp4"),
        os.path.join(args.outputData, "data.mp4"),
    )

    return args.outputData


if __name__ == "__main__":
    SPMaterial()  # pylint: disable=no-value-for-parameter
