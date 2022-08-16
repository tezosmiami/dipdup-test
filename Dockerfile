FROM dipdup/dipdup:6.0

COPY pyproject.toml poetry.lock ./
# Uncomment the following line if you have dependencies other than dipdup in pyproject.toml
# RUN inject_pyproject

COPY src/dipdup_test dipdup_test
