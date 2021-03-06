# revision 33276
# category Package
# catalog-ctan /macros/latex/contrib/fontaxes
# catalog-date 2014-03-23 16:44:03 +0100
# catalog-license lppl1.3
# catalog-version 1.0d
Name:		texlive-fontaxes
Version:	1.0d
Release:	6
Summary:	Additional font axes for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fontaxes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontaxes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontaxes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontaxes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package adds several new font axes on top of LaTeX's New
Font Selection Scheme. In particular, it splits the shape axis
into a primary and a secondary shape axis, and it adds three
new axes to deal with the different figure versions offered by
many professional fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fontaxes/fontaxes.sty
%doc %{_texmfdistdir}/doc/latex/fontaxes/README
%doc %{_texmfdistdir}/doc/latex/fontaxes/fontaxes.pdf
%doc %{_texmfdistdir}/doc/latex/fontaxes/test-fontaxes.tex
#- source
%doc %{_texmfdistdir}/source/latex/fontaxes/fontaxes.dtx
%doc %{_texmfdistdir}/source/latex/fontaxes/fontaxes.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
