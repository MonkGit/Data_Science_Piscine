#!/bin/sh

OUT_FILE=concatenator.csv

echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > $OUT_FILE
cat 20*.csv | sed -En '/^"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"$/!p' >> $OUT_FILE