#!/bin/bash

for i in {1..1500}
do
  echo "print('committed successfully')" >> commit.py
  git add .
  git commit -m "committed ad commit py file"
done

