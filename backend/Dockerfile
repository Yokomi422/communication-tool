FROM python:3.10

RUN apt-get update &&\
    apt-get -y install locales &&\
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install --upgrade pip

# Poetryのインストール
RUN curl -sSL https://install.python-poetry.org | python -

# Poetryのパスの設定
ENV PATH /root/.local/bin:$PATH

# Poetryが仮想環境を生成しないようにする
RUN poetry config virtualenvs.create false

COPY pyproject.toml /pyproject.toml

RUN poetry add fastapi uvicorn[standard]

# コンテナ実行後に行いたいコマンドを記述する FastAPIの場合の例は下記
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]