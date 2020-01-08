#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Specify a mp3 file which you want to convert into flac." 1>&2
  exit 1
fi


MP3_FILE=$1

FLAC_FILE="$(echo $MP3_FILE | sed 's/.mp3/.flac/')"

echo "ffmpeg -i $MP3_FILE -vn -ar 16000 -ac 1 -acodec flac -f flac $FLAC_FILE"
ffmpeg -i $MP3_FILE -vn -ar 16000 -ac 1 -acodec flac -f flac $FLAC_FILE
