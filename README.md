<img src="https://www.peamarte.it/env/html-guide/img/logo_circle_60x60_readme.png" width="100" height="100" style="vertical-align: middle;">
# Envion  
Algorithmic Dynatext Envelope Sequencer in **Pure Data (PlugData & iPadOS)**  
by **Emiliano Pennisi** — 2025



---

> **Full documentation & tutorials**  
> 👉 [https://www.peamarte.it/env/envion_v3.6.html](https://www.peamarte.it/env/envion_v3.6.html)  
> Visit the website for the complete usage guide, module reference, and setup details.

---

## Overview

**Envion** is an *envelope-first* ecosystem for **algorithmic and procedural composition** in Pure Data (Pd).  
It redefines sampling as a **gesture-based process** — thousands of dynamic envelopes (*Dynatext triplets*) continuously sculpt micro-events and temporal shapes.

Through its web-driven submodule **Net-Audio**, Envion fetches random sound atoms from the Internet (Internet Archive, Wikimedia Commons, Freesound) and transforms contingent data into **acousmatic gestures**, **algorithmic textures**, and **cybernetic listening ecologies**.

Envion is open-source, compatible with **PlugData** on macOS, Windows, and iPadOS, and released under the **MIT License (with Attribution)**.

---

## Quick Start

1. **Install [PlugData](https://plugdata.org/)** — includes core externals (`cyclone`, `else`).  
2. Open the main patch:  
   ```bash
   Envion_v3.9_Plugdata.pd
   ```
3. Activate **DSP**, load any sample, or pick a built-in preset (bottom-right).  
4. Use the checkboxes **Random List** / **Random Terna** for procedural randomization.  
5. On iPadOS, Envion works out-of-the-box — optional libs (`ggee`, `simplex`, `ceammc`) add visuals but are not required.

**Complete setup & iPad guide:**  
[Envion Website › Documentation](https://www.peamarte.it/env/envion_v3.6.html)

---

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

[**Envion — YouTube Playlist**](https://youtu.be/JEuB3KBAxeg?si=lSOaNRazd1CgjL80)  
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
_Last update: 2025-10-15 05:53 CEST_
<!--UPDATE_TS_END-->
