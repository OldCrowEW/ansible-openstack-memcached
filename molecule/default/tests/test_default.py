import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_memcached_is_installed(host):
    package = host.package('memcached')

    assert package.is_installed


def test_python_memcached_is_installed(host):
    package = host.package('python-memcached')

    assert package.is_installed


def test_sysconfig_memcached_file(host):
    f = host.file('/etc/sysconfig/memcached')

    assert f.exists


def test_memcached_running_and_enabled(host):
    service = host.service('memcached')

    assert service.is_running
    assert service.is_enabled
