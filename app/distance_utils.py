import difflib

import Levenshtein as lv


def compute_distance_with_lv(word, possibilities):
    distances = [lv.distance(word, s) for s in possibilities]
    return distances


def compute_distance_with_difflib(word, possibilities, cutoff=0.6, junk_str=""):
    # Reference: https://docs.python.org/3/library/difflib.html#difflib.get_close_matches

    s = difflib.SequenceMatcher(isjunk=lambda x: x in junk_str)
    s.set_seq2(word)

    distances = []
    for x in possibilities:
        s.set_seq1(x)
        if (
            s.real_quick_ratio() >= cutoff
            and s.quick_ratio() >= cutoff
            and s.ratio() >= cutoff
        ):
            # Reference: https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.ratio
            similarity = s.ratio()
        else:
            similarity = 0

        distances.append(1.0 - similarity)

    return distances


def compute_distances(word, possibilities, use_levenshtein=True):
    if use_levenshtein:
        distances = compute_distance_with_lv(word, possibilities)
    else:
        distances = compute_distance_with_difflib(word, possibilities)

    return distances
