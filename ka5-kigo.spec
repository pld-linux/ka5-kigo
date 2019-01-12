%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kigo
Summary:	kigo
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2c1563f5fe28911f794e5b03dc5d2eeb
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-kio-devel >= 5.30.0
BuildRequires:	kf5-knewstuff-devel >= 5.30.0
BuildRequires:	kf5-ktextwidgets-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kigo is an open-source implementation of the popular Go game.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kigo-games.knsrc
/etc/xdg/kigo.knsrc
%attr(755,root,root) %{_bindir}/kigo
%{_desktopdir}/org.kde.kigo.desktop
%{_datadir}/config.kcfg/kigo.kcfg
%{_iconsdir}/hicolor/128x128/apps/kigo.png
%{_iconsdir}/hicolor/16x16/apps/kigo.png
%{_iconsdir}/hicolor/22x22/apps/kigo.png
%{_iconsdir}/hicolor/32x32/apps/kigo.png
%{_iconsdir}/hicolor/48x48/apps/kigo.png
%{_iconsdir}/hicolor/64x64/apps/kigo.png
%{_datadir}/kigo
%{_datadir}/kxmlgui5/kigo
%{_datadir}/metainfo/org.kde.kigo.appdata.xml
