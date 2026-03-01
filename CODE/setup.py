import os
from glob import glob
from setuptools import setup

package_name = 'oreo_robot'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # Include config files (params.yaml)
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your@email.com',
    description='OREO V2 Quadruped Robot Control Package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial_bridge = oreo_robot.serial_bridge_node:main',
            'kinematics = oreo_robot.oreo_control_nodes:main',
            'vision = oreo_robot.vision_node:main',
        ],
    },
)