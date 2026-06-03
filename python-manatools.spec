%define module manatools
%define oname python_manatools

Name:		python-manatools
Version:	0.99.2
Release:	1
Summary:	Framework to build ManaTools applications
Group:		System/Libraries
License:	LGPL-2.0-or-later
URL:		https://github.com/manatools/python-manatools
Source0:	https://github.com/manatools/python-manatools/archive/%{version}/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)
# Provide these as we cannot know beforehand which UI frameworks consumers
# are using with manatools.
# Qt support
Requires:	python%{pyver}dist(pyside6)
# GTK support
Requires:	python%{pyver}dist(pycairo)
Requires:	python%{pyver}dist(pygobject)


%description
%{name} builds on the original Perl-based ManaTools idea, keeping
the same goal of a shared toolkit and consistent UX while moving to Python to
match systemd and D-Bus APIs.

We are grateful to libyui for the foundation it provided, but this project
now ships its own AUI layer and keeps evolving independently.

Today it focuses on a backend-agnostic UI abstraction for GTK, Qt, and
ncurses, plus the services and helpers needed by ManaTools.

%prep -a
# Fix shebangs
sed -i 's:^#!/usr/bin/env python3:#!%{__python}:' \
	manatools/aui/backends/curses/radiobuttoncurses.py \
	manatools/aui/yui.py

%install -a
# Set executable bit on installed python scripts
chmod +x %{buildroot}%{python_sitelib}/manatools/aui/backends/curses/radiobuttoncurses.py \
	%{buildroot}%{python_sitelib}/manatools/aui/yui.py

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{oname}-%{version}.dist-info
