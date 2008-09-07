%define name    qipmsg
%define version 0.9.5
%define dist .fc9
%define release 1

%define is_mandrake %(test -e /etc/mandrake-release && echo 1 || echo 0)
%define is_suse %(test -e /etc/SuSE-release && echo 1 || echo 0)
%define is_fedora %(test -e /etc/fedora-release && echo 1 || echo 0)
%define qmake qmake
%define lrelease lrelease

%if %is_fedora
%define distr %(cat /etc/fedora-release)
%define qmake qmake-qt4
%define lrelease lrelease-qt4
%endif
%if %is_suse
%define distr %(head -1 /etc/SuSE-release)
%endif
%if %is_mandrake
%define distr %(cat /etc/mandrake-release)
%endif

Name:           %{name}
Summary:        Chat and transfer file over local network
License:        GPL
Group:          Applications/Network
URL:            http://code.google.com/p/qipmsg/
Version:        %{version}
Release:        %{release}%{dist}

Source0:        %{name}-%{version}.tar.bz2

Packager:       Yichi Zhang <zyichi@gmail.com>
Distribution:   %{distr}
BuildRoot:      %{_tmppath}/%{name}-buildroot
Autoreqprov:    On

BuildRequires: desktop-file-utils
BuildRequires: qt4-devel

%description
qipmsg is a IP Messenger clone for linux platforms. Visit
http://www.ipmsg.org/index.html.en for more info about IP Messenger.
qipmsg is developed with the Qt toolkit.

%prep
%setup -q

# fix path of docs
sed -i 's|DOC_PATH=$(PREFIX)/share/doc/qipmsg|DOC_PATH=$(PREFIX)/share/doc/qipmsg-%{version}|' Makefile

# use %{?_smp_mflags}
sed -i '/cd src && $(QMAKE) $(QMAKE_OPTS) && $(DEFS) make/s!$! %{?_smp_mflags}!' Makefile

%build
make PREFIX=/usr QMAKE=%{qmake} LRELEASE=%{lrelease}

%install
make PREFIX=/usr DESTDIR=%{?buildroot:%{buildroot}} install

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
touch --no-create %{_datadir}/pixmaps
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database &> /dev/null || :

%postun
touch --no-create %{_datadir}/icons/hicolor
touch --no-create %{_datadir}/pixmaps
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database &> /dev/null || :

%files
%defattr (-,root,root,-)
# %doc Copying.txt ChangeLog PROT-ENG.TXT Install.txt ReleaseProcess.txt
%{_docdir}/%{name}-%{version}/
%{_bindir}/qipmsg
%{_bindir}/qipmsg-xdg-open
%{_datadir}/applications/qipmsg.desktop
%{_datadir}/pixmaps/qipmsg.png
%{_datadir}/icons/hicolor/*/apps/qipmsg.png
%{_datadir}/qipmsg/translations/qipmsg_zh_CN.qm
%{_datadir}/qipmsg/sounds/*.wav
%{_datadir}/qipmsg/icons/*.xpm
%{_datadir}/qipmsg/

%changelog
* Mon Jul 22 2008 Yichi Zhang <zyichi@gmail.com>
  - first spec file
