#!/bin/sh

FILE_NAME="./hh.json"
LENGTH="20"

NAME="${1/ /+}"

curl -k "https://api.hh.ru/vacancies?text=$NAME&per_page=$LENGTH" | jq > $FILE_NAME
