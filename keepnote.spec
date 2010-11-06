Name:           keepnote
Version:        0.6.5
Release:        %mkrel 2
Group:          Development/Other
License:        GPLv2
Summary:        KeepNote lets you keep notes
Source:         keepnote-%{version}.tar.gz
URL:            http://rasm.ods.org/keepnote/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel

%description
KeepNote is an application that lets organize your notes.
Keepnote replaces knowit (which is incompatible with kde4).

%prep
%setup -q

%build

%install
%__rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%_bindir/%name
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py%{py_ver}.egg-info
%{_datadir}/applications/keepnote.desktop
%{_datadir}/icons/hicolor/48x48/apps/keepnote.png
