# Distinguish multiple affiliations with a slash rather than a comma
# (since the comma is also used within a single affiliation) and
# minor (obvious spelling mistakes)
affils_bugfix_dict = {
    "Adobe, CMU": "Adobe / CMU",
    "Samsung, Stanford, HKUST": "Samsung / Stanford / HKUST",
    "The University of Tokyo, Preferred Networks Inc.": "The University of Tokyo / Preferred Networks Inc.",
    "Sorbonne University, Ecole Polytechnique": "Sorbonne University / Ecole Polytechnique",
    "CMU, Strategic Machine, Strategy Robot, Optimized Markets": "CMU / Strategic Machine, Strategy Robot, Optimized Markets",
    "TAU, GOOGLE": "TAU / GOOGLE",
    "KAIST, AITRICS": "KAIST / AITRICS",
    "University of Oxford, DeepMind": "University of Oxford / DeepMind",
    "DeepMind, UCL": "DeepMind / UCL",
    "Yandex, Higher School of Economics": "Yandex / Higher School of Economics",
    "Google Research, Brain Team": "Google Research, Brain", # appears as both
    "Hitachi,Ltd.": "Hitachi, Ltd.", # typo
    '" University of Oregon, USA"': "University of Oregon, USA", # string quoting error
    "University of California, Irivine": "University of California, Irvine" # typo
}
author_bugfix_dict = {
    "Aldo Glielmo (International School for Advanced Studies (SISSA)))": "Aldo Glielmo (International School for Advanced Studies (SISSA))" 
}
# Aldo Glielmo: surplus closing bracket in attribution prevents parsing
