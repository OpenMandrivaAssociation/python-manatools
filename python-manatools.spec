Name:		python-manatools
Version:	0.1
Release:	0.18.05.2019
Summary:	A python framework to build ManaTools application
Group:		System/Libraries
License:	LGPLv2+
URL:		https://github.com/manatools/python-manatools
Source0:	python-manatools-master-18.05.2019.zip

BuildRequires:	pkgconfig(libyui)
BuildRequires:  pkgconfig(libyui-mga)
BuildRequires:	pkgconfig(python)
BuildRequires:  python-libyui

%description
libYUI is a library written entirely in C++ to provide an abstraction layer
for Qt, GTK and ncurses UI frameworks. This means that a single code in YUI
can be used to produce outputs using any of the 3 UI frameworks listed above.
This library was (and still is) used to create the YaST2 User Interface. 
