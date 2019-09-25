# coding=utf-8
from __future__ import absolute_import, print_function

import torch
import pickle
import torch.nn as nn

from suanpan.components import Result
from suanpan.storage.arguments import File
from suanpan.storage.arguments import Folder

class MediaFile(File):
    FILENAME = "media"
    FILETYPE = None