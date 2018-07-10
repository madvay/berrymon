#!/usr/bin/env python3

# Copyright (c) 2018 by Advay Mengle - https://github.com/madvay/berrymon
#
# WARNING: You are responsible for following all relevant safety
# precautions and using your device responsibly. You must independently
# assess whether any advice or recommendations contained in this
# software (including all documentation) is suitable and safe for you and
# your device. Do not rely on temperature or other measurements from this
# software to ensure safety - measurements may be out of date or wrong.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this software except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
assert sys.version_info >= (3,5)

import copy
import subprocess
import urllib.parse
import time
import datetime
import platform
import threading
from datetime import datetime
from threading import Thread
from time import sleep
import urllib.request
import os
import re
import logging
from logging.handlers import TimedRotatingFileHandler
import signal
import argparse


parser = argparse.ArgumentParser(description="""Monitor Logger Spy

- Serves various properties of other system being monitored by
berrymon.
""",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                 epilog="""Copyright (c) 2018 Advay Mengle and others - see the LICENSE and NOTICE files included with this software.
                                 
WARNING: You are responsible for following all relevant safety
precautions and using your device responsibly. You must independently
assess whether any advice or recommendations contained in this
software (including all documentation) is suitable and safe for you and
your device. Do not rely on temperature or other measurements from this software
to ensure safety - measurements may be out of date or wrong.
                                 """)
parser.add_argument("--server", help="run a webserver with monitoring on this IP", type=str, default="0.0.0.0")
parser.add_argument("--server_port", help="webserver port", type=int, default=8080)

parser.add_argument("--default_hosts", help="hosts to connect to if none specified by user", nargs='+', default=[])

parser.add_argument("--log", help="path to log to", type=str, default=None)
parser.add_argument("--log_days", help="days of logs to keep", type=int, default=7)
parser.add_argument("--log_period", help="print/log every N executions", type=int, default=1)


# Sets up our logs, and redirects stdout/err to those logs
def setup_logs(path, days):
    logger = logging.getLogger(__name__)
    handler = TimedRotatingFileHandler(path, when='midnight', backupCount=days)
    formatter = logging.Formatter('%(asctime)s [%(levelname)-10s] <%(name)s> %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    class LoggerStream:
        def __init__(self, logger, level):
            self.logger = logger
            self.level = level

        def write(self, msg):
            # skip the garbage
            if msg != '\n':
                self.logger.log(self.level, msg)

        def flush(self):
            # can't force a flush of the logger
            return

    sys.stderr = LoggerStream(logger, logging.ERROR)
    sys.stdout = LoggerStream(logger, logging.INFO)
    return logger


args = parser.parse_args()

if args.log:
    setup_logs(args.log, args.log_days)

def run_server():
    sys.path.append('./third_party/bottle/')
    from bottle import route, run, request, response

    @route('/')
    @route('/simple')
    def main():
        refms = 0
        if request.query.refresh:
            refms = int(request.query.refresh) * 1000
        if request.query.format == 'json':
            return ret
        hosts = request.query.hosts.split(',')
        if len(hosts) == 0 or hosts[0] == '':
            hosts = args.default_hosts
        vs = []
        refset = "<script>refms={0};</script>".format(refms)
        style = refset + """<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<style>iframe {
    border-style: solid;
    border-width: 0.1px;
    width:300px;
    height:300px;
}

h4 {
    margin: 0.5em 0;
    text-align: center;
}</style><script>
var refresh = function(){$('iframe').each(function() {
  this.src = this.src;
});};
if ( refms >0){setInterval(refresh, refms );}
</script>"""
        for h in hosts:
            vs.append('<div style="display:inline-block"><h4>{0}</h4><iframe src="http://{0}"></iframe></div>'.format(h))
        return style + '' + ''.join(vs) + ''

    def launch():
        run(host=args.server, port=args.server_port)
    
    launch()
    

run_server()

