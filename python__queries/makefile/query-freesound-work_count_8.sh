#!/bin/bash
cd /Users/emiliano/Documents/PureData/Envion-Algo-Score

python3 python__queries/make_raw_list.py \
  --url "https://www.peamarte.it/freesound_get.php?q=metal,glass,wood,plastic,paper,stone,ceramic,sand,gravel,wire,impact,friction,object&max_dur=12&mode=raw" \
  --count 8 \
  --out-dir "/Users/emiliano/Documents/PureData/Envion-Algo-Score/netsound" \
  --history "/Users/emiliano/Documents/PureData/Envion-Algo-Score/netsound/netsound_history.txt" \
  --dedupe \
  --insecure
