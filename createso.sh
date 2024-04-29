#!/bin/sh
base="$(dirname "$0")"
code="$(cd "${base}/advanced_input"; pwd)"

gcc -shared -o $code/inputExtention.so -fPIC $code/inputExtention.c -D LINUX
