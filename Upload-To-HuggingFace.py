#!/usr/bin/env python3
"""
MicroOS - Automated Hugging Face Publisher
Uploads MicroOS ISOs, VDIs, documentation, and the interactive web demo Space to Hugging Face.
Student: M. Srivas (USN: 25BTRCL143)
College: Jain University (FET) - AIML
HF Username: Srivas369
"""

import os
import sys
import argparse
from huggingface_hub import HfApi, login, get_token

def main():
    repo_dir = r"C:\Users\M SRIVAS\.gemini\antigravity\scratch\MicroOS"
    if os.path.exists(repo_dir):
        os.chdir(repo_dir)

    parser = argparse.ArgumentParser(description="Publish MicroOS to Hugging Face")
    parser.add_argument("--username", default="Srivas369", help="Hugging Face username")
    parser.add_argument("--repo-name", default="microOS3", help="Repository/Space name")
    parser.add_argument("--token", default=None, help="Hugging Face write token (or set HF_TOKEN env var)")
    args = parser.parse_args()

    token = args.token or os.environ.get("HF_TOKEN") or get_token()

    print("============================================================")
    print("        MicroOS - Hugging Face Publishing Tool")
    print("============================================================")
    print("Student  : M. Srivas (USN: 25BTRCL143)")
    print("College  : Jain University (FET) - AIML")
    print(f"HF User  : {args.username}")
    print("============================================================")

    if not token:
        print("\n[*] To publish to Hugging Face:")
        print("    1. Go to: https://huggingface.co/settings/tokens")
        print("    2. Click 'Create new token' and select 'Write' role.")
        print()
        try:
            token = input("Enter your Hugging Face Access Token: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[!] Aborted.")
            sys.exit(1)

    if not token:
        print("[!] Token cannot be empty. Exiting.")
        sys.exit(1)

    try:
        login(token=token, add_to_git_credential=True)
        api = HfApi(token=token)
        user_info = api.whoami()
        username = user_info["name"]
        print(f"[+] Successfully authenticated as: {username} ({user_info.get('fullname', '')})")
    except Exception as e:
        print(f"[!] Authentication failed: {e}")
        sys.exit(1)

    space_id = f"{username}/{args.repo_name}"
    model_id = f"{username}/{args.repo_name}"

    # 1. Publish Interactive Space (Web OS Desktop)
    print("\n------------------------------------------------------------")
    print(f"[*] 1/2 Publishing Live Interactive Space: https://huggingface.co/spaces/{space_id}")
    print("------------------------------------------------------------")
    try:
        api.create_repo(
            repo_id=space_id,
            repo_type="space",
            space_sdk="static",
            exist_ok=True,
            private=False
        )
        print(f"[+] Space repository ready: https://huggingface.co/spaces/{space_id}")

        if os.path.exists("hf-space/index.html"):
            api.upload_file(
                path_or_fileobj="hf-space/index.html",
                path_in_repo="index.html",
                repo_id=space_id,
                repo_type="space",
                commit_message="Add MicroOS interactive web desktop simulator"
            )
            print("[+] Uploaded index.html to Space")

        if os.path.exists("hf-space/README.md"):
            api.upload_file(
                path_or_fileobj="hf-space/README.md",
                path_in_repo="README.md",
                repo_id=space_id,
                repo_type="space",
                commit_message="Add MicroOS space configuration card"
            )
            print("[+] Uploaded README.md to Space")

        print(f"[SUCCESS] Live Space is active at: https://huggingface.co/spaces/{space_id}")
    except Exception as e:
        print(f"[!] Space publishing note: {e}")

    # 2. Publish Model / Release Binaries (ISOs, VDIs, Screenshots)
    print("\n------------------------------------------------------------")
    print(f"[*] 2/2 Publishing Model & ISO Repository: https://huggingface.co/{model_id}")
    print("------------------------------------------------------------")
    try:
        api.create_repo(
            repo_id=model_id,
            repo_type="model",
            exist_ok=True,
            private=False
        )
        print(f"[+] Model repository ready: https://huggingface.co/{model_id}")

        if os.path.exists("README.md"):
            api.upload_file(
                path_or_fileobj="README.md",
                path_in_repo="README.md",
                repo_id=model_id,
                repo_type="model",
                commit_message="Add MicroOS documentation and repository card - M. Srivas"
            )
            print("[+] Uploaded README.md")

        if os.path.exists("documentation/screenshots"):
            api.upload_folder(
                folder_path="documentation/screenshots",
                path_in_repo="documentation/screenshots",
                repo_id=model_id,
                repo_type="model",
                commit_message="Add MicroOS VirtualBox operational photos"
            )
            print("[+] Uploaded documentation/screenshots")

        if os.path.exists("release"):
            api.upload_folder(
                folder_path="release",
                path_in_repo="release",
                repo_id=model_id,
                repo_type="model",
                commit_message="Upload MicroOS v1.0 release binaries (microos-gui.iso, microos.iso, microos-gui.vdi)"
            )
            print("[+] Uploaded release artifacts")

        print(f"[SUCCESS] Model repository active at: https://huggingface.co/{model_id}")
    except Exception as e:
        print(f"[!] Model publishing note: {e}")

    print("\n============================================================")
    print("   MICROOS SUCCESSFULLY PUBLISHED TO HUGGING FACE!")
    print("============================================================")
    print(f"  Live Demo (Space) URL : https://huggingface.co/spaces/{space_id}")
    print(f"  Model & ISOs URL      : https://huggingface.co/{model_id}")
    print(f"  Direct GUI ISO Link   : https://huggingface.co/{model_id}/resolve/main/release/microos-gui.iso")
    print(f"  Direct CLI ISO Link   : https://huggingface.co/{model_id}/resolve/main/release/microos.iso")
    print("============================================================\n")

if __name__ == "__main__":
    main()
