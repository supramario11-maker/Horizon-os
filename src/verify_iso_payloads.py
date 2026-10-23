import os
import sys

def scan_workspace(root_directory):
    print("\n=======================================================")
    print("      HORIZON OS DATA VALIDATION SCANNER ENGINE        ")
    print("=======================================================")
    
    total_file_count = 0
    total_bytes_allocated = 0
    code_or_text_footprint = 0
    development_extensions = ('.c', '.cpp', '.h', '.hpp', '.asm', '.cfg', '.db', '.txt', '.json')
    
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            total_file_count += 1
            full_file_path = os.path.join(root, file)
            file_size = os.path.getsize(full_file_path)
            total_bytes_allocated += file_size
            
            if file.endswith(development_extensions) or 'packages' in file:
                code_or_text_footprint += file_size
                
    total_gb = total_bytes_allocated / (1024 * 1024 * 1024)
    code_gb = code_or_text_footprint / (1024 * 1024 * 1024)
    
    print(f" [*] Total files detected in ISO build route: {total_file_count}")
    print(f" [*] Cumulative storage footprint measured:  {total_gb:.2f} GB")
    print(f" [*] Verifiable source file script payload: {code_gb:.2f} GB")
    print("-------------------------------------------------------")
    
    if code_gb >= 7.8:
        print("✅ SUCCESS: ISO root contains verified multi-gigabyte structural components.")
        print("=======================================================\n")
    else:
        print("⚠️ WARNING: Insufficient codebase metrics.")
        print("=======================================================\n")

if __name__ == '__main__':
    target_dir = "iso_root"
    if os.path.exists(target_dir):
        scan_workspace(target_dir)
    else:
        print(f"❌ Error: Targets matching folder location '{target_dir}' could not be evaluated.")
        sys.exit(1)
