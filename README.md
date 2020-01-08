## Documents for Google Cloud Speech
- https://cloud.google.com/speech-to-text/docs/async-recognize



## How to use?
- Set up Google Cloud API and SDKs
- Convert mp3 to flac via ffmpeg
```
$ ./mp3_to_flac.sh <mp3 file path>
```
- Upload your mp3 file to Google Cloud Storage
- Call Cloud Speech-to-Text API
```
$ python transcribe_gcs.py <gcs_uri>
```
