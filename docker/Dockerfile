FROM python:3.11-slim

WORKDIR /artifact

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY statistical_analysis/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /artifact
RUN chmod +x scripts/*.sh scripts/*.py || true

CMD ["bash", "scripts/phase3c_ci_verify.sh"]
