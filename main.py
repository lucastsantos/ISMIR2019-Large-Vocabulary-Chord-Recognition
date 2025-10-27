from pathlib import Path
from chord_recognition import chord_recognition 

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Perform chord recognition on a directory of audio files.")
    parser.add_argument('input_dir', type=str, help='Path to input directory of audio files.')
    args = parser.parse_args()

    audio_files = []
    audio_extensions = ['*.mp3', '*.wav', '*.flac', '*.ogg', '*.m4a', '*.aac', '*.wma']
    for ext in audio_extensions:
        audio_files.extend(Path(args.input_dir).rglob(ext))

    for audio_file in audio_files:
        output_file = audio_file.with_suffix('.lab')
        chord_recognition(audio_file, output_file)
        print(f"Performed chord recognition on {audio_file} and saved to {output_file}")