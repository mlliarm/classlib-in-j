import os

# Target the paths inside the 'apl/' folder explicitly
input_file = os.path.join("../apl", "contenido_funciones.txt")
output_file = os.path.join("../apl", "contenido_funciones_with_del.txt")

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found. Please verify the folder structure.")
    exit(1)

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

processed_lines = []
current_block = []
in_code_zone = False

for line in lines:
    # Check for the header boundaries
    if line.startswith("======"):
        # If we were already tracking a function code block, it just ended.
        # Wrap it with the closing del and flush it.
        if in_code_zone and current_block:
            # Strip trailing blank lines from the code block before appending ∇
            while current_block and not current_block[-1].strip():
                current_block.pop()
            if current_block:
                current_block.append("∇\n")
            processed_lines.extend(current_block)
            current_block = []
            in_code_zone = False
        
        processed_lines.append(line)
        continue

    if line.startswith("FUNCTION:"):
        processed_lines.append(line)
        # The next non-header lines will be actual APL code
        in_code_zone = True
        continue

    if in_code_zone:
        # If this is the very first line of APL code in this block, prepend '∇ '
        if not current_block and line.strip():
            current_block.append("∇ " + line.lstrip())
        else:
            current_block.append(line)
    else:
        # This preserves the headers or structural gaps outside the function blocks
        processed_lines.append(line)

# Handle the absolute last function in the file if it didn't hit a trailing ===== boundary
if in_code_zone and current_block:
    while current_block and not current_block[-1].strip():
        current_block.pop()
    if current_block:
        current_block.append("∇\n")
    processed_lines.extend(current_block)

# Save the polished output inside the 'apl/' folder
with open(output_file, "w", encoding="utf-8") as out:
    out.writelines(processed_lines)

print(f"Success! Delimiters added cleanly. File saved inside the folder as '{output_file}'.")

