# classlib-in-x
A port of prof. Charles C. Sims' CLASSLIB APL library into language X.

*Note:* For now only the full APL code is available, along with instructions of use. 

## CLASSLIB

This was the library prof. Charles C. Sims wrote and used in his seminal ['Abstract Algebra: A Computational Approach'](https://dl.acm.org/doi/abs/10.5555/781) book.

Got the `apl/classlib.atf` file that contains all the functions from [this repository](https://github.com/Angeldude/classlib) by @Angeldude. Thanks.

## Extraction

### GNU APL 2.0

I've built localy [GNU APL 2.0](https://ftp.gnu.org/gnu/apl/) in order to read the classlib.atf file. I've named the binary `apl-2.0` to remember the version. If you're a Dyalog APL user, you can use that too.

If you want to play with the `classlib.atf` library with GNU APL 2.0 and follow Sim's book with APL you'll need to install an APL keyset on your OS.

Assuming that you have a GNU/Linux flavor, [one way to do this](https://github.com/ilovezfs/gnu-apl/blob/master/README-3-keyboard), and use Dyalog's APL keyset is to run within GNU APL's folder:

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

**Caution**: say bye bye to `Alt+Tab` window rotation after applying the above command. You'll have to use a different key for that.

Another way to get the APL keyset in your modern GNU/Linux or similar `*`nix systemis to go to the Layouts and search for `APL` and choose a variant. The only downside is that you'll have to switch from EN to APL and back when you're going through the code examples of Sims' book. But one cannot have everything. At least this solution won't mess up any other keyboard layouts that you may have in parallel to EN.

Now load the library `classlib.atf` and have fun:

```apl
)IN ./apl/classlib.atf
```

### Function names

After that, running the following code in my GNU/Linux environment calling the GNU APL binary printed the names of the functions in a txt file named `funciones.txt`:

```bash
echo -e ")IN ./classlib.atf\n)FNS\n)OFF" | apl-2.0 --silent --noSV > funciones.txt
```

### Function definitions

Then I wanted to extract the APL code per function without having to read all the ATF files from Angeldude's project.

It was hard to do it with a bash & APL code so with Gemini we created [this python script](./tools/extract_funciones.py) which saved inside
the [TXT](./apl/contenido_funciones.txt) file the definitions. A syntax highlighted version of that is the [APL](./apl/contenido_funciones.apl) file.

A catch here: because `⎕←⎕CR 'FUNCTION_NAME'` returns the function content as it is, one might want to see how it looks in edit mode.

As we know, in edit mode the header of the function starts with `∇` and the last line of the function is `∇`.

For this reason with the help of Gemini we created a [second python script](./tools/wrap_del.py) that added in the start and the end of the functions
the `∇` character, so it's better visible that this is the definition of a function. You can find the corresponding files [here in TXT](./apl/contenido_funciones_with_del.txt) and [here in APL highlighted syntax](./apl/contenido_funciones_with_del.apl).

## Original code

Please read first the last section, `Provenance` regarding its origin.

### Classlib

The Classlib version I got from Angeldude lies inside `apl/`. The original (professor's) version lies inside `apl/classlib0/`. The program `diff` says that the binaries differ. So far I've only tested partially the first version.

### Examples

Within that code there were the examples. Now the trick is that `apl/examples0.atf` crashes when one tries to `)IN` from GNU APL, because Sims used a different type of APL, probably IBM APL 2. With the help of Claude I managed to create `apl/examples.apl` that has the instructions of all the examples. You can load all the commands either by hand, or in a new APL session with the command:

```bash
apl-2.0 -f ./apl/examples0.apl
```

### Solutions

In the archive there were also some solutions. You can find them in `apl/classlib0/solutions0.atf`.

### Clbutil

A few util functions. Can be found in `apl/classlib0/clbutil0.atf`.

## Use

### APL

To use CLASSLIB with APL, import the library `classlib.atp` as follows:

- GNU APL

```apl
)IN ./apl/classlib.atf
```

- Dyalog APL

```apl
]IN ./apl/classlib.atf
```

Have fun !

### X=j

TBD

## Files

### Folder `apl/`

- `funciones.txt`: contains the names of all the 227 functions.
- `contenido_funciones.txt`: contains the definitions of all the functions.
- `contenido_funciones.apl`: contains the syntax highlighted definitions of all the functions.
- `contenido_funciones_with_del.txt`: contains the definitions of all the functions in edit mode.
- `contenido_funciones_with_del.apl`: contains the syntax highlighted definitions of all the functions in edit mode.
- `classlib.atf`: the original ATF file that contains all the functions. You need to use that if you want to use APL with prof. Sims' book.
- `examples0.apl`: the examples shared for the book in unsolved problems. Extracted from `classlib0/examples0.atf`.
- `classlib0/`: the original (professor's) code set files (zipped and unzipped).
- `LICENCE-CLASSLIB.md`: transparency note and disclaimer regarding professor's code.

### Folder `j/`

Where the J translation of the APL code will be.

Ongoing work.

### Folder `tools/`

- `extract_funciones.py`: python script to extract the definitions for each function and save them into `apl/contenido_funciones.txt`.
- `wrap_del.py`: python script to add the `∇` character at the begining and the end of each function, and save them into `apl/contenido_funciones_with_del.txt`.

## Provenance

The original APL source files (`classlib0.atf`, `examples0.atf`, `solutions0.atf`, `clbutil0.atf`) originate from Charles C. Sims (1937–2017), professor of mathematics at Rutgers University, who wrote CLASSLIB to accompany his book *Abstract Algebra: A Computational Approach*.

According to [a 2020 post on the NARS2000 forum](https://www.tapatalk.com/groups/nars2000/viewtopic.php?p=2080#p2080) by user `dougt719` ("Doug"), Doug held an email from Professor Sims stating that CLASSLIB could be posted on the Internet with no restrictions. Doug shared the files with the NARS2000 forum's maintainer, Bob Smith, for possible inclusion with the NARS2000 APL interpreter. See [the original thread](https://www.tapatalk.com/groups/nars2000/apl-abstract-algebra-library-classlib-t640.html).

The copy of the files in this repository was obtained directly from Bob Smith, the forum's maintainer and the recipient of the files from Doug; he is not himself the source of Sims' stated permission.

This repository has not independently verified the original Sims → Doug email. If you have a copy of that correspondence, or are able to confirm its contents, please open an issue.
