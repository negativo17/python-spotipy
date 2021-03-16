%global real_name spotipy

Name:           python-spotipy
Version:        2.17.1
Release:        1%{?dist}
Summary:        A light weight Python library for the Spotify Web API
License:        MIT
URL:            http://spotipy.readthedocs.org/
BuildArch:      noarch

Source0:        https://github.com/plamere/%{real_name}/archive/%{version}.tar.gz#/%{real_name}-%{version}.tar.gz
Patch0:         %{real_name}-lower-requirements.patch

BuildRequires:  python3-devel

%description
Spotipy is a lightweight Python library for the Spotify Web API. With Spotipy
you get full access to all of the music data provided by the Spotify platform.

%package     -n python3-spotipy
Summary:        A light weight Python library for the Spotify Web API

%description -n python3-spotipy
Spotipy is a lightweight Python library for the Spotify Web API. With Spotipy
you get full access to all of the music data provided by the Spotify platform.

%prep
%autosetup -p1 -n %{real_name}-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

#%check
#%{__python3} setup.py test

%files -n python3-spotipy
%license LICENSE.md
%doc CHANGELOG.md README.md
%{python3_sitelib}/*

%changelog
* Tue Mar 16 2021 Simone Caronni <negativo17@gmail.com> - 2.17.1-1
- Update to 2.17.1.

* Thu Nov 05 2020 Simone Caronni <negativo17@gmail.com> - 2.16.1-1
- Update to 2.16.1.

* Tue Oct 06 2020 Simone Caronni <negativo17@gmail.com> - 2.16.0-1
- Update to 2.16.0.

* Wed Jul 08 2020 Simone Caronni <negativo17@gmail.com> - 2.13.0-1
- Update to 2.13.0.

* Sun Jun 14 2020 Simone Caronni <negativo17@gmail.com> - 2.12.0-1
- First build.
