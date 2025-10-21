#!/usr/bin/env python3
import os
import argparse
import subprocess
import tempfile
import random
import requests
import soundfile as sf

# ===========================
# CONFIG FREESOUND
# ===========================
FREESOUND_API_KEY = "NrNpk3OUT2DMJ27S07XO7sycwBPHwesUgE5iPQUA"
FREESOUND_SEARCH_URL = "https://freesound.org/apiv2/search/text/"

DEFAULT_KEYWORDS = [
    "click", "field recording", "metal clang", "strike", "metal hit",
    "wood strike", "glass tap", "plastic click", "small impact",
    "key press", "stone tap", "water drop", "pinch", "snap",
    "sound effect", "shortwave", "ambient", "concrete", "percussion",
    "industrial", "micro sound", "metal hit short", "tiny impact",
    "experimental noise", "found sound", "mechanical click", "tap"
]

COUNTER_FILENAME = ".envion_counter"
HISTORY_FILENAME = ".envion_history"

# ===========================
# FREESOUND FUNCTIONS
# ===========================
def search_freesound(keyword, page_size=50):
    headers = {"Authorization": f"Token {FREESOUND_API_KEY}"}
    params = {
        "query": keyword,
        "fields": "id,previews,name,duration",
        "page_size": page_size,
        "filter": "duration:[0.1 TO 60.0]"
    }
    r = requests.get(FREESOUND_SEARCH_URL, headers=headers, params=params, timeout=30)
    r.raise_for_status()
    results = r.json().get("results", [])
    urls = []
    for sample in results:
        preview_url = sample.get("previews", {}).get("preview-hq-mp3")
        if preview_url:
            urls.append(preview_url)
    return urls

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

def format_envion_name(index):
    return f"envion_{index:04d}.wav"

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

def slice_audio_and_write(input_file, outdir, start, dur, envion_index):
    outname = format_envion_name(envion_index)
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
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    else:
        for f in os.listdir(outdir):
            path = os.path.join(outdir, f)
            if os.path.isfile(path) and f not in [COUNTER_FILENAME, HISTORY_FILENAME]:
                os.remove(path)

# ===========================
# MAIN
# ===========================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument("--keywords", nargs="+", default=DEFAULT_KEYWORDS)
    parser.add_argument("--out", default="./micro")
    parser.add_argument("--files-per-run", type=int, default=8)  # massimo 8 microfile totali
    parser.add_argument("--slices-per-file", type=int, default=1)  # 1 slice per file = massimo 8 microfile
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
                urls = search_freesound(kw, page_size=50)
            except Exception as e:
                print("Freesound search error:", e)
                continue
            if not urls:
                continue
            file_url = random.choice(urls)
            if file_url in history:
                continue
            print(f"Downloading: {file_url}")
            infile = download_file(file_url, tmpdir)
            if not infile:
                continue
            duration = read_duration(infile) or 10.0
            dur = round(random.uniform(0.05, 0.8), 3)
            start = 0.0 if duration <= dur else round(random.uniform(0, max(0.0, duration - dur)),3)
            slice_audio_and_write(infile, args.out, start, dur, current_index)
            current_index += 1
            files_found += 1
            new_history.add(file_url)

    save_history(args.out, new_history)
    if args.persist_counter:
        save_counter(args.out, current_index)
    else:
        save_counter(args.out, current_index)

    print(f"Done. {files_found} microfile(s) processed. Microfiles saved in: {args.out}")
    print(f"Next envion index will be: {current_index}")

if __name__ == "__main__":
    main()
