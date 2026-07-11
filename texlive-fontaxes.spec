%global tl_name fontaxes
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.2
Release:	%{tl_revision}.1
Summary:	Additional font selection axes for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fontaxes
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontaxes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontaxes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontaxes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package adds several new font axes on top of LaTeX's New Font
Selection Scheme. In particular, it splits the shape axis into a primary
and a secondary shape axis, and it adds three new axes to deal with the
different figure versions offered by many professional fonts. This
package has nowadays been deprecated in favour of the figureversions
package.

