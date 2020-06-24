FROM python:3

WORKDIR /usr/src/app

# install libraries
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# add files (実際必要なのは bot.pyだけだから、これだけ渡す)
COPY bot.py .
CMD ["python", "./bot.py"]