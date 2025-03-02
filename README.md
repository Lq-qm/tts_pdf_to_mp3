# A Gradio Frontend for TTS - PDF to MP3

This ia a Gradio Frontend for TTS in AMD GPUS with CoquiTTS.

### Prerequisites

Requirements

* Python 3.10 - Torch ROCM.
  
* Everything else is in the Requirements File.

### Installing

```
~❯ python3.10 -m venv venv --system-site-packages

~❯ pip install -r requirements.txt
```

### Running the tests

```
~❯ python torchtest.py

~❯ HSA_OVERRIDE_GFX_VERSION=10.3.0 python main.py
```
