#!/bin/bash

EDIT_MODE=false

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    --__edit)
    EDIT_MODE=true
    shift # past argument
    shift # past value
    ;;
    *)    # unknown option
    POSITIONAL+=("$1") # save it in an array for later
    shift # past argument
    ;;
esac
done

if [ $EDIT_MODE == true ]
then
    echo "Edit Mode"
    cp /yanqing/train.sh /workspace/run.sh
    chmod +x /workspace/run.sh
    cp /yanqing/train_save.sh /workspace/save.sh
    chmod +x /workspace/save.sh
    jupyter notebook --NotebookApp.port=8888 --NotebookApp.password_required=False --NotebookApp.base_url=/proxy/${SP_USER_ID}/${SP_APP_ID}/${SP_NODE_ID}/8888/ --NotebookApp.open_browser=False --NotebookApp.ip=0.0.0.0 --NotebookApp.token='' --NotebookApp.notebook_dir=${PWD} --allow-root
else
    echo "Run Mode"
    bash -c "${SP_DISTRIBUTED_CMD} python /yanqing/run.py components.docker.SPTrainLab.SPTrainLab"
fi
