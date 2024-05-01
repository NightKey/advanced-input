@echo off
SET name=advanced_input
echo "Deleting dist"
del /Q dist\*
echo "Creating DLL file"
call createdll.bat
echo "Creating SO file with WSL"
wsl bash createso.sh
echo "Building Module"
python -m build
pause
echo "Uploading Module"
python -m twine upload dist/*
pause
echo "Forcing release of new version"
python -m pip install --upgrade %name%
echo "Installing new version"
python -m pip install --upgrade %name%
