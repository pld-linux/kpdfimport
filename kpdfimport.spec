
# TODO:
# Fix build failure (at least with qt 3.0.5
#   transform.h: warning: 1 trigraph(s) encountered
#   FilterPage.cpp: In method `void PDFImport::Page::dump(const PDFImport::Paragraph &)':
#   FilterPage.cpp:568: ambiguous overload for `const PDFImport::Link *const & ? const char[2] : const QString &'
#   FilterPage.cpp:568: candidates are: operator ?:(bool, QString, QString) <builtin>
#   FilterPage.cpp:568:                 operator ?:(bool, const char *, const char *) <builtin>

Summary:	PDF import filter for KOffice (at the moment only for KWord).
Summary(pl):	Filtr importu pdf dla KOffice (aktualnie tylko dla KWorda).
Name:		kpdfimport
Version:	0.5
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/kpdfimport/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
PDF import filter for KOffice (at the moment only for KWord). It
currently imports text with formatting (font, color, tabulations) and
images.

%description -l pl
Filtr importuj±cy pliki pdf dla pakietu KOffice (aktualnie tylko dla
KWord). Aktualnie importuje tekst z formatowaniem (font, kolor,
tabulacje) oraz obrazki.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
kde_appsdir="%{_applnkdir}"; export kde_appsdir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc
%defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/%{name}
# %{_datadir}/apps/%{name}/*.rc
# %{_applnkdir}/Applications/%{name}.desktop
# %{_pixmapsdir}/*/*/apps/%{name}.png
