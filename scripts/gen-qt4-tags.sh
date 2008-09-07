#!/bin/bash

QTDIR=\
" /usr/include/Qt/"\
" /usr/include/QtCore/"\
" /usr/include/Qt3Support/"\
" /usr/include/QtAssistant/"\
" /usr/include/QtDBus/"\
" /usr/include/QtDesigner/"\
" /usr/include/QtGui/"\
" /usr/include/QtNetwork/"\
" /usr/include/QtOpenGL/"\
" /usr/include/QtScript/"\
" /usr/include/QtSql/"\
" /usr/include/QtSvg/"\
" /usr/include/QtTest/"\
" /usr/include/QtUiTools/"\
" /usr/include/QtXml/"

echo $QTDIR

for dir in $QTDIR
do
	ctags -R --c++-kinds=+p --fields=+iaS --extra=+q -a -f qt4-tags $dir
done

