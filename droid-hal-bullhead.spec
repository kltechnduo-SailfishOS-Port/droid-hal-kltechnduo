#These and other macros are documented in dhd/droid-hal-device.inc
%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^/system/bin/.*$
%define __find_provides %{nil}
%define __find_requires %{nil}
%define device bullhead
%define vendor lge
%define vendor_pretty LG
%define device_pretty Nexus 5x
%define installable_zip 1
%define device_target_cpu aarch64
%define straggler_files \
/verity_key\
%{nil}
%include rpm/dhd/droid-hal-device.inc
