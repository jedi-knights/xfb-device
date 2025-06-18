# Extreme Feedback Device

This project implements a simple CI build monitor using a Raspberry Pi 5 and a 7" touchscreen display. It monitors Jenkins, GitHub Actions, and Travis CI jobs and gives visual and audio feedback on build status.

## 🔧 Required Hardware

* Raspberry Pi 5
* ROADOM 7’’ Raspberry Pi Screen (IPS 1024×600, HDMI + USB, Touch + Audio)
* MicroSD card with Raspberry Pi OS
* Internet connection (Wi-Fi or Ethernet)
* USB power supply (at least 3A)

## 📂 Required Software

* Python 3.9+
* `flit` (for building and packaging)
* System packages:

  ```bash
  sudo apt update && sudo apt install -y python3-pip python3-pil python3-pygame feh git
  ```

## 📦 Python Dependencies

Installed automatically using Flit or pip:

* `requests`
* `pillow`
* `pygame`

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/youruser/xfb-device.git
cd xfb-device
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flit
```

### 3. Install the Package

```bash
flit install --symlink
```

### 4. Add CI Jobs to Monitor

Edit `config/jobs.yaml`:

```yaml
jobs:
  - system: github
    name: my-repo-ci
    url: https://api.github.com/repos/myuser/myrepo/actions/runs
```

### 5. Run the Poller

```bash
python poll_builds.py
```

The screen will display:

* A green screen with job name and CI provider for successful builds
* A red screen with job name and CI provider for failed builds
* An audio cue for both

## 🚰 Future Features

* Configurable alert thresholds
* Touch interaction to acknowledge failures
* CI authentication via tokens
* Docker support

## 📄 License

MIT
