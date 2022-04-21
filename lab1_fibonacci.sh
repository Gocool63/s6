read -p "Enter the number of numbers in the series: " N

A=0
B=1
C=1

echo $A
if [ $N != 1 ]
then
	echo $B
fi
N=`expr $N - 2`

while [ $N -gt 0 ]
do
	echo $C
	A=$B
	B=$C
	C=`expr $A + $B`
        N=`expr $N - 1`	
done