for i in {1..100}; do echo -n '['; echo -n `date`; echo -n ']    '; ping -c 1 www.google.com | grep 'packets transmitted'; sleep 300 ; done
