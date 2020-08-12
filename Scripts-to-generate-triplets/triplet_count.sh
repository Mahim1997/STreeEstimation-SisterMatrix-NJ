#!/bin/sh

# it requires 64 bit machine
# usage inputfile outputfile
tmp=`mktemp`
#cat $1| xargs -I@ sh -c 'echo -n "@" >'$tmp'; /projects/sate7/tools/bin/triplets.soda2103 fancy printQuartets '$tmp';'
#cat $1| xargs -I@ sh -c 'echo -n "@" >'$tmp'; /projects/sate7/tools/bin/triplets.soda2103 printQuartets '$tmp';'|sed 's/.*: //'| python /u/bayzid/Research/simulation_study/tools/run_scripts/summarize.triplets.py


#cat $1| xargs -I@ sh -c 'echo -n "@" >'$tmp'; /projects/sate7/tools/bin/triplets.soda2103 printQuartets '$tmp';'|sed 's/.*: //' > $2

#cat $1| xargs -I@ sh -c 'echo -n "@" >'$tmp'; /projects/sate7/tools/bin/triplets.soda2103 printQuartets '$tmp';'|sed 's/.*: //' 

#cat $1| xargs -I@ sh -c 'echo -n "@" >'$tmp'; /projects/sate7/tools/bin/triplets.soda2103 printQuartets '$tmp';'|sed 's/.*: //'| sed 's/^/\(\(/'| sed 's/$/\)\)\;/'| sed 's/ | /\),\(/'| sed 's/ /\,/g';


#cat $1| xargs -I@ sh -c 'echo -n "@" >'$tmp'; /projects/sate7/tools/bin/triplets.soda2103 fancy printTriplets '$tmp'; echo "newgene"'|sed 's/.*: //'| sed 's/^/\(\(/'| sed 's/$/\)\)\;/'| sed 's/ | /\),\(/'| sed 's/ /\,/g';

#|sed 's/.*: //'| sed 's/^/\(\(/'| sed 's/$/\)\)\;/'| sed 's/ | /\),\(/'| sed 's/ /\,/g'

#printTriplets

#cat $1| xargs -I@ sh -c 'echo -n "@" >'$tmp'; /projects/sate7/tools/bin/triplets.soda2103 printTriplets '$tmp'; echo "newgene"'| sed 's/^/\(/' | sed 's/$/\)\)\;/' | sed 's/ | /,\(/'| sed 's/ /\,/g';


cat $1| xargs -I@ sh -c 'echo -n "@" >'$tmp'; ./triplets.soda2103 printTriplets '$tmp';'| sed 's/^/\(/' | sed 's/$/\)\)\;/' | sed 's/ | /,\(/'| sed 's/ /\,/g';
