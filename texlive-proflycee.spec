Name:		texlive-proflycee
Version:	64967
Release:	1
Summary:	A LaTeX package for French maths teachers in high school
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/proflycee
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proflycee.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proflycee.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides some commands to help French mathematics
teachers for 15-18 years olds, for example: \SplineTikz to
create splines with "derivative control";
\CalculFormelParametres and \CalculFormelLigne in order to
create an xcas-windows-like; \CodePythonLstFichier to create
code presentation and code execution with pythontex.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/proflycee
%doc %{_texmfdistdir}/doc/latex/proflycee

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
