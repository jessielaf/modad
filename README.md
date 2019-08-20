# Modad
Modad (Module ass- and dissembler) a tool that helps with your workflow when using the modular monoliths, micro kernel or modular kernel solution. This can be done by creating a yaml that looks like this:

> This module is not usable in production!

```yaml
# modad.yaml

dest: modules
modules:
  - name: employees
    repo: git@github.com:jessielaf/effe
    version: master
  - name: shifts
    repo: git@github.com:jessielaf/effe
    version: master
```

## Usage

### Install

```
python setup.py install
```

### Assemble
```
modad assemble
```

### Dissemble
```
modad dissemble {{ modul_name }} {{ dissemble_destination }}
```

### Options
|Option|Default|Example|Description|
|---|---|---|---|
|`-c` or `--config`|`modad.yml`|`custom.yml`|The file in which the config is located|
