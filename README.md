# napalm-gaia

Unofficial CheckPoint GaiaOS driver-plugin for NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support) python library.<br> 
Certain commands will require expert password. <br>
This driver is experimental, check the docs what is possible at the moment.


## Compatibility

documented functions were successfully tested against:
 - R77.30 Gaia
 - R80.10 Gaia
 - R80.20 Gaia  
 - R80.30 Gaia
 - R80.40 Gaia
 
untested yet:

 
not supported:
 - R77.30 SPLAT
 

 
 
 
## install
 
    pip install napalm-gaia

## documentation

https://napalm-gaia.readthedocs.io/en/latest


## contact

You can reach us via [networktocode](https://networktocode.herokuapp.com/) #napalm-gaia

## simple test
    #!/usr/bin/env python3
    from napalm import get_network_driver    
    
    driver = get_network_driver('gaiaos')   
    optional_args = {'secret': 'expert-password'}
    device = driver('1.1.1.1', 'username', 'password', optional_args=optional_args)
    device.open()    
    vals = device.get_users()    
    print(vals)
    vals = device.get_config('retrieve='all')
    print(vals)
    vals = device.get_config('retrieve='ntp')
    print(vals)
    vals = device.send_clish_cmd('show route')
    print(vals)
    device.set_virtual_system(2)
    vals = device.send_clish_cmd('show route')
    print(vals)
    vals = device.send_expert_cmd('uname -a')
    print(vals)    
    device.close()
    
