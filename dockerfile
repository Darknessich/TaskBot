FROM python:3.10-slim-bullseye AS compile-image
COPY requirements.txt .
RUN apt update && \
    pip install --no-cache -r requirements.txt && \
    pip wheel --no-cache-dir --wheel-dir /opt/pip_wheels -r requirements.txt

FROM python:3.10-slim-bullseye AS run-image
COPY --from=compile-image /opt/pip_wheels /opt/pip_wheels
RUN pip install --no-cache /opt/pip_wheels/* && rm -rf /opt/pip_wheels
COPY . .

CMD ["python", "-m", "bot"]