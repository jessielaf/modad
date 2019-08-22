# Modad
Modad (Module ass- and dissembler) a tool that helps with your workflow when using the modular monoliths, micro kernel or modular kernel solution. This can be done by creating a yaml that looks like this:

> This module is not usable in production!

```yaml
# modad.yml

dest: modules
modules:
  - name: employees
    repo: git@github.com:jessielaf/effe
    version: master
  - name: shifts
    repo: git@github.com:jessielaf/effe
    version: master
```


## Install

```
python setup.py install
```

## Commands

### Assemble
```
modad assemble
```

### Dissemble
```
modad dissemble {{ modul_name }} {{ dissemble_destination }}
```

### Options
|Option|Default|Description|Example|
|---|---|---|---|
|`-c` or `--config`|`modad.yml`|The file in which the config is located|`custom.yml`|

## Config

### Dest

Destination shows where the modules should be copied to. This can either be a `dict` or a `str`

#### String

The module will be coupled entirely to `dest/{{ module_name }}`

**Example**
```yaml
dest: modules
```

#### Dict

The folders inside the module will be copied to the respective directories

**Example** 
```yaml
dest:
  - src: pages
    dest: src/pages
  - src: module
    dest: modules
```

In this example the pages folder inside the module will be copied to `src/pages/{{ module_name }}` and module folder to `modules/{{ module_name }}`

### Modules

Modules have three attributes

|Name|Default|Description|Example|
|---|---|---|---|
|name|-|Name of the module. This decides in which folders the module gets copied|`shift`|
|repo|-|Repository where the module should be cloned from. This has to be a git link|`git@github.com:jessielaf/modad.git`|
|version|`master`|Version of the module|`company-a`|