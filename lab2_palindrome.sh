echo "Enter the string:" 
read STRING

LENGTH=${#STRING}
REVERSE=""

for (( i=$LENGTH-1; i>=0; i-- ))
do
	REVERSE="$REVERSE${STRING:$i:1}"
done

if [ $STRING == $REVERSE ]
then
	echo "$STRING is palindrome"
else
	echo "$STRING is not palindrome"
fi