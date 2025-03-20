from services.autoloader import autoloader
from hooks.test import test

autoloader(['Person', 'Animal'])

test()