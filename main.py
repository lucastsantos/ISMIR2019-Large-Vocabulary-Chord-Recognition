from pathlib import Path
from chord_recognition import chord_recognition 

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Perform chord recognition on a directory of audio files.")
    parser.add_argument('input_dir', type=str, help='Path to input directory of audio files.')
    args = parser.parse_args()

    audio_files = Path(args.input_dir).rglob('*.mp3')
    for audio_file in audio_files:
        output_file = audio_file.with_suffix('.lab2')
        chord_recognition(audio_file, output_file)
        print(f"Performed chord recognition on {audio_file} and saved to {output_file}")