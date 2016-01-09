%define		pkg	init-package-json
Summary:	A node module to get your node module started
Name:		nodejs-%{pkg}
Version:	0.0.17
Release:	1
License:	ISC
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	e5649ebd0ae17cb40160a3d85810c8a7
URL:		https://github.com/isaacs/init-package-json
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-glob < 3.3.0
Requires:	nodejs-glob >= 3.2.7
Requires:	nodejs-promzard < 0.3.0
Requires:	nodejs-promzard >= 0.2.0
Requires:	nodejs-read < 1.1.0
Requires:	nodejs-read >= 1.0.1
Requires:	nodejs-read-package-json < 2
Requires:	nodejs-read-package-json >= 1
Requires:	nodejs-semver <= 3.0.0
Requires:	nodejs-semver >= 2.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A node module to get your node module started.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -a package.json default-input.js %{pkg}.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
