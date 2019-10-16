#!/bin/bash

echo "Edit Mode"
cp /yanqing/train.sh /workspace/run.sh
chmod +x /workspace/run.sh
cp /yanqing/train_save.sh /workspace/save.sh
chmod +x /workspace/save.sh
jupyter notebook --NotebookApp.port=8888 --NotebookApp.password_required=False --NotebookApp.base_url=/proxy/${SP_USER_ID}/${SP_APP_ID}/${SP_NODE_ID}/8888/ --NotebookApp.open_browser=False --NotebookApp.ip=0.0.0.0 --NotebookApp.token='' --NotebookApp.notebook_dir=${PWD} --allow-root

