# About
## PackageImporter is a simple project for importing projects according to different types (DataScience, Plotting, etc.)
# Installation
## To install PackageImporter, run this command into your terminal (Use Windows Powershell because I love it):
### pip install packageimporter
## For a specific version, run:
### pip install packageimporter=={version}
## To upgrade the exsisting PackageImporter module (which you probably don't):
### pip install --upgrade packageimporter
## note: you can either use python -m pip or py -m pip if it's different. (It may) PackageImporter has only one limitation: Python>=3.6 (Because there are f-strings)

# Usage Example
## from packageimporter import Importer
## Importer.stable.Plotter.plotly.express(alias="i_love_plotly_express")
## # This will import plotly.express as i_love_plotly_express (weird alias) and raise an ModuleNotFoundError if plotly.express is not globally installed.

# Update Notes:
## Added "ScienceAndMaths" Class that supports scipy and sympy
## Added "MyOwnModules" Class to import my own simple modules from PyPI
## Added "PackageImporterVersionCheck" Class to check the version.
## Fixed some minor grammartical issues with the README.md file#   P a c k a g e I m p o r t e r 
 
 
