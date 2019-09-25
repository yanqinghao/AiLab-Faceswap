ARG PYTHON_VERSION=3.7

FROM registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/docker_base:${PYTHON_VERSION} as builder

ENV PYPI_MIRROR "https://mirrors.aliyun.com/pypi/simple"

RUN pip config set global.index-url ${PYPI_MIRROR}

RUN pip install --upgrade pip

RUN pip install --no-cache-dir pyarmor

WORKDIR /build

COPY . /build

RUN bash tools/compress.sh

FROM registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/docker_base:${PYTHON_VERSION}

WORKDIR /yanqing

ENV PYPI_MIRROR "https://mirrors.aliyun.com/pypi/simple"

RUN pip config set global.index-url ${PYPI_MIRROR}

RUN pip install --upgrade pip

RUN add-apt-repository ppa:jonathonf/ffmpeg-4 && apt-get update

RUN apt-get install ffmpeg -y

COPY --from=builder /build /yanqing

RUN pip install -r requirements.txt

ENTRYPOINT [ "/sbin/my_init", "--" ]

CMD [ "bash" ]
