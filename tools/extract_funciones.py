 import subprocess
 import os
 import re
 
 # Define file paths
 input_file = "../apl/funciones.txt"
 output_file = "../apl/contenido_funciones.txt"
 
 # Regex pattern to match all types of ANSI escape sequences (colors, line clears)
 ansi_escape_pattern = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
 
 # 1. Read and parse function names from funciones.txt
 if not os.path.exists(input_file):
     print(f"Error: {input_file} not found. Please make sure it exists.")
     exit(1)
 
 with open(input_file, "r", encoding="utf-8") as f:
     raw_content = f.read()
 
 # Split by spaces/newlines and filter out any empty strings
 function_names = [name.strip() for name in raw_content.split() if name.strip()]
 
 print(f"Found {len(function_names)} functions to extract. Starting processing...")
 
 # 2. Iterate through each function name and query GNU APL
 with open(output_file, "w", encoding="utf-8") as out:
     for idx, fn_name in enumerate(function_names, start=1):
         print(f"[{idx}/{len(function_names)}] Extracting: {fn_name}...")
 
         # Prepare the exact sequence of commands for GNU APL
         apl_commands = f")IN ./classlib.atf\n⎕←⎕CR '{fn_name}'\n)OFF\n"
 
         # Kept the exact same working flags from your successful test
         process = subprocess.Popen(
             ["apl-2.0", "--silent", "--noSV"],
             stdin=subprocess.PIPE,
             stdout=subprocess.PIPE,
             stderr=subprocess.PIPE,
             text=True
         )
 
         stdout, stderr = process.communicate(input=apl_commands)
 
         # Scrub the raw string to remove ANSI layout codes completely
         clean_stdout = ansi_escape_pattern.sub('', stdout).strip()
 
         # Write custom header and the clean extracted code to your contents file
         out.write(f"{'='*50}\n")
         out.write(f"FUNCTION: {fn_name}\n")
         out.write(f"{'='*50}\n")
         out.write(clean_stdout + "\n\n")
 
print(f"Finished! All function contents have been saved cleanly to '{output_file}'.")
