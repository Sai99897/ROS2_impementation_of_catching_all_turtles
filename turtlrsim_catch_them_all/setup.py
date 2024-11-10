from setuptools import setup
from glob import glob
import os

package_name = 'turtlrsim_catch_them_all'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (os.path.join('share/', package_name,'launch'), glob('launch/*.py')),
        
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    
    
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sai',
    maintainer_email='saiprasanth345@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    

    entry_points={
        'console_scripts': [
            "turtlesim_controller=turtlrsim_catch_them_all.turtle_controller:main",
            "turtle_spawner=turtlrsim_catch_them_all.turtle_spawner:main",
            
        ],
    },
)
