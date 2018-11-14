#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR
fab -u herbfoods -H aed.herbfoods.eu:10376 deploy
