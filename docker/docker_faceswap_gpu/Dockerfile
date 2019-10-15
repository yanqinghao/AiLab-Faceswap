ARG PYTHON_VERSION=3.7

FROM registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/horovod_docker_base:${PYTHON_VERSION} as builder

ENV PYPI_MIRROR "https://mirrors.aliyun.com/pypi/simple"

RUN pip config set global.index-url ${PYPI_MIRROR}

RUN pip install --upgrade pip

RUN pip install --no-cache-dir pyarmor

WORKDIR /build

COPY . /build

RUN bash tools/compress.sh

FROM registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/horovod_docker_base:${PYTHON_VERSION}

WORKDIR /yanqing

ENV PYPI_MIRROR "https://mirrors.aliyun.com/pypi/simple"

ENV PYTHONIOENCODING "utf-8"

ENV LANG "zh_CN.UTF-8"

RUN pip config set global.index-url ${PYPI_MIRROR}

RUN pip install --upgrade pip

RUN add-apt-repository -y ppa:jonathonf/ffmpeg-4 && apt-get update

RUN apt-get install ffmpeg -y && apt-get install -y language-pack-zh-hans dumb-init && apt-get clean

RUN pip install --no-cache-dir jupyter jupyter_contrib_nbextensions jupyter_nbextensions_configurator yapf tornado==5.1.1 \
 && jupyter contrib nbextension install --user \
 && jupyter nbextensions_configurator enable --user \
 && jupyter nbextension enable code_prettify/code_prettify \
 && jupyter nbextension enable hinterland/hinterland

COPY --from=builder /build /yanqing

COPY docker/python/common/notebook/configs /etc/jupyter

RUN pip install -r requirements_gpu.txt

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/usr/bin/dumb-init", "--" ]

CMD [ "jupyter", "notebook" ]
