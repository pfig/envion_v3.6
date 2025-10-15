<img src="https://www.peamarte.it/env/html-guide/img/logo_circle_60x60_readme.png" width="100" height="100" style="vertical-align: middle; margin-bottom: -20px;">

# Envion  
Algorithmic Dynatext Envelope Sequencer in **Pure Data (PlugData & iPadOS)**  
by **Emiliano Pennisi** — 2025

![](https://www.peamarte.it/env/html-guide/img/concept-envion.png)

---

> **Full documentation & tutorials**  
> 👉 [https://www.peamarte.it/env/envion_v3.6.html](https://www.peamarte.it/env/envion_v3.6.html)  
> Visit the website for the complete usage guide, module reference, and setup details.

---

## Overview

**Envion** is an *envelope-first* ecosystem for **algorithmic and procedural composition** in Pure Data (Pd).  
It redefines sampling as a **gesture-based process** — thousands of dynamic envelopes (*Dynatext triplets*) continuously sculpt micro-events and temporal shapes.

Through its web-driven submodule **Net-Audio**, Envion fetches random sound atoms from the Internet (Internet Archive, Wikimedia Commons, Freesound) and transforms contingent data into **acousmatic gestures**, **algorithmic textures**, and **and emergent listening structures**.

Envion is open-source, compatible with **PlugData** on macOS, Windows, and iPadOS, and released under the **MIT License (with Attribution)**.

---

> ℹ️ **Envion quick setup**

With **PlugData**, `cyclone` and `else` are already included.  
Mandatory libraries: `ggee`, `audiolab` — for the 3D scope you can (optionally) add: `simplex`.

- `cyclone` — included in PlugData  
- `else` — included in PlugData  
- `ggee`  
- `ceammc`  
- `simplex` — optionally  
- `audiolab`  

**Open:** `Envion_v4.5_Plugdata.pd` → play presets (bottom-right), tweak behavior, load new samples.

---

![Envion Quick Start](https://www.peamarte.it/env/html-guide/img/envion-quick-start.png)  
**Envion Quick Start**


### 📱 **PlugData on iPadOS/iOS**

The core functionality of Envion works out-of-the-box on PlugData for iPadOS/iOS because **cyclone** and **else** libraries are built-in.

If you see dependency warnings when opening the patch on iPadOS:
- These warnings refer to **optional libraries** (ggee, ceammc, simplex, audiolab)
- **You can safely ignore these warnings** — the patch will work without them
- The optional libraries add extra features like 3D scope visualization, but are not required for core functionality
- Currently, installing external libraries on iPadOS/iOS is not supported through PlugData's interface

**What works on iPadOS without additional libraries:**

✅ All envelope seq and dynatext features  
✅ Audio playback and sample manipulation  
✅ All preset functionality  
✅ Recording and real-time processing  
✅ Manual and automatic triggering  

**What requires optional libraries (desktop only):**


⚠️ 3D scope visualization (requires `simplex`)  
⚠️ Some advanced audio processing features (requires `audiolab`, `ceammc`, `ggee`)


### What doesn’t work (yet) on iPadOS

🧩 **Net-Audio** is currently **not functional** on iPadOS.  
A related issue has been opened on the **PlugData repository**, which will eventually allow URL-based loading and fetching functions to work correctly once resolved.  
Until then, the Net-Audio module will remain inactive in the iPadOS version.

📖 **[Read the full iPadOS/iOS guide](IPAD_GUIDE.md)** for detailed instructions and troubleshooting.

## Concept

Instead of triggering samples on a timeline, Envion **writes trajectories on sound** through textual sequences of **triplets**  
`(amplitude, duration, offset)` → sent to `vline~`.

Each line of a text file defines a gesture; switching line means switching gesture.  
Thousands of these triplets, stored in the `/data` folder, create a vast reservoir of *living envelopes*.

> *A single fragment becomes thousands of distinct articulations —  
> sound as motion, not repetition.*


---

## Net-Audio Module

**Net-Audio** extends Envion into the network, automatically fetching unpredictable sonic material from public archives.  
Python scripts build `.txt` lists of direct URLs, which Envion reads and articulates through its envelope engine.  
Each session produces unique textures — embracing randomness as compositional method.

**Module guide:** [peamarte.it/env/envion_netaudio.html](https://www.peamarte.it/env/envion_netaudio.html)

---

## Video Playlist

[**Envion — YouTube Playlist**](https://www.youtube.com/watch?v=JEuB3KBAxeg&list=PLLITukQh1_l61lP6GMfa1Hz4Db7_wrTTT)  
A curated selection of process demos, behind-the-scenes sessions, and live excerpts documenting Envion’s envelope-first philosophy.

---

## 📜 License

Envion is released under the **MIT License with Attribution**.  
You are free to use, modify, and redistribute this project — including for commercial purposes —  
as long as you credit **Envion** and **Emiliano Pennisi**.  
See the [LICENSE](LICENSE) file for details.

---

## Links

- 🌐 **Website:** [peamarte.it/env/envion_v3.6.html](https://www.peamarte.it/env/envion_v3.6.html)  
- **Portfolio:** [http://www.emilianopennisi.it](http://www.emilianopennisi.it)  
- **YouTube Series:** [Envion — Official Playlist](https://www.youtube.com/watch?v=gA-pdHQwibA&list=PLLITukQh1_l61lP6GMfa1Hz4Db7_wrTTT)  
- **Community:** [r/musiconcrete](https://www.reddit.com/r/musiconcrete)  
- ✉️ **Contact:** [metrostation@gmail.com](mailto:metrostation@gmail.com)

---

*Built in Pure Data / PlugData (2024–2025)*  
*© Emiliano Pennisi*

<!--UPDATE_TS_START-->
_Last update: 2025-10-15 06:37 CEST_
<!--UPDATE_TS_END-->
