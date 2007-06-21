Summary:	grandr - GTK+ application to configure RandR
Summary(pl.UTF-8):	grandr - aplikacja GTK+ do konfiguracji RandR
Name:		xorg-app-grandr
Version:	0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/grandr-%{version}.tar.bz2
# Source0-md5:	e265c8e89aab39c55cb24ad8230c3933
Patch0:		%{name}-gconf.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXrandr-devel >= 1.2
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXrandr >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
grandr - GTK+ application to configure RandR.

%description -l pl.UTF-8
grandr - aplikacja GTK+ do konfiguracji RandR.

%prep
%setup -q -n grandr-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/grandr
