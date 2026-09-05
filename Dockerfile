FROM python:3.13-slim-trixie AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install \
    --no-cache-dir \
    --prefix=/install \
    -r requirements.txt


FROM python:3.13-slim-trixie AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN groupadd --system --gid 10001 sentinel \
    && useradd \
        --system \
        --uid 10001 \
        --gid sentinel \
        --no-create-home \
        sentinel    

WORKDIR /app

COPY --from=builder /install /usr/local
COPY --chown=sentinel:sentinel app ./app

USER sentinel

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]