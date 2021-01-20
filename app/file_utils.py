import json
from pathlib import Path


def load_json(fname):
    with open(fname, "r", encoding="utf8") as f:
        data = json.load(f)
    return data


def get_data_folder():
    return "data/"


def get_fname_for_lower_case_texts():
    fname = get_data_folder() + "app_names_lower_case.json"
    return fname


def load_app_ids():
    fname = get_data_folder() + "app_ids.json"
    return [int(app_id) for app_id in load_json(fname)]


def load_app_names():
    fname = get_data_folder() + "app_names.json"
    return load_json(fname)


def convert_indices_to_ids(indices):
    app_ids = load_app_ids()
    return [app_ids[ind] for ind in indices]


def convert_indices_to_names(indices):
    app_names = load_app_names()
    return [app_names[ind] for ind in indices]


def generate_database_with_lower_case_text():
    app_names_lower_case = [s.lower() for s in load_app_names()]

    with open(get_fname_for_lower_case_texts(), "w", encoding="utf8") as f:
        json.dump(app_names_lower_case, f)

    return


def load_app_names_lower_case():
    fname = get_fname_for_lower_case_texts()
    if not Path(fname).exists():
        generate_database_with_lower_case_text()
    return load_json(fname)


if __name__ == "__main__":
    generate_database_with_lower_case_text()
