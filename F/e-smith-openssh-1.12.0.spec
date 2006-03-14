Summary: e-smith module to configure and enable ssh
%define name e-smith-openssh
Name: %{name}
%define version 1.11.0
%define release 29
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: e-smith, openssl, 
Requires: openssh >= 3.5
Requires: openssh-clients
Requires: openssh-server
Requires: e-smith-lib >= 1.15.1-19
Requires: runit
AutoReqProv: no

%changelog
* Tue Mar 14 2006 Charlie Brady <charlie_brady@mitel.com> 1.12.0-01
- Roll stable stream version. [SME: 1016]

* Mon Mar 13 2006 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-29
- Expand /etc/rssh.conf in user-{create,delete,lock,modify} [SME: 877]

* Mon Mar 13 2006 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-28
- A user is allowed access to rssh protocols if:
  - They have PasswordSet==yes 
  - They have AllowRSSH==yes or
    VPNClientAccess==yes but not AllowRSSH==no [SME: 877]

* Mon Mar 13 2006 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-27
- Remove defaults for sshd{Allow*} and the templates for rssh.conf [SME: 877]
- Allow a user all of the rssh protocols if AllowSSH is yes [SME: 877]

* Thu Mar 02 2006 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-26
- Adjust sftp-server path in sshd_config to match rssh [SME: 924]

* Wed Mar 01 2006 Charlie Brady <charlie_brady@mitel.com> 1.11.0-25
- Add syslog socket inside privsep chroot jail [SME: 916]

* Tue Jan 24 2006 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-24
- Default sshd{AllowRSYNC} == yes [SME: 42]

* Mon Jan 23 2006 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-23
- Add template for /etc/rssh.conf [SME: 42]
- Default sshd{AllowSCP, AllowSFTP} == yes [SME: 532]
- Default sshd{AllowRDIST,AllowRSYNC,AllowCVS} == no

* Fri Jan 6 2006 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-22
- Default sshd{PasswordAuthentication} to "no" [SME: 377]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-21
- Bump release number only

* Wed Aug 10 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-20]
- Delete test related requires (not really required) and add runit.

* Wed Jul 20 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-19]
- Set $sshd{TCPPort} and remove obsolete masq template fragment. [SF: 1241409]

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-18]
- Update to current db access APIs. [SF: 1216546]

* Tue Jul  5 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-17]
- Configure MaxAuthTries (our default is 2). [SF: 1232544]

* Thu Jun 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-16]
- Ensure that 'status' property is recognised at startup. [MN00061795]

* Tue May 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-15]
- Default to protocol 2 only on new installs, and '2,1' for
  upgrades where $sshd{Protocol} is not defined.

* Mon Mar 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-14]
- Use generic_template_expand action for all template expansions from
  sshd-conf.  Update e-smith-lib dependency. [MN00064130]
- Replace sshd-reload with call to 'adjust-services'. [MN00065576]

* Tue Sep 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-13]
- Updated requires with new perl dependencies. [charlieb MN00040240]
- Clean BuildRequires. [charlieb MN00043055]

* Mon Dec 22 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-12]
- Added host key generation code to run script. [msoulier 9549]

* Wed Dec 10 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-11]
- Fixed a bug in the genfilelist options. [msoulier 9549]

* Fri Dec  5 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-10]
- Put full path to sshd in run script to work around assumption of full path
  in sshd sighup handler. [msoulier 9549]

* Fri Dec  5 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-09]
- Updated sshd-reload to use daemontools wrapper. [msoulier 9549]

* Fri Dec  5 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-08]
- Moved the shebang line to a place where it actually matters. Tell me it's
  friday. [msoulier 9549]

* Fri Dec  5 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-07]
- Fixed a couple of typos preventing multilog from starting. [msoulier 9549]

* Fri Dec  5 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-06]
- Moved initscript to /etc/init.d/supervise/sshd. [msoulier 9549]

* Fri Dec  5 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-05]
- Fixed a couple of specfile typos. [msoulier 9549]

* Fri Dec  5 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-04]
- Adding supervision of sshd. [msoulier 9549]
- Updated createlinks to latest api.

* Tue Sep 16 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-03]
- Remove deprecated RhostsAuthentication from sshd_config. [charlieb 10014]

* Thu Aug 21 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-02]
- Replace sshd-conf-startup action with default db fragments.
  [charlieb 9553]

* Thu Aug 21 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-01]
- Changing version to development stream number - 1.11.0

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Changing version to stable stream number - 1.10.0

* Mon Apr 21 2003 Mark Knox <markk@e-smith.com>
- [1.9.0-10]
- Enforce 0600 on sshd_config [markk 8407]

* Tue Apr 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-09]
- Add Compression and UsePrivilegeSeparation options [gordonr 8173]

* Tue Apr  8 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-08]
- Backed-out 1.9.0-07. [msoulier 5782]

* Tue Apr  8 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-07]
- Shut off tcp forwarding in the daemon. [msoulier 5782]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-06]
- Actually reload ssh rather than restarting in sshd-reload [gordonr 7785]

* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-05]
- Deleted ./root/.ssh/config/template-begin [lijied 3295]

* Mon Mar 17 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-04]
- Deleted template-begin/end file [lijied 3295]

* Tue Mar  4 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-03]
- s/HostsAllowSpec/hosts_allow_spec/ [charlieb 5650]

* Fri Feb 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-02]
- Re-do hosts.allow template to use esmith::ConfigDB::HostsAllowSpec.
  Add dependency on up-to-date e-smith-lib. [charlieb 5650]

* Fri Feb 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- Roll development stream to 1.9.0

* Mon Feb 24 2003 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-02]
- Allow MaxStartups to be tunable from the config DB [charlieb 7362]

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Rolling stable version number to 1.8.0

* Wed Oct  2 2002 Mark Knox <markk@e-smith.com>
- [1.7.3-04]
- Remove stray braces in hosts.allow template [markk 3786]

* Mon Sep 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.3-03]
- Fix hosts.allow template problem introduced by last change [charlieb 3786]

* Tue Sep 10 2002 Mark Knox <markk@e-smith.com>
- [1.7.3-02]
- Remove deprecated split on pipe [markk 3786]

* Tue Aug 20 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.3-01]
- Add rc7.d symlink and don't set deprecated InitscriptsOrder property
  [charlieb 4458]
- Change use of allow_tcp_in() function to allow dynamic reconfig.
  [charlieb 4501]

* Thu Aug  8 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-01]
- Change masq script fragment to use allow_tcp_in() function. [charlieb 4499]

* Wed Jul 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-01]
- Change masq script fragment to use iptables. [charlieb 1268]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- Changing version to maintained stream number to 1.7.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Changing version to maintained stream number to 1.6.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.6-01]
- RPM rebuild forced by cvsroot2rpm

* Mon May 13 2002 Kirrily Robert <skud@e-smith.com>
- [1.5.5-01]
- Added buildtests [skud 2932]

* Fri Apr 26 2002 Tony Clayton <apc@e-smith.com>
- [1.5.4-01]
- add -t option to ssh-keygen call in sshd-conf [tonyc]

* Fri Mar  6 2002 Michael G Schwern <schwern@e-smith.com>
- [1.5.3-01]
- Tested & documented sshd-reload action [schwern 2932]
- Tested & documented sshd-conf and sshd-conf-startup actions [schwern 2932]
- Changed all actions to use esmith::ConfigDB [schwern 2932]
- Fixed dependencies. [schwern]

* Thu Feb 14 2002 Kirrily Robert <skud@e-smith.com>
- [1.5.2-01]
- CVS testing

* Thu Feb 14 2002 Kirrily Robert <skud@e-smith.com>
- [1.5.0-01]
- rollRPM: Rolled version number to 1.5.0-01. Includes patches up to 1.4.0-06.

* Mon Nov 05 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-06]
- Remove obsoleted "CheckMail no" fragment from sshd_config template.

* Tue Aug 28 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.0-05]
- Removed links from deprecated post-restore event

* Fri Aug 17 2001 gordonr
- [1.4.0-04]
- Autorebuild by rebuildRPM

* Tue Aug 14 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-03]
- Change back to Protocol 1 until known_hosts2 and authorized_keys2 files are
  implemented on both sides.

* Tue Aug 14 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-02]
- Add template fragements to generate /root/.ssh/config host
  config sections for any hostnames added to %e_smith_hosts by
  other fragements numbered between 00 and 19.
- Delete useless template-end for /root/.ssh/config.

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-10.

* Wed Aug 8 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-10]
- Use restart instead of reload as some initscripts don't have the latter

* Sun Jul 8 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-09]
- Check "access" property of sshd service

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [1.3.0-08]
- Changed license to GPL

* Thu Jul 05 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-07]
- Explicitly disable ChallengeResponseAuthentication and
  KbdInteractiveAuthentication

* Wed May 30 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-06]
- Added HostKey line for /etc/ssh/ssh_host_rsa_key for SSH version 2

* Tue May 29 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-05]
- fixed actions that had tied %conf when calling serviceControl (2 actions)

* Mon May 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-04]
- Added links to /usr/libexec and /usr/local/libexec to enable
  sftp for more client systems under protocol V1

* Mon May 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-03]
- Revised after comments from Charlie
- Added documentation for MaxStartups and cleaner perl idiom for
  SubsystemSftp test

* Mon May 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-02]
- Enabled sftp subsystem by default with correct path to sftp-server
- Added MaxStartups configuration

* Mon May 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-01]
- Rolled version number to 1.3.0-01. Includes patches upto 1.2.0-06.

* Wed May 09 2001 Tony Clayton <tonyc@e-smith.com>
- [1.2.0-06]
- Forgot to add last patch to %setup.  Adding it now.

* Wed May 09 2001 Tony Clayton <tonyc@e-smith.com>
- [1.2.0-05]
- Add /root/.ssh/config template-{begin,end} fragments
- Expand config template from sshd-conf

* Thu Apr 27 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.2.0-04]
- Rolled version for GPG signing - no change

* Mon Apr  9 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.2.0-03]
- Extra HostKey line for openssh-2.5

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-02]
- Rolling release number for GPG signing.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-23.

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-23]
- use serviceControl()

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-22]
- reload sshd (and possibly kill it off) in post-restore

* Thu Jan 11 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-21]
- fully qualify path to killall in sshd-reload

* Wed Jan 10 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-20]
- Kill existing ssh sessions if we have just stopped the service

* Wed Jan 10 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-19]
- Use sshd reload instead of killall -HUP - that closes current connections

* Tue Jan 9 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-18]
- Make new bootstrap-console-save event - the Lite version
- Make sshd-reload shut down sshd if it has been disabled
- Don't redo conf-sshd-startup with every console-save

* Fri Jan 5 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-17]
- Added missing use esmith::util to sshd-reload

* Thu Jan 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-16]
- Added missing use esmith::db

* Wed Jan 03 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-15]
- sshd-reload now starts sshd if not running and service enabled

* Thu Dec 28 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-14]
- Process sshd_config template in remoteaccess-update

* Thu Dec 28 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-13]
- Provide defaults for PermitRootLogin and PasswordAuthentication properties

* Thu Dec 21 2000 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-12]
- Don't restart sshd after config change, just reload config.

* Sat Dec 16 2000 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-11]
- Fix typo

* Fri Dec 15 2000 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-10]
- Move AllowSSH packet filter template fragment here.

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-9]
- Disable ssh by default

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-8]
- Fixed typo in hosts.allow fragment for private access

* Wed Dec 13 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-7]
- Added sshd-restart to remoteaccess-update event (and others)
- Renamed scripts to sshd-{conf,conf-startup,restart}
- Enable private ssh access by default

* Tue Dec 12 2000 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-6]
- fixed location of ssh_host_key in 20HostKey fragment

* Wed Dec 06 2000 Peter Samuel <peters@e-smith.com
- [1.1.0-5]
- Fixed sshd_config templates for PermitRootLogin and
  PasswordAuthentication

* Wed Dec 06 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-4]
- conf-ssh-startup: PasswordAuthentication=yes and RootLogin=no
- Fixed ordering of Port/Listen fragments

* Tue Dec 05 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-3]
- Changed sshd_config into a directory template
- Used services notation to enable/disable
- sshd_config: PasswordAuthentication and RootLogin - both disabled by default

* Tue Dec 05 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-1]
- Rolled version to 1.1.0. Includes patches up to 0.6-3

* Tue Oct 31 2000 Charlie Brady <charlieb@e-smith.com>
- Ensure that conf-ssh-startup is run during post-upgrade event.
- Fix missing " in hosts.allow template.

* Tue Oct 31 2000 Charlie Brady <charlieb@e-smith.com>
- Merge services database back into configuration database.

* Thu Oct 26 2000 Peter Samuel <peters@e-smith.com>
- Rolled version to 0.6. Includes patches up to 0.5-17

* Fri Oct 06 2000 Adrian Chung <adrian.chung@e-smith.com>
- Fixed a typo in conf-ssh-startup.

* Fri Oct 06 2000 Adrian Chung <adrian.chung@e-smith.com>
- Move %post code to conf-ssh-startup instead
- Default to enabled for sshd in services database if not
  already set.

* Thu Oct 05 2000 Adrian Chung <adrian.chung@e-smith.com>
- Change %post to setdefault ... enabled.

* Wed Oct 4 2000 Charlie Brady <charlieb@e-smith.com>
- Use db_get_type to get service status - to be safe against
  defined service properties
- Do not init services database during post-install event -
  it is done during %post action.

* Wed Oct 4 2000 Charlie Brady <charlieb@e-smith.com>
- Only initialise services database during post-install action.
- Only expand hosts.allow/sshd if sshd service is enabled.

* Wed Oct 4 2000 Charlie Brady <charlieb@e-smith.com>
- Fix typo

* Tue Oct 3 2000 Charlie Brady <charlieb@e-smith.com>
- Update services database when enabling startup

* Mon Oct 2 2000 Gordon Rowell <gordonr@e-smith.com>
- rewrote spec file to use e-smith-devtools

* Mon Sep 25 2000 Paul Nebsit <pkn@e-smith.com>
- updated contact and URL info

* Thu Sep 14 2000 Gordon Rowell <gordonr@e-smith.com>
- Removed obsolete rc7.d symlink from createlinks

* Thu Sep 14 2000 Gordon Rowell <gordonr@e-smith.com>
- Rebuilt using latest e-smith-devtools - hosts.allow template fragment missing

* Tue Aug 30 2000 Paul Nesbit <pkn@e-smith.com>
- added 'use e-smith::util' line to conf-ssh-startup

* Thu Aug 24 2000 Gordon Rowell <gordonr@e-smith.com>
- Rewrote conf-ssh-startup to use serviceControl()

* Sun Jul 2 2000 Charlie Brady <charlieb@e-smith.net>
- Make S85sshd symlink absolute so that RPM verifies

* Sat Jun 17 2000 Charlie Brady <charlieb@e-smith.net>
- Rewrite createlinks in perl
- Add sshd template for /etc/hosts.allow
- Fix ssh-keygen options code

* Mon Jun 12 2000 Charlie Brady <charlieb@e-smith.net>
- Remove /etc/rc.d/rc7.d symlink before (re-)creating it. Avoids logfile mess.
- Change backgroundCommand call to use array instead of string - avoid shell
  parsing.

* Thu May 11 2000 Charlie Brady <charlieb@e-smith.net>
- Change rc?.d directory from 3 to 7.

%description
e-smith server enhancement to configure and enable openssh

%prep
%setup

%build
for i in console-save \
    post-install \
    post-upgrade \
    remoteaccess-update \
    bootstrap-console-save
do
    mkdir -p root/etc/e-smith/events/$i
done
perl createlinks
# build the test suite from embedded tests
/sbin/e-smith/buildtests e-smith-openssh

# Compatibilty symlinks to allow sftp to work with more clients under
# protocol version 1
for dir in usr/libexec usr/local/libexec
do
    mkdir -p root/$dir
    ln -s /usr/libexec/openssh/sftp-server root/$dir/sftp-server
done

# Manage supervise and multilog.
mkdir -p root/service
ln -s ../var/service/sshd root/service/sshd
mkdir -p root/var/service/sshd/supervise
touch root/var/service/sshd/down
mkdir -p root/var/service/sshd/log/supervise
mkdir -p root/var/log/sshd

%install
rm -rf $RPM_BUILD_ROOT
( cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT )
rm -f %{name}-%{version}-%{release}-filelist

/sbin/e-smith/genfilelist \
    --dir '/var/service/sshd' 'attr(1755,root,root)' \
    --file '/var/service/sshd/down' 'attr(0644,root,root)' \
    --file '/var/service/sshd/run' 'attr(0755,root,root)' \
    --dir '/var/service/sshd/supervise' 'attr(0700,root,root)' \
    --dir '/var/service/sshd/log' 'attr(1755,root,root)' \
    --dir '/var/service/sshd/log/supervise' 'attr(0700,root,root)' \
    --file '/var/service/sshd/log/run' 'attr(0755,root,root)' \
    --dir '/var/log/sshd' 'attr(2750,root,nofiles)' \
    $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist

echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
