sed -i "s/cpu/nvidia/g" ./config/.faceswap
docker build -t registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/facelab-docker-gpu:$1 -f docker/docker_yanqing_gpu/Dockerfile .
sed -i "s/nvidia/cpu/g" ./config/.faceswap
docker build -t registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/facelab-docker:$1 -f docker/docker_yanqing/Dockerfile .


docker push registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/facelab-docker:$1
docker push registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/facelab-docker-gpu:$1