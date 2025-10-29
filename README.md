<img src="https://www.peamarte.it/env/html-guide/img/logo_circle_60x60_readme.png" width="100" height="100" style="vertical-align: middle; margin-bottom: -20px;">

# Envion  
Algorithmic Dynatext Envelope Sequencer for **Pure Data (PlugData & iPadOS)**  
by **Emiliano Pennisi** — 2025

---

**Documentation & Tutorials:**  
[https://www.peamarte.it/env/envion_v3.6.html](https://www.peamarte.it/env/envion_v3.6.html)  
Please visit the website for the complete usage guide, module reference, and setup details.

---

## Overview

Envion is an envelope-first ecosystem for algorithmic and procedural composition in Pure Data (Pd).  
It redefines sampling as a gesture-based process: thousands of dynamic envelopes ("Dynatext triplets") continuously sculpt micro-events and temporal shapes.

The Net-Audio submodule fetches random sound atoms from online archives (Internet Archive, Wikimedia Commons, Freesound), transforming contingent data into acousmatic gestures.

Envion is open-source, compatible with PlugData on macOS, Windows, and iPadOS, and released under the MIT License (with Attribution).

---

## Requirements

- PlugData (includes `cyclone` and `else`)
- Mandatory Libraries:  
  - `ggee`  
  - `audiolab`  
- Optional Libraries:  
  - `ceammc`  
  - `simplex` (for 3D visualization)

---

## Quick Setup

Open `Envion_v4.5_Plugdata.pd` in PlugData to play presets, tweak behavior, and load new samples.

---

Before you start — Envion is not a single .pd file
Envion will not work if you only download the Envion_v5.1_Plugdata.pd file. The patch depends on its full folder structure (libs, core, utils, netsound, data etc.). You must download the entire repository.
Correct installation (desktop)

Download the full repository ZIP
https://github.com/aveniridm/envion/archive/refs/heads/main.zip
Unzip it — this creates a folder such as envion-main/
Do not move the .pd patch out of this folder
Open Envion_v5.1_Plugdata.pd from inside that same folder
envion-main/
   ├── Envion_v5.1_Plugdata.pd
   ├── /core
   ├── /libs
   ├── /netsound
   ├── /utils
   ├── /data
   └── /audio
When the patch is outside its directory tree, PlugData cannot resolve its abstractions and support files — resulting in silent loading or missing modules. Keeping the folder intact ensures everything loads correctly.
Once the dependencies are installed, you can simply turn on the DSP and load the first preset, as shown in the image.

Envion may look complex at first glance, but it’s actually very easy to start making sound. You don’t need to understand every module right away — just activate the DSP and try one of the included presets.
Start with the main master preset, conveniently located to the right of the DSP activation (the large bang button)
Local presets on the right
Network-based presets on the left (fetching sounds directly from the web)
Ability to load your own samples into any preset
Take your time to explore the deeper functions later — for now, focus on playing, listening, and discovering how Envion responds. Exploration is part of the philosophy, but sound comes instantly once you start.


## iPadOS/iOS Compatibility

PlugData for iPadOS/iOS includes core libraries.  
Optional libraries (ggee, ceammc, simplex, audiolab) add extra features but are not required for basic functionality.

If dependency warnings appear, they refer to optional libraries.  
The patch remains operational without them, except for features such as 3D scope visualization.

### Net-Audio module on iPadOS/iOS

**Important:**  
The Net-Audio module is **not functional on iPadOS** as of this release.  
Due to current limitations in PlugData for iPadOS/iOS, URL-based loading and fetching are not supported.  
As a result, the Net-Audio module will remain inactive in the iPadOS version until the necessary functionality is implemented upstream.  
A related issue has been opened in the PlugData repository; updates will be provided when support is available.

For detailed instructions and troubleshooting, refer to [IPAD_GUIDE.md](IPAD_GUIDE.md).

---

## Concept

Envion operates by writing trajectories on sound through textual sequences of triplets `(amplitude, duration, offset)` sent to `vline~`.  
Each line of a text file defines a gesture.  
Thousands of these triplets, stored in the `/data` folder, create a reservoir of living envelopes.

---

## Net-Audio Module (desktop only)

Net-Audio extends Envion by automatically fetching sonic material from public archives.  
Python scripts build `.txt` lists of direct URLs, which Envion reads and articulates through its envelope engine.

Module guide: [peamarte.it/env/envion_netaudio.html](https://www.peamarte.it/env/envion_netaudio.html)

---

## Video Playlist

[Envion — YouTube Playlist](https://www.youtube.com/watch?v=JEuB3KBAxeg&list=PLLITukQh1_l61lP6GMfa1Hz4Db7_wrTTT)

---

## License

Envion is released under the MIT License with Attribution.  
You are free to use, modify, and redistribute this project, including for commercial purposes, as long as you credit Envion and Emiliano Pennisi.  
See the [LICENSE](LICENSE) file for details.

---

## Links

- Website: [peamarte.it/env/envion_v3.6.html](https://www.peamarte.it/env/envion_v3.6.html)
- Portfolio: [http://www.emilianopennisi.it](http://www.emilianopennisi.it)
- YouTube Series: [Envion — Official Playlist](https://www.youtube.com/watch?v=gA-pdHQwibA&list=PLLITukQh1_l61lP6GMfa1Hz4Db7_wrTTT)
- Community: [r/musiconcrete](https://www.reddit.com/r/musiconcrete)
- Contact: [metrostation@gmail.com](mailto:metrostation@gmail.com)

---

Built in Pure Data / PlugData (2024–2025)  
© Emiliano Pennisi

<!--UPDATE_TS_START-->
_Last update: 2025-10-29 09:49 CET_
<!--UPDATE_TS_END-->
=======
<!--UPDATE_TS_END-->
>>>>>>> Stashed changes
=======
_Last update: 2025-10-15 06:37 CEST_
<!--UPDATE_TS_END-->
>>>>>>> Stashed changes
