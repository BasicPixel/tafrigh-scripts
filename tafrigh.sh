tafrigh './audio/' -w $1 --output_formats txt -o './text/'
for file in ./text/*
do
	sed  's/ آآ //g;s/ اه //g' file
done
python3 $2
