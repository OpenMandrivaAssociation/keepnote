Name:		keepnote
Version:	0.7.7
Release:	%mkrel 1
Group:		Development/Other
License:	GPLv2
Summary:	KeepNote lets you keep notes
Source:		http://rasm.ods.org/keepnote/download/keepnote-%{version}.tar.gz
URL:		http://rasm.ods.org/keepnote/
BuildArch:	noarch
BuildRequires:	python-devel

%description
KeepNote is an application that lets organize your notes.
Keepnote replaces knowit (which is incompatible with kde4).

%prep
%setup -q

#fix desktop file, add ; to end of Categories list
%__sed -i -e 's|\(Categories.*\)|\1;|' desktop/keepnote.desktop

%build

%install
%__rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

#find_lang causes problems here

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py%{py_ver}.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
