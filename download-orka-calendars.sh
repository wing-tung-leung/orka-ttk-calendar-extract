#!/bin/bash

# requirements
#  - manual construct senior-html.txt and junior-html.txt lists with URL links
#  - copy session cookie "MySession" from browser

for i in `cat senior-html.txt `;
do
	echo $i;
	name=`echo $i | sed 's/.*_\(.\)/orka-\1.html/g'`;
	echo $name;
	wget --header "Cookie: MySession=94185980a2b34ffcb434063207c4d4f3" $i -O $name;
done

for i in `cat junior-html.txt `;
do
	echo $i;
	name=`echo $i | sed 's/.*_\(.\)/junior-\1.html/g'`;
	echo $name;
	wget --header "Cookie: MySession=94185980a2b34ffcb434063207c4d4f3" $i -O $name;
done

