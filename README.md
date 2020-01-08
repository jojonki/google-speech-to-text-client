## Documents for Google Cloud Speech
- https://cloud.google.com/speech-to-text/docs/async-recognize



## How to use?
- Set up Google Cloud API and SDKs
- Convert mp3 to flac via ffmpeg
```
$ ffmpeg -i small.mp3 -vn -ar 16000 -ac 1 -acodec flac -f flac small.flac
```
- Upload your mp3 file to Google Cloud Storage
- Call Cloud Speech-to-Text API
```
$ python transcribe_gcs.py <gcs_uri>
```
