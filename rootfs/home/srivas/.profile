export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:/usr/games"
export HOME="/home/srivas"
export USER="srivas"
export LOGNAME="srivas"
export HOSTNAME="microos"
export ENV="/etc/shinit"

ESC=$(printf '\033')
export PS1="${ESC}[1;36msrivas@microos${ESC}[1;34m:\w${ESC}[1;32m$ ${ESC}[0m"

help() {
    /usr/bin/help "$@"
}
alias help='/usr/bin/help'
alias commands='/usr/bin/help'
alias '?'='/usr/bin/help'
