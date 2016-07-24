Configure Python collectd module along following example:
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

