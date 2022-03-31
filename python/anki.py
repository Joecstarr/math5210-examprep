import genanki
import re

def_model = genanki.Model(
  1607392319,
  'Math model',
  fields=[
    {'name': 'Name'},
    {'name': 'Defintion'},
  ],
  templates=[
    {
      'name': 'Defintion',
      'qfmt': '{{Name}}',
      'afmt': "{{FrontSide}}"+r"""

<script>
  MathJax.config.tex['extensions'] = ["AMSmath.js", "AMSsymbols.js","AMScd.js"];
</script>
<hr id="answer"><div>

\(\newcommand{\N}{\mathbb{N}}\)
\(\newcommand{\Z}{\mathbb{Z}}\)
\(\newcommand{\Q}{\mathbb{Q}}\)
\(\newcommand{\R}{\mathbb{R}}\)
\(\newcommand{\LP}{\left(}\)
\(\newcommand{\RP}{\right)}\)
\(\newcommand{\LS}{\left\lbrace}\)
\(\newcommand{\RS}{\right\rbrace}\)
\(\newcommand{\LB}{\left[}\)
\(\newcommand{\RB}{\right]}\)
\(\newcommand{\MM}{\ \middle|\ }\)
\(\newcommand{\abs}[1]{\left\vert#1\right\vert}\)
\(\newcommand{\norm}[1]{\left\vert\left\vert#1\right\vert\right\vert}\)
\(\newcommand{\msr}[1]{m\left(#1\right)}\)
\(\newcommand{\Diff}[3]{Diff_{#1}#2\left(#3\right)}\)
\(\newcommand{\Av}[3]{Av_{#1}#2\left(#3\right)}\)
\(\newcommand{\met}[1]{\rho\LP#1\RP}\)
\(\newcommand{\ball}[2]{B_{#1}\left(#2\right)}\)
\(\newcommand{\cball}[2]{\overline{B}_{#1}\left(#2\right)}\)
\(\newcommand{\opn}{\mathcal{O}}\)
\(\newcommand{\diam}{\operatorname{diam}}\)
\(\newcommand{\ext}{\operatorname{ext}}\)
\(\newcommand{\inter}{\operatorname{int}}\)
\(\newcommand{\bd}{\operatorname{bd}}\)
\(\renewcommand{\bar}[1]{\overline{#1}}\)
</div>
"""+"{{Defintion}}",
    },
  ])

def_deck = genanki.Deck(
  2059400110,
  'prepsheet')
def_deck.add_model(def_model)


reg = r"\\boxset\{(.*)?\}\n\{([\w\W]*?)\}\n"

with open("prepsheet.tex") as file:

  data = file.read()

  finds = re.findall( reg, data)
  for find in finds:
    name      = re.sub(r"\$(.*?)\$",r"\(\1\)",find[0])
    defintion = re.sub(r"\$(.*?)\$",r"\(\1\)",find[1])
    my_note = genanki.Note(
              model=def_model,
              fields=[name, defintion],
              guid=f"prepsheet.tex-{find[0]}")
    def_deck.add_note(my_note)
  genanki.Package(def_deck).write_to_file('prepsheet.apkg')