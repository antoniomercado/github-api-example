FROM python:3.10.5-slim-bullseye as base

# Install dependencies
FROM base as python-deps
RUN  apt-get update \
  && apt-get -y install build-essential libssl-dev git libffi-dev libgfortran5 pkg-config cmake gcc \
  && apt-get clean \
  && pip install --upgrade pip

# Copy dependencies to runtime-image
FROM base as runtime-image
COPY --from=python-deps /usr/local/lib /usr/local/lib

WORKDIR /app
ENV LD_LIBRARY_PATH /usr/local/lib

COPY . /app
RUN pip install -e . --no-cache-dir --no-build-isolation

ENTRYPOINT ["/usr/local/bin/python3","main.py"]
CMD [ "--help" ]