import heapq

import Levenshtein as lv

from app.file_utils import (
    load_app_names_lower_case,
    convert_indices_to_ids,
    convert_indices_to_names,
)


def find_indices_of_nsmallest(n, l):
    # Reference: https://stackoverflow.com/a/33623271/
    return heapq.nsmallest(n, range(len(l)), key=l.__getitem__)


def find_most_similar_game_names(query_name, num_matches=5):
    query_name_lower_case = query_name.lower()

    distances = [
        lv.distance(query_name_lower_case, s) for s in load_app_names_lower_case()
    ]

    indices = find_indices_of_nsmallest(num_matches, distances)

    ids = convert_indices_to_ids(indices)
    names = convert_indices_to_names(indices)

    data = [{"id": id, "name": name} for (id, name) in zip(ids, names)]

    return data


if __name__ == "__main__":
    data = find_most_similar_game_names(query_name="Crash Bandicoot", num_matches=5)
    print(data)