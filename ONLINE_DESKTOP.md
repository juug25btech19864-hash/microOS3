# 🖥️ MicroOS Desktop Environment — Access Links & Quick Start Guide

**Project Name:** MicroOS — Ultra-Lightweight Linux Operating System & Multitasking Desktop  
**Student:** M. Srivas (Mandhadi Srivas)  
**USN:** `25BTRCL143`  
**Department:** Artificial Intelligence & Machine Learning (AIML)  
**Institution:** Faculty of Engineering and Technology (FET), Jain University, Bangalore  
**Course:** Operating Systems Lab (2026)  
**Faculty / Evaluator:** Dr. Sujeet S Jagtap  

---

## 🌐 Live Online Desktop (Cloud Access)

You can launch and interact with the complete MicroOS Desktop Environment directly in your web browser from any device (laptop, tablet, phone) without installing any virtual machine or software:

| Environment | Access Link | Description |
| :--- | :--- | :--- |
| **🚀 Live Interactive Space** | **[https://huggingface.co/spaces/Srivas369/microOS3](https://huggingface.co/spaces/Srivas369/microOS3)** | Official Hugging Face interactive space with integrated GUI desktop, terminal, and apps |
| **📺 Fullscreen Web App** | **[https://srivas369-microos3.hf.space](https://srivas369-microos3.hf.space)** | Full-viewport distraction-free live desktop experience |
| **📦 GitHub Repository** | **[https://github.com/juug25btech19864-hash/microOS3](https://github.com/juug25btech19864-hash/microOS3)** | Complete source code, ISO build pipelines, and documentation |
| **💾 Model & ISO Repository** | **[https://huggingface.co/Srivas369/microOS3](https://huggingface.co/Srivas369/microOS3)** | Bootable hybrid ISO images, VDI disks, and SHA256 checksums |

---

## 💻 Local Desktop Access (On Host Machine)

If you are running the project locally on your machine:

1. **Local Web Server**:
   ```bash
   python web/server.py
   ```
   Open your browser and navigate to:  
   👉 **[http://localhost:8080](http://localhost:8080)**

2. **Direct Local File (Offline)**:  
   Open the file `web/index.html` directly in Google Chrome, Microsoft Edge, or Mozilla Firefox.

---

## 🖲️ In VirtualBox (Native Operating System)

When booting the MicroOS ISO image in VirtualBox:

1. Power on the VirtualBox VM attached to `microos.iso`.
2. At the shell prompt `srivas@microos:~$ `, simply enter:
   ```bash
   desktop
   ```
   *(or `gui`)* and press **Enter**.
3. To open the terminal from within the desktop, click the **Developer Terminal** icon or press **T**.
4. To return to the desktop from the terminal, type `exit` or `q`.

---

## ✨ Features Available in MicroOS Desktop

* **Desktop Aesthetics**:
  * Windows 11 Blue Bloom acrylic glass interface with dynamic theme switching (Bloom Dark, Bloom Light, Satin Wave).
  * 2-column quick launcher grid with 22 system applications, diagnostics, and tools.
* **Developer Terminal**:
  * Real-time command execution with full Linux BusyBox environment.
  * Default 4-packet auto-terminating `ping` diagnostic with latency statistics (`seq=0..3`).
  * Instant manual and command lookup via `help` and `help <topic>` (e.g., `help wifi`, `help ping`, `help arcade`).
* **Wireless Network Manager**:
  * Pre-configured live Wi-Fi profile (`MOJO-JAN-C1-F9`, Wi-Fi 6 802.11ax, 1201 Mbps).
  * Interactive scan showing surrounding 2.4 GHz and 5 GHz networks with signal strength indicators.
* **Retro Arcade Gaming Suite**:
  * 8 offline built-in C arcade games: Snake, Tetris, Pong, Minesweeper, 2048, Tic-Tac-Toe, Guess, and Space Invaders.
* **System Telemetry & Monitoring**:
  * Visual task manager, RAM memory gauge, CPU utilization meter, and storage partition viewer.

---

*Submitted for Operating Systems Coursework & Continuous Assessment — Jain University (FET AIML).*
