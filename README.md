# Mic Identification

This Python code allows you to identify connected microphones on your system.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/iamironman0/Mic-Identification.git
```
2. Navigate to the project directory:

```
cd Mic-Identification
```

3. Install the required dependencies:
```
pip install SoundCard==0.4.2
```
# Usage

```python
from mic_identification import MicIdentification

mic_identification = MicIdentification()
print(mic_identification.get_connected_microphones()) # Example usage: get list of all connected microphones
mic_identification.search_microphone(by_index=0)  # Example usage: searching by index
mic_identification.search_microphone(by_name="Microphone")  # Example usage: searching by name
```
