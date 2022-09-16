#!/bin/sh

FILE_NAME="./hh.json"
LENGTH="20"

SEARCH_PARAMS="${1/ /+}"

curl -s -k -H 'User-Agent: api-test-agent' "https://api.hh.ru/vacancies?text=$SEARCH_PARAMS&per_page=$LENGTH" | jq > $FILE_NAME
