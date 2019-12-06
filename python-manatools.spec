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
BuildRequires:  pkgconfig(libyui-qt)
BuildRequires:	pkgconfig(python)
BuildRequires:  python-libyui
BuildRequires:  python3egg(setuptools)
BuildRequires:  python3egg(pyyaml)

Requires:  python-distribute

%description
Python ManaTools starts from the experience of tools and framework written in Perl, since most systemd and dbus API are python based instead a this way seemed to be natural.
Python ManaTools aim is to help in writing tools based on libYui (Suse widget abstraction library), to be collected under the same ManaTool hat and hopefully with the same look and feel.
Every output modules can of course be run using QT, Gtk or ncurses interface.

%prep
%setup -q -n python-manatools-master
%autopatch -p1

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{python_sitelib}/manatools/*
%{python_sitelib}/python_manatools*
