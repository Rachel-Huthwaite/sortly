"""
Core logic for scanning and organising files into categorised folders.
"""

import shutil
import os
from categories import FILE_CATEGORIES, SENSITIVE_EXTENSIONS, NEVER_MOVE


def scan_directory(directory):
    """
    Scans a given directory and categorises each file found.
    Returns a dictionary of categorised files and a list of sensitive files.
    """
    categorised_files = {}
    sensitive_files = []

    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)

        if not os.path.isfile(full_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        if ext in NEVER_MOVE:
            continue

        # Check if file is sensitive before categorising
        if _is_sensitive(ext):
            sensitive_files.append(full_path)
            continue

        matched_category = None
        for category, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                matched_category = category
                break

        if matched_category is None:
            matched_category = "Misc"

        if matched_category not in categorised_files:
            categorised_files[matched_category] = []

        categorised_files[matched_category].append(full_path)

    return categorised_files, sensitive_files


def organise_files(directory, categorised_files):
    """
    Takes the dictionary of categorised files and moves them into
    their respective subfolders within the target directory.
    Returns a summary of moved files and any errors.
    """
    summary = {"moved": [], "errors": []}

    for category, file_paths in categorised_files.items():
        category_dir = os.path.join(directory, category)
        os.makedirs(category_dir, exist_ok=True)

        for source_path in file_paths:
            filename = os.path.basename(source_path)
            destination_path = os.path.join(category_dir, filename)

            if os.path.exists(destination_path):
                destination_path = _handle_duplicate_name(destination_path)

            try:
                shutil.move(source_path, destination_path)
                summary["moved"].append((filename, category))
            except Exception as e:
                summary["errors"].append((filename, str(e)))

    return summary


def _is_sensitive(ext):
    """
    Checks if a file extension is in any sensitive category.
    Returns True if sensitive, False otherwise.
    """
    for extensions in SENSITIVE_EXTENSIONS.values():
        if ext in extensions:
            return True
    return False


def _handle_duplicate_name(filepath):
    """
    Appends a counter to the filename if a file with the same name already exists.
    e.g., 'document.pdf' becomes 'document_1.pdf'
    """
    base, ext = os.path.splitext(filepath)
    counter = 1

    while os.path.exists(f"{base}_{counter}{ext}"):
        counter += 1

    return f"{base}_{counter}{ext}"