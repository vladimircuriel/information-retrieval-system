FROM python:3.13-slim

WORKDIR /app
ENV PIP_ROOT_USER_ACTION=ignore
ENV PYTHONPATH=/app/src

COPY pyproject.toml poetry.lock .python-version LICENSE ./

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

RUN python -m nltk.downloader -d /usr/local/nltk_data stopwords punkt wordnet averaged_perceptron_tagger

COPY src ./src

# cd /src/app && streamlit run src/app/main.py
EXPOSE 8501

CMD ["streamlit", "run", "src/app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]