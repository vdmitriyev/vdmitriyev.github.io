@echo off
REM @author Viktor Dmitriyev
cd ../blog/
popd .
python -m SimpleHTTPServer 8000
pushd .