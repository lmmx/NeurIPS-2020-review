# NeurIPS 2020 Review

- Pandoc conversion from [HTML](neurips2020proc/data/AcceptedPapersInitial.html) ([via neurips.cc](https://neurips.cc/Conferences/2020/AcceptedPapersInitial))
  to markdown, manually trimmed ⇢ [AcceptedPapersInitial.md](neurips2020proc/data/AcceptedPapersInitial.md)
- Markdown converted to Pandas dataframe `accepted_papers` by [parse_accepts.py](neurips2020proc/src/parse_accepts.py)

Drop into a shell with the dataset by running

```sh
python -im neurips2020proc
```
⇣
```STDOUT
Parsed ⠶ List of 1900 papers                                                                                         
```

Then the `PaperList` object (a list of `Paper` objects) can be inspected or processed:

```py
for p in accepted_paper_list: print(p)
```
⇣
```STDOUT
Neverova et al. — "Continuous Surface Embeddings"
Krishnan et al. — "Improving model calibration with accuracy versus uncertainty optimization"
Li et al. — "Few-shot Image Generation via Self-Adaptation"
Simsekli et al. — "Hausdorff Dimension, Heavy Tails, and Generalization in Neural Networks"
De Bortoli et al. — "Quantitative Propagation of Chaos for SGD in Wide Neural Networks"
Mendler-Dünner et al. — "Stochastic Optimization for Performative Prediction"
...
```

This is useful to look over, but:

- there are no paper links
- the object is not a dataframe

To assist with processing, the `PaperList` class provides a `as_df` method to produce a
`pandas.DataFrame` representation from the objects. This simply merges the dataframes
from the `Paper` class (this should work nicely with filtering operations).

```py
accepted_paper_list.as_df()
```
⇣
```STDOUT
                                                  title                                            authors                                       affiliations
0                         Continuous Surface Embeddings  [Natalia Neverova, David Novotny, Marc Szafran...  [[Facebook AI Research], [Facebook AI Research...
1     Improving model calibration with accuracy vers...                 [Ranganath Krishnan, Omesh Tickoo]                            [[Intel Labs], [Intel]]
2         Few-shot Image Generation via Self-Adaptation  [Yijun Li, Richard Zhang, Jingwan (Cynthia) Lu...  [[Adobe Research], [Adobe], [Adobe Research], ...
3     Hausdorff Dimension, Heavy Tails, and Generali...  [Umut Simsekli, Ozan Sener, George Deligiannid...  [[Institut Polytechnique de Paris, University ...
4     Quantitative Propagation of Chaos for SGD in W...  [Valentin De Bortoli, Alain Durmus, Xavier Fon...  [[ENS Paris-Saclay], [ENS Paris Saclay], [ENS ...
...                                                 ...                                                ...                                                ...
1895  Distribution-free binary classification: predi...  [Chirag Gupta, Aleksandr Podkopaev, Aaditya Ra...  [[Carnegie Mellon University], [Carnegie Mello...
1896  Lipschitz Bounds and Provably Robust Training ...  [Vishaal Krishnan, Abed AlRahman Al Makdah, Fa...  [[University of California, Riverside], [Unive...
1897         Agnostic Learning with Multiple Objectives  [Corinna Cortes, Mehryar Mohri, Javier Gonzalv...  [[Google Research], [Courant Inst. of Math. Sc...
1898            Model Class Reliance for Random Forests    [Gavin Smith, Roberto Mansilla, James Goulding]  [[University of Nottingham], [University of No...
1899  Mitigating Local Identifiability in Probabilis...  [Shib Dasgupta, Michael Boratko, Dongxu Zhang,...  [[University of Massachusetts Amherst], [UMass...

[1900 rows x 3 columns]
```

Lastly, to view all the papers in your system pager, run:

```py
dfpager(accepted_paper_list.as_df())
```

This uses the `pydoc.pager` function (an undocumented part of Python standard library), which requires you
to set your `$PAGER` environment variable. My `bashrc` has it set with:

```sh
# for Python with pydoc.pager in ~/.pythonrc :: listpager()
export PAGER='less -S'
```

- See [here](https://github.com/lmmx/devnotes/wiki/Tabulated-pager-cheat-sheet-and-paging-lists-and-Pandas-DataFrames-with-pydoc's-pager)
  for my notes on `pydoc.pager` usage with Python lists and pandas `DataFrame`s.

## Advice on usage

- I tried to clean it up (see [bug_fixes.py](neurips2020proc/src/structure/bug_fixes.py))
  but there may be some typos I didn't see.
- The main cleanup I did was to separate out distinct research institutions with a `/`
  where they were ambiguously separated by a comma (modified before parsing by a check
  against `affils_bugfix_dict` in the `Affiliations` class in
  [authors.py](neurips2020proc/src/structure/authors.py))
- There's one name in what looks like Chinese Unicode characters
- There's one entry with name and affiliation identical (this is an error in the listing,
  not my parsing of it!)
  - This is the paper on 'Deep Graph Pose' by "The International Brain Laboratory The
    International Brain Laboratory (The International Brain Laboratory)"

## Next steps

Usually this kind of preprocessing precedes analysis of submissions per-company/academic institution,
for which you'd have to deduplicate more carefully.

It'd be useful to separate out these listings by category/topic, but for this
you may need the abstracts.

The papers for many (all?) of these acceptances appear to be online, but I assume
the links will be posted shortly, so I don't know if it's worth sourcing them or
just waiting.
