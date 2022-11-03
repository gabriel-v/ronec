#!/bin/bash
set -ex
for pattern in 'î/i' 'ă/a' 'â/a' 'ș/s' 'ț/t' 'Î/I' 'Ă/A' 'Â/A' 'Ș/S' 'Ț/T'; do
	for i in $(ls *.json); do
		sed -i.bak "s/$pattern/g" $i
		rm $i.bak
	done
done
