import subprocess
import shlex


def run_ffprobe(url):
    command = f"ffprobe {url}"
    process = subprocess.run(shlex.split(
        command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if process.returncode != 0:
        print(f"Error running ffprobe: {process.stderr.decode()}")
        return False

    return "Subtitle" in process.stderr.decode()


def run_ffmpeg(url, output_file):
    command = f'ffmpeg -i "{url}" -map 0:s:0 "{output_file}.srt"'
    process = subprocess.run(shlex.split(
        command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if process.returncode != 0:
        print(f"Error running ffmpeg: {process.stderr.decode()}")
        return False

    return True


def run_removeSubtitleData(output_file):
    command = f'python3 removeSubtitleData.py "{output_file}.srt" "{output_file}.txt"'
    process = subprocess.run(shlex.split(
        command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if process.returncode != 0:
        print(
            f"Error running removeSubtitleData.py: {process.stderr.decode()}")
        return False

    print(
        f"Metadata scrubbed successfully. File viewable at: {output_file}.srt and {output_file}.txt")
    return True


def main():
    url = input("Enter URL: ")
    output_file = input("Enter output file name: ")

    if run_ffprobe(url):
        print("Subtitle detected. Running ffmpeg...")
        if run_ffmpeg(url, output_file):
            if input("Scrub subtitle metadata? (y/n): ").lower() == 'y':
                if not run_removeSubtitleData(output_file):
                    print("Failed to scrub subtitle metadata.")
            else:
                print("Skipping subtitle metadata scrubbing.")
        else:
            print("Failed to extract subtitle with ffmpeg.")
    else:
        print("No subtitle detected.")


if __name__ == "__main__":
    main()
