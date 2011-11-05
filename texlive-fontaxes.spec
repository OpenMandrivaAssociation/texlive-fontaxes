# revision 24223
# category Package
# catalog-ctan /macros/latex/contrib/fontaxes
# catalog-date 2011-10-06 16:06:09 +0200
# catalog-license lppl1.3
# catalog-version 1.0a
Name:		texlive-fontaxes
Version:	1.0a
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package adds several new font axes on top of LaTeX's New
Font Selection Scheme. In particular, it splits the shape axis
into a primary and a secondary shape axis, and it adds three
new axes to deal with the different figure versions offered by
many professional fonts.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
