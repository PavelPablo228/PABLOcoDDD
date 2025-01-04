def split_file_by_lines(file_path, lines_per_part):
    part_number = 1
    current_line_count = 0
    part_file = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if current_line_count % lines_per_part == 0:
                if part_file:
                    part_file.close()  
                part_filename = f"{file_path}.part{part_number}"
                part_file = open(part_filename, 'w', encoding='utf-8')
                part_number += 1
            
            part_file.write(line)
            current_line_count += 1

        if part_file:
            part_file.close()  

    print(f"file '{file_path}' drop {lines_per_part} str.")

split_file_by_lines(r"C:\Users\...\output.txt", 25000000)
