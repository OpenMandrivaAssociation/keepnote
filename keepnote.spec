Name:           keepnote
Version:        0.6.4
Release:        %mkrel 1
Group:          Development/Other
License:        GPLv2
Summary:        KeepNote lets you keep notes
Source:         keepnote-%{version}.tar.gz
URL:            http://rasm.ods.org/keepnote/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python-devel

%description
KeepNote is an application that lets organize your notes.
Keepnote replaces knowit (which is incompatible with kde4).

%prep
%setup -q

%build
#make

%install
%__rm -rf %{buildroot}
#mkdir -p %{buildroot}%{_bindir}
python setup.py install --prefix=%{buildroot}%_prefix --install-lib=%{buildroot}%{_libdir}/python2.6/site-packages
%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%_bindir/%name
%{py_platsitedir}
%{_datadir}/applications/keepnote.desktop
%{_datadir}/icons/hicolor/48x48/apps/keepnote.png


