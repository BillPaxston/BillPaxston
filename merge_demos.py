#!/usr/bin/env python3
"""Overwrite template_X.html with template_X_demo.html content, then delete demos."""

import os
import shutil

BASE = "C:/claude_projects"

templates = [
    "restaurant",
    "dental",
    "massage",
    "school",
    "cafe",
    "gym",
    "chiro",
    "nail",
    "realestate",
]

for name in templates:
    demo = os.path.join(BASE, f"template_{name}_demo.html")
    tpl  = os.path.join(BASE, f"template_{name}.html")
    if os.path.exists(demo):
        shutil.copy2(demo, tpl)
        os.remove(demo)
        print(f"OK: template_{name}.html ← demo (demo deleted)")
    else:
        print(f"SKIP: template_{name}_demo.html not found")

print("\nDone.")
