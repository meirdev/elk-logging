FROM --platform=arm64 python:3.11.2-buster

# add poetry to path
ENV POETRY_HOME=/opt/poetry
ENV PATH=$POETRY_HOME/bin:$PATH

# install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false

# install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

WORKDIR /app

ENTRYPOINT [ "python", "main.py" ]
