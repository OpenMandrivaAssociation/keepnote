Name:		keepnote
Version:	0.7.7
Release:	3
Group:		Development/Other
License:	GPLv2
Summary:	Lets you keep notes
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
python setup.py install --root=%{buildroot}

#find_lang causes problems here

%clean

%files
%{_bindir}/%{name}
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py%{py_ver}.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Tue Feb 14 2012 Andrey Bondrov <abondrov@mandriva.org> 0.7.7-1mdv2011.0
+ Revision: 774032
- New version 0.7.7

* Sun Jul 03 2011 Jani Välimaa <wally@mandriva.org> 0.7.3-1
+ Revision: 688595
- new version 0.7.3

* Wed Jun 01 2011 Jani Välimaa <wally@mandriva.org> 0.7.2-1
+ Revision: 682298
-new version 0.7.2

* Sun Apr 03 2011 Jani Välimaa <wally@mandriva.org> 0.7-1
+ Revision: 649993
- new version 0.7
- drop buildroot definition
- minor .spec cleanup

* Wed Nov 24 2010 Jani Välimaa <wally@mandriva.org> 0.6.7-1mdv2011.0
+ Revision: 600405
- new version 0.6.7
- fix .desktop file

* Sat Nov 20 2010 Olivier Faurax <ofaurax@mandriva.org> 0.6.6-3mdv2011.0
+ Revision: 599267
- adding correct sources
- New version + use URL as Source

* Sat Nov 20 2010 Olivier Faurax <ofaurax@mandriva.org> 0.6.5-3mdv2011.0
+ Revision: 599263
- rebuild

* Sat Nov 06 2010 Jani Välimaa <wally@mandriva.org> 0.6.5-2mdv2011.0
+ Revision: 594289
- tag package as noarch
- install files to python_sitelib

* Sat Oct 23 2010 Olivier Faurax <ofaurax@mandriva.org> 0.6.5-1mdv2011.0
+ Revision: 587596
- new version 0.6.5

* Thu Aug 19 2010 Olivier Faurax <ofaurax@mandriva.org> 0.6.4-1mdv2011.0
+ Revision: 571380
- New version 0.6.4
- Corrections from Nicnlecureuil: use %%_datadir rather than %%_prefix/share
- lang handling
- don't own system dirs

* Sat Mar 13 2010 Olivier Faurax <ofaurax@mandriva.org> 0.6.2-1mdv2010.1
+ Revision: 518619
- New version 0.6.2
- Revert unneeded dependency
- Added libpython-devel dependency

* Thu Dec 24 2009 Olivier Faurax <ofaurax@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 481932
- Missing python-devel dependency
--install-lib for 64bits build
- import keepnote


