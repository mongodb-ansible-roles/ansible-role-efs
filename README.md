Ansible role for efs
==================================

Mounts EFS directory

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-efs/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-efs/actions?query=workflow%3ARelease)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-efs/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-efs/actions?query=workflow%3A%22Molecule+Test%22)

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `efs_directory_owner` | Directory owner | string | "" | yes |
| `efs_in_container` | Specify if running in container. /etc/hosts task will fail inside of a container| boolean | false | yes |
| `efs_src` | Source directory to mount to EFS | string | "" | yes |
| `efs_mount_options` | Options to mount directory with | string | "" | yes |
| `efs_fstype` | File system type to mount as | string | "" | yes |

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

License
-------

[Apache License](LICENSE)
