%define		_rel	1
Summary:	EPLIP [Enhanced Parallel Line IP] module 
Summary(pl):	Modó³ EPLIP [Enhanced parallel Line IP]
Name:		eplip
Version:	0.5.6
Release:	%{_rel}@%{_kernel_ver_str}
Copyright:	GPL
Group:		Base/Kernel
Source0:	http://e-plip.sourceforge.net/%{name}-%{version}.tar.gz
#BuildRequires:	
#Requires:	
Patch0:		kernel-%{name}-Rules.make-fix.patch
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
cp Rules.make Rules.make.smp
%patch0 -p0

%build
cp Rules.make Rules.make.up
mv Rules.make.smp Rules.make
%{__make}
mv eplip.o eplip-smp
mv Rules.make.up Rules.make
%{__make} clean
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc
install eplip-smp $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/eplip.o
install eplip.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc

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
/lib/modules/%{_kernel_ver}/misc/*

%files -n kernel-smp-eplip
%defattr(644,root,root,755)
%doc
/lib/modules/%{_kernel_ver}smp/misc/*
