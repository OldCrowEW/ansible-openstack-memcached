# Role Name

https://travis-ci.org/OldCrowEW/ansible-openstack-memcached.svg?branch=master

Ansible role to install and configure Memcached for OpenStack. This follows the install guide for better or worse :D

## Requirements

None

## Role Variables

None

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: oldcrowew.ansible_openstack_common }
         - { role: ansible-openstack-memcached }

## License

BSD

## Author Information

John Favorite