# vim: sw=4:ts=4:et


%define selinux_policyver 3.13.1-102

Name:   webapp_selinux
Version:	1.0
Release:	1%{?dist}
Summary:	SELinux policy module for web applications

Group:	System Environment/Base		
License:	GPLv2+	
# This is an example. You will need to change it.
URL:		http://HOSTNAME
Source0:	webapp.pp
Source1:	webapp.if


Requires: policycoreutils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils
Requires(postun): policycoreutils
BuildArch: noarch

%description
This package installs and sets up the  SELinux policy security module for web applications.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}/etc/selinux/targeted/contexts/users/


%post
semodule -n -i %{_datadir}/selinux/packages/webapp.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy

fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r webapp
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy

    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/webapp.pp
%{_datadir}/selinux/devel/include/contrib/webapp.if


%changelog
* Thu Aug 24 2017 Gyorgy Demarcsek <dgy.jr92@gmail.com> 1.0-1
- Initial version

