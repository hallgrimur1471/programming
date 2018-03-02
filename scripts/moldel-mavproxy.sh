#!/bin/bash
# This is a helper script to aid with running mavproxy.py as a daemon by systemd

function mavproxy_start()
{
	if [ -e /tmp/mavproxy.pid ]; then
		echo "MAVProxy: daemon service already running (with PID=$(cat /tmp/mavproxy.pid))"
	else
		host_address="0.0.0.0"
		host_port="14551"
		host_protocol="udpin"
		remote_address="0.0.0.0"
		remote_port="14550"
		remote_protocol="udpin"

		logdir="${HOME}/mavproxy-logs"
		mkdir -p $logdir
		logfile="mav.tlog"

		mavproxy.py --master=${host_protocol}:${host_address}:${host_port} --out=${remote_protocol}:${remote_address}:${remote_port} --logfile=${logdir}/${logfile} --daemon & echo $! > /tmp/mavproxy.pid

		echo "MAVProxy: daemon service started with PID=$(cat /tmp/mavproxy.pid)"
	fi
}

function mavproxy_stop()
{
	if [ -e /tmp/mavproxy.pid ]; then
		kill $(cat /tmp/mavproxy.pid)
		echo "MAVProxy: daemon service stopped [PID=$(cat /tmp/mavproxy.pid)]"
		rm /tmp/mavproxy.pid
	else
		echo "MAVProxy: daemon service is not running"
	fi
}

function mavproxy_status()
{
	if [ -e /tmp/mavproxy.pid ]; then
		echo "MAVProxy daemon service running with PID=$(cat /tmp/mavproxy.pid)"
	elif [ -n "$(ps -ef | grep '/usr/bin/python.*/usr/local/bin/mavproxy.py.*' | grep -v grep)" ]; then
		printf "MAVProxy daemon service not running but it seems there are other instances of mavproxy running.\n  see the processes by running:\n    ps -ef | grep '/usr/bin/python.*/usr/local/bin/mavproxy.py.*' | grep -v grep\n"
	else
		echo "MAVProxy daemon service currently not running"
	fi
}

case "$1" in
	start)
		mavproxy_start
		;;
	stop)
		mavproxy_stop
		;;
	status)
		mavproxy_status
		;;
	reload)
		mavproxy_stop
		sleep 10
		mavproxy_start
		;;
	*)
		echo "Usage: $0 {start | stop | reload | status}"
		exit 1
		;;
esac

exit 0
