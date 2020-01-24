import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_mount(host):
    assert host.mount_point("/efs").exists
    assert host.file("/efs/test").exists

    cmd = host.run("ls /efs/*/info")
    assert cmd.succeeded
    cmd = host.run("ls /efs/*/info/distro_name")
    assert cmd.succeeded
    cmd = host.run("ls /efs/*/scons-cache")
    assert cmd.succeeded
