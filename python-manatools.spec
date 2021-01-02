%global debug_package %{nil}

Name:		python-manatools
Version:	0.0.3
Release:	1
Summary:	A python framework to build ManaTools application
Group:		System/Libraries
License:	LGPLv2+
URL:            https://github.com/manatools/python-manatools
Source0:        https://github.com/manatools/python-manatools/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(libyui)
BuildRequires:  pkgconfig(libyui-mga)
BuildRequires:  pkgconfig(libyui-qt)
BuildRequires:	pkgconfig(python)
BuildRequires:  python-libyui
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pyyaml)

Requires: python3dist(dbus-python)
Requires: python3dist(python-gettext)
Requires: python3dist(setuptools)
Requires: python-libyui

%description
Python ManaTools starts from the experience of tools and framework written in Perl, since most systemd and dbus API are python based instead a this way seemed to be natural.
Python ManaTools aim is to help in writing tools based on libYui (Suse widget abstraction library), to be collected under the same ManaTool hat and hopefully with the same look and feel.
Every output modules can of course be run using QT, Gtk or ncurses interface.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/manatools/*
%{python_sitelib}/python_manatools*
