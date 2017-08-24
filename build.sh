#!/bin/bash
set -x
make -f /usr/share/selinux/devel/Makefile webapp.pp || exit
/usr/sbin/semodule -i webapp.pp

# Generate a man page off the installed module
#sepolicy manpage -p . -d webapp_domain
# Generate a rpm package for the newly generated policy

pwd=$(pwd)
rpmbuild --define "_sourcedir ${pwd}" --define "_specdir ${pwd}" --define "_builddir ${pwd}" --define "_srcrpmdir ${pwd}" --define "_rpmdir ${pwd}" --define "_buildrootdir ${pwd}/.build"  -ba webapp_selinux.spec
