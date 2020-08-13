Ansible role for efs
==================================

Mounts EFS directory

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-efs/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-efs/actions?query=workflow%3ARelease)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-efs/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-efs/actions?query=workflow%3A%22Molecule+Test%22)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| efs\_directory\_owner | Directory owner | string | "" | yes |
| efs\_src | Source directory to mount to EFS | string | "" | yes |
| efs\_mount\_options | Options to mount directory with | string | "" | yes |
| efs\_fstype | File system type to mount as | string | "" | yes |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-efs
      vars:
        efs_src: /tmp/efs
        efs_mount_options: bind
        efs_fstype: none
```

Development
-----------

Testing this role locally requires the CircleCI [Local CLI](https://circleci.com/docs/2.0/local-cli/).

To install the CLI for macOS and Linux, invoke the following command:

    $ curl -fLSs https://circle.ci/cli | DESTDIR=/usr/local/bin bash

After installing the CLI, invoke the following command to run the Molecule tests:

    $ make test

License
-------

[Apache License](LICENSE)
