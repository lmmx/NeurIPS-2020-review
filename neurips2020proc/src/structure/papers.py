from .authors import Attribution

__all__ = ["Paper", "PaperList"]

class Paper:
    def __init__(self, paper_block_lines):
        title, attribution = self.parse_lines(paper_block_lines)
        self.title = title
        self.attribution = attribution

    @staticmethod
    def parse_lines(block_lines):
        breaking_i = next(i for i,l in enumerate(block_lines) if l.endswith("\\"))
        title = " ".join(block_lines[:breaking_i + 1]).rstrip("\\").strip("*")
        attribution = Attribution(" ".join(block_lines[breaking_i + 1:]).strip("*"))
        return title, attribution

    def __repr__(self):
        return f'"{self.title}"'

class PaperList(list):
    def __init__(self, paperlist):
        self.extend(paperlist)

    def __repr__(self):
        return f"List of {len(self)} papers"
