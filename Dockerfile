FROM python:3.9.0-buster

ENV WORKDIR="/opt/app"
WORKDIR ${WORKDIR}
COPY . ${WORKDIR}

ENV LINE_CHANNEL_ACCESS_TOKEN=0
ENV LINE_CHANNEL_SECRET=0
RUN make init