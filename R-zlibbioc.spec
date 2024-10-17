%global packname  zlibbioc
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.8.0
Release:          2
Summary:          An R packaged zlib-1.2.5
Group:            Sciences/Mathematics
License:          Artistic-2.0 + file LICENSE
URL:              https://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/zlibbioc_1.8.0.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    zlib-devel

%description
This package uses the source code of zlib-1.2.5 to create libraries for
systems that do not have these available via other means (most Linux and
Mac users should have system-level access to zlib, and no direct need for
this package). See the vignette for instructions on use.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

