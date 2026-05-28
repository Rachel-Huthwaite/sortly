"""
Core logic for scanning and organising files into categorised folders.
"""

import os
from categories import FILE_CATEGORIES, SENSITIVE_EXTENSIONS, NEVER_MOVE


def scan_directory(directory):
    """
    Scans a given directory and categorises each file found.
    Returns a dictionary of categorised files.
    """
    categorised_files = {}

    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)

        # Skip folders, only process files
        if not os.path.isfile(full_path):
            continue

        # Get the file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Skip files that should never move
        if ext in NEVER_MOVE:
            continue

        # Check which category it belongs to
        matched_category = None
        for category, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                matched_category = category
                break

        # Files that don't match any category go to Misc
        if matched_category is None:
            matched_category = "Misc"

        # Add to categorised_files
        if matched_category not in categorised_files:
            categorised_files[matched_category] = []

        categorised_files[matched_category].append(full_path)

    return categorised_files