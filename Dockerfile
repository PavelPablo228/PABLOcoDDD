FROM python:3.13-slim

WORKDIR /
COPY requirements.txt uv.lock ./
RUN pip install uv --no-cache-dir
RUN uv pip install --no-cache-dir --system --strict -r requirements.txt

COPY . .

CMD ["sh","entrypoint.sh" ]
