NAMESPACE=("shuzhi-amd64")
for i in ${NAMESPACE[*]}
do
    sed -i "s/cpu/nvidia/g" ./config/.faceswap
    docker build --build-arg NAME_SPACE=${i} -t registry-vpc.cn-shanghai.aliyuncs.com/${i}/facelab-docker-gpu:$1 -f docker/docker_faceswap_gpu/Dockerfile .
    sed -i "s/nvidia/cpu/g" ./config/.faceswap
    docker build --build-arg NAME_SPACE=${i} -t registry-vpc.cn-shanghai.aliyuncs.com/${i}/facelab-docker:$1 -f docker/docker_faceswap/Dockerfile .


    docker push registry-vpc.cn-shanghai.aliyuncs.com/${i}/facelab-docker:$1
    docker push registry-vpc.cn-shanghai.aliyuncs.com/${i}/facelab-docker-gpu:$1
done