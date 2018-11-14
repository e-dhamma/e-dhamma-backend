#!/bin/bash

set -e  # exit script if any command exits with error
set -u  # exit script with error if any variable is undefined

cd "$( dirname "$0" )/.." # move to git base dir

[[ $(git status --porcelain) == "" ]] || { echo "FAIL: Git status dirty, see 'git status' output:"; git status; exit 1; }

