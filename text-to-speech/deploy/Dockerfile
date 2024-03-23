FROM daswer123/xtts-api-server

ARG HOST_MODEL_FOLDER="/model"
ARG HOST_SPEAKERS_FOLDER="/speakers"

ENV MODEL_VERSION="custom_model"
ENV DEEPSPEED="true"
ENV USE_CACHE="true"

COPY ${HOST_MODEL_FOLDER} /app/xtts_models/custom_model
COPY ${HOST_SPEAKERS_FOLDER} /app/speakers

CMD ["/bin/sh", "-c", "echo \"y\" | python3 -m xtts_api_server -hs 0.0.0.0  -v ${MODEL_VERSION} -t \"http://localhost:8020\""]