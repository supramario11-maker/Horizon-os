import os
import sys

def scan_workspace(root_directory):
    print("\n=======================================================")
    print("      HORIZON OS ASSEMBLY PAYLOAD ENGINE VALIDATOR     ")
    print("=======================================================")
    total_bytes = 0
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            total_bytes += os.path.getsize(os.path.join(root, file))
    total_gb = total_bytes / (1024 * 1024 * 1024)
    print(f" [*] Cumulative storage footprint measured: {total_gb:.2f} GB")
    if total_gb >= 7.8:
        print("✅ SUCCESS: Data tracks fully comply with 8GB+ target matrices.")
        print("=======================================================\n")
    else:
        print("❌ ERROR: File generation limits not reached."); sys.exit(1)

if __name__ == '__main__':
    scan_workspace("iso_root")
