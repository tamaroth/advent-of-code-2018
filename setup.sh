#!/bin/bash
#
# Setup the environment.
#

SCRIPT_DIR="$(cd "$(dirname "$0")"; pwd -P)"
VIRTUALENV_DIR="$SCRIPT_DIR/venv"
if hash python3.7 2> /dev/null; then
	PYTHON_PATH="python3.7"
else
	PYTHON_PATH="python3"
fi

print_error() {
	echo "$0: $1" >&2
}

print_phase() {
	printf "%-45s " "$1"
}

print_phase_end() {
	echo "[$1]"
}

install_package() {
	print_phase " - $1"
	PIP_ARGS=(install --upgrade "$1")
	if [ ! -z "$2" ]; then
		PIP_ARGS+=(--index-url "$2")
	fi
	pip "${PIP_ARGS[@]}" > /dev/null || exit 1
	print_phase_end "OK"
}

print_phase "Checking Python version..."
PYTHON_VERSION="$("$PYTHON_PATH" --version | cut -d\  -f2)"
if [[ "$PYTHON_VERSION" =~ ^3\.[0-6] ]]; then
	print_phase_end "FAIL"
	print_error "Python >= 3.7 is required (have only $PYTHON_VERSION)"
	exit 1
fi
print_phase_end "OK"


print_phase "Creating a virtual environment..."
if [ ! -d "$VIRTUALENV_DIR" ]; then
	"$PYTHON_PATH" -m venv "$VIRTUALENV_DIR" || exit 1
	pushd "$VIRTUALENV_DIR"/lib/ > /dev/null || exit 1
	ln -s "$(ls | head -n1)" python || exit 1
	popd > /dev/null || exit 1
fi
print_phase_end "OK"


print_phase "Activating it..."
source "$VIRTUALENV_DIR/bin/activate" || exit 1
print_phase_end "OK"


print_phase "Updating pip..."
pip install --upgrade pip > /dev/null || exit 1
print_phase_end "OK"

print_phase "Installing all Python requirements..."
echo ""

install_package "wheel"
install_package "autopep8"
install_package "click"
install_package "flake8"
install_package "nose"
install_package "numpy"
install_package "scipy"

echo ""
echo "Setup complete. Now activate virtualenv by executing:"
echo "    source $(realpath --relative-to=. "$VIRTUALENV_DIR")/bin/activate"
