# Date: 05-01-2021

"""
    *. virtual_environment:
    an environment which is same as the system_interpreter but is isolated from the other python_environment on
    the system.

    *. installation:
    to use virtual environment, we write
            pip install virtualenv ---> install the package

    we create a new environment using:
            virtualenv my_project_env(projectName) ---> create a new venv

    *. the next step after creating the virtual environment is, to activate it.
    *. we can now use this virtual environment as a separate python installation.

    *. NOTE:
    [linux_user/MacOs_user: venv activate_command -- projectName/bin/activate]
    [windows_user: venv activate_command -- .\projectName\Scripts\activate.ps1]

    *. to deactivate_venv -- command will be 'deactivate'

    *. pip freeze command:
    pip freeze returns all the package installed in a given python environment along with the versions.
            command -- 'pip freeze > requirement.txt'

    *. the above command creates a file named requirement.txt in the same directory containing,
    the output of 'pip freeze'.
    *. we can distribute this file to other users and they can recreate the sane environment using:
                'pip install -r .\requirement.txt'



"""
