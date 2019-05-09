#!/usr/bin/env bash
ndir="*/"
narr=($ndir)
darr=()
for d in ${narr[*]}
do
    [[ $d =~ (static|misc|init|template|api|scripts) ]] && darr+=($d)
done

for n in ${darr[*]}
do
    makePath=$n"migrations/"
    rm -R $makePath 2>/dev/null
    mkdir $makePath 2>/dev/null
    initPath=$makePath"__init__.py"
    touch $initPath 2>/dev/null
done

python3 manage.py makemigrations

for d in ${darr[*]}
do
    deletePath=$d"migrations/"
    rm -R $deletePath 2>/dev/null
done
