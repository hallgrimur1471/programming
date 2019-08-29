# Awesome Ubuntu 18 setup

Installs the following stuff with my custom configs:

* ../python
* ../essentials
* ../ultimate_vim_configuration
* ../tmux
* ../sublime_text_3
* ../terminal_elementary_theme

# Installing

```
sudo apt-get install -y curl
curl -o awesome_ubuntu_18_setup.py \
  https://raw.githubusercontent.com/hallgrimur1471/programming/master/install_scripts/awesome_ubuntu_18_setup/install.py
sudo chmod +x awesome_ubuntu_18_setup.py
./awesome_ubuntu_18_setup.py
```

# Testing the install script

```
./tests/test_install_script_in_docker.py
```
