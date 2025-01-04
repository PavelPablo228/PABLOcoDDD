import os
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = b""
        for _ in range(5):  
            chunk = f.read(1024)
            if not chunk:
                break
            raw_data += chunk
    result = chardet.detect(raw_data)
    return result['encoding']

def merge_files(file_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in file_list:
            if os.path.isfile(filename):
                print(f"obrabotka: {filename}")
                
                encoding = detect_encoding(filename)
                print(f"unucode: {encoding}")

                try:
                    with open(filename, 'r', encoding=encoding) as infile:
                        for line in infile:
                            outfile.write(line)
                        outfile.write("\n")
                except Exception as e:
                    print(f"error {filename}: {e}")
            else:
                print(f"file {filename} not found.")

files_to_merge = [
    r"C:\Users...\part_1.txt",
    r"C:\Users...\part_2.txt",
    r"C:\Users...\part_3.txt",
    r"C:\Users...\part_4.txt",
    r"C:\Users...\part_5.txt",
    r"C:\Users...\part_6.txt",
    r"C:\Users...\part_7.txt"
] 
output_filename = r"C:\Users...\merged_file.txt"

merge_files(files_to_merge, output_filename)
print(f"check the {output_filename}")
