#!/bin/bash


input_folder=$2
output_name=$3

for (( c=1; c<=$1; c++))
do
	if [[ $c == 1 ]]; then
		output=1
		hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
		-file pagerank_mapper.py    -mapper pagerank_mapper.py \
		-file pagerank_reducer.py   -reducer pagerank_reducer.py \
		-input $input_folder -output "$output_name$output"
	else
		input="$output_name$(($c-1))"
		output=$c
		hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
		-file pagerank_mapper.py    -mapper pagerank_mapper.py \
		-file pagerank_reducer.py   -reducer pagerank_reducer.py \
		-input "$input" -output "$output_name$output"
	fi	

done

hdfs dfs -cat ./"$output_name$1"/part-00000 >> output.txt
