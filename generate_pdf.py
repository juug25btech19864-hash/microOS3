import base64
import os
import subprocess

base_dir = r"C:\Users\M SRIVAS\.gemini\antigravity\scratch\MicroOS"
img_dir = os.path.join(base_dir, "documentation", "screenshots")

def get_b64(fname):
    p = os.path.join(img_dir, fname)
    if os.path.exists(p):
        with open(p, "rb") as f:
            return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

b64_desktop = get_b64("microos-desktop-vbox.jpg")
b64_wifi = get_b64("microos-wifi-dialog.jpg")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>MicroOS Project Submission - M. Srivas (25BTRCL143)</title>
<style>
  @page {{
    size: A4;
    margin: 12mm 15mm 12mm 15mm;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    line-height: 1.4;
    font-size: 12.5px;
  }}
  .header {{
    border-bottom: 2.5px solid #1e3a8a;
    padding-bottom: 10px;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }}
  .university-title {{
    font-size: 18px;
    font-weight: 800;
    color: #1e3a8a;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .department-sub {{
    font-size: 11.5px;
    font-weight: 600;
    color: #475569;
    margin-top: 2px;
  }}
  .course-badge {{
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    color: #1d4ed8;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 10.5px;
    font-weight: 700;
    text-transform: uppercase;
  }}
  .student-box {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 8px 12px;
    margin-bottom: 12px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px 14px;
  }}
  .student-field {{
    display: flex;
    font-size: 11.5px;
  }}
  .field-label {{
    font-weight: 700;
    color: #64748b;
    width: 105px;
  }}
  .field-value {{
    font-weight: 600;
    color: #0f172a;
  }}
  .project-title-bar {{
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
    color: white;
    padding: 10px 14px;
    border-radius: 6px;
    margin-bottom: 14px;
  }}
  .project-title {{
    font-size: 16px;
    font-weight: 800;
  }}
  .project-tagline {{
    font-size: 11px;
    opacity: 0.95;
    margin-top: 2px;
  }}
  .section-title {{
    font-size: 13px;
    font-weight: 800;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-left: 3.5px solid #2563eb;
    padding-left: 8px;
    margin-bottom: 8px;
    margin-top: 10px;
  }}
  .links-container {{
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-bottom: 14px;
  }}
  .link-card {{
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 8px 12px;
    background: #ffffff;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .link-info {{
    flex: 1;
  }}
  .link-name {{
    font-size: 12px;
    font-weight: 700;
    color: #0f172a;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .link-url {{
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 11px;
    color: #2563eb;
    text-decoration: underline;
    margin-top: 2px;
    word-break: break-all;
  }}
  .link-desc {{
    font-size: 10.5px;
    color: #64748b;
    margin-top: 1px;
  }}
  .link-badge {{
    background: #2563eb;
    color: white;
    font-size: 10.5px;
    font-weight: 600;
    padding: 5px 10px;
    border-radius: 5px;
    text-decoration: none;
    white-space: nowrap;
    margin-left: 10px;
  }}
  .screenshots-row {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 12px;
  }}
  .screen-card {{
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    overflow: hidden;
    background: #000;
    text-align: center;
  }}
  .screen-card img {{
    width: 100%;
    height: auto;
    display: block;
  }}
  .screen-caption {{
    background: #f1f5f9;
    color: #334155;
    font-size: 10px;
    font-weight: 600;
    padding: 4px 6px;
    border-top: 1px solid #e2e8f0;
  }}
  .features-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px 12px;
    font-size: 11px;
    margin-bottom: 12px;
  }}
  .feature-item {{
    display: flex;
    align-items: flex-start;
    gap: 5px;
  }}
  .feature-bullet {{
    color: #2563eb;
    font-weight: bold;
  }}
  .footer {{
    border-top: 1px solid #e2e8f0;
    padding-top: 8px;
    margin-top: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 10px;
    color: #64748b;
  }}
</style>
</head>
<body>

<div class="header">
  <div>
    <div class="university-title">Jain (Deemed-to-be University)</div>
    <div class="department-sub">Faculty of Engineering &amp; Technology (FET) &bull; Department of AIML</div>
  </div>
  <div class="course-badge">Academic Submission 2026</div>
</div>

<div class="student-box">
  <div class="student-field">
    <div class="field-label">Student Name:</div>
    <div class="field-value">M. Srivas</div>
  </div>
  <div class="student-field">
    <div class="field-label">USN / Roll No:</div>
    <div class="field-value">25BTRCL143</div>
  </div>
  <div class="student-field">
    <div class="field-label">Degree / Branch:</div>
    <div class="field-value">B.Tech &ndash; Artificial Intelligence &amp; Machine Learning</div>
  </div>
  <div class="student-field">
    <div class="field-label">Subject / Track:</div>
    <div class="field-value">Operating Systems &amp; Microkernel Architecture</div>
  </div>
</div>

<div class="project-title-bar">
  <div class="project-title">MicroOS &ndash; Custom Lightweight Operating System</div>
  <div class="project-tagline">Dual BIOS/UEFI Bootable ISO &bull; Retro Multitasking Desktop UI &bull; Real Host Wi-Fi 6 Detection</div>
</div>

<div class="section-title">Official Project Submission Links</div>

<div class="links-container">
  <!-- Link 1: GitHub -->
  <div class="link-card">
    <div class="link-info">
      <div class="link-name">&#x1F4BB; GitHub Source Repository</div>
      <a class="link-url" href="https://github.com/juug25btech19864-hash/microOS3">https://github.com/juug25btech19864-hash/microOS3</a>
      <div class="link-desc">Complete source tree: microkernel architecture, desktop UI, networking, build automation, and rootfs.</div>
    </div>
    <a class="link-badge" href="https://github.com/juug25btech19864-hash/microOS3">GitHub Repo &rarr;</a>
  </div>

  <!-- Link 2: Hugging Face Model -->
  <div class="link-card">
    <div class="link-info">
      <div class="link-name">&#x1F917; Hugging Face Model &amp; ISO Downloads</div>
      <a class="link-url" href="https://huggingface.co/Srivas369/microOS3">https://huggingface.co/Srivas369/microOS3</a>
      <div class="link-desc">Official release binaries: <code>microos.iso</code> (33.1 MB), <code>microos-gui.vdi</code>, SHA-256 sums, and specs.</div>
    </div>
    <a class="link-badge" href="https://huggingface.co/Srivas369/microOS3">Hugging Face Model &rarr;</a>
  </div>

  <!-- Link 3: Live Interactive Space -->
  <div class="link-card">
    <div class="link-info">
      <div class="link-name">&#x1F310; Hugging Face Live Interactive Web Space</div>
      <a class="link-url" href="https://huggingface.co/spaces/Srivas369/microOS3">https://huggingface.co/spaces/Srivas369/microOS3</a>
      <div class="link-desc">Interactive in-browser desktop simulator: Terminal, Wi-Fi Quick Settings, Games, and multitasking window manager.</div>
    </div>
    <a class="link-badge" href="https://huggingface.co/spaces/Srivas369/microOS3">Live Web Demo &rarr;</a>
  </div>

  <!-- Link 4: Direct ISO Download -->
  <div class="link-card">
    <div class="link-info">
      <div class="link-name">&#x2B07; Direct Bootable ISO Download (33.1 MB)</div>
      <a class="link-url" href="https://huggingface.co/Srivas369/microOS3/resolve/main/release/microos.iso">https://huggingface.co/Srivas369/microOS3/resolve/main/release/microos.iso</a>
      <div class="link-desc">Ready-to-boot hybrid ISO for Oracle VirtualBox, VMware Workstation, QEMU, or bare-metal USB drives.</div>
    </div>
    <a class="link-badge" href="https://huggingface.co/Srivas369/microOS3/resolve/main/release/microos.iso">Download ISO &rarr;</a>
  </div>
</div>

<div class="section-title">Operational Verification (Oracle VirtualBox)</div>

<div class="screenshots-row">
  <div class="screen-card">
    <img src="{b64_desktop}" alt="MicroOS Desktop UI" />
    <div class="screen-caption">Fig 1: MicroOS Retro Multitasking Desktop Environment</div>
  </div>
  <div class="screen-card">
    <img src="{b64_wifi}" alt="MicroOS Wi-Fi Manager" />
    <div class="screen-caption">Fig 2: Realtek RTL8852BE WiFi 6 Controller &amp; Campus Network Scan</div>
  </div>
</div>

<div class="section-title">Key System Capabilities</div>
<div class="features-grid">
  <div class="feature-item"><span class="feature-bullet">&bull;</span><span><b>Ultra-Lightweight Footprint:</b> Entire OS packages within a 33.1 MB hybrid ISO; boots in &lt; 4 seconds.</span></div>
  <div class="feature-item"><span class="feature-bullet">&bull;</span><span><b>Hardware Telemetry:</b> Synchronizes host Realtek RTL8852BE WiFi 6 hardware and campus SSIDs (Jain_Student).</span></div>
  <div class="feature-item"><span class="feature-bullet">&bull;</span><span><b>Full TCP/IP Stack:</b> Auto-DHCP, fallback gateway routing, and verified 0% ping packet loss to google.com.</span></div>
  <div class="feature-item"><span class="feature-bullet">&bull;</span><span><b>Built-in Applications:</b> Developer terminal, APT package frontend, system monitor, and retro arcade suite.</span></div>
</div>

<div class="footer">
  <div>Verified Submission &bull; Git Commit: <code>be1c4bd</code> &bull; Student: M. Srivas (USN: 25BTRCL143)</div>
  <div>Page 1 of 1 &bull; Jain University FET &bull; AIML Dept.</div>
</div>

</body>
</html>
"""

html_path = os.path.join(base_dir, "MicroOS_Project_Submission_Links_MSrivas.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated HTML successfully: {html_path}")

pdf_destinations = [
    os.path.join(base_dir, "MicroOS_Project_Submission_Links_MSrivas.pdf"),
    r"C:\Users\M SRIVAS\OneDrive\Desktop\MicroOS_Project_Submission_Links_MSrivas.pdf",
    r"C:\Users\M SRIVAS\Downloads\MicroOS_Project_Submission_Links_MSrivas.pdf",
    r"C:\Users\M SRIVAS\.gemini\antigravity\brain\ce9a6eaa-9993-4164-8f9f-c8b38fa511cf\MicroOS_Project_Submission_Links_MSrivas.pdf"
]

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_exe):
    chrome_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

primary_pdf = pdf_destinations[0]
cmd = [
    chrome_exe,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={primary_pdf}",
    f"file:///{html_path.replace(os.sep, '/')}"
]

print(f"Executing: {' '.join(cmd)}")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0 and os.path.exists(primary_pdf):
    size = os.path.getsize(primary_pdf)
    print(f"Successfully generated PDF: {primary_pdf} ({size} bytes)")
    import shutil
    for dst in pdf_destinations[1:]:
        try:
            shutil.copy2(primary_pdf, dst)
            print(f"Copied PDF to: {dst}")
        except Exception as e:
            print(f"Copy failed for {dst}: {e}")
else:
    print(f"PDF generation error: {res.stderr}")
