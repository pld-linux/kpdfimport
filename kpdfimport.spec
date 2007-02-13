
# TODO:
# - fails on sizeof(size_t) != sizeof(unsigned int)
# Fix build failure (at least with qt 3.0.5
#   transform.h: warning: 1 trigraph(s) encountered
#   FilterPage.cpp: In method `void PDFImport::Page::dump(const PDFImport::Paragraph &)':
#   FilterPage.cpp:568: ambiguous overload for `const PDFImport::Link *const & ? const char[2] : const QString &'
#   FilterPage.cpp:568: candidates are: operator ?:(bool, QString, QString) <builtin>
#   FilterPage.cpp:568:                 operator ?:(bool, const char *, const char *) <builtin>

Summary:	PDF import filter for KOffice (at the moment only for KWord)
Summary(pl.UTF-8):	Filtr importu pdf dla KOffice (aktualnie tylko dla KWorda)
Name:		kpdfimport
Version:	0.5
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kpdfimport/%{name}-%{version}.tar.bz2
# Source0-md5:	222ecf1f2c9b5775e935e48c169dd1f5
URL:		http://sourceforge.net/projects/kpdfimport/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	koffice-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PDF import filter for KOffice (at the moment only for KWord). It
currently imports text with formatting (font, color, tabulations) and
images.

%description -l pl.UTF-8
Filtr importujący pliki pdf dla pakietu KOffice (aktualnie tylko dla
KWord). Aktualnie importuje tekst z formatowaniem (font, kolor,
tabulacje) oraz obrazki.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* admin
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc kpdfimport/README kpdfimport/CHANGELOG kpdfimport/TODO
%defattr(644,root,root,755)
%{_libdir}/kde3/*
%{_datadir}/services/*
