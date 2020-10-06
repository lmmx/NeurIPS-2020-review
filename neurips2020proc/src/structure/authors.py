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

    def get_surname(self):
        "Rough guess at the surname"
        return " ".join(self.name.split(" ")[1:])
    
    def __repr__(self):
        return f"{self.name} ({' / '.join(self.affils)})"

class AuthorList(list):
    def __init__(self, authors):
        self.extend(authors)

    def __repr__(self):
        s = "" if len(self) == 1 else "s"
        return f"List of {len(self)} author{s}"

    def abbrev_repr(self):
        return self[0].get_surname()

class Attribution:
    def __init__(self, attribution_string):
        authors = [Author(a.strip()) for a in attribution_string.split("·")]
        self.authors = AuthorList(authors)

    def __repr__(self):
        r = ', '.join([f"{a!r}" for a in self.authors])
        return r
