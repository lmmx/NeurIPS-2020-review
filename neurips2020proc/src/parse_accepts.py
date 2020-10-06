import pandas as pd
from ..data import data_dir
from .structure import Paper, PaperList

accepted_papers = data_dir / "AcceptedPapersInitial.md"

with open(accepted_papers, "r") as f:
    md_lines = [l.rstrip("\n") for l in f.readlines()]

def process_papers():
    processed_papers = parse_md_lines()
    #accepts_df = pd.DataFrame(processed_papers)
    return processed_papers #accepts_df

def parse_md_lines(md_lines=md_lines):
    papers = []
    header_read = False
    in_paper_block = False
    for l in md_lines + [""]: # add a blank line at the end to ensure completion
        if l.startswith("#"): # heading line
            continue # do not process the heading
        elif len(l) == 0: # blank line
            if in_paper_block: # closing an open paper's line block
                paper = Paper(paper_block_lines) # only now parse completed line block
                papers.append(paper) # add it to list of processed papers
            in_paper_block = False # close the now-processed paper's line block
        else: # the line is within a paper block (either continuing or newly opening)
            if in_paper_block: # continue an open paper's line block
                paper_block_lines.append(l) # extend stored list of lines for the block
            else: # open a new paper's line block
                paper_block_lines = [l] # initialise a stored list of lines for a block
            in_paper_block = True
    return PaperList(papers)
