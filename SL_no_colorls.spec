#
Summary: This will change the default ls behavior to no color
Name: SL_no_colorls
Version: 1.0
Release: 3
License: GPL
Group: SL
Vendor: Scientific Linux
Packager: Kevin Hill
Obsoletes: zz_no_colorls
BuildArchitectures: noarch
#requires: 
%description

This rpm removes the default color ls behavior by renaming /etc/profile.d/colorls.[c]sh 
 
%files
%post

#
# This will append a line to /etc/sysconfig/i18n iff it exists and
# doesn't contain a LC_COLLATE definition and the LANG is set 
#

file=/etc/profile.d/colorls

if [ -f $file.sh ] 
then
	mv $file.sh $file.sh.not
fi

if [ -f $file.csh ]
then
	mv $file.csh $file.csh.not
fi

%postun

file=/etc/profile.d/colorls

if [ -f $file.sh.not ]
then
	mv $file.sh.not $file.sh
fi

if [ -f $file.csh.not ]
then
	mv $file.csh.not $file.csh
fi

