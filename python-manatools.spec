%define module manatools
%define oname python_manatools

Name:		python-manatools
Version:	0.99.2
Release:	3
Summary:	Framework to build ManaTools applications
Group:		Development/Python
License:	LGPL-2.0-or-later
URL:		https://github.com/manatools/python-manatools
Source0:	https://github.com/manatools/python-manatools/archive/%{version}/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	gettext
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
%{name} builds on the original Perl-based ManaTools idea, keeping
the same goal of a shared toolkit and consistent UX while moving to Python to
match systemd and D-Bus APIs.

We are grateful to libyui for the foundation it provided, but this project
now ships its own AUI layer and keeps evolving independently.

Today it focuses on a backend-agnostic UI abstraction for GTK, Qt, and
ncurses, plus the services and helpers needed by ManaTools.

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{oname}-%{version}.dist-info


%package qt
Summary:	Metapackage for %{name}: qt extra
Group:		Development/Python
Requires:	python%{pyver}dist(python-manatools) = %{EVRD}
Requires:	pyside6-core
Requires:	pyside6-gui
Requires:	pyside6-widgets

%description -n %{name}-qt
This is a metapackage bringing in Qt extra requirements for %{name}.
It contains no code and only ensures that the Qt dependencies are installed.

%files qt
# intentionally blank for meta package

%package gtk
Summary:	Metapackage for %{name}: gtk extra
Group:		Development/Python
Requires:	python%{pyver}dist(python-manatools) = %{EVRD}
Requires:	python%{pyver}dist(pycairo)
Requires:	python%{pyver}dist(pygobject)
Requires:	typelib(GLib)
Requires:	typelib(GObject)
Requires:	typelib(Gdk) = 4.0
Requires:	typelib(GdkPixbuf) = 2.0
Requires:	typelib(Gio) = 2.0
Requires:	typelib(Gtk) = 4.0
Requires:	typelib(Pango)

%description -n %{name}-gtk
This is a metapackage bringing in GTK extra requirements for %{name}.
It contains no code and only ensures that the GTK dependencies are installed.

%files gtk
# intentionally blank for meta package

%prep -a
# Fix shebangs
sed -i 's:^#!/usr/bin/env python3:#!%{__python}:' \
	manatools/aui/backends/curses/radiobuttoncurses.py \
	manatools/aui/yui.py

%install -a
# Set executable bit on installed python scripts
chmod +x %{buildroot}%{python_sitelib}/manatools/aui/backends/curses/radiobuttoncurses.py \
	%{buildroot}%{python_sitelib}/manatools/aui/yui.py

