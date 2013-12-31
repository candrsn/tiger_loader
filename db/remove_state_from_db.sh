#!/bin/bash

st=$1

if [ -z "$st" ]; then
  echo "usgae:"
  exit
fi

echo "SELECT 'DROP TABLE '||schemaname||'.'||tablename||';' from pg_tables
  WHERE schemaname = 't1992' and tablename like '%_$st';" | psql -t -A census > cmd.log 

echo "now!
psql census < cmd.log "
psql census < cmd.log

grep -v "^${st}" process.list > tmp.lst
mv tmp.lst process.list


