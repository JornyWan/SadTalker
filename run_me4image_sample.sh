#!/bin/bash

# Directory containing the WAV files
WAV_DIR="./voice"

# Source image path
SOURCE_IMAGE="overwatch.png"

# Loop through each WAV file in the directory
for wav_file in "$WAV_DIR"/*.wav; do
    echo "Processing file: $wav_file"
    python inference.py --driven_audio "$wav_file" --source_image "$SOURCE_IMAGE" --enhancer gfpgan
done

