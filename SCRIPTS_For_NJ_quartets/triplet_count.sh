#Author: Md. Shamsuzzoha Bayzid
#!/bin/sh

# it requires 64 bit machine
# usage inputfile outputfile
tmp=`mktemp`
#cat $1| xargs -I@ sh -c 'echo -n "@" >'$tmp'; /projects/sate7/tools/bin/triplets.soda2103 fancy printQuartets '$tmp';'

#Here, $2 is the parameter PATH given to by the shell triplet-encoding-controller.sh
cat $1| xargs -I@ sh -c "echo -n '@' >'$tmp'; $2/triplets.soda2103 printTriplets '$tmp';"| sed 's/^/\(/' | sed 's/$/\)\)\;/' | sed 's/ | /,\(/'| sed 's/ /\,/g';