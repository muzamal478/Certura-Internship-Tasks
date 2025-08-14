# Task 2: Automate File Organization 🗂️

## Description
Python script organizes files by type using os/shutil. Inputs directory, creates subfolders, moves files based on extensions.

## Objective
Automate file sorting to learn directory ops and efficiency.

## Features
- Path validation.
- Subfolders: Images, Documents, Videos, Others.
- Customizable extensions.
- Skips non-files; catch-all for unknowns.

## Usage
Run: `python file_organizer.py`
Input: e.g., C:\TestFolder

## Example Input/Output
Input: /path/with/files (photo.jpg, doc.pdf)
Output:
Moved photo.jpg to Images
Moved doc.pdf to Documents
Files organized successfully!

## Edge Cases
- Empty dir: No action.
- Invalid path: Reprompt.
- Unknown ext: To Others.

Video demo on LinkedIn. Add extensions as needed.

"The only place success comes before work is in the dictionary" - Vidal Sassoon

Author: Muzamal Asghar | Date: August 14, 2025