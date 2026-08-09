# classlib-in-j
A translation of Charles Sims' CLASSLIB APL library into J.

## CLASSLIB

This was the library Charles C. Sims wrote and used in his seminal ['Abstract Algebra: A Computational Approach'](https://dl.acm.org/doi/abs/10.5555/781) book.

Got the `apl/classlib.atf` file that contains all the functions from [this repository](https://github.com/Angeldude/classlib) by @Angeldude. Thanks.

## Extraction

### GNU APL 2.0

I've build localy [GNU APL 2.0](https://ftp.gnu.org/gnu/apl/) in order to read the classlib.atf file. If you're a Dyalog APL user, you can use that too.

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

**Caution**: say bye bye to `Alt+Tab` window rotation after applying the above command. You'll have to use a different key for that.

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

A catch here: because `⎕←⎕CR← 'FUNCTION_NAME'` returns the function content as it is, one might want to see how it looks in edit mode.

As we know, in edit mode the header of the function starts with `∇` and the last line of the function is `∇`.

For this reason with the help of Gemini we created a [second python script](./tools/wrap_del.py) that added in the start and the end of the functions
the `∇` character, so it's better visible that this is the definition of a function. You can find the corresponding files [here in TXT](./apl/contenido_funciones_with_del.txt) and [here in APL highlighted syntax](./apl/contenido_funciones_with_del.apl).

## Output

### Folder `apl/`

- `funciones.txt`: contains the names of all the 227 functions.

- `contenido_funciones.txt`: contains the definitions of all the functions.

- `contenido_funciones.apl`: contains the syntax highlighted definitions of all the functions.

- `contenido_funciones_with_del.txt`: contains the definitions of all the functions in edit mode.

- `contenido_funciones_with_del.apl`: contains the syntax highlighted definitions of all the functions in edit mode.

- `classlib.atf`: the original ATF file that contains all the functions. You need to use that if you want to use APL with Sim's book.

### Folder `j/`

Where the J translation of the APL code will be.

Ongoing work.
