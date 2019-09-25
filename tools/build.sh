docker build -t registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/pytorch-docker-gpu:$1 -f docker/docker_yanqing_gpu/Dockerfile .
sed -i "s/cpu/cu100/g" .dockerignore
docker build -t registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/pytorch-docker:$1 -f docker/docker_yanqing/Dockerfile .
sed -i "s/cu100/cpu/g" .dockerignore

docker push registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/pytorch-docker:$1
docker push registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/pytorch-docker-gpu:$1