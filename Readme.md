# pyqtapplicationhelper

## Distributing

Check any of the Release/* branches to find the needed version
Check under dist for the .whl file

```bash
pip install *.whl
```

## Making Wheel

```bash
python setup.py bdist_wheel --universal
```

## Update Modules

### Windows

```powershell
pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
```

### Unix

```bash
pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U 
```
