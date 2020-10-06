from .authors import Attribution
import pandas as pd

__all__ = ["Paper", "PaperList"]

class Paper:
    def __init__(self, paper_block_lines):
        title, attribution = self.parse_lines(paper_block_lines)
        self.title = title
        self.attribution = attribution

    @staticmethod
    def df_retrieval_dict():
        return {
            "title": lambda p: p.title,
            "authors": lambda p: [a.name for a in p.attribution.authors],
            "affiliations": lambda p: [a.affils for a in p.attribution.authors]
        }

    @staticmethod
    def parse_lines(block_lines):
        breaking_i = next(i for i,l in enumerate(block_lines) if l.endswith("\\"))
        title = " ".join(block_lines[:breaking_i + 1]).rstrip("\\").strip("*")
        attribution = Attribution(" ".join(block_lines[breaking_i + 1:]).strip("*"))
        return title, attribution

    @property
    def first_auth_surname(self):
        return self.attribution.authors.abbrev_repr()

    @property
    def et_al(self):
        return "" if len(self.attribution.authors) == 1 else " et al."

    def __repr__(self):
        return f'{self.first_auth_surname}{self.et_al} — "{self.title}"'

    def as_df(self):
        df_dict = {}
        for col_name, retrieval_func in self.df_retrieval_dict().items():
            col_val = retrieval_func(self)
            df_dict.update({col_name: [col_val]})
        df = pd.DataFrame.from_dict(df_dict)
        return df

class PaperList(list):
    def __init__(self, paperlist):
        self.extend(paperlist)

    def __repr__(self):
        return f"List of {len(self)} papers"

    def as_df(self):
        paper_df_list = list(map(lambda p: p.as_df(), self))
        df_merged = pd.concat(paper_df_list).reset_index(drop=True)
        return df_merged
