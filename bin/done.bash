#!/bin/bash

today=`date '+%Y-%m-%d %H:%M:%S'`

git add .
git commit -m "$today"

git status

read -p "ok? (y/N): " yn
case "$yn" in [yY]*) ;; *) echo "abort." ; exit ;; esac

git push origin main