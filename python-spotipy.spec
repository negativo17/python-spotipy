%global real_name spotipy

Name:           python-spotipy
Version:        2.19.0
Release:        3%{?dist}
Summary:        A light weight Python library for the Spotify Web API
License:        MIT
URL:            http://spotipy.readthedocs.org/
BuildArch:      noarch

Source0:        https://github.com/plamere/%{real_name}/archive/%{version}.tar.gz#/%{real_name}-%{version}.tar.gz
Patch0:         %{real_name}-lower-requirements.patch

BuildRequires:  python3-devel
#BuildRequires:  python3dist(pytest)

%global _description %{expand:
Spotipy is a lightweight Python library for the Spotify Web API. With Spotipy
you get full access to all of the music data provided by the Spotify platform.}

%description %_description

%package     -n python3-spotipy
Summary:        %{summary}

%description -n python3-spotipy %_description

%prep
%autosetup -p1 -n %{real_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files spotipy

%check
# Requires network:
#tox
%py3_check_import %{real_name}

%files -n python3-spotipy -f %{pyproject_files}
%license LICENSE.md
%doc CHANGELOG.md README.md

%changelog
* Mon Sep 27 2021 Simone Caronni <negativo17@gmail.com> - 2.19.0-3
- Update SPEC file for current packaging guidelines.

* Wed Sep 22 2021 Fabio Valentini <decathorpe@gmail.com> - 2.19.0-2
- Add BR: python3-setuptools to fix build on Fedora 35+.

* Fri Sep 17 2021 Simone Caronni <negativo17@gmail.com> - 2.19.0-1
- Update to 2.19.0.

* Thu May 27 2021 Simone Caronni <negativo17@gmail.com> - 2.18.0-1
- Update to 2.18.0.

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
