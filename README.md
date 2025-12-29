# FM Transceiver Project

## Overview
This project implements a **complete FM transmitter and receiver system** using GNU Radio Companion (GRC). It includes modulation, demodulation, filtering, and visualization of signals, along with RDS (Radio Data System) encoding and decoding.

## Requirements
- GNU Radio 3.8+
- Python 3.x
- Optional: RTL-SDR or USRP hardware for real-time RF transmission/reception
- Audio playback capability for local testing

## File Structure
```
my-fm-rds-project/
├── flowgraphs/
│   └── FM_RDS.grc                                         # Main GNU Radio flowgraph
├── data/
│   └── Thalapathy_Kacheri_-_Anirudh_Ravichander.mp3       # Example audio input
├── README.md                                              # Project description
└── .gitignore
```

## GNU Radio Flowgraph Description
The flowgraph is split into two main sections: **Transmitter** and **Receiver**.

### Transmitter
- Audio Source / WAV File Source → Resampling → Filters → FM Modulation
- RDS Encoder → PSK Modulation → Combined with audio
- QT GUI Sinks for time and frequency domain visualization
- Output → WBFM Transmit block (or audio sink for testing)

### Receiver
- WBFM Receive block → Filters → Multipliers → FM Demodulation
- BPSK Demodulator → RDS Decoder
- Audio Sink for recovered audio
- QT GUI Sinks for real-time signal observation

## Running the Flowgraph
1. Open the `.grc` file in GNU Radio Companion:
```
gnuradio-companion flowgraphs/fm_rds_transceiver.grc
```
2. Connect your SDR device or use local audio sources.
3. Click **Run** in GRC to start the flowgraph.
4. Observe signals in the QT GUI time/frequency sinks.

## Visualization
- **Time Sink** – Real-time waveform display
- **Frequency Sink** – FFT-based spectrum analysis
- **Waterfall Sink** – Frequency vs. time visualization

