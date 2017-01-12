#!/bin/bash
for f in `svn status | awk '{print $2}'` ;do
	sed -i  "/Copyright/ s/\([0-9]\+\) \([0-9]\+\)/\1-2017/" $f
done
