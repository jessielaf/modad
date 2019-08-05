# Monoa
Monoa is a assembler for modular monoliths. This can be done by creating a yaml that looks like this:

```yaml
dest_dir: modules
modules:
  employees:
    repo: git@github.com:jessielaf/effe
    version: master
  shifts:
    repo: git@github.com:jessielaf/effe
    version: master
```
