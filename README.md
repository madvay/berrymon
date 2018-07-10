# berrymon

Tools to monitor your single board computer.

<img src="./imgs/photo-low-use-c.jpg" height="300"/> <img src="./imgs/photo-high-use-c.jpg" height="300"/>

During low usage; and during high usage

__WARNING:__ You are responsible for following all relevant safety
precautions and using your device responsibly. You must independently
assess whether any advice or recommendations contained in this
software (including all documentation) is suitable and safe for you and
your device. Do not rely on temperature or other measurements from this
software to ensure safety - measurements may be out of date or wrong.

## Usage
````
usage: berrymon.py [-h] [-s] [--sensehat_required] [-i]
                   [--ifttt_period IFTTT_PERIOD] [-p PERIOD]
                   [--min_temp MIN_TEMP] [--max_temp MAX_TEMP]
                   [--min_freq MIN_FREQ] [--max_freq MAX_FREQ]
                   [--led_rotation LED_ROTATION] [--power_management]
                   [--log LOG] [--log_days LOG_DAYS] [--log_period LOG_PERIOD]
                   [--server SERVER] [--server_port SERVER_PORT]

Monitor Logger - Monitors various properties of the system, logs them,
displays them on a Sense HAT board, and advertises them as a server (see
options).

optional arguments:
  -h, --help            show this help message and exit
  -s, --sensehat        enables the Sense HAT LEDs, optionally (default:
                        False)
  --sensehat_required   fails if the Sense HAT LED cannot be loaded (requires
                        --sensehat also) (default: False)
  -i, --ifttt           posts metrics to IFTTT using the key stored in env var
                        IFTTT_TOKEN (default: False)
  --ifttt_period IFTTT_PERIOD
                        send an IFTTT post every N executions (default: 1)
  -p PERIOD, --period PERIOD
                        seconds to sleep between monitoring (default: 1)
  --min_temp MIN_TEMP   Min bar graph temperature (default: 40)
  --max_temp MAX_TEMP   Max bar graph temperature (default: 80)
  --min_freq MIN_FREQ   Min bar graph frequency (default: 600000000)
  --max_freq MAX_FREQ   Max bar graph frequency (default: 1400000000)
  --led_rotation LED_ROTATION
                        rotation of the Sense HAT LEDs (90deg increments)
                        (default: 0)
  --power_management    allows joystick power control (middle=sudo shutdown,
                        others=sudo reboot) (default: False)
  --log LOG             path to log to (default: None)
  --log_days LOG_DAYS   days of logs to keep (default: 7)
  --log_period LOG_PERIOD
                        print/log every N executions (default: 1)
  --server SERVER       run a webserver with monitoring on this IP (default:
                        None)
  --server_port SERVER_PORT
                        webserver port (default: 8080)
````

Requires Python 3.5 or later.

## Sense HAT display

<img src="./imgs/leds.svg" />

Includes:

* (a) Alternate blinking light to indicate berrymon is running.  Also provides a reference point for the bottom-right and orientation.
* (b) Bar graph of SoC temperature (default: 40C to 80C)
* (c) Bar graph of arm core frequency (default: 600MHz to 1400MHz)
* (d) Current throttling status: bottom/red - undervoltage; middle/green - frequency capped; blue/top - throttled  
* (e) Past throttling status (see (d) for colors)

## Running as a daemon

_TODO_

* The daemon user will need:
  * `video` and `input` group membership if `--sensehat` is used
  * `/etc/sudoers` no password access to `shutdown` and `reboot` if `--power-management` is used
* Provide `IFTTT_TOKEN` environment variable if `--ifttt` is used

## berryspy



## License Notice
See [LICENSE](LICENSE) and [NOTICE](NOTICE).
