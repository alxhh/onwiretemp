import collectd

# XXX: fix hard coding.

sensors = {}

class W1Mon(object):
    def __init__(self):
        self.plugin_name = 'temperature'
        self._interval = 60
        self.verbose_logging = False

    def configure_callback(self, conf):
        """
        Receive configuration block
        """
        for node in conf.children:
            if node.key == 'Interval':
                self._interval = int(node.values[0])
            elif node.key == 'Sensor':
                sensors[node.values[0]] = node.values[1]
                collectd.warning('Sensor: ' + node.values[0] + ' Named: ' +
                node.values[1])
            else:
                collectd.warning('collectd-w1 plugin: Unknown config key: %s.' % node.key)
        collectd.register_read(mon.read_callback, mon._interval)
        self.log_verbose('Configured with interval=%s' %
                         (self._interval,))


    def log_verbose(self, msg):
        if not self.verbose_logging:
            return
        collectd.info(self.plugin_name + ' plugin [verbose]: %s' % msg)


    def dispatch_value(self, plugin_instance, value_type, instance, value):
        """
        Dispatch a value to collectd
        """
        self.log_verbose('Sending value: %s.%s.%s=%s' % (self.plugin_name, plugin_instance, instance, value))
        val = collectd.Values()
        val.plugin = self.plugin_name
        val.plugin_instance = plugin_instance
        val.type = value_type
        val.type_instance = instance
        val.values = [value, ]
        val.interval = self._interval
        self.log_verbose("DIR: %s, %s %s" % (dir(val), val.interval, val))
        val.dispatch()

    def read_callback(self):
        """
        Collectd read callback
        """
        self.log_verbose('Read callback called')

        for _id, _name in sensors.iteritems():
                f = open("/sys/bus/w1/devices/" + _id +"/w1_slave")
                text = f.read()
                l = text.split("\n")[1]
                t = float(l[l.index("t=")+2:])/1000
                if t > 84:
                    # On timeout, we get 85 degrees, handle that.
                    continue
                self.dispatch_value('', 'temperature', _name, t)

if __name__ == '__main__':
    pass
else:
    import collectd
    mon = W1Mon()
    # register callbacks
    collectd.register_config(mon.configure_callback)
