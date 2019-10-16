#!/bin/bash

set -e

# apt install xxx

# pip install -r requirements.txt

bash -c "${SP_DISTRIBUTED_CMD} python /yanqing/run.py components.docker.SPTrainSync.SPTrainSync $@"