FROM python:3.9-slim

# Install FFmpeg
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["bash"]