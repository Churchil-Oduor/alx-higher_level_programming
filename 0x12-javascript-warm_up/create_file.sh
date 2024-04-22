#!/usr/bin/bash

# This bash code creates a new file
# that contains the repeated formats required
# in the projects.

template="template_file.js"

if [ $# -ge 1 ]; then
	for arg in "$@"; do
		cp $template $arg
	done
else
	echo "No variables have been passed"

fi
