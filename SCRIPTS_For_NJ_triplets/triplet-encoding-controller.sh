#!/bin/sh

usage ()
{
  echo 'Usage : triplet-encoding-controller.sh <input-genetree-file> <output-triplet_list>'
  exit
}

if [ "$#" -ne 2 ]
then
  usage
fi

#sh triplet_count.sh $1 | perl summarize_triplets_stdin.pl > $2
rm -f $2 	#To remove the output file just in case 
sh triplet_count.sh $1 $PWD| perl summarize_triplets_stdin.pl > $2 	#To pass the PATH as parameter to the shell script triplet_count.sh
