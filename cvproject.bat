@echo off

if [%1]==[] goto usage

rmdir /s /q .vs_proj

mkdir .vs_proj

pushd .vs_proj

cmake .. -A Win32 -DCMAKE_BUILD_TYPE=%1

popd

@echo Project make done!
goto :eof

:usage
@echo Usage: %0 ^<build_type^>
PAUSE
exit /B 1