%define		_rel	1
Summary:	e-plip
Summary(pl):	e-plip
Name:		eplip
Version:	0.5.6
Release:	%{_rel}@%{_kernel_ver_str}
Copyright:	GPL
Group:		Base/Kernel
Source0:	http://e-plip.sourceforge.net/%{name}-%{version}.tar.gz
#BuildRequires:	
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		/sbin/depmod

%define	_prefix	/usr

%description

%description -l pl

%package -n kernel-smp-eplip
Summary:	e-plip
Summary(pl):	e-plip
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Prereq:		/sbin/depmod

%description -n kernel-smp-eplip

%description -n kernel-smp-eplip -l pl

%prep
%setup -q

#%patch

%build
#./configure --prefix=%{_prefix}
%{__make} SMP=1
mv eplip.o eplip-smp.o
%{__make} clean
undef CONFIG_SMP
%{__make} SMP=0

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post
/sbin/depmod -a

%postun
/sbin/depmod -a

%post -n kernel-smp-eplip
/sbin/depmod -a

%postun -n kernel-smp-eplip
/sbin/depmod -a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)

%files -n kernel-smp-eplip
%defattr(644,root,root,755)
%doc
%attr(,,)
