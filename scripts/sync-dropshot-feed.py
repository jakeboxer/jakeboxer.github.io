#!/usr/bin/env python3
"""Copy the canonical Dropshot feed to the URL used by older installed apps."""
from pathlib import Path
from shutil import copyfile
from xml.etree import ElementTree

root = Path(__file__).resolve().parents[1]
source = root / "dropshot/appcast.xml"
ElementTree.parse(source)
destination = root / "Dropshot-releases/appcast.xml"
destination.parent.mkdir(exist_ok=True)
copyfile(source, destination)
print("Updated Dropshot-releases/appcast.xml from dropshot/appcast.xml")
