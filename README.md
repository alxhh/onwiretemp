# Collectd-oneworetemp

Collects Temperature Data from Linux One-Wire Kernel Driver into collectd

## Getting Started

Install collectd with python module, this script and put all Sensors into your
collectd.conf

### Prerequisities

You need a collectd with python support.

```
sudo apt-get install collectd
```

### Installing

After installing collectd, make a directory for your python modules:

```
sudo mkdir /usr/local/lib/collectd
```

Copy python file into directory:

```
sudo cp collectd_w1.py /usr/local/lib/collectd
```

Put the following block into your collectd.conf and change it to you sensor ids
an names.

```
<Plugin python>
        ModulePath "/usr/local/lib/collectd"
        LogTraces true
#       Interactive true
        Import "collectd_w1"
        <Module collectd_w1>
                Interval 60
                Sensor "28-0000079dc68e" "Kuehlschrank"
        </Module>
</Plugin>
```

Activate the python plugin by unkommenting the LoadPlugin block.

You will find the Sensors in

    /sys/bus/w1/devices

After restarting collectd your new sensorgraphs should show up.

## Authors

* **Tollef Fog Heen** - *Initial script* -
* [tfheen](https://github.com/tfheen)

## License

This project is licensed under the MIT License - see the
[LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to my family, who delayed the whole thing for hours.

