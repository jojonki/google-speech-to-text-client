import sys
import pickle
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def save_pickle(d, path):
    print('save pickle to', path)
    with open(path, mode='wb') as f:
        pickle.dump(d, f)


def load_pickle(path):
    print('load', path)
    with open(path, mode='rb') as f:
        return pickle.load(f)


def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    if not gcs_uri:
        print('You need to specify Google Cloud Storage URL for your audio file')
        return
    print('Transcribe', gcs_uri)
    audio_file_name = gcs_uri.split('/')[-1]
    if not audio_file_name:
        audio_file_name = 'out'
    audio_file_name = audio_file_name.replace('.flac', '')
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = operation.result(timeout=36000)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    # save_pickle(response.results, './results/' + audio_file_name + '.pkl')
    lines = []
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        lines.append(result.alternatives[0].transcript)
        print(u'Transcript: {}'.format(lines[-1]))
        print('Confidence: {}'.format(result.alternatives[0].confidence))

    if lines:
        fout_file = './results/' + audio_file_name + '.txt'
        print('Write', fout_file)
        with open(fout_file, 'w') as fout:
            fout.write('\n'.join(lines))


if __name__ == '__main__':
    transcribe_gcs(sys.argv[1])
