#!/bin/bash
#Author: timger <yishenggudou@gmail.com>
#weibo <http://t.sina.com/zhanghaibo>
#@yishenggudou http://twitter.com/yishenggudou
filepath=$1
sofilename=`echo "${filepath}"|awk -F '.' '{print $1}'`
sofile="${sofilename}.so"
cfile="${sofilename}.c"
execfile="${sofilename}.sh"
macpython="/usr/local/Cellar/python/2.7.5/Frameworks/Python.framework/Versions/2.7/include/python2.7"
if ! [ -z "${filepath}" ]
then
    cython ${filepath} -o ${cfile}
    if [ -d "${macpython}" ]
    then
        echo gcc -shared -o ${sofile} ${cfile} -I${macpython}  -fPIC
        echo "mac "
        gcc -shared -o ${sofile} ${cfile} -I${macpython} -fPIC
    else
        echo gcc -shared -o ${sofile} ${cfile} -I/usr/include/python2.6/ -fPIC
        echo "linux"
        gcc -shared -o ${sofile} ${cfile} -I/usr/include/python2.6 -fPIC
    fi
    echo "compress to ${filepath} => ${cfile} => ${sofile}"
else
    echo "usage sh $0 xx.pyx"
fi
