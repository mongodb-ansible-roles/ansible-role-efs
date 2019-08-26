Ansible role for efs
==================================

Mounts EFS directory

[![CircleCI](https://img.shields.io/circleci/build/github/mongodb-ansible-roles/ansible-role-efs/master?style=flat-square)](https://circleci.com/gh/mongodb-ansible-roles/ansible-role-efs)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| name | desc | type | default | required |

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
