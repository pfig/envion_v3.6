#!/usr/bin/env python3
import os
import argparse
import subprocess
import tempfile
import random
import requests
import soundfile as sf
import shutil

# ===========================
# ARCHIVE CONFIG
# ===========================
ARCHIVE_SEARCH_URL = "https://archive.org/advancedsearch.php"

DEFAULT_KEYWORDS = [
    "click", "field recording", "metal clang", "strike", "metal hit",
    "wood strike", "glass tap", "plastic click", "small impact",
    "key press", "stone tap", "water drop", "pinch", "snap",
    "short sound", "micro sound", "concrete sound", "found sound"
]

COUNTER_FILENAME = ".envion_counter"
HISTORY_FILENAME = ".envion_history"

# ===========================
# ARCHIVE FUNCTIONS
# ===========================
def search_archive(keyword, rows=50):
    # Query generica: qualsiasi audio, escluse parole chiave "sermon" e "podcast"
    query = f'("{keyword}") AND mediatype:(audio) AND NOT collection:(sermon OR podcast)'
    params = {"q": query, "fl[]": "identifier", "rows": rows, "output": "json"}
    r = requests.get(ARCHIVE_SEARCH_URL, params=params, timeout=30)
    r.raise_for_status()
    docs = r.json().get("response", {}).get("docs", [])
    return [d["identifier"] for d in docs]

def pick_random_audio_file(identifier):
    meta_url = f"https://archive.org/metadata/{identifier}"
    r = requests.get(meta_url, timeout=30)
    r.raise_for_status()
    files = r.json().get("files", [])
    audio_files = [f["name"] for f in files if f.get("format","").lower() in ("mp3","wav","flac","ogg")]
    if not audio_files:
        return None
    return f"https://archive.org/download/{identifier}/{random.choice(audio_files)}"

# ===========================
# GENERIC FUNCTIONS
# ===========================
def download_file(url, tmpdir):
    filename = os.path.join(tmpdir, "source.wav")
    cmd = ["curl", "-L", "-s", "-o", filename, url]
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("Download failed:", url)
        return None
    return filename

def read_duration(input_file):
    try:
        f = sf.SoundFile(input_file)
        duration = f.frames / f.samplerate
        f.close()
        return duration
    except Exception:
        return None

def format_envion_name(global_index, run_index):
    return f"{run_index:02d}_envion_{global_index}.wav"

def load_counter(outdir):
    path = os.path.join(outdir, COUNTER_FILENAME)
    if os.path.exists(path):
        try:
            with open(path, "r") as fh:
                return int(fh.read().strip())
        except:
            pass
    return 1

def save_counter(outdir, index):
    path = os.path.join(outdir, COUNTER_FILENAME)
    with open(path, "w") as fh:
        fh.write(str(index))

def load_history(outdir):
    path = os.path.join(outdir, HISTORY_FILENAME)
    if os.path.exists(path):
        with open(path, "r") as fh:
            return set(line.strip() for line in fh if line.strip())
    return set()

def save_history(outdir, identifiers):
    path = os.path.join(outdir, HISTORY_FILENAME)
    with open(path, "a") as fh:
        for ident in identifiers:
            fh.write(ident + "\n")

def slice_audio_and_write(input_file, outdir, start, dur, global_index, run_index):
    outname = format_envion_name(global_index, run_index)
    outfile = os.path.join(outdir, outname)
    cmd = [
        "ffmpeg", "-y",
        "-i", input_file,
        "-ss", str(start),
        "-t", str(dur),
        "-ar", "48000",
        outfile
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return outfile

def cleanup_outdir(outdir):
    if os.path.exists(outdir):
        for f in os.listdir(outdir):
            path = os.path.join(outdir, f)
            if os.path.isfile(path):
                if f not in [COUNTER_FILENAME, HISTORY_FILENAME]:
                    os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
    else:
        os.makedirs(outdir)

# ===========================
# MAIN
# ===========================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument("--keywords", nargs="+", default=DEFAULT_KEYWORDS)
    parser.add_argument("--out", default="./micro")
    parser.add_argument("--files-per-run", type=int, default=8)
    parser.add_argument("--slices-per-file", type=int, default=1)
    parser.add_argument("--persist-counter", action="store_true")
    args = parser.parse_args()

    cleanup_outdir(args.out)
    current_index = load_counter(args.out)
    history = load_history(args.out)
    tmpdir = tempfile.mkdtemp()
    files_found = 0
    new_history = set()

    if args.fetch:
        while files_found < args.files_per_run:
            kw = random.choice(args.keywords)
            try:
                ids = search_archive(kw, rows=50)
            except Exception as e:
                print("Archive.org search error:", e)
                continue
            if not ids:
                continue
            random.shuffle(ids)
            for identifier in ids:
                if files_found >= args.files_per_run:
                    break
                if identifier in history:
                    continue
                file_url = pick_random_audio_file(identifier)
                if not file_url:
                    continue
                print(f"Downloading: {file_url}")
                infile = download_file(file_url, tmpdir)
                if not infile:
                    continue
                duration = read_duration(infile) or 10.0
                dur = round(random.uniform(0.05, 0.8), 3)
                start = 0.0 if duration <= dur else round(random.uniform(0, max(0.0, duration - dur)),3)
                slice_audio_and_write(infile, args.out, start, dur, current_index, files_found + 1)
                current_index += 1
                files_found += 1
                new_history.add(identifier)
               if files_found >= args.files_per_run:

                    break

    save_history(args.out, new_history)
    if args.persist_counter:
        save_counter(args.out, current_index)
    else:
        save_counter(args.out, current_index)

    print(f"Done. {files_found} microfile(s) processed. Microfiles saved in: {args.out}")
    print(f"Next envion index will be: {current_index}")

if __name__ == "__main__":
    main()
