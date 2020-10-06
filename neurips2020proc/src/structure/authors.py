from .parse_util import GetOpeningOfLastBracket
from .bug_fixes import author_bugfix_dict, affils_bugfix_dict

__all__ = ["Affiliation", "Affiliations", "Author", "Attribution"]

class Affiliation(str):
    def __init__(self, affil_str):
        self += affil_str

class Affiliations(list):
    def __init__(self, affils_str):
        if affils_str in affils_bugfix_dict:
            affils_str = affils_bugfix_dict[affils_str]
        affiliations = [Affiliation(a.strip()) for a in affils_str.split("/")]
        self.extend(affiliations)

class Author:
    def __init__(self, author_str):
        if author_str in author_bugfix_dict:
            author_str = author_bugfix_dict[author_str]
        affiliation_start_i = GetOpeningOfLastBracket(author_str)
        self.name = author_str[:affiliation_start_i].strip()
        self.affils = Affiliations(author_str[affiliation_start_i:].strip()[1:-1])
    
    def __repr__(self):
        return f"{self.name} ({' / '.join(self.affils)})"

class Attribution:
    def __init__(self, attribution_string):
        self.authors = [Author(a.strip()) for a in attribution_string.split("·")]

    def __repr__(self):
        r = ', '.join([f"{a!r}" for a in self.authors])
        return r
