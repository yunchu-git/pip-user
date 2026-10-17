import subprocess
import warnings

def print_output (order,capture_output=True,text=True,shell=True):
    result = subprocess.run(order, capture_output=capture_output,text=text,shell=shell)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    del result

def pip_install (python="python"):
    print_output("curl.exe https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
    print_output(f"{python} get-pip.py")

def install (name,pip="pip",mirror="https://pypi.tuna.tsinghua.edu.cn/simple"):
    print_output(f"{pip} install {name} -i {mirror}")

def uninstall (name,pip="pip",confirm=False):
    if confirm:
        print_output(f"{pip} uninstall {name} -y")
    else:
        warnings.warn("1*000001",UserWarning)

def upgrade (name,pip="pip",mirror="https://pypi.tuna.tsinghua.edu.cn/simple"):
    print_output(f"{pip} install {name} --upgrade -i {mirror}")

def pip_list (pip="pip"):
    print_output(f"{pip} list")
