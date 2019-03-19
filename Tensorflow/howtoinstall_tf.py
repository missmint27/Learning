#1. Install the Python development environment on your system
#https://www.tensorflow.org/install/pip#1.-install-the-python-development-environment-on-your-system
$python3 --version
$pip3 --version
$virtualenv --version

$/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$export PATH="/usr/local/bin:/usr/local/sbin:$PATH"
$brew update
$brew install python  # Python 3
$sudo pip3 install -U virtualenv  # system-wide install

#2. Create a virtual environment (recommended)
$virtualenv --system-site-packages -p python3 ./venv
$source ./venv/bin/activate  # sh, bash, ksh, or zsh
(venv)$pip install --upgrade pip
(venv)$pip list  # show packages installed within the virtual environment
(venv)$deactivate  # don't exit until you're done using TensorFlow

#3. Install the TensorFlow pip package
#virtualenv install:
(venv)$pip install --upgrade tensorflow
(venv)$python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
#system install:
$pip3 install --user --upgrade tensorflow  # install in $HOME
$python3 -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"