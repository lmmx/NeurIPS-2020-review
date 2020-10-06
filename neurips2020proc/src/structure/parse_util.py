def GetOpeningOfLastBracket(br_str, DEBUG=False):
    """
    Get the index of the opening bracket which opens the last-to-close
    bracket of a string which may contain multiply nested brackets.
    """
    openers = [i for i,v in enumerate(br_str) if v == "("]
    closers = [i for i,v in enumerate(br_str) if v == ")"]
    if len(openers) == len(closers) == 1:
        if DEBUG: print(f"Trivial: {openers[0]}")
        return openers[0] # trivial, most common case
    br_dict = {**{i: -1 for i in openers}, **{i: 1 for i in closers}}
    depth = -1 # initialise at 0 and retrieve the index when depth returns to 0
    for i,(k,v) in enumerate(reversed(sorted(br_dict.items()))):
        pre_depth = depth
        depth += v
        if DEBUG: print(f"[{i}@{k}] Depth {pre_depth} += {v} --> {depth}")
        if depth < 0 and i > 0:
            # reached index of the opening bracket which opens the final closing bracket
            if DEBUG: print(f"Non-trivial: {k} ({i}'th bracket of {len(br_dict)})")
            return k
    raise ValueError(f"Depth {depth} did not reach 0, are brackets balanced? {br_str}")
