"""
Organizing the different file types and what folders they will go into
As well as keeping into account Sensitive file types and file types that should never be moved
"""

#Most common file types
FILE_CATEGORIES = {
    "Images": [".jpeg", ".jpg", ".gif", ".png", ".webp", ".svg", ".bmp", ".tiff", ".heic"],
    "Videos": [".wmv", ".mov", ".mpg", ".mpeg", ".mkv", ".avi", ".mp4"],
    "Zips": [".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".zip"],
    "PDFs": [".pdf"],
    "Music": [".mp3", ".msv", ".wav", ".wma", ".aac", ".flac", ".ogg", ".aiff", ".aif", ".opus", ".amr", ".mid", ".midi", ".msv", ".ra", ".rm"],
    "Word_Documents" : [".doc", ".docx"],
    "Plain_Text": [".rtf", ".txt"],
    "SpreadSheets": [".numbers", ".ods", ".xlr", ".xls", ".xlsx"]
}

#File types you may not want to move
SENSITIVE_EXTENSIONS = {
    # Adobe design files — often linked to other assets, moving breaks those links
    "Adobe": [".psd", ".ai", ".indd", ".indb", ".idml", ".aep", ".prproj"],
    "3D_Animation": [".blend", ".c4d", ".ma", ".mb", ".fla", ".f4a"],
    "Code_Config": [".json", ".xml", ".env", ".yaml", ".yml", ".ini", ".cfg"],
}

#Files that would break your system if they moved
NEVER_MOVE = [".exe", ".dll", ".sys", ".bat", ".sh", ".inf", ".drv", ".dat", ".msi", ".swap", ".temp", ".lnk", ".app", ".cmd"]