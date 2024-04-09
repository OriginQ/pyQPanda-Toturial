from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os
import shutil
from setuptools import setup, find_packages
import platform 

# shell :  python ./setup-cpython.py build_ext --inplace

def list_allfile(path, all_files=[]):
    if os.path.exists(path):
        files = os.listdir(path)
    else:
        print('this path not exist')
    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            list_allfile(os.path.join(path, file), all_files)
        else:
            if "__init__" in file:
                continue
            if file.endswith('py'):
                all_files.append(os.path.join(path, file))
    #print(all_files)
    return all_files


def find_pyx(path='.'):
    pyx_files = []
    for root, dirs, filenames in os.walk(path):
        for fname in filenames:
            if "__init__" in fname:
                continue
            if fname.endswith('.py'):
                pyx_files.append(os.path.join(root, fname))
    return pyx_files


def cp_pyi(source_path='kyber_alg', target_dir='kyber_alg'):
    pyx_files = []
    for root, dirs, filenames in os.walk(source_path):
        for fname in filenames:
            if fname.endswith('.pyi'):
                pyx_files.append(os.path.join(root, fname))
    for pname in pyx_files:
        target_path = str.rfind(pname)


def remove_all(path, all_files=[]):
    if os.path.exists(path):
        files = os.listdir(path)
    else:
        print('this path not exist')
    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            remove_all(os.path.join(path, file), all_files)

        else:
            print(f"start {file}")
            if "__init__.py" in file:
                continue
            if file.endswith('.py'):
                # os.remove(os.path.join(path, file))
                pass
            if file.endswith('.c'):
                os.remove(os.path.join(path, file))
            if file.endswith('.pyc'):
                os.remove(os.path.join(path, file))
    return all_files



pyfiles = list_allfile('kyber_alg')

from pathlib import Path
from Cython.Distutils import build_ext

class MyBuildExt(build_ext):
    def run(self):
        build_ext.run(self)

        build_dir = Path(self.build_lib)
        root_dir = Path(__file__).parent
        target_dir = build_dir if not self.inplace else root_dir
        
        self.copy_file(Path('kyber_alg') / '__init__.py', root_dir, target_dir)
        remove_all(target_dir)

    def copy_file(self, path, source_dir, destination_dir):
        if not (source_dir / path).exists():
            return
        shutil.copyfile(str(source_dir / path), str(destination_dir / path))


requirements = open('requirements.txt').readlines()
requirements = [r.strip() for r in requirements]

is_win = (platform.system() == 'Windows')
if is_win:
    pd_files = ['*.pyd', '*.dll', '*.pyi']
else :
    pd_files = ['*.so', '*.pyi']

setup(
    name="kyber_alg",
    version='1.0.1',
    license = "Apache Licence", 
    author = "OriginQ",
    install_requires=requirements,
    description= "A kyber_alg Environment Kit.",
    long_description=__doc__,
    ext_modules=cythonize(find_pyx('kyber_alg'),
                          build_dir="build",
                          language_level=3),
    cmdclass=dict(build_ext=MyBuildExt),
    packages = find_packages(),
    package_data={
        '': pd_files,
    },
    include_package_data = True,  
    classifiers=[
	"Development Status :: 4 - Beta",
	"Operating System :: MacOS :: MacOS X",
	"Operating System :: Microsoft :: Windows :: Windows 10",
	"Operating System :: POSIX :: Linux",
	"Topic :: Software Development :: Libraries :: Python Modules",
	"Programming Language :: Python",
	"Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
	],
)

