# classlib-in-j
A translation of Charles Sims' CLASSLIB APL library into J.

## CLASSLIB

This was the library Charles C. Sims wrote and used in his seminal ['Abstract Algebra: A Computational Approach'](https://dl.acm.org/doi/abs/10.5555/781) book.

Got the *.atf functions from [this repository](https://github.com/Angeldude/classlib) of @Angeldude. Thanks.

## Extraction

### GNU APL 2.0

I've build localy [GNU APL 2.0](https://ftp.gnu.org/gnu/apl/) in order to read the *.atf files.

If you want to play with the `classlib.atf` library with GNU APL 2.0 and follow Sim's book with APL you'll need to install an APL keyset on your OS.

Assuming that you have a GNU/Linux flavor, [the easier way to do this](https://github.com/ilovezfs/gnu-apl/blob/master/README-3-keyboard), and use Dyalog's APL keyset is to run within GNU APL's folder:

```bash
xmodmap support-files/Dyalog-Keyboard/apl.xmodmap
```

After that, using the `Alt` key you'll be able to select the APL characters based on the following keyboard map:

```
╔════╦════╦════╦════╦════╦════╦════╦════╦════╦════╦════╦════╦════╦═════════╗
║ ~  ║ !⌶ ║ @⍫ ║ #⍒ ║ $⍋ ║ %⌽ ║ ^⍉ ║ &⊖ ║ *⍟ ║ (⍱ ║ )⍲ ║ _! ║ +⌹ ║         ║
║ `◊ ║ 1¨ ║ 2¯ ║ 3< ║ 4≤ ║ 5= ║ 6≥ ║ 7> ║ 8≠ ║ 9∨ ║ 0∧ ║ -× ║ =÷ ║ BACKSP  ║
╠════╩══╦═╩══╦═╩══╦═╩══╦═╩══╦═╩══╦═╩══╦═╩══╦═╩══╦═╩══╦═╩══╦═╩══╦═╩══╦══════╣
║       ║ Q  ║ W⍹ ║ E⋸ ║ R  ║ T⍨ ║ Y¥ ║ U  ║ I⍸ ║ O⍥ ║ P⍣ ║ {⍞ ║ }⍬ ║  |⊣  ║
║  TAB  ║ q? ║ w⍵ ║ e∈ ║ r⍴ ║ t∼ ║ y↑ ║ u↓ ║ i⍳ ║ o○ ║ p⋆ ║ [← ║ ]→ ║  \⊢  ║
╠═══════╩═╦══╩═╦══╩═╦══╩═╦══╩═╦══╩═╦══╩═╦══╩═╦══╩═╦══╩═╦══╩═╦══╩═╦══╩══════╣
║ (CAPS   ║ A⍶ ║ S  ║ D  ║ F  ║ G  ║ H⍙ ║ J⍤ ║ K  ║ L⌷ ║ :≡ ║ "≢ ║         ║
║  LOCK)  ║ a⍺ ║ s⌈ ║ d⌊ ║ f_ ║ g∇ ║ h∆ ║ j∘ ║ k' ║ l⎕ ║ ;⍎ ║ '⍕ ║ RETURN  ║
╠═════════╩═══╦╩═══╦╩═══╦╩═══╦╩═══╦╩═══╦╩═══╦╩═══╦╩═══╦╩═══╦╩═══╦╩═════════╣
║             ║ Z  ║ Xχ ║ C¢ ║ V  ║ B£ ║ N  ║ M  ║ <⍪ ║ >⍙ ║ ?⍠ ║          ║
║  SHIFT      ║ z⊂ ║ x⊃ ║ c∩ ║ v∪ ║ b⊥ ║ n⊤ ║ m| ║ ,⍝ ║ .⍀ ║ /⌿ ║  SHIFT   ║
╚═════════════╩════╩════╩════╩════╩════╩════╩════╩════╩════╩════╩══════════╝
```

### Function names

After that, running the following code in my GNU/Linux environment calling the GNU APL binary printed the names of the functions in a txt file named `funciones.txt`:

```bash
echo -e ")IN ./classlib.atf\n)FNS\n)OFF" | apl-2.0 --silent --noSV > funciones.txt
```

### Function definitions

Then I wanted to extract the APL code per function without having to read all the ATF files from Angeldude's project.

It was hard to do it with a bash & APL code so with Gemini we created the following solution:

```python3
 import subprocess
 import os
 import re
 
 # Define file paths
 input_file = "funciones.txt"
 output_file = "contenido_funciones.txt"
 
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
```

## Output

### Folder `apl/`

- For the function names check: `funciones.txt`

- For the function definitions check: `contenido-funciones.txt`

- For the function definitions with APL syntax highlight check: `contenido-funciones.apl`

- For the original file that I extracted the functions, should you want to load it in GNU APL with `)IN ./classlib.atf`: `classlib.atf`

### Folder `j/`

Where the J translation of the APL code is.

Ongoing work.
