Name:           spotipy
Version:        2.12.0
Release:        1%{?dist}
Summary:        A light weight Python library for the Spotify Web API
License:        MIT
URL:            http://spotipy.readthedocs.org/
BuildArch:      noarch

Source0:        https://github.com/plamere/spotipy/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
%autosetup

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
* Sun Jun 14 2020 Simone Caronni <negativo17@gmail.com> - 2.12.0-1
- First build.
